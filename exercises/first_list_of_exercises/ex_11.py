# Напишите программу, которая принимает текст (от 5 слов с пробелами) и выводит два слова:
# наиболее часто встречающееся в тексте и самое длинное. Если все слова встречаются по 1 разу
# (или часто встречающиеся получатся с одинаковой частотой) вывести первое из них.

# 5 words -> duplicated words -> lengthOfWords
# 5 words -> words[0]

# words counting
list = input("insert 5 words") # string
words = list.split() # list
lengthOfList = len(words)

# sort for more convenience
sortedList = sorted(words, key=len)

# method of finding the longest word
def lengthOfWords():
    theLongestWord = sortedList[-1]
    print("The longest word is", theLongestWord)

# method for finding not unique words
def uniqueWords():
    duplictedWords = [x for i, x in enumerate(words) if i != words.index(x)]
    if len(duplictedWords) == 0:
        print("There is no coincidences, so the first word is", words[0])
    else:
        print("The duplicated word is", duplictedWords)

# main condition
def mainCondition():
    if lengthOfList < 5:
        print("There's a condition to insert more that 5 words")
    else:
        lengthOfWords()
        uniqueWords()

mainCondition()


