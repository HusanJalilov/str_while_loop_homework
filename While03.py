def count_punctuation(ch):
    if not ch.isdigit() and not ch.isalpha():
        return 1
    else:
        return 0 
def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx = 0
    x = 0
    while idx < len(s):
        x += count_punctuation(s[idx])
        idx += 1
    return x
print(main("@## jnjd #12"))



