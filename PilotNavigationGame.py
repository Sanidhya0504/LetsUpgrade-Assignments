import random

print("Welcome to pilot navigation game.")
print("You are the pilot of a plane and you need to land at the upcoming Airport.")
print(" For landing the plain you need to attain the Altitude of 3000ft, which is safe for landing.")
print(" Above 6000ft you will not be allowed to land")
print(" If the plane is between 3000ft and 6000ft there will be 75% chance for a safe landing")
print(" Altitude between 3000ft and 1000ft is safe for landing")
print("Beware!! going below 1000ft will crash the plane")
h = int(input("Enter the current height of the plane"))
print("Use 'W' to move up, 'S' to move down and 'A' to ask for landing")

while h>1000:
    if h>3000:
        while h > 3000:
            n=input()
            if n == 'w' :
                h=h+250
                print(h)
            elif n == 's' :
                h=h-250
                print(h)
            elif n == 'a' :
                if h>=6000 :
                    print("Permission Denied!! Height too much. Not safe to land")
                    print("Navigate the plane with 'W' and 'S'")
                elif h>3000 and h<6000 :
                    print("Permission Granted!! But height is still too much. 75% chances of safe landing.")
                    print("Press D to land or press C to cancel landing")
                    choice=input()
                    if choice == 'd':
                        print("Opening landing gear")
                        li=[0,0,0,1]
                        success=random.choice(li)
                        if success == 0:
                            print("Congratulations! Plane landed successfully")
                        else :
                            print("Game Over!! The plane crashed")
                    if choice == 'c':
                        print("Landing Canceled. Navigate the plane with 'W' and 'S'")

    elif h<=3000 and h>1000:
        while h>1000:
            n = input()
            if n == 'w':
                h = h + 250
                print(h)
            elif n == 's':
                h = h - 250
                print(h)
            elif n == 'a':
                print("Permission Granted!! Safe to land")
                print("Press D to land or press C to cancel landing")
                choice = input()
                if choice == 'd':
                    print("Opening landing gear")
                    print("Congratulations! Plane landed successfully")
                if choice == 'c':
                    print("Landing Canceled. Navigate the plane with 'W' and 'S'")


if h<=1000 :
    print("Game Over!! The height became too low. The plane crashed")