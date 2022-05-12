##############################################################################
#1. Создать программный файл в текстовом формате, записать в него построчно 
#данные, вводимые пользователем. Об окончании ввода данных будет 
#свидетельствовать пустая строка.

my_list = []
while True:
    line = input("Введите данные: ")
    if line == '':
        print(my_list)
        break
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open("test_1.txt", "w") as file_obj:
        file_obj.writelines(my_list)


###############################################################################
#2. Создать текстовый файл (не программно), сохранить в нём несколько строк, 
#выполнить подсчёт строк и слов в каждой строке.

lines = 0
with open("2.txt", "r") as file:
    for line in file:
        lines += 1
        words = len(line.split())
        print(f'В {lines} строке {words} слов')
    print(f'Всего {lines} строк')

###############################################################################
#3. Создать текстовый файл (не программно). Построчно записать фамилии 
#сотрудников и величину их окладов (не менее 10 строк). Определить, кто из 
#сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
#Выполнить подсчёт средней величины дохода сотрудников.
#Пример файла: Иванов 23543.12
              #Петров 13749.32

with open(r'C:\Users\green\OneDrive\Рабочий стол\Основы языка Python\sal.txt', 'r') as my_file:
    sal = []
    poor = []
    my_list = my_file.readlines() 
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            poor.append(i[0])
            sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(float, sal)) / len(sal)}')

###############################################################################
#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
#При этом английские числительные должны заменяться на русские. 
#Новый блок строк должен записываться в новый текстовый файл.

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open(r'C:\Users\green\OneDrive\Рабочий стол\Основы языка Python\file.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open(r'C:\Users\green\OneDrive\Рабочий стол\Основы языка Python\filenew.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

##############################################################################
#5. Создать (программно) текстовый файл, записать в него программно набор чисел, 
#разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и 
#выводить её на экран.

def summary():
     with open(r"C:\Users\green\OneDrive\Рабочий стол\Основы языка Python\test1.txt", "x") as file_obj:
            line = input('Введите цифры через пробел ')
            file_obj.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
summary()

##############################################################################
#6. Сформировать (не программно) текстовый файл. В нём каждая строка должна 
#описывать учебный предмет и наличие лекционных, практических и лабораторных 
#занятий по предмету. Сюда должно входить и количество занятий. Необязательно, 
#чтобы для каждого предмета были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее количество занятий 
#по нему. Вывести его на экран.
#Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

dct={}
with open(r"C:\Users\green\OneDrive\Рабочий стол\Основы языка Python\test2.txt", "r") as file_obj:
    for line in file_obj:
        print(line)
        subject, lecture, practice, lab = line.split()
        dct[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {dct}')
    
    
##############################################################################
#7. Создать вручную и заполнить несколькими строками текстовый файл, в котором 
#каждая строка будет содержать данные о фирме: название, форма собственности,
#выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.

#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а 
#также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её 
#не включать.

import json
profits=[]  
dct_profits={} 
аverage_profit={} 
with open(r"C:\Users\green\OneDrive\Рабочий стол\Основы языка Python\TEST3.txt", "r") as file_obj:
    content=file_obj.readlines()
    for i in content:
        i = i.split()
        profit=int(i[2])-int(i[3])
        profits.append(profit)
        if profit>0:
            аverage=sum(map(int, profits))/len(profits)
            аverage_profit['Средняя прибыль = ']=аverage

#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
#а также словарь со средней прибылью. Если фирма получила убытки, также 
#добавить её в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, 
#                {“average_profit”: 2000}].

    for i in content:
        name, form, revenue, costs = i.split()
        dct_profits[name] = int(revenue)-int(costs)

    print("Прибыльные компании: ", dct_profits)
    print("Средняя прибыль = ", аverage)

result_list = [dct_profits, аverage_profit]
print(result_list)

#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджер контекста.    
with open("my_file.json", "w") as write_f:
    json.dump(result_list, write_f)    
    





















