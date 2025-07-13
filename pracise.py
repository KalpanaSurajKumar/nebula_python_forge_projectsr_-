import multiprocessing


def print_cube(num):
    print(f"Cube: {num**3}")


def print_square(num):
    print(f"Square: {num**2}")


if __name__ == "__main__":
 p1 = multiprocessing.Process(target=print_square,args=[9])
 p2= multiprocessing.Process(target=print_cube,args=[9])
 p1.start()
 p2.start()
 
 p1.join()
 p2.join()
 
 print("Done!")

    