import random

def elso():
    rnd = random.randint(1, 50)
    print(f"I/A:\n\t A generált szám: {rnd}")
    if rnd % 5 == 0:
        print("I/B:\n\t A szám öttel osztható!")
    elif rnd % 3 == 0:
        print("I/B:\n\t A szám hárommal  osztható!")
    elif rnd % 5 and 3 == 0:
        print("I/B:\n\t A szám öttel és hárommal is osztható!")