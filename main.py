from ast import Break
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
    print("1)Search for the tools \n")
    while(1):    
        ans=input("Enter the choice : ")
        if(ans=='1'):
            print("\n Where to search for the tools ?")
            print('''
1) Kitchen
2)Cells
3)Utility Rooms \n''')
            ans1=input("Enter the choice:")
            while(1):
                if(ans1=='1'):
                    print("Hurray....You found a spoon here \n")
                    
                    print('''Where to search for the tools ?
2)Cells
3)Utility Rooms \n''')
                    ans2=input("Enter the choice:")
                    if(ans2=='2'):
                        print(" While searching the cells, You found a saw hidden behind the sink \n ")
                        print('''Where to search for the tools ?
3)Utility Rooms \n''')
                    ans3=input("Enter the choice:")
                    if(ans3=='3'):
                        print("There you go....You saw an old vacuum cleaner kept at back at the trash box. Might have been there for months. \n ")
                        break
                    elif(ans2=='3'):
                        print("There you go....You saw an old vacuum cleaner kept at back at the trash box. Might have been there for months. ")
                        print('''\n Where to search for the tools ?
2)Cells \n''')
                    ans3=input("Enter the choice:")
                    if(ans3=='2'):
                        print(" While searching the cells, You found a saw hidden behind the sink  \n ")
                    break
                    
                elif(ans1=='2'):
                    print(" While searching the cells, You found a saw hidden behind the sink ")
                    
                    print('''Where to search for the tools ?
1) Kitchen
3)Utility Rooms \n''')
                    ans2=input("Enter the choice:")
                    if(ans2=='1'):
                        print("Hurray....You found a spoon here \n")
                        print('''Where to search for the tools ?
3)Utility Rooms \n''')
                        ans3=input("Enter the choice:")
                        if(ans3=='3'):
                            print("There you go....You saw an old vacuum cleaner kept at back at the trash box. Might have been there for months. ")        
                        break
                    elif(ans2=='3'):
                        print("There you go....You saw an old vacuum cleaner kept at back at the trash box. Might have been there for months. ")
                        print('''Where to search for the tools ?
2)Cells \n''')
                        ans3=input("Enter the choice:")
                        if(ans3=='2'):
                            print(" While searching the cells, You found a saw hidden behind the sink ")    
                        break

                elif(ans1=='3'):
                    print("There you go....You saw an old vacuum cleaner kept at back at the trash box. Might have been there for months. ")
                    
                    print('''Where to search for the tools ?
1) Kitchen
2)Cells \n''')
                    ans2=input("Enter the choice:")
                    if(ans2=='1'):
                        print("Hurray....You found a spoon here \n")
                        print('''Where to search for the tools ?
2)Cells \n''')
                        ans3=input("Enter the choice:")
                        if(ans3=='2'):
                           print(" While searching the cells, You found a saw hidden behind the sink ")    
                        break
                    elif(ans2=='2'):
                        print(" While searching the cells, You found a saw hidden behind the sink ")    
                        print('''Where to search for the tools ?
1)Kitchen \n''')
                        ans3=input("Enter the choice:")
                        if(ans3=='1'):
                            print("Hurray....You found a spoon here \n")
                        break
            break
        else:
                    print("\n Enter correct choice")

def seebehind():
    dte = '''what do you do? \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('''
1) Fight 
2) Ignore
3) Explain the plan\n''')
   
    while(1):
            ans= input("Enter the choice no: ")
            if(ans == '1'):
                print('''\nYOU DIE. YOU DONT FIGHT WITH FELLOW INMATES (BROCODE) ''')
                print("TRY AGAIN")
            elif(ans == '2'):
                print('''He Reports you to the warden and you get caught. ''')
                print("TRY AGAIN")
            elif(ans == '3'):
                print('''You think about the plan that you can't do shit on your own so you explain the plan to him and he seems interested. ''')
                print('''But he wants to include one another person to the plan ''')
                break
            else:
                print("Enter correct choice")
    
    dte = '''what do you do? \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('''
1)Include the other person in the plan
2) Refuse \n''')
    
    while(1):
            ans= input("Enter the choice no: ")
            if(ans == '1'):
               print('''Now that you are all together, you begin plotting your escape, but digging a tunnel is too common and requires somewhat more complicated tools. ''') 
               break 
            elif(ans == '2'):
                print('''You refuse to include the other person since its your own so the other two inmates rat you out to the guards and follows your plan. ''')
                print("TRY AGAIN")
            else:
                print("Enter correct choice")
    
def plan1():
    dte = '''what do you do? \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('''
1) Ask the other inmates
2) Think about your own plan
3) Explore the Prison\n''')
    while(1):
            ans= input("Enter the choice no: ")
            if(ans == '1'):
                print('''\nThe other inmates disagree after seeing the no of failed attempts as escaping the prison is nearly impossible.
36 men tried 14 separate escapes. Nearly all were caught or didn’t survive the attempt.''')
                print("TRY AGAIN")
            elif(ans == '2'):
                print('''You think of your own plan of escaping the prison.
You see a ceiling 30 meters high''')
                break
            elif(ans == '3'):
                print('''You start exploring the prison for something which can help you escape the hard life of being a prisoner and 
you came a across a ceiling which is 30 m up''')
                break
            else:
                print("Enter correct choice")
    
    sleep(4)
    clrscr()
    dte = '''what do you do? \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    print('''1) Climb the ceiling
2) Find some other plan \n ''')
    while (1):
            ans1=input("Enter your choice :")
            if(ans1=='1'):
                print("\n In order to climb the ceiling , you require tools. \n")
                tools()
                return
            elif(ans1=='2'):
                print("\n You think of diggin a tunnel but that's too common isn't but it requires tools too \n")
                tools()
                return
            else:
                print("Enter correct choice \n")

def plan2():
    print("\n While leaving the cell with all the tools you had , Someone interrupts you \n")
    dte = '''what do you do? \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    print('''\n 1) Run
    2) See Behind''')
    while(1):
            ans= input("Enter the choice no: ")
            if(ans == '1'):
                print('''\nYou started to run and gets caught by the guards. Your all tools are gone and you are now moved to more secure facility with much more sentence. So ESCAPING IS NOT AN OPTION. 
                TRY AGAIN''')
            elif(ans == '2'):
                print('''You check behind and you see that there is some inmate you stole the saw from , he looks familiar to you ''')
                seebehind()
                break
            else:
                print("Enter correct choice \n")

def makeboat():
    print('''You decide to set up a secret workshop in the empty top level of the cellblock.
You stole and gathered over fifty raincoats and deciding to turn them into makeshift life preservers and a 6x14 foot rubber raft, carefully stitching the seams together and "vulcanizing" them by the prison's hot steam pipes. ''')
    print('''Whoops! You completely forgot about the guards! They might notice your absence while you are in the workshop working on your plan.''')
    dte = '''what do you do? \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('''\n 1) Make dummy heads
    2) Bribe the guard
    3) Shoot the guard''')
    while(1):
            ans= input("Enter the choice no: ")
            if(ans == '1'):
                print('''You sculpt dummy heads out of a hand-made papier-mâché-like mixture of soap, toothpaste, concrete dust, and toilet paper, then give them a realistic appearance with paint from the maintenance shop and hair from the barbershop floor.
and then place them strategically in your bunks so that they appear to be sleeping ''')
                break
            elif(ans == '2'):
                print('''\nYou bribe the guard with money and alcohol that you stole and saved for later. But he still informs his officials about you, and you are sent to the dump to die.
                TRY AGAIN''')
            elif(ans == '3'):
                print('''Your escape plan is still incomplete. And committing another crime while in prison is not a wise decision. You are sent to solitary confinement.''')
            else:
                print("Enter correct choice \n")

def plan3():
    print('''As you consider alternative strategies, the air vent at the back of your cell catches your eye. 
You begin widening the ventilation ducts beneath the sinks using discarded saw blades found on the prison grounds, 
metal spoons from the mess hall, and the makeshift drill improvised from the motor of the broken vacuum cleaner.  ''')
    print('''uh but this hole is visible and if the guard comes by for his routine check, he might notice it and you will all be in big trouble. ''')
    
    dte = '''what do you do? \n \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('''
    1) Hide it
    2) Leave it
    3) Bribe the  guard''')
    while(1):
        ans= input("Enter the choice no: ")
        if(ans == '1'):
            print('''\nYou concealed the ducts with whatever you could find such as a suitcase or a piece of cardboard, etc.''')
            dte = '''Once the ducts becomes wide enough to pass through what do you do? \n \n'''
            for char in dte:
                sleep(0.20)
                sys.stdout.write(char)
                sys.stdout.flush()
            print("1)Enter the vent \n")
            while(1):    
                ans=input("Enter the choice : ")
                if(ans=='1'):
                    print('''On entering the vent you find a common, unguarded utility corridor.''')
                    print('''You three make your way down this corridor and up to the roof of the cell block inside the building.
The prison is surrounded by the cold, rough waters of the Pacific. So you'll need something to get to the other side.
''')        
                    dte = '''what do you do? '''
                    for char in dte:
                        sleep(0.20)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                    print('''\n 
            1) Make a boat
            2) Try swimming''')
                    while(1):    
                        ans12= input("Enter the choice no: ")
                        if(ans12 == '1'):
                            print('''You decide to set up a secret workshop in the empty top level of the cellblock.
You stole and gathered over fifty raincoats and deciding to turn them into makeshift life preservers and a 6x14 foot rubber raft, carefully stitching the seams together and "vulcanizing" them by the prison's hot steam pipes. ''')
                            print('''Whoops! You completely forgot about the guards! They might notice your absence while you are in the workshop working on your plan.''')
                            dte = '''what do you do? \n \n'''
                            for char in dte:
                                sleep(0.20)
                                sys.stdout.write(char)
                                sys.stdout.flush()
                            print('''\n 1) Make dummy heads
2) Bribe the guard
3) Shoot the guard''')
                            while(1):
                                ans= input("Enter the choice no: ")
                                if(ans == '1'):
                                    print('''You sculpt dummy heads out of a hand-made papier-mâché-like mixture of soap, toothpaste, concrete dust, and toilet paper, then give them a realistic appearance with paint from the maintenance shop and hair from the barbershop floor.
and then place them strategically in your bunks so that they appear to be sleeping ''')
                                    break
                                elif(ans == '2'):
                                    print('''\nYou bribe the guard with money and alcohol that you stole and saved for later. But he still informs his officials about you, and you are sent to the dump to die.
                TRY AGAIN''')
                                elif(ans == '3'):
                                    print('''Your escape plan is still incomplete. And committing another crime while in prison is not a wise decision. You are sent to solitary confinement.''')
                                else:
                                    print("Enter correct choice \n")
                        
                            break
                        
                        elif(ans12=='2'):
                            print('''you jumped into the water and attempted to swim to San Francisco, but quickly gave up. You drowned in the bay, and your body was swept out to sea by the bay's strong current. ''')
                            print('''TRY AGAIN''')
                    
                        else:
                            print("Enter correct choice \n")
                        
                    break

                else:
                    print("Enter correct choice \n")

            break

        elif(ans == '2'):
            print('''\nYou are caught by the guards, who then beat you with a baton before throwing you into The Dump. The cold and dark isolation ward is hard to survive. 
                TRY AGAIN''')
            
        elif(ans == '3'):
            print('''\nYou bribe the guard with money and alcohol that you stole and saved for later. But he still informs his officials about you, and you are sent to the dump to die.
                TRY AGAIN''')

        else:
            print("Enter correct choice \n")

def plan4():
    clrscr()
    dte='''11th June 1962 '''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
    print(''' \n \n The raft is ready and it is time to initiate the plan.\n''')
    print(''' You board the raft, launch it, and head two miles north to your destination, Angel Island. \n \n''')
    dte='''YOU ARE FREE !!! \n'''
    for char in dte:
        sleep(0.20)
        sys.stdout.write(char)
        sys.stdout.flush()
plan1()
plan2()
plan3()
plan4()
