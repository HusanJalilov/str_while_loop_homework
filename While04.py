def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    m=0
    idx=0
    while idx<len(s):
        if s[idx].isupper():
            m+=1
    
        idx=idx+1
    return m
print(main("HusanJalL s  FF er"))

