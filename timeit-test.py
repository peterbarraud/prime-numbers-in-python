import timeit

def main():
    for i in range(250000000):
        i += 1

if __name__ == "__main__":
    # main()
    t = timeit.timeit(stmt=main, number=1)
    print(t)