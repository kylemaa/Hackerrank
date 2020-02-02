def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split(' ')
    newwords = []
    for word in words:
        # Create the pig latin word and add it to the list

        # Turn the list back into a phrase
        newwords.append(word[1:len(word)]+word[0]+"ay")
    for i in newwords:
        say += " "+i
    return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# Should be "rogrammingpay niay ythonpay siay unfay"
print(pig_latin("programming in python is fun"))
