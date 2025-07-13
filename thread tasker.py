import time
from concurrent.futures import ThreadPoolExecutor
# Threading in Python
def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

y=time.perf_counter()
def pollingDemo():
    with ThreadPoolExecutor() as executer:
        # future1=executer.submit(func,3)
        # future2=executer.submit(func,2)
        # future3=executer.submit(func,4)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l=[3,5,1,2]
        results=executer.map(func,l)
        for result in results:
            print(result)

pollingDemo()

print(time.perf_counter()-y)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13