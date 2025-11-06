def fib(num: int) -> int:
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


def main():
    print(
        "This first case should print the first 10 iterations of the fibonnaci sequence"
    )
    print(fib(7))


main()
