from graphics import *


def greet(name):
    print("Hello", name + ".")
    if len(name) > 20:
        print("That's a long name!")


def canYouVote(age):
    if age >= 18:
        print("You can vote")
    else:
        print("Sorry, you can't vote")


def getDegreeClass(mark):
    if mark >= 70:
        return "1st"
    elif mark >= 60:
        return "2:1"
    elif mark >= 50:
        return "2:2"
    elif mark >= 40:
        return "3rd"
    else:
        return "Fail"


# We'll simplify this isLeapYear function in a later lecture / tutorial.
def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def daysInMonth(month, year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        return 31


def overlyComplexDaysInMonth(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or \
       month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif isLeapYear(year):
        return 29
    else:
        return 28


def countDown():
    for i in range(10, 0, -1):
        print("{} ...".format(i), end=" ")
    print("Blast Off!")


def exerciseRoutine():
    for day in range(1, 8):  # Outer loop (days)
        print("Currently on day {}".format(day))
        for exercise in range(1, 4):  # Inner loop (exercises)
            print("\tDoing exercise{} of day {}".format(exercise, day))


def numberedTriangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def drawPatch():
    win = GraphWin("Patch", 100, 100)
    for y in range(10, 100, 20):
        for x in range(10, 100, 20):
            circle = Circle(Point(x, y), 10)
            circle.draw(win)

            if (y == 30 or y == 70) and x >= 30 and x <= 70:
                circle.setFill("red")
            elif y == 50 and x >= 30 and x <= 70:
                circle.setFill("blue")
            else:
                circle.setFill("green")


# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


# For exercise 8
def drawColouredEye(win, centre, radius, colour):
    pass
    # remove the pass and add your code here
