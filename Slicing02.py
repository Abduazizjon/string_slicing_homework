def main(s):
    """
    The s string variable is given. return four characters from the end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
   
    a = s[3::-1]
    s = "maktab"
    return a



print(main("maktab"))