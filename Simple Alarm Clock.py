import time
from datetime import datetime

# Function to get alarm time from the user
def get_alarm_time():
    alarm_hour = int(input("Enter the alarm hour (1-12): "))
    alarm_minute = int(input("Enter the alarm minutes (0-59): "))
    period = input("Enter AM or PM: ").upper()
    alarm_time_str = f"{alarm_hour:02}:{alarm_minute:02} {period}"
    return alarm_time_str

# Function to check the current time against the alarm time
def check_alarm_time(alarm_time):
    while True:
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"Current time: {current_time}", end="\r")
        if current_time == alarm_time:
            print("\nIt's time to wake up!")
            break
        time.sleep(20)
       
# Main program execution
if __name__ == "__main__":
    print("Welcome to the Simple Alarm Clock!")
    alarm_time = get_alarm_time()
    print(f'Alarm set for {alarm_time}.')
    check_alarm_time(alarm_time)
