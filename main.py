from time import sleep
import sys
import os
def clrscr():
    _ = os.system("clear")


print('''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠋⠈⠀⠀⠀⠀⠐⠺⣖⢄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⢀⡆⠀⠀⠀⢋⣭⣽⡚⢮⣲⠆⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⡼⠀⠀⠀⠀⠈⠻⣅⣨⠇⠈⠀⠰⣀⣀⣀⡀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⢷⣶⠶⣃⢀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠈⠓⠚⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⡠⠀⡄⣀⠀⠀⠀⢻⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠐⠉⠀⠀⠙⠉⠀⠠⡶⣸⠁⠀⣠⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣦⡆⠀⠐⠒⠢⢤⣀⡰⠁⠇⠈⠘⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠠⣄⣉⣙⡉⠓⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⠀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            THE ROCK
''')

def intro():
    dte='''11 DECEMBER 1962
Alcatraz Federal Penitentiary, United States \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()

    dte1 = '''You commited the crime of bank robbery and now serving a sentence at Alcatraz Federal Penitentiary.
Its been days since you saw sunlight in the most secure prison in the world. 
also the food here is pretty bad but that's not the only reason you want to escape 
You want to continue the legacy of your prison escapes.'''
    for char in dte1:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(2)
    print("\nErr....")
    sleep(2)
    print("Errrrrr")
    sleep(2)
    print('''
So
You decided to escape the prison
Now you need a plan
    ''')
    sleep(5)
intro()
clrscr()

def tools():
    dte = '''what do you do? \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("1)Search for the tools")
    ans=input("Enter the choice : ")
    if(ans=='1'):
        print("Where to search for the tools ?")
        while(1):
            print('''1) Kitchen"
            2)Cells
            3)Utility Rooms''')
            ans1=input("Enter the choice:")
            if(ans1=='1'):
                print("Hurray....You found a spoon here")
            elif(ans1=='2'):
                print(" While searching the cells, You found a saw hidden behind the sink ")
            elif(ans1=='3'):
                print("There you go....You saw an old vacuum cleaner kept at back at the trash box. Might have been there for months. ")
            else:
                print("Enter the correct choice")
                return

    else:
        print("Enter correct choice")


def plan1():
    dte = '''what do you do? \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(2)
    print('''
1) Ask the other inmates\n
2) Think about your own plan\n
3) Explore the Prison\n''')
    while(1):
            ans= input("Enter the choice no: ")
            if(ans == '1'):
                print('''\nThe other inmates disagree after seeing the no of failed attempts as escaping the prison is nearly impossible.
        36 men tried 14 separate escapes. Nearly all were caught or didn’t survive the attempt.''')
            elif(ans == '2'):
                print('''You think of your own plan of escaping the prison.
            You see a ceiling 30 meters high''')
            return
    clrscr()
    dte = '''what do you do? \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(2)
        print('''1) Climb the ceiling
        2) Find some other plan
        ''')
        while (1):
            ans1=input("Enter your choice :")
            if(ans1=='1'):
                print("In order to climb the ceiling , you require tools.")
                tools()
                return
            elif(ans1=='2'):
                print("You think of diggin a tunnel but that's too common isn't but it requires tools too")
                tools()
                return
            else:
                print("Enter correct choice")

plan1()

