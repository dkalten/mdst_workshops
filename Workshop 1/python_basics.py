"""
MDST Workshop 1 - Python Basics Starter Code
"""
import random
import base64
# Add any imports you need here:


def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    if(num%2==0):
        print("Even")
    else:
        print("Odd")

def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    num=random.randint(0, 9)
    guessstr=input("Guess: ")
    while(guessstr!="exit"):
        guessint=int(guessstr)
        if(guessint<num):
            print("Too low")
        elif (guessint>num):
            print("Too high")
        else:
            print("You got it!")
        guessstr=input("Guess: ")
                  
def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    s2=string[::-1]
    print(s2==string)


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    f=open(filename,"w")
    
    f.write(str(base64.b64encode(username.encode("utf-8")),"utf-8"))
    f.write("\n")
    f.write(str(base64.b64encode(password.encode("utf-8")),"utf-8"))
    f.close()

def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    f=open(filename,'r')
    i=0
    user=""
    for line in f:
        if(i<3):
            user=base64.b64decode(line)
            i=5
        print(base64.b64decode(line))
    f.close()
    if(password!=None):
        f2=open(filename,"w")
        f2.write(str(base64.b64encode(user),"utf-8"))
        f2.write("\n")
        f2.write(str(base64.b64encode(password.encode("utf-8")),"utf-8"))
        f2.close()
if __name__ == "__main__":
    #part1(3)  # odd!
    #part1(4)  # even!
    #part2()
    #part3("ratrace")  # False
    #part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
