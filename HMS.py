import datetime


def gettime():
    # This function prints Date and Time in the file whenever it is updated/logged
    return datetime.datetime.now()


def F1(k):
    # This function is for user input
    if k == 1:
        c = int(input("\nEnter 1 for Workout and 2 for Diet:-"))
        if c == 1:
            value = input("Type here\n")
            with open("YashWorkout.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successful!")
        elif c == 2:
            value = input("Type here\n")
            with open("YashDiet.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successful!")
    elif k == 2:
        c = int(input("Enter 1 for Workout and 2 for Diet:-\n"))
        if c == 1:
            value = input("Type here\n")
            with open("SurajWorkout.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
                print("Successful!")
        elif c == 2:
            value = input("Type here\n")
            with open("SurajDiet.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
                print("Successful!")
    elif k == 3:
        c = int(input("Enter 1 for Workout and 2 for Diet:-\n"))
        if c == 1:
            value = input("Type here\n")
            with open("RaviWorkout.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
                print("Successful!")
        elif c == 2:
            value = input("Type here\n")
            with open("RaviDiet.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
                print("Successful!")

    else:
        print("Invalid input!")


def retrieve(k):
    # This function is to retrieve the file content
    if k == 1:
        c = int(input("Enter 1 for Workout and 2 for Diet:-\n"))
        if c == 1:
            with open("YashWorkout.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("YashDiet.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:
        c = int(input("Enter 1 for Workout and 2 for Diet:-\n"))
        if c == 1:
            with open("SurajWorkout.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("SurajDiet.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 3:
        c = int(input("Enter 1 for Workout and 2 for Diet:-\n"))
        if c == 1:
            with open("RaviWorkout.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("RaviDiet.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Invalid input!\n")


print("\nHealth Management System\n")
a = int(input("1:-To log\n""2:-To retrieve \n"))

if a == 1:
    b = int(input("1:-Yash\n""2:-Suraj\n""3:-Ravi\n"))
    F1(b)
else:
    b = int(input("1:-Yash\n""2:-Suraj\n""3:-Ravi\n"))
    retrieve(b)
