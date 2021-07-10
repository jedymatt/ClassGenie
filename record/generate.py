import random

from record import StudentRecord, transmute_grade, Component


def random_scores(highest_scores: list, threshold=1.0):
    if threshold > 2:
        raise ValueError('Threshold exceeded to 2.0, should be 1.0 - 2.0')

    return [random.randint(round(threshold * score) - score, score) for score in highest_scores]


def randomize_student_record(student_record: StudentRecord, expected_average, highest_component: list[Component]):
    while transmute_grade(student_record.initial_average()) != expected_average:
        components = student_record.components()

        for i in range(len(components)):
            component: Component = components[i]
            component.scores = random_scores(highest_component[i].scores, 1.5)


if __name__ == '__main__':
    ww = Component([10, 10, 20, 10], 85, 0.50)
    pt = Component([11, 13, 20, 18], 75, 0.50)

    sr = StudentRecord(
        written_works=ww,
        performance_tasks=pt,
    )
    highest_components = [
        Component([20, 25, 20, 20], 85, 0.50),
        Component([15, 15, 25, 20], 75, 0.50)
    ]

    randomize_student_record(sr, 91, highest_components)
    print(sr.written_works.weighted_average(), sr.performance_tasks.weighted_average())
    print(sr.initial_average())
    print(transmute_grade(sr.initial_average()))
    print(sr.written_works.scores, sr.performance_tasks.scores)
