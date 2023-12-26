def calculate_target_heart_rate(age, resting_hr, intensity):
    max_heart_rate = 220 - age
    target_heart_rate = (((max_heart_rate - resting_hr) * intensity) + resting_hr)
    return target_heart_rate

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def main():
    age = get_integer_input("Enter your age: ")
    resting_hr = get_integer_input("Enter your resting heart rate: ")

    print("\nIntensity | Target Heart Rate")
    print("----------|-------------------")

    for intensity in range(55, 96, 5):
        target_hr = calculate_target_heart_rate(age, resting_hr, intensity / 100)
        print(f"{intensity}%      | {int(target_hr)} bpm")


main()
