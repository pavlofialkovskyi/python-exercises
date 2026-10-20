def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aoeui":
            count += 1
    return count



print(count_vowels("Hello World"))   # 3
print(count_vowels("banana"))        # 3
print(count_vowels("xyz"))           # 0
print(count_vowels(""))              # 0
print(count_vowels("AEIOU"))         # 5
print(count_vowels("Sky, 42!"))      # 0