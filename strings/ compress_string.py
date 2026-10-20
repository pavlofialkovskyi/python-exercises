def compress_string(phrase):
    if phrase != "":
        # I added a sentinel as an extra last character for the comparison reason i+1
        if phrase[-1] == " ":
            big_string = phrase + "_"
        else:
            big_string = phrase + " "

        new_string = ""
        k = 1

        for i, ch in enumerate(big_string[:-1]):
            if big_string[i] != big_string[i + 1]:
                new_string += big_string[i]
                new_string += str(k)
                k = 1
            else:
                k += 1
    else:
        new_string = ""

    return new_string



print(compress_string("aaabbc"))     # a3b2c1
print(compress_string("abc"))        # a1b1c1
print(compress_string("aaaa"))       # a4
print(compress_string("a"))          # a1
print(compress_string(""))           # 
print(compress_string("aabaa"))      # a2b1a2
print(compress_string("aA"))         # a1A1
print(compress_string("a "))         # a1 1
print(compress_string(" "))          #  1
print(compress_string("12asdad "))   # 1121a1s1d1a1d1 1