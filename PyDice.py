from time import sleep
import random

print("select your dice")
print("""1. Cube dice
2. Tetrahedron dice
3. n Dices
 """)

# def Rolling():
#     i=3
#     print("\nRolling the dice in ")
#     while i >= 1:
#         p1 = "." * i
#         print(f"{i}{p1}"); sleep(1)
#         i -= 1


def Cube():
    #print("You have selected Cube dice")
    #print("A common die. The sum of the numbers on opposite faces is 7."); sleep(3)
    val = random.randint(1,6)
    Rolling()
    print(f"You got: {val}")


def Tetrahedron():
    #print("You have selected Tetrahedron dice")
    #print("Each face has three numbers, arranged such that the upright number, placed either near the vertex or near the opposite edge, is the same on all three visible faces. The upright numbers represent the value of the roll.")
    #print("\nFace values are:\nFace 1: 1 2 3 \nFace 2: 4 5 6\nFace 3: 7 8 9\nFace 4: 10 11 12");
    val = random.randint(1,12)
    Rolling()
    if val >= 1 and val <= 3:
        print("You rolled Face 1") ;sleep(2)
        print(f"You got: {val}")
    elif val >= 4 and val <= 6:
        print("You rolled Face 2") ;sleep(2)
        print(f"You got: {val}")
    elif val >= 7 and val <= 9:
        print("You rolled Face 3") ;sleep(2)
        print(f"You got: {val}")
    else:
        print("You rolled Face 4") ;sleep(2)
        print(f"You got: {val}")


def N_Dice():
    i=1
    sum = 0
    num = int(input("Enter the number of dices \n>"))
    Rolling()
    while i <= num:
        val = random.randint(1,6)
        print(f"Dice {i} value: {val}"); #sleep(1.5)
        i += 1
        sum += val
    print(f"Sum of all rolled value is {sum}")

choice  = int(input(">"))

if choice == 1:
    Cube()
elif choice == 2:
    Tetrahedron()
elif choice == 3:
    N_Dice()
else:
    pritn("Invalid options")






















































#     def Set6():
#     print("This is a common dice where you can set the probablity of 6 to be rolled")
#     a = int(input("Enter percentage\n> "))
#     p = random.randint(1,100)
#     Rolling()
#     if a <= 100:
#         if p <= a:
#             print("6")
#         else:
#             print("You got :",random.randint(1,5))
#     else:
#         print("That will only roll 6")

# Set6()
