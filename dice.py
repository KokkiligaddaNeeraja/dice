import random
def roll_dice():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)
def main():
    print("Welcome to the Roll the Dice Game!")
    while True:
        input("Press Enter to roll the dice...")
        number = roll_dice()
        print(f"You rolled a {number}!")
        roll_again = input("Do you want to roll again? (yes/no): ").lower()
        if roll_again not in ['yes', 'y']:
            print("Thank you for playing. Goodbye!")
            break
if __name__ == "__main__":
    main()
