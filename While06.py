def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    idx=0
    number=0
    while idx<len(s):
        if s[idx]!="a" or s[idx]!="e" or s[idx]!="i" or s[idx]!="o" or s[idx]!="u"  or s[idx]!=" ":
            number+=1
        idx=idx+1
    return number

        


print(main("ausan jalilov"))