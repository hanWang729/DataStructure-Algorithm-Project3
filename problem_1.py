def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        print("Error, the input can't be negative")
        return
    if number == 0 or number == 1:
        return number
    
    upper_bound = number
    lower_bound = 0
    while True:
        mid = (upper_bound - lower_bound) // 2 + lower_bound
        if mid * mid < number:
            lower_bound = mid
        elif mid * mid > number:
            upper_bound = mid
        else:
            return mid
        if upper_bound - lower_bound <= 1:
            return lower_bound



print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")