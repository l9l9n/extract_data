from loads_csv import load_csv
from metric import count_total_events, count_events_user, count_events_action, action_user, top_users, analyz_sessions
from report import print_report



events = load_csv('events-1.csv')

total = count_total_events(events)

user = count_events_user(events)

action = count_events_action(events)

sessions = analyz_sessions(events)

top = top_users(user)

print_report(total, user, action, sessions, top)




if __name__ == "__main__":
    pass



# print(f"Total events: {count_total_events(events)}")
# print(f"Events user: {count_events_user(events)}")
# print(f"Events action: {count_events_action(events)}")
# print(f"Action user: {action_user(events)}")
# print(f"Top users: {top_users(events)}")
# print(f"Analyze sessions: {analyze_sessions(events)}")