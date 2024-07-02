import random


def foldandswap(numbers):
    n = len(numbers)
    mid = n // 2
    for i in range(mid):
        numbers[i], numbers[-(i + 1)] = numbers[-(i + 1)], numbers[i]
    return numbers
   

def main():
    numbers = [2, 3, 0, 5, 4, 1, 6, 9, 8, 7]
    print(numbers)
    foldandswap(numbers)
    print(numbers)

    numbers = [random.randint(0, 10) for i in range(10)]
    print(numbers)
    foldandswap(numbers)
    print(numbers)


if __name__ == '__main__':
    main()
