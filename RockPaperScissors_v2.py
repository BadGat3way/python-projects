# Rock, Paper, Scissors!

import random as rn
logfile = open("/home/dashtrox/Documents/Playlog.txt","w")

print ("ROCK, PAPER, SCISSORS")
win=0
loss=0
tie=0
print ("Wins =",win,", Losses =",loss,", Ties =",tie)

move = input("Enter you move: (r)ock, (p)aper, (s)cissors or (q)uit\n")

possmoves = ['ROCK','PAPER','SCISSORS']
possmovedict = {'ROCK':'r','PAPER':'p','SCISSORS':'s'}
while move.lower not in ['r','p','s']:
    print ("\nWrong Input! Try Again")
    move = input("Enter you move: (r)ock, (p)aper, (s)cissors or (q)uit\n")
    
    
while move.lower() != 'q':
    sysmove = rn.choice(possmoves)

    if move.lower() == 'p':
        print ("\nPAPER versus....")
        print (sysmove)
        if possmovedict[sysmove] == 'p':
            print ("It's a tie!")
            tie+=1
        elif possmovedict[sysmove] == 'r':
            print ("You win!")
            win+=1
        elif possmovedict[sysmove] == 's':
            print ("You lose!")
            loss+=1

    elif move.lower() == 'r':
        print ("\nROCK versus....")
        print (sysmove)
        if possmovedict[sysmove] == 'p':
            print ("You lose!")
            loss+=1
        elif possmovedict[sysmove] == 'r':
            print ("It's a tie!")
            tie+=1
        elif possmovedict[sysmove] == 's':
            print ("You win!")
            win+=1
            
    elif move.lower() == 's':
        print ("\nSCISSORS versus....")
        print (sysmove)
        if possmovedict[sysmove] == 'p':
            print ("You win!")
            win+=1
        elif possmovedict[sysmove] == 'r':
            print ("You lose!")
            loss+=1
        elif possmovedict[sysmove] == 's':
            print ("It's a tie!")
            tie+=1

    print ("\nWins =",win,", Losses =",loss,", Ties =",tie)
    move = input("\nEnter you move: (r)ock, (p)aper, (s)cissors or (q)uit\n")
    
    
logfile.close()