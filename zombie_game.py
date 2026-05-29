import random

health = 100

print("=== Zombie Survival Game ===")
print("Survive as long as possible.\n")

while health > 0:
    print("\nYour health:", health)

    action = input("Choose action (run / fight / hide): ").lower()

    zombie_attack = random.randint(10, 30)

    if action == "run":
        print("You escaped safely!")

    elif action == "fight":
        if random.choice([True, False]):
            print("You defeated the zombie!")
        else:
            health -= zombie_attack
            print("The zombie attacked you!")

    elif action == "hide":
        print("You are hiding...")

    else:
        print("Invalid action")

    if health <= 0:
        print("\nGame Over. You did not survive.")
