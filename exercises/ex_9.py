# Студент решил вспомнить старые времена
# В свое время было модно писать сообщения с чередующимися заглавной и малой буквами.
# Он захотел изобрести функцию, которая будет делать с любой предоставленной строкой аналогичное.
# Первая буква малая, следующая Заглавная и так далее чередуется по всей строке.
# Ваша задача: создать такую функцию, с учетом того, что пробелы и знаки препинания
# не должны влиять на чередование регистра символов (они в этом процессе не учитываются,
# но возвращаются в итоговой строке).

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
newText = ""
j = 1

for i in range(len(text)):
    if text[i] == " ":
        newText += " "
        continue
    elif text[i] == ",":
        continue
    if j % 2 != 0:
        newText += (text[i].upper())
        j += 1
    else:
        newText += (text[i].lower())
        j += 1

print(newText)


