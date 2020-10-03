import sys


def fibonacci(n):
    first = 1
    second = 1

    print(first, end = ' ')
    print(second, end = ' ')

    for x in range(n-2):
        next = first + second
        print(next, end = ' ')
        temp = second
        first = temp
        second = next
        
def main(args):
    try:
        fibonacci(int(args[0]))
    except (IndexError, ValueError):
        print("Usage: please input the count of fibonacci numbers to output")
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
