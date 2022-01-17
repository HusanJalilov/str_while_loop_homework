def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    sd=0
    while idx<len(s):
        sd+=int(s[idx])
        

        idx=idx+1
    return sd
        
print(main("123456789"))
    