from functools import reduce, partial
from collections import defaultdict
from itertools import groupby


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


def count_field(events, field):
    # кол-во событий для каждого значения поля field
    field_events = defaultdict(int)
    for event in events:
        value = event[field]
        field_events[value] += 1
    return dict(field_events)

count_events_action = partial(count_field, field='action')


def action_user(events):
    # кол-во событий для каждого действия и пользователя
    rusult = {}
    events_sorted = sorted(events, key=lambda e: e['user'])

    for user, group in groupby(events_sorted, key=lambda e: e['user']):
        action_counts = defaultdict(int)

        for event in group:
            action_counts[event['action']] += 1
        rusult[user] = dict(action_counts)

    return rusult
