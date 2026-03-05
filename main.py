from loads_csv import load_csv
from metric import count_total_events


events = load_csv('events-1.csv')
total_events = count_total_events(events)

print(f"events: {total_events}")


if __name__ == "__main__":
    pass