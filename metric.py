from functools import reduce


def count_total_events(events):
    # считает общее количество событий в списке events
    return reduce(lambda acc, event: acc + 1, events, 0)