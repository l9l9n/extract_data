from functools import reduce
from collections import defaultdict


def count_total_events(events):
    # считает общее количество событий в списке events
    return reduce(lambda acc, event: acc + 1, events, 0)


def count_events_user(events):
    # кол-во событий для каждого пользователя
    user_events = defaultdict(int)
    for event in events:
        user = event['user']
        user_events[user] += 1
    return dict(user_events)

