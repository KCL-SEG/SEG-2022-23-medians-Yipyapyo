"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def median(args):
    args.sort()
    range = int(len(args))
    middle = range//2
    if (range % 2) == 0:
        arithmeticMean = (((middle) + middle+1)/2)
        return arithmeticMean
    else:
        return args[middle]

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
print(f"the median is {median(numbers)}")
