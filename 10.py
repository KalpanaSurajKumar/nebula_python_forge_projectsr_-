import time
nam=input("Enter your name:\n")
suraj=time.strftime('%H:%M:%S')
print("The time is:",suraj)
h=int(time.strftime("%H"))
m=int(time.strftime("%M"))
s=int(time.strftime("%S"))
if(h>=1 and h<=12):
    if  h==12 and m>0:
        print("Good afternoon")
    else:    
     print("Good morning",nam)
elif(h>12 and h<=16):
    if h==16 and m>0:
        print("Good evening")
    else:    
      print("Good afternoon ",nam)
elif(h>16 and h<=20):
    if h==20 and m>0:
      print("Good night",nam)
    else:
       print("Good Evening",nam)  
else:
    print("Good night",nam)            