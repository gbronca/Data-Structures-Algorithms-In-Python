import time

NEMO = ["nemo"]
EVERYONE = [
    "dory",
    "bruce",
    "marlin",
    "nemo",
    "gill",
    "bloat",
    "nigel",
    "squirt",
    "darla",
    "hank",
]
LARGE = ["nemo" for _ in range(10000)]


def find_nemo(array):
    t0 = time.time()
    for i in range(len(array)):
        if array[i] == "nemo":
            print("Found NEMO!")
    t1 = time.time()
    print(f"Call to find Nemo took {(t1 - t0)} milliseconds")


find_nemo(EVERYONE)
