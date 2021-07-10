import os.path
from collections import namedtuple

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
    def __init__(self, scores: list, weight: float, highest_total_score: int = -1):
        self.scores = scores
        self.highest_total_score = highest_total_score
        self.weight = weight

        if sum(scores) > highest_total_score != -1:
            raise ValueError("Sum of scores exceeded the highest_total_score.")

    def _percentage_score(self):
        return round((sum(self.scores) / self.highest_total_score) * 100, 2)

    def weighted_average(self):
        return round(self._percentage_score() * self.weight, 2)


class StudentRecord:
    def __init__(self, written_works, performance_tasks, quarterly_assessment=None):
        self.written_works = written_works
        self.performance_tasks = performance_tasks
        self.quarterly_assessment = quarterly_assessment

        if not self.is_valid_weight():
            raise ValueError("Total weight is not 1 or 100%")

    def is_valid_weight(self):
        weights = [component.weight for component in
                   [self.written_works, self.quarterly_assessment, self.performance_tasks] if component is not None]
        return sum(weights) == 1

    def initial_average(self):
        weighted_averages = [component.weighted_average() for component in
                             [self.written_works, self.quarterly_assessment, self.performance_tasks] if
                             component is not None]

        return sum(weighted_averages)

    def transmuted_average(self):
        return transmute_grade(self.initial_average())

    def components(self):
        return [component for component in [self.written_works, self.performance_tasks, self.quarterly_assessment] if
                component is not None]


if __name__ == '__main__':
    ww = Component([10, 10, 20, 10], 0.50, 85)
    pt = Component([11, 13, 20, 18], 0.50, 75)
    print(ww.weighted_average(), pt.weighted_average(), ww.weighted_average() + pt.weighted_average())

    student_record = StudentRecord(
        written_works=ww,
        performance_tasks=pt
    )

    print(student_record.initial_average())
    print(transmute_grade(student_record.initial_average()))
