#Подсчитайте количество слов во входных данных. В этой задаче словом будет считаться любая последовательность строчных букв.
# Например, «привет» — это слово, но и всякие бессвязные наборы букв вроде «sdfsdf» тоже считаются словами.
# Входными данными будет одна строка текста, состоящая из строчных букв и пробелов. Между каждой парой слов будет ровно один пробел,
# при этом перед первым словом и после последнего слова их не будет. Максимальная длина строки — 800 символов.

# text for debugging and testing
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

# uncomment if you want to insert your own
# text = str(input("Insert your text"))

words = text.split() # convert a string into a list
lengthOfList = len(words)

print(lengthOfList)

