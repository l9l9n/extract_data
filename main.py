from loads_csv import load_csv
from metric import count_total_events, count_events_user, count_field


events = load_csv('events-1.csv')
total_events = count_total_events(events)
user_events = count_events_user(events)
count_event_action = count_field(events, 'action')

# print(f"events: {total_events}")
# print(f"events user: {user_events}")
print(f"events field: {count_event_action}")


if __name__ == "__main__":
    pass