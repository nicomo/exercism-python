def verify(isbn):
    try:
        cISBN = cleanISBN(isbn)
        return checkLastDigit(cISBN)
    except ValueError:
        return False
    
def cleanISBN(isbn):
    res = []
    for c in isbn:
        if ord(c) >=48 and ord(c) <= 57: # ascii table 0 to 9 
            res.append(int(c))
        elif ord(c) == 88: # ascii table X
            res.append(10)
			# X only allowed as a check digit, i.e. last digit
            if len(res) != 10:
                raise ValueError("X only allowed as a check digit")
    if len(res) != 10:
        raise ValueError("Burp...")
    return res

def checkLastDigit(cISBN):
    sum = 0
    for i, v in enumerate(cISBN):
        sum += (i-10)*v
    return (sum % 11) == 0