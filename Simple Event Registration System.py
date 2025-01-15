# List to store events
events = []

# Function to create a new event
def create_event():
    name = input("Event Name: ")
    date = input("Event Date: ")
    location = input("Event Location: ")
    capacity = int(input("Event Capacity: "))
    events.append({"name": name, "date": date, "location": location, "capacity": capacity, "participants": []})
    print(f'Event {name} created successfully!')

# Function to list all events
def list_events():
    for event in events:
        print(f"{event['name']} on {event['date']} at {event['location']} ({len(event['participants'])}/{event['capacity']} participants)")

# Function to register a participant for an event
def register_for_event():
    event_name = input("Event Name: ")
    for event in events:
        if event['name'] == event_name:
            if len(event['participants']) < event['capacity']:
                name = input("Participant Name: ")
                email = input("Participant Email: ")
                event['participants'].append({"name": name, "email": email})
                print(f"{name} has been Successfully registered for '{event_name}'.")
            else:
                print("Event is full.")
            return
    print("Event not found.")

# Function to generate the participant list for an event
def generate_participant_list():
    event_name = input("Event Name: ")
    for event in events:
        if event['name'] == event_name:
            print(f"Participants for {event_name}:")
            for i, participant in enumerate(event['participants'], start=1):
                print(f"{i}. {participant['name']} ({participant['email']})")
            return
    print("Event not found.")

# Main program loop
while True:
    print("\n1. Create Event\n2. List Events\n3. Register for Event\n4. Generate Participant List\n5. Exit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        create_event()
    elif choice == 2:
        list_events()
    elif choice == 3:
        register_for_event()
    elif choice == 4:
        generate_participant_list()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")
