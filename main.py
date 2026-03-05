from loads_csv import load_csv
from metric import count_total_events, count_events_user


events = load_csv('events-1.csv')
total_events = count_total_events(events)
user_events = count_events_user(events)

# print(f"events: {total_events}")
# print(f"events user: {user_events}")


if __name__ == "__main__":
    pass