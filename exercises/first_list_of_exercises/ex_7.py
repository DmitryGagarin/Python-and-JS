# Напишите функцию search_substr(subst, st), которая принимает 2 строки и определяет, имеется ли подстрока subst в строке st.
# В случае нахождения подстроки, возвращается фраза «Есть контакт!», а иначе «Мимо!».
# Должно быть найдено совпадение независимо от регистра обеих строк.

right_result = "Есть Контакт!"
wrong_result = "Мимо"

def search_substr(subst, st):
	if subst.lower() in st.lower():
		return right_result
	else:
		return wrong_result

print(search_substr('Дул', 'дУлО'))
print(search_substr('Дом', 'аВтОзак'))
print(search_substr('Арбуз', 'Арбузный'))


