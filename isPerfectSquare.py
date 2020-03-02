# perfect square test

def digital_root(n):
    x = sum(int(digit) for digit in str(n))
    if x < 10:
        return x
    else:
        return digital_root(x)
    
def isPerfectSqr(N):
    if N%8 == 1:
            return "Yes"
    elif N%2==0:
        if N%10 == 4 or N%10 == 6:
            if digital_root(N) in [1,7,4,9]:
                return "Yes"
        
    return "No"

isPerfectSqr(1454)
