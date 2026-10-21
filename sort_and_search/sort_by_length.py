def sort_by_length(sentence):

    prepared_sent = sentence.lower().strip()
    cleaned = ""
    # remove the symbols like ","
    for i in range(len(prepared_sent)):
        if (prepared_sent[i].isalnum() or (prepared_sent[i] == " ")):
            cleaned += prepared_sent[i]

    phrazes = cleaned.split() # get a list of strings-words
      
    if len(phrazes) > 1:   # empty or 1 word sentence protection
        i = 0
        while i < (len(phrazes) - 1):    # a loop to sort the nearby strings by length
            if len(phrazes[i]) > len(phrazes[i + 1]):
                swapper = phrazes[i]
                phrazes[i] = phrazes[i + 1]
                phrazes[i + 1] = swapper
                i = -1  # loot reset back to start on successfull swap of words
            i += 1
        return " ".join(phrazes)
    else:
        return prepared_sent

print(sort_by_length("1 a 122 sdqs t a "))              # 1 a t a 122 sdqs
print(sort_by_length("Hello, big world!"))              # big hello world
print(sort_by_length("It's 5 o'clock."))                # 5 its oclock
print(sort_by_length("  spaced    out  "))              # out spaced
print(sort_by_length("hi!"))                            # hi
print(repr(sort_by_length("   ")))                      # ''
print(repr(sort_by_length("")))                         # ''
print(sort_by_length("Hello, big world! It's 5 o'clock."))   # 5 big Its Hello world oclock