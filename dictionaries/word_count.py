def word_count(sentense):
    d = {}
    
    words = sentense.lower().split()  # split() will break the string into list, will take the spaces "  " as a breaker, no matter how many are in the order, one or many   "I am      big am" , if not, it will work around a white space as a word.

    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

   
    return d


print(word_count("the cat the dog"))   # {'the': 2, 'cat': 1, 'dog': 1}
print(word_count("Hi hi HI"))          # {'hi': 3}
print(word_count(""))                  # {}
print(word_count("a  b"))              # {'a': 1, 'b': 1}