#Задача 5.Вариант 29.
#Напишите программу, которая бы при запуске случайным образом отображала имя одного из пяти членов экипажей программы "Союз - Апполон".
#Чинкиров В.В.
#28.03.2016

import random
print("Программа случайным образом отображает имя одного из пяти членов экипажа Союз-Апполон")
x =  int (random.randint(1,5))
print ("Один из основателей - ", end = "")
if x == 1:
     print ("Томас Стаффорд")
elif x == 2:
     print ("Вэнс Бранд ")
elif x == 3:
    print ("Дональд Слейтон ")
elif x == 4:
    print ("Алексей Леонов ")      
else:
    print ("Валерий Кубасов")
     
input("Для выхода нажмите Enter.")       
       