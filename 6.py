import os
for dirpath,dirname,filename in os.walk("C:\\Users\\suraj\\OneDrive\\Desktop\\Python files"):
       for file in dirpath:
           print(file,end="")
        