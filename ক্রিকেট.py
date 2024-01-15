print("Rules of the game: 2 overs and 3 wickets available for each side")
print("")
import random
toss=random.randint(1,2)
penalty=0
if toss == 1:
    print ("You are batting first")
    print ("DISCLAIMER: Entering numbers out of range will result in penalty for the opponent, as it is considered unfair means of game")
    w,r=0,0
    balls=0
    while (w<=2) and (balls<12):
        x=random.randint(1,6)
        y=int(input("Choose your number between 0 to 6:"))  #Defense allowed for batting side
        print ("Computer selected:", x)
        if (y>=7 or y<0):
            penalty=penalty+1
        if (x!=y) and (y<=6 and y>0):
            r=r+y
        if x==y:
            w+=1
        balls=balls+1
    print ("You scored ", r , " runs")
    strike_rate=(r/balls)*100
    print("Your batting strike rate: ", strike_rate)
    print("")
    print("You are bowling")
    w1,r1=0,0
    ball=0
    while (w1<=2) and (ball<12):
        x=random.randint(0,6)
        y=int(input("Choose number between 1 to 6:")) #Defense allowed only for batting side
        print ("Computer selected:", x)
        if y>6 or y<1:
            penalty=penalty+1
            ball=ball-1
        if x!=y:
            r1=r1+x
        if x==y and y>0 and y<=6:
            w1+=1
        ball+=1
        if r1>r:
            break
    r1=r1+penalty
    print ("Computer scored ", r1 , " runs")
    if w!=0:
        sr=ball/w
        print ("Your bowling strike rate:", sr)
    if (r>r1):
        print ("You won")
    if (r1>r):
        print ("You lost")
    if (r1==r):
        print ("Match tied")
    
if toss==2:
    print("You are bowling first")
    w1,r1=0,0
    ball=0
    while (w1<=2) and (ball<12):
        x=random.randint(0,6)
        y=int(input("Choose number between 1 to 6:")) #Defense allowed only for batting side
        print ("Computer selected:", x)
        if y>6 or y<1:
            penalty=penalty+1
            ball=ball-1
        if x!=y:
            r1=r1+x
        if x==y and y>0 and y<=6:
            w1+=1
        ball+=1
        r1=r1+penalty
    print ("Computer scored ", r1 , " runs")
    if w1!=0:
        sr=ball/w1
        print ("Your bowling strike rate:", sr)
    print ("You are batting ")
    print ("DISCLAIMER: Entering numbers out of range will result in penalty for the opponent, as it is considered unfair means of game")    
    w,r=0,0
    balls=0
    while (w<=2) and (balls<12):
        x=random.randint(1,6)
        y=int(input("Choose your number between 0 to 6:"))  #Defense allowed for batting side
        print ("Computer selected:", x)
        if (y>=7 or y<0):
            penalty=penalty+1
        if (x!=y)and (y<=6 and y>0):
            r=r+y
        if x==y :
            w+=1
        balls=balls+1
        if r>(r1+penalty):
            break
    r1=r1+penalty
    print ("You scored ", r , " runs")
    strike_rate=(r/balls)
    print("Your batting strike rate: " , strike_rate)
    print ("Computer scored ", r1 , " runs (including penalty)")
    if (r>r1):
        print ("You won")
    if (r1>r):
        print ("You lost")
    if (r1==r):
        print ("Match tied")
    
    
