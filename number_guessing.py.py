
import random

print("=" * 50)
print("🎯          NUMBER GUESSING GAME          🎯")
print("=" * 50)

print("\n📌 Choose Difficulty")
print("┌────────────────────────────────────┐")
print("│ 1️⃣  Easy    → 10 Attempts          │")
print("│ 2️⃣  Medium  → 7 Attempts           │")
print("│ 3️⃣  Hard    → 5 Attempts           │")
print("└────────────────────────────────────┘")


def play_game():

    secret_number = random.randint(1, 100)
    

    choice = input("\n🎮 Enter difficulty level (1-3): ")

    if choice == "1":
        max_attempts = 10
    elif choice == "2":
        max_attempts = 7
    elif choice == "3":
        max_attempts = 5
    else:
        print("❌ Wrong Choice!")
        return

    attempts = 0
    count = []

    print("\n" + "=" * 50)
    print("🎲 Game Started!")
    print("Guess a number between 1 and 100")
    print("=" * 50)

    while True:

        guess = int(input("\n🔢 Enter your guess: "))
        difference = abs(guess - secret_number)
        
        
        if difference  <= 5:
              print( "🔥 Very Close")
        elif difference  <= 15:
            print( " 😊 Close")
        elif  difference <=30:
             print( "😮 Far")
        else:
            print(" 🥶 very Far")
                 
        
        
        
        if guess in count:
            print("⚠️ You've already guessed that number!")
            continue

        count.append(guess)
        attempts += 1

        print("\n📜 Guess History :", count)

        remaining = max_attempts - attempts
        print("❤️ Remaining Attempts :", remaining)

        if guess == secret_number:

            print("\n" + "=" * 50)
            print("🎉 CONGRATULATIONS 🎉")
            print(f"🏆 You guessed the number in {attempts} attempts.")
            print("=" * 50)
            break

        elif guess > secret_number:

            print("📉 Too High! Try a lower number.")

        else:

            print("📈 Too Low! Try a higher number.")

        if attempts >= max_attempts:

            print("\n" + "=" * 50)
            print("💀 GAME OVER")
            print(f"🎯 Secret Number was : {secret_number}")
            print("=" * 50)
            break


def play_again():

    while True:

        ask = input("\n🔄 Do you want to play again? (yes/no): ")

        if ask.lower() == "yes":
            play_game()

        elif ask.lower() == "no":
            print("\n👋 Thanks for playing!")
            break

        else:
            print("❌ Please enter only yes or no.")


play_game()
play_again()