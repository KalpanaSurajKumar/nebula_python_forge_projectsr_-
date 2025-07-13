import os
a=1
b=0 
for dirpath,dirname,filename in os.walk("C:\\Users\\suraj\\OneDrive\\Desktop\\Python files"):
    for Files in filename:
        x=os.path.join("C:\\Users\\suraj\\OneDrive\\Desktop\\Python files",Files)
        ex=os.path.splitext(x)
        if ex[-1]=='.py':
            b=b+a
            n=os.path.join(f"C:\\Users\\suraj\\OneDrive\\Desktop\\Python files\\{b}.py")
            os.rename(x,n)

        
               
                
                