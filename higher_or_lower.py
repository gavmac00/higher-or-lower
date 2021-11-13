import random as random

answer = random.randint(1,100) #goal
number = random.randint(1,100) #user number
print("A number has been chosen, between 1 and 100, the number you will start with is: " + str(number))

choice = input("Enter a number higher or lower than " + str(number) + ": ")
choice = int(choice)

counter = 1

if choice < answer:
    print("Go Higher")
else:    
    print("Go Lower")

while(choice != answer):
    choice = input("Enter a number higher or lower than " + str(number) + ": ")
    choice = int(choice)

    counter = counter + 1

    if choice == answer: break

    if choice < answer:
        print("Go Higher")
    else:    
        print("Go Lower")

print("Well done!, the answer was " + str(answer) + ", you took " + str(counter) + " goes.")