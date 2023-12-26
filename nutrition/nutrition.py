
user_input = input("Enter a fruit: ").lower()

fruit_calories = {
    "apple": 130,
    "avocado": 50,
    "sweet cherries": 100,
    "kiwifruit": 90,
    "pear": 100,
}

if user_input in fruit_calories:
    calories = fruit_calories[user_input]
    print("Calories:", calories)
else:
    False