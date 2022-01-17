def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    num=0
    while idx<len(s):
        sd=int(s[idx])%2
        if sd==0:
            num+=1    
    
       

        idx=idx+1
    return num
        
print(main("146789"))