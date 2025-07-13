# Random module Tutorial
import random 
# # 1. randint()
# # (i)
# num = random.randint(6,8)  # note randint() main ye dono include hote hai
# print(num)
# # (ii)
# print(random.randint(1,100))

# # (iii)
# print(random.randint(20000,30000))


# 2. randrange()
# # (i)
# num = random.randrange(1,100)  # note yaad rakhna ki isme sirf pehle wala include hota hai last wala nahi ie. 1 include hoga lekin 100 include nahi hoga


# print(num)
# # (ii)

# print(random.randrange(200,300))

# # (iii)

# ran = random.randrange(-344,300000)

# print(ran)
# 3. choice()
# (i)

# fruits = ["apple ","orange","banana","mango","Litchi","pineapple"]
# print(random.choice(fruits))
# # (ii)

# friends= ["Suraj","Shruti","Juhi","Saurav","Rahul","Abhinav","Maya"]
# print("My favourite friend is:",random.choice(friends))
# # (iii)

# books = ["Bhagwat geeta","Ramayan","Discovery of india","Purana","Quran"]

# print("My favourite book is:",random.choice(books))

# 4. random()
# # (i)
# print(random.random())
# # (ii)
# print(random.random())
# # (iii)
# print(random.random())

# Note yaad rakhna ki ye 0 and 1 ke bech main se koin bhi float number lel
 # leta hai


# 5. shuffle()
# (i)
# li = [10,20,30,40,50,60]

# la = random.shuffle(li)
# print(la)
# # (ii)

# ga = [100,200,300,400,500,600]

# print(random.shuffle(ga))
# # (iii)

# ta = [400,600,700,900]

# print(random.shuffle(ta))
# 6. uniform()
# (i)
print(random.uniform(10,100))
# (ii)
print(random.uniform(30,1000))
# (iii)

print(random.uniform(3000000,10))

