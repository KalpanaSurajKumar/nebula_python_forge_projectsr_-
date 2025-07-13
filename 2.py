import random
print("_______________________________________________________________")
print(" ♨️♨️♨️ *******🐍Snake🌊Water 🔫Gun Game🎮🎮🎮🎮***********♨️♨️♨️")
print("_______________________________________________________________")

player=input("Choose 🐍Snake,🌊Water or 🔫Gun\n")


computer_list=[-1,0,1]
computer_choosed=random.choice(computer_list)

if computer_choosed==-1:
    picked="Snake"

elif computer_choosed==0:
    picked="Water"

else :
    picked="Gun"


print("You Choosed:",player)
print("Computer Choosed:",picked)

if (player=="snake" or player=="Snake") and picked=="Snake":
    print("🌞🌞🌞Match is tied🟰🟰\n")

elif (player=="snake" or player=="Snake") and picked=="Water":

    print("🐍Snake beats the 🌊Water\n")
    print("You Win 🏆🏆\n")
    

elif ((player=="gun" or player=="Gun") and picked=="Gun" ) :
    print("🌞🌞🌞Match is tied🟰🟰\n")

elif (player=="gun" or player=="Gun") and picked=="Snake":
    print("The 🔫Gun beats the 🐍Snake\n")
    print("You Win🏆🏆\n")

elif (player=="water" or player=="Water") and picked=="Water":
    print("🌞🌞🌞Match is tied🟰🟰\n")

elif (player=="water" or player=="Water") and picked=="Gun":
    print("🌊Water beats the 🔫Gun\n")

    print("You Win🏆🏆\n")

elif (player=="water" or player=="Water") and picked=="Snake":
    print("🐍Snake beats the 🌊water\n")
    print("You Loose😥😥\n")


elif (player=="snake" or player=="Snake") and picked=="Gun":
    print("The 🔫Gun beats the 🐍Snake\n")
    print("You Loose😥😥\n")

elif (player=="gun" or player=="Gun") and picked=="Water":
    print("The 🌊Water beats the 🔫Gun\n")
    print("You Loose😥😥\n")

else:
    print("☠️☠️☠️Something went Wrong☠️☠️☠️")
print("_______________________________________________________________")
print("👀****Created By 🎮🎮🎮Game Developer Suraj Kumar🌞🌞🌞*****👀")
print("_______________________________________________________________")