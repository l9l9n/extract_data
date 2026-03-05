from loads_csv import load_csv
from metric import count_total_events, count_events_user, count_events_action, action_user


events = load_csv('events-1.csv')


print(f"Total events: {count_total_events(events)}")

print(f"Events user: {count_events_user(events)}")

print(f"Events action: {count_events_action(events)}")

print(f"Action user: {action_user(events)}")














if __name__ == "__main__":
    pass