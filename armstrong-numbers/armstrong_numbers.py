def is_armstrong(number):
    digits = list(str(number))
    armNumber = 0
    for d in digits:
        armNumber += int(d) ** len(digits)
    if number != armNumber:
        return False
    else:
        return True
