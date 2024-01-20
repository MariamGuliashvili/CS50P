import random
while True:
    try:
        n = int(input("Level: "))
        number = random.randint(1, n)
        guess = int(input("Guess: "))
        if guess < number:
            print("Too small!")
            continue
        elif guess > number:
            print("Too Large!")
            continue
        else:
            print("Just right!")
    except ValueError:
        continue
        
    break
