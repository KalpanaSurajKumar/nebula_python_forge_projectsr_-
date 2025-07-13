# 1
# import asyncio

# async def fun():
#     print("some things is good")
#     await asyncio.sleep(2)
#     print("Really it i amazing")
#     await asyncio.sleep(3)
#     print("This is something that is super coolings")

# asyncio.run(fun())
# 2
# import asyncio
# async def fun1():
#     print("I am the first funtion which is executing")
#     print("you really want to")
#     await fun2()
#     await fun3()
#     await asyncio.sleep(1)
#     print("This is somethings")


# async def fun2():
#     print("I am the second funtion which is executing")
#     print("I am the second")
#     await asyncio.sleep(3)
#     print("I am second and still executing")


# async def fun3():
#     print("I am the third funtion which is executing")
#     print("I am the third")
#     await asyncio.sleep(3)
#     print("I am third and still executing")


# asyncio.run(fun1())
    

# 3
# import asyncio
# async def main():
#     print("This is the main funtion")
#     asyncio.create_task(main2())
#     print("This is main and executing")
#     await asyncio.sleep(3)
#     print("Hello from main")


# async def main2():
#     print("This is main2() funtion ")
#     await asyncio.sleep(3)
#     print("from main2")
#     await asyncio.sleep(2)
#     print("This is from main2")

# asyncio.run(main())






# # 4
# import asyncio
# async def main1():
#     print("main1() is executing")
#     await asyncio.sleep(3)
#     print("main1() finished")

# async def main2():
#     print("main2() is executing")
#     await asyncio.sleep(3)
#     print("main2() finished")

# async def main3():
#     print("main3() is executing")
#     await asyncio.sleep(3)
#     print("main3() finished")

# async def maa():
#     await asyncio.gather(
#         main1(),
#         main2(),
#         main3(),
#     )


# asyncio.run(maa())

import asyncio

async def fun1():
    print("I am fun1 and executing")
    await asyncio.sleep(3)
    print("fun1 finished")


async def fun2():
    print("I am fun2 and executing")
    await asyncio.sleep(3)
    print("fun2 finished")



async def fun3():
    print("I am fun3 and executing")
    await asyncio.sleep(3)
    print("fun3 finished")


async def fun4():
    print("I am fun4 and executing")
    await asyncio.sleep(3)
    print("fun4 finished")
async def fun5():
    print("I am fun5 and executing")
    await asyncio.sleep(3)
    print("fun5 finished")
async def fun6():
    print("I am fun6 and executing")
    await asyncio.sleep(3)
    print("fun6 finished")


async def such():
    await asyncio.gather(
        fun1(),
        fun2(),
        fun3(),
        fun4(),
        fun5(),
        fun6()
    )

asyncio.run(such())
                   


k