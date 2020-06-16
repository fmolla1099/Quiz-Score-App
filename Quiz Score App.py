import time

score = 0

name = str(input("What's your name? "))
print("Welcome, "+name+" to the quiz!")

def scorePlus():
    global score
    score += 1
    print("Your score: " ,score)

def scoreMinus():
    global score
    score -= 1
    print("Your score: " ,score)
def q1():
    global score
    print("\n1. What is El Capitan?")
    time.sleep(0.5)
    print("a) An operating system for Windows")
    print("b) An operating system for Mac")
    print("c) A third-party application\n")

    answer = str(input("What's the right answer: "))

    if answer == "b":
        print("well done, that's correct!")
        scorePlus()
    else:
        print("Sorry, that was the wrong answer!")
        scoreMinus()

    q2()

def q2():
    global score
    time.sleep(0.5)
    print("\n2. What is Apple's latest device?")
    print("a) iPhone")
    print("b) MacBook Pro")
    print("c) iPod Touch\n")

    answer = str(input("What's the right answer: "))

    if answer == "b":
        print("well done, that's correct!")
        scorePlus()
    else:
        print("Sorry, that was the wrong answer!")
        scoreMinus()
        

    q3()

def q3():
    global score
    time.sleep(0.5)
    print("\n3. Who is the CEO of KARSID?")
    print("a) Karthik N")
    print("b) Bill G")
    print("c) Steve J\n")

    answer = str(input("What's the right answer: "))

    if answer == "a":
        print("well done, that's correct!")
        scorePlus()
    else:
        print("Sorry, that was the wrong answer!")
        scoreMinus()

q1()
