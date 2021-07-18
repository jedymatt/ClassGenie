import random

from class_record import StudentRecord, Component


class MaximumLoopReached(RuntimeError):
    def __init__(self, *args):
        super().__init__(*args)


def random_scores(highest_scores: list, threshold=1.0, existing_scores: list = None):
    if threshold > 2:
        raise ValueError('Threshold exceeded to 2.0, it should be in 1.0 - 2.0')

    if existing_scores is None:
        return [random.randint(round(threshold * score) - score, score) for score in highest_scores]

    if len(existing_scores) != len(highest_scores):
        raise ValueError('length of highest scores and existing scores is not equal.')

    return [random.randint(round(threshold * highest) - highest, highest) if existing is None else existing
            for highest, existing in zip(highest_scores, existing_scores)]


def randomize_student_record(sr: StudentRecord, expected_average, highest_component: list[Component],
                             max_loop=500, threshold=1.5, overwrite_all=True, average_limit=100):
    old_scores = [component.scores for component in sr.components]

    existing_scores = old_scores if overwrite_all is False else ([None] * len(old_scores))

    if sr.transmuted_average > average_limit:
        return

    loop_count = 0
    while sr.transmuted_average != expected_average and loop_count <= max_loop:

        for idx, component in enumerate(sr.components):
            component.scores = random_scores(highest_component[idx].scores, threshold,
                                             existing_scores=existing_scores[idx])

            loop_count += 1

    if loop_count > max_loop:

        for idx, component in enumerate(sr.components):
            component.scores = old_scores[idx]

        raise MaximumLoopReached('Maximum loop reached.')
