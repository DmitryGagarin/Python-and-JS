#используем библиотеку csv
#Требуется создать csv-файл «rows_300.csv» со следующими столбцами (разделитель столбцов ‘;’ ) :
#– No - номер по порядку (от 1 до 300);
#– Дата и время – текущая дата и время на вашем ПК;
#– Секунда – текущая секунда на вашем ПК;
#– Микросекунда – текущая миллисекунда на часах.
#На каждой итерации цикла искусственно приостанавливается скрипт на 0,01 секунды. Файл тоже публикуется на гитхаб вместе с кодом.

import csv
import datetime
import time

date = time.strftime("%Y-%m-%d-%H-%M")

file = open("rows_300.csv", "w+")
fileWriter = csv.writer(file, delimiter = " ")
fileWriter.writerow(["Rows","Date","Seconds","Milliseconds"])
for strings in range(1, 301):
    currentTime = datetime.datetime.now()
    fileWriter.writerow([strings, "--", date, "--", currentTime.second, "--", currentTime.microsecond])
    time.sleep(0.01)




