# Задача 4. Вариант 8.
# Напишите программу, которая выводит имя, под которым скрывается


# Карамян Н.Г.
# 18.05.2016

real_name = 'Алексей Максимович Пешков'
p_name = 'Максим Горький'
interests = ('Проза и драматургия')
born_place = 'Новгород'
born_year = 1868
death_year = 1936
death_oldness = death_year - born_year

print(real_name +', ' + ' \nболее известный под псевдонимом '
              + p_name + ',')
print('родился в ' + born_place + 'е' +
      ' в ' + str(born_year) + ' году.')
print(str (interests) + ' сопровождали Горького всю сознательную жизнь.')
print('Целых 5 раз он был номинирован на Нобелевскую премию по литературе, но так и не дождался заветной награды и покинул нас в ' + str (death_year) + ' году,')
print('прожив ' + str (death_oldness ) + ' лет, полных счастья и горечи, радости и грусти, надежды и разочарования.')

input('\nНажмите Enter для выхода.')
