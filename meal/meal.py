def main():
    # Prompt the user for input
    user_input = input("what time is it? ")

    # Check if the input is a valid time format
    if validate_time_format(user_input):
        # Convert the user input to hours as a float
        hours = convert(user_input)

        # Check which mealtime it is and print the result
        if is_breakfast_time(hours):
            print("breakfast time")
        elif is_lunch_time(hours):
            print("lunch time")
        elif is_dinner_time(hours):
            print("dinner time")

def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = time.split(":")

    # Convert hours and minutes to integers
    hours = int(hours)
    minutes = int(minutes)

    # Calculate the total hours, including minutes as a fraction of an hour
    total_hours = hours + minutes / 60

    return total_hours

def validate_time_format(time):
    # Split the time string into hours and minutes
    hours, minutes = time.split(":")

    # Check if hours and minutes are valid integers
    if hours.isdigit() and minutes.isdigit():
        # Convert hours and minutes to integers
        hours = int(hours)
        minutes = int(minutes)

        # Check if hours are in the valid range (0-23) and minutes are in the valid range (0-59)
        if 0 <= hours <= 23 and 0 <= minutes <= 59:
            return True

    # If any condition fails, return False
    return False

def is_breakfast_time(hours):
    return 7 <= hours < 8

def is_lunch_time(hours):
    return 12 <= hours <= 13

def is_dinner_time(hours):
    return 18 <= hours < 19

if __name__ == "__main__":
    main()
