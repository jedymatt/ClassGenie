from record import Component, StudentRecord
from record.generate import randomize_student_record

# students = int(input('Number of students: '))
increment = 2
print('Grades:')
expected_grades = []
while True:
    grade = input()
    if grade != '':
        expected_grades.append(int(grade) + increment)
    else:
        break
print(len(expected_grades))
highest_ww = Component(scores=[20, 20, 20, 20], weight=0.3)
highest_pt = Component(scores=[5, 5, 5, 5], weight=0.7)

student_records = [StudentRecord(
    written_works=Component([], highest_ww.weight, sum(highest_ww.scores)),
    performance_tasks=Component([], highest_pt.weight, sum(highest_pt.scores)),
) for _ in range(len(expected_grades))]

for record in student_records:
    idx = student_records.index(record)
    randomize_student_record(record, expected_grades[idx], [highest_ww, highest_pt])


def print_component_scores(component: Component):
    for i in component.scores:
        print(i, end='\t')
    print()


print('WrittenWorks')
for record in student_records:
    print_component_scores(record.written_works)

print('PerformanceTasks')
for record in student_records:
    print_component_scores(record.performance_tasks)
