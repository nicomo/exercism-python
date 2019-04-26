from math import sqrt

def score(x, y):
    # get rid of negative numbers
    squared = sqrt(x*x+y*y)

    if squared <= 1.0:
        return 10
    elif squared <= 5.0:
        return 5
    elif squared <= 10.0:
        return 1
    else:
        return 0
