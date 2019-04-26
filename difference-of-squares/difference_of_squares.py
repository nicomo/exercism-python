def square_of_sum(count):
    sum = 0
    for n in range(count+1):
        sum += n
    return sum * sum

def sum_of_squares(count):
    return sum(n * n for n in range(count + 1))

def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
