#number memory test
import random
import time
print("Let's test how many digits can you remember")
num=0
response=0
a,b,pause=1,10,3
while num==response:
    start=time.time()
    num=int(random.randint(a,b))
    print("number to be remembered : ",num)
    time.sleep(pause)
    end=time.time()
    nxt_line="\n"
    print(nxt_line*35)
    response=int(input("enter the number you saw correctly : "))
    if response==num:
        print("Good, now let's make it a little more difficult")
    else:
        dig=len(str(a-1))
        if dig>=14:
            print("what the ...!! What do you eat to grow your memory like this!!! You can remember upto ",dig," digits")
        elif dig>12 and dig<14:
            print("Wow, You have a good memory power!! You can remember upto ",dig," digits")
        elif dig>10 and dig<12:
            print("Good, you have a nice memory! You can remember upto ",dig," digits")
        elif dig>8 and dig<10:
            print("Okay, you have a decent memory, but do develop it! You can remember upto ",dig," digits")
        elif dig>6 and dig<8:
            print("Nice, you have put the idle brain of yours to Use! You can remember upto ",dig," digits")
        elif dig>4 and dig<6:
            print("okay,You atleast have something inside your tiny little brain. You can remember only upto ",dig," digits")
        else:
            print("What do you have inside ur head, brain or clay ! You can remember only upto ",dig," digits")
    a*=10
    b*=10
    pause+=1
    start=end=0
        
    
