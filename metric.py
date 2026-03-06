from functools import partial
from collections import defaultdict
from itertools import groupby




def count_total_events(events):
    return len(events)


def count_events_user(events):
    user_events = defaultdict(int)
    for event in events:
        user = event['user']
        user_events[user] += 1
    return dict(user_events)


def count_field(events, field):
    field_events = defaultdict(int)
    for event in events:
        value = event[field]
        field_events[value] += 1
    return dict(field_events)

count_events_action = partial(count_field, field='action')


def action_user(events):
    rusult = {}
    events_sorted = sorted(events, key=lambda e: e['user'])

    for user, group in groupby(events_sorted, key=lambda e: e['user']):
        action_counts = defaultdict(int)

        for event in group:
            action_counts[event['action']] += 1
        rusult[user] = dict(action_counts)

    return rusult


def top_users(users):
    return sorted(users.items(), key=lambda x: x[1], reverse=True)



def analyz_sessions(events):
    sessions = defaultdict(lambda: {"completed": 0, "incomplete": 0})
    active_sessions = defaultdict(int)

    for event in events:

        user = event["user"]
        action = event["action"]

        if action == "login":
            active_sessions[user] += 1

        elif action == "logout":

            if active_sessions[user] > 0:
                active_sessions[user] -= 1
                sessions[user]["completed"] += 1

    for user, count in active_sessions.items():
        sessions[user]["incomplete"] += count

    return dict(sessions)
