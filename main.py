import time
import timeit

if __name__ == "__main__":
    print("Somebody once told me")
    print("The world is gonna roll me")
    print("I ain't the sharpest tool in the shed")

    gods = time.process_time()

    xxx = 0
    to = input("how long?")
    for x in range(int(to)):
        xxx += x

    print(time.process_time() - gods)

