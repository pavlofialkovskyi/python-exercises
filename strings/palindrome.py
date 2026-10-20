def is_palindrome(s):
    char = list(s.lower())
    order = []
    for i in range(len(char)):
        if char[i].isalnum():
            order.append(char[i])
    return order == order[::-1]



print(is_palindrome("A man, a plan, a canal: Panama"))   # True
print(is_palindrome("hello"))                            # False
print(is_palindrome(""))                                 # True
print(is_palindrome("a"))                                # True