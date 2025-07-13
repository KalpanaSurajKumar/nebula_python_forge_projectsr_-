nam=input("Enter Your name\n")
you=input(f" {nam} are you ready to play Kaun Banega crorepatti with Suraj kumar?\n")
if you=='yes':
    print('''Now i tell some rules about this game
          In this game KBC there are total of 10 question 1 question gives you 2000 rupees similarly
          Q2 gives you 5000 rupees:  Q3 gives you  10000 rupees: Q4 gives you 20000 rupees: Q5 gives you 100000 rupees : Q6 gives you 5000000 rupees : Q7 gives you 10000000 rupees: Q8 gives you 20000000 rupees: Q9 gives you 30000000 rupees: Q10 gives you 50000000 rupees\n'''
           )
    print(" Also you have only 2 life lines\n First is:\n 1. Ask the Expert\n 2. You can google only 1 time\n")
    print("So",nam,"Let's play Kaun banega Crorepatti with Suraj Kumar")
    for i in range(1):
        a="1.Who is the prime minister of india?\n"
        print(a)
        sol1=["a.Narendra Modi","b.Rahul Gandhi","c.Manmohan Singh","d.Amit shah"]
        print("your options are:\n")
        for i in sol1:
          print(i)
        s1 =input("Enter your answer \n")
        if s1=='a' or s1=='A':
          print("Congratulations",nam,"You have won 2,000 rupees\n")
            
        else:
            print("Sorry,it is wrong play next time\n")
            break
        
        b="2.Who is the first president of india?\n" 
        print(b)
        sol2=["a.Sheela dikshit", "b.ram nath kovind","c. Dr.Rajendra prasad","d. Draupdi murmur"]
        print("Your options are:\n")
        for i in sol2:
         print(i)
        c=input("Enter your answer\n")
        if (c=='c') or( c=='C'):
          print("Congratulations",nam,"you have  won 5,000 rupees")
      
        else:
           print("Congratulations",nam,"You have won 2,000 rupees\n")
           print(" Sorry,But it is wrong play next time\n")
           f1=input(f"{nam},How do you use your money?\n")
           print("OK ,that is good, best of luck\n")
           f2=input(f"{nam},Enter your bank name\n")
           print("OK",nam,"Congratulations your money have been tranfered in your",f2,"\n" )
           break
       
        q3="3.WHO stands for?\n"
        print(q3)
        sol3=["a.World Help Organisation","b.World Health Organisation","c.World Half Day"]
        print("Your options are:\n")
        for i in sol3:
            print(i)
        a3=input("Enter your answer\n")
        if a3=='b' or a3=='B':
              print("Congratulation",nam,"you have won 10,000 rupees\n" )
        else:
              print("Congratulations",nam,"you have  won 5,000 rupees\n")
              print(" Sorry,But it is wrong play next time\n")
              f1=input(f"{nam},How do you use your money?\n")
              print("OK ,that is good, best of luck\n")
              f2=input(f"{nam},Enter your bank name\n")
              print("OK",nam,"Congratulations your money have been tranfered in your",f2,"\n" )
              break
        q4= "4.where Ram Mandir is situated?\n"
        print(q4)
        sol4=["a.Sri Lanka","b.Kashi","c.Ayodhya","d.Meethala"]
        print("Your options are:\n")
        for i in sol4:
             print(i)
        a4=input("Enter your answer\n")
        if a4=='c' or a4=='C':
           print("Congratulations",nam,"you have won 20,000\n")
        else:
            print("Congratulations",nam,"you have won 10,000\n")
            print("Sorry,But it is wrong play next time\n")
            f1=input(f"{nam},How do you use your money?\n")
            print("OK ,that is good, best of luck\n")
            f2=input(f"{nam},Enter your bank name\n")
            print("OK",nam,"Congratulations your money have been tranfered in your",f2,"\n" )
            break

        q5= "5.Who is the founder of buddhism?\n"
        print(q5)
        sol5=["a.Mahatma Budh","b.Dayanand Sarswati","c.Shankara charya","d.Kabir"]
        print("Your options are:\n")
        for i in sol5:
           print(i)
        a5=input("Enter your answer\n")
        if a5=='a' or a5=='A':
           print("Congratulations",nam,"you have won 1,00,000 rupees\n")
        else:
            print("Congratulations",nam,"You have won 20,000 rupees\n")
            print("Sorry, it is wrong play next time\n")
            f1=input(f"{nam},How do you use your money?\n")
            print("OK ,that is good, best of luck\n")
            f2=input(f"{nam},Enter your bank name\n")
            print("OK",nam,"Congratulations your money have been tranfered in your",f2,"\n" )
            break
        q6= "6.The term'ecosystem' was first coined by?\n"
        print(q6)
        sol6=["a.Helen keler","b.William Henry","c. G.Tansley","d.Tom leo"]
        print("Your options are:\n")
        for i in sol6:
          print(i)
        a6=input("Enter your answer\n")
        if a6=='c' or a6=='C':
            print("Congratulations",nam,"you have won 50,00,000 rupees\n")
        else:
           print("Congratulations",nam,"You have won 1,00,000 rupees\n")
           print("Sorry,but play next time\n" )
           f1=input(f"{nam},How do you use your money?\n")
           print("OK ,that is good, best of luck\n")
           f2=input(f"{nam},Enter your bank name\n")
           print("OK",nam,"Congratulations your money have been tranfered in your",f2,"\n" )
           break 
        q7= "7.Where is the Chinnar Wlidlife Santuary situated?\n"
        print(q7)
        sol7=["a.Chennai","b.Kolkata","c.Bhopal","d.Kerela"]
        print("Your options are:\n")
        for i in sol7:
          print(i)
        a7=input("Enter your answer\n")
        if a7=='d' or a7=='D':
          print("Congratulations",nam,"you have won 1,00,00,000\n")
        else:
           print("Congratulations",nam,"you have won 50,00,000 rupees\n")
           print("Sorry, but play next time\n")
           f1=input(f"{nam},How do you use your money?\n")
           print("OK ,that is good, best of luck\n")
           f2=input(f"{nam},Enter your bank name\n")
           print("OK",nam,"Congratulations your money have been tranfered in your",f2,"\n" )
           break    
         
        q8= "8.Which Vitamin help in Clotting of Blood?\n"
        print(q8)
        sol8=["a.Vitamin A","b.Vitamin B","c.Vitamin K","d.Vitamin D"]
        print("Your options are:\n")
        for i in sol8:
            print(i)
        a8=input("Enter your answer\n")
        if a8=='c' or a8=='C':
            print("Congratulations",nam,"you have won 2,00,00,000 rupees\n")
        else:
            print("Congratulations",nam,"you have won 1,00,00,000 rupees\n")
            print("Sorry ,But play next time\n")
            f1=input(f"{nam},How do you use your money?\n")
            print("OK ,that is good, best of luck\n")
            f2=input(f"{nam},Enter your bank name\n")
            print("OK",nam,"Congratulations your money have been tranfered in your",f2,"\n" )
            break
        q9= "9.Name an alloy of mercury?\n"
        print(q9)
        sol9=["a.Bronze","b.Iridium","c.gam","d.Amalgam"]
        print("Your options are:\n")
        for i in sol9:
           print(i)
        a9=input("Enter your answer\n")
        if a9=='d' or a9=='D':
           print("Congratulations",nam,"you have won 3,00,00,000 rupees\n")
        else:
           print("Congratulations",nam,"you have won 2,00,00,000 rupees\n")
           print("Sorry, play next time\n")
           f1=input(f"{nam},How do you use your money?\n")
           print("OK ,that is good, best of luck\n")
           f2=input(f"{nam},Enter your bank name\n")
           print("OK",nam,"Congratulations your money have been tranfered in your",f2,"\n" )
           break  

        q10= "10.Which State is the oldest producer of oil  in India?\n"
        print(q10)
        sol10=["a.Assam","b.Gujrat","c.Haryana","d.Rajasthan"]
        print("Your options are:\n")
        for i in sol10:
          print(i)
        a10=input("Enter your answer\n")
        if a10=='a' or a10=='A':
          print("Congratulations",nam,"you have won 5,00,00,000 rupees\n")
          print("Congratulations",nam,"you are a Crorepatti\n")
          print("Your money is transfered in your bank\n")
          print("YOU ARE INCREDIBLE!\n")
          f1=input(f"{nam},How do you use your money?\n")
          f2=input(f"{nam},Enter your bank name\n")
          print("OK",nam,"Congratulations your money have been tranfered in your",f2,"\n" )
          print("OK ,that is good, best of luck\n")
        else:
           print("Congratulations",nam,"you have won 3,00,00,000 rupees\n")
           print("Opps!",nam, "you made a mistake but you are amazing\n" )
           print("You only missed one step\n")
           print("Your money is tranfered in your bank\n")
           f1=input(f"{nam},How do you use your money?\n")
           print("OK ,that is good, best of luck\n")
           f2=input(f"{nam},Enter your bank name\n")
           print("OK",nam,"Congratulations your money have been tranfered in your",f2,"\n" )
           break

       
            
else:
   print("Ok",nam,"You can go\n")
   print("You are Roadpatti\n")
   print("I eat you!\n")
   print("We are coming! your home to beat you\n") 



