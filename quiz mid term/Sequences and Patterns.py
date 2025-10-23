def reverse_string():
    q = list(map(str ,input("Enter a string to reverse: ").split()))
    z = q.reverse()
    return z
def sum_digits():
    x = list(map(str ,input("Enter a number to sum its digits: ").split()))
    y = sum(n for n in x)
    return y

