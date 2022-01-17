def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    num=0
    while idx<len(s):
        sd=int(s[idx])
        if sd%2!=0:
            num+=sd
           

        

        idx=idx+1
    return num
        
print(main("34733"))