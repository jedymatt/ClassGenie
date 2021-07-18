import os.path
from collections import namedtuple

import xlwings as xw

TRANSMUTATION_TABLE_PATH = 'resources/transmutation_table.txt'

RangeTuple = namedtuple('RangeTuple', ['min', 'max', 'transmuted'])

with open(os.path.join(os.path.dirname(__file__), TRANSMUTATION_TABLE_PATH), 'r') as f:
    _data = f.read().strip()
    _rows = [row.strip().split(',') for row in _data.splitlines()]
    TRANSMUTATION_TABLE = []
    for row in _rows:
        _range = tuple(map(float, row[0].split('-')))
        _transmuted = int(row[1].strip())
        TRANSMUTATION_TABLE.append(
            RangeTuple(min=_range[0], max=_range[1], transmuted=_transmuted)
        )


def transmute_grade(initial_grade):
    for row in TRANSMUTATION_TABLE:
        if row.min <= initial_grade <= row.max:
            return row.transmuted


class Component:
    def __init__(self, scores: list, weight: float, highest_total_score: int = None, label=None):
        self.scores = scores
        self.highest_total_score = highest_total_score if highest_total_score is not None else (self._sum_scores())
        self.weight = weight
        self.label = label

        if self._sum_scores() > self.highest_total_score:
            raise ValueError("Sum of scores exceeded the highest_total_score.")

    def _percentage_score(self):
        return round((self._sum_scores() / self.highest_total_score) * 100, 2)

    def weighted_average(self):
        return round(self._percentage_score() * self.weight, 2)

    def _sum_scores(self):
        return sum([score for score in self.scores if score is not None])

    def __repr__(self):
        return "<Component(label='{}', scores='{}', highest_total_score='{}', weight='{}')>".format(
            self.label, self.scores, self.highest_total_score, self.weight
        )


class StudentRecord:
    def __init__(self, *, name=None, components: list):
        if components is None:
            components = []
        self.name = name
        self.components = components

        if not self.is_valid_weight() and components != []:
            raise ValueError("Total weight is not 1 or 100%")

    def is_valid_weight(self):
        weights = [component.weight for component in self.components]
        return sum(weights) == 1

    @property
    def initial_average(self):
        weighted_averages = [component.weighted_average() for component in self.components]

        return sum(weighted_averages)

    @property
    def transmuted_average(self):
        return transmute_grade(self.initial_average)

    def __repr__(self):
        return "<StudentRecord(name='{}', components='{}', transmuted_average='{}')>".format(self.name, self.components,
                                                                                             self.transmuted_average)


class ClassSheet:

    def __init__(self, sheet: xw.Sheet):
        self._sheet: xw.Sheet = sheet

        self._max_row = None
        self._max_column = None
        self._used_range = None
        self._label = None
        self._label_components = None
        self._head_components = None
        self._students = None
        self._student_records = None

        self._student_males_idx = None
        self._student_females_idx = None

    @property
    def sheet(self) -> xw.Sheet:
        return self._sheet

    @property
    def max_row(self) -> int:
        if self._max_row is None:
            self._max_row = self._sheet.used_range.last_cell.row

        return self._max_row

    @property
    def max_column(self) -> int:
        if self._max_column is None:
            self._max_column = self._sheet.range('A1').merge_area.last_cell.column

        return self._max_column

    @property
    def used_range(self) -> xw.Range:
        if self._used_range is None:
            self._used_range = self._sheet.range('A1', (self.max_row, self.max_column))

        return self._used_range

    @property
    def label(self) -> xw.Range:
        if self._label is None:
            rows = self.used_range.rows
            for idx, rng in enumerate(rows):
                if str(rng.value[0]).endswith('QUARTER'):
                    self._label = rows[idx + 1]
                    break

        return self._label

    @property
    def head_components(self) -> list[Component]:
        if self._head_components is None:
            rng: xw.Range = self.label.offset(2, 0)  # 2 rows below the label is the component data
            component_ranges = self.get_component_ranges(rng)

            self._head_components = [self.generate_component(rng, label.value) for rng, label in
                                     zip(component_ranges, self.label_components)]

        return self._head_components

    @property
    def label_components(self) -> list[xw.Range]:
        if self._label_components is None:
            labels = []
            for label in self.label.columns:
                if label.value is not None and label.merge_cells and label.value != "LEARNERS' NAMES":
                    labels.append(
                        label
                    )
            self._label_components = labels

        return self._label_components

    def get_component_ranges(self, rng: xw.Range) -> list[xw.Range]:
        # slicing the columns, and convert it into components
        ranges = []
        for label in self.label_components:
            col = label.column
            end_col = label.merge_area.last_cell.column

            ranges.append(
                rng.columns[col - 1:end_col].rng
            )
        return ranges

    @staticmethod
    def generate_component(rng: xw.Range, label=None, highest_total_score=None, weight=None, fixed_scores_length=None):

        data = rng.value
        if fixed_scores_length is None:
            scores = [i for i in data[:len(data) - 3] if i is not None]
        else:
            scores = [i for i in data[:len(data) - 3]]
            scores = scores[:fixed_scores_length]

        if weight is None:
            weight = data[len(data) - 1]

        return Component(
            label=label,
            scores=scores,
            highest_total_score=highest_total_score,
            weight=weight
        )

    @property
    def students(self):

        if self._students is None:

            male_std = None
            female_std = None
            last_idx = 0
            # male
            for idx, row in enumerate(self.used_range.rows):
                if str(row.value[1]).startswith('MALE'):
                    male_std = self.used_range.rows[idx + 1].expand('down')
                    last_idx = male_std.last_cell.row - 1
                    break
            # female
            for idx, row in enumerate(self.used_range.rows[last_idx:], start=last_idx):
                if str(row.value[1]).startswith('FEMALE'):
                    female_std = self.used_range.rows[idx + 1].expand('down')
                    break

            students = [std for std in male_std.rows]
            students.extend([std for std in female_std.rows])
            self._students = students

        return self._students

    @property
    def student_records(self):
        if self._student_records is None:
            student_records = []
            for rng in self.students:
                component_ranges = self.get_component_ranges(rng)
                components = [
                    self.generate_component(rng=rng,
                                            weight=head.weight,
                                            highest_total_score=head.highest_total_score,
                                            fixed_scores_length=len(head.scores)
                                            ) for head, rng in zip(self.head_components, component_ranges)
                ]
                student_records.append(
                    StudentRecord(name=rng.value[1], components=components)
                )

            self._student_records = student_records

        return self._student_records

    def save_sheet(self):
        for rng, record in zip(self.students, self.student_records):
            comp_ranges = self.get_component_ranges(rng)
            student_components = record.components
            for comp_rng, comp in zip(comp_ranges, student_components):
                comp_rng.value = comp.scores

        self.sheet.book.save()


class ClassRecord:
    def __init__(self, males: list, females: list) -> None:
        self.males = males
        self.females = females


if __name__ == '__main__':
    app = xw.App(visible=False, add_book=False)
    wb = app.books.open('D:/PycharmProjects/ClassGenie/GRADE-3-4TH-QUARTER-new.xlsx', update_links=False,
                        read_only=True)

    ws = wb.sheets['MTB']
    print(ws)
    cs = ClassSheet(ws)

    app.kill()
