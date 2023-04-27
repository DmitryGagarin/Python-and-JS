# Выберите любую папку на своем компьютере, имеющую вложенные папки, на несколько уровней вглубь (папка01
# лежит внутри папки02 и т.д.). Задайте путь к ней в строковой переменной.
# Выведите на печать в терминал содержимое папки (имена файлов), а также имена всех вложенных папок
# (с неограниченной глубиной поиска) при помощи функции print_docs(directory).

import os

# walk() - goes through all catalogs and files
# EXAMPLE AND TEST:
# Fatsievich_Dmitry contains README.md, forceOfGravity and exercises
def print_docs(directory):
    all = os.walk(directory)
    for file_name in all:
        print("Folder", all[0], "contains:")
        print("Directory: ", ''.join([folder for folder in file_name[1]]))
        print("Files are: ", ''.join([file for file in file_name[2]]))

path = "/Users/dmitryfatsievich/Desktop/education/IT/semester_2/Fatsievich_Dmitry"
print_docs(path)
