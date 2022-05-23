##############################################################################
#1. Реализовать класс «Дата», функция-конструктор которого должна принимать 
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать 
# два метода. 

# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и 
#преобразовывать их тип к типу «Число».

# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца 
# и года (например, месяц — от 1 до 12). 

#Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, str_date:str):
        self.str_date=str_date
    
    @classmethod
    def metod_1(cls, str_date):
        d, m, y = str_date.split('-')
        return int(d), int(m), int(y)
    
    @staticmethod
    def metod_2 (str_date):
        d, m, y = str_date.split('-')
        if 1<int(d)<=31:
            if 1<=int(m)<=12:
                if 0<int(y)<=2999:
                    return 'Всё верно'
                else:
                    return 'Неправильно указан год'
            else:
                return 'Неправильно указан месяц'
        else:
            return 'Неправильно указан день'

d='20-05-2022'
print(Date.metod_1(d))
print(Date.metod_2(d))

d2='32-12-2021'
print(Date.metod_2(d2))


##############################################################################
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
# Проверьте его работу на данных, вводимых пользователем. 
# При вводе нуля в качестве делителя программа должна корректно обработать 
# эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def divide_by_null(self):
        try:
            return round(self.a / self.b, 2)
        except ZeroDivisionError:
            return "На ноль делить нельзя!"
        
d=OwnError(100, 10)
print(d.divide_by_null())
d2=OwnError(100, 0)
print(d2.divide_by_null())

###############################################################################
#3. Создайте собственный класс-исключение, который должен проверять содержимое 
# списка на наличие только чисел. Проверить работу исключения на реальном примере. 
# Запрашивать у пользователя данные и заполнять список необходимо только числами. 
# Класс-исключение должен контролировать типы данных элементов списка.

# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, 
# пока пользователь сам не остановит работу скрипта, введя, например, команду «stop». 
# При этом скрипт завершается, сформированный список с числами выводится на экран.

# Подсказка: для этого задания примем, что пользователь может вводить только числа 
# и строки. Во время ввода пользователем очередного элемента необходимо 
# реализовать проверку типа элемента. Вносить его в список, только если введено число. 
# Класс-исключение должен не позволить пользователю ввести текст (не число) и 
# отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

       while True:
            try:
                val = int(input('Введите значения и нажмите Enter '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print("Недопустимое значение - строка")
                y_or_n = input('Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return 'Вы вышли'
                else:
                    return 'Вы вышли'

try_except = Error(1)
print(try_except.my_input())

##############################################################################
# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
# А также класс «Оргтехника», который будет базовым для классов-наследников. 
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
# В базовом классе определите параметры, общие для приведённых типов. 
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.


# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают 
# за приём оргтехники на склад и передачу в определённое подразделение компании. 
# Для хранения данных о наименовании и количестве единиц оргтехники, 
# а также других данных, можно использовать любую подходящую структуру (например, словарь).


# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых 
# пользователем данных. Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, 
# изученных на уроках по ООП.

class OfficeEquipment:
    
   def __init__(self, price, color, producer):
        self.price = price
        self.color = color
        self.producer = producer
        
class Printer(OfficeEquipment):
    amount_printer = 0

    def __init__(self, price, color, producer, type_printer):
        super().__init__(price, color, producer)
        self.type_printer = type_printer
        Printer.amount_printer += 1
        
    @staticmethod
    def name():
        return "<<Принтер>>"

    def type_printer(self):
        return self.type_printer

    def __str__(self):
        return f" цена: {self.price} \tцвет: {self.color} \tпроизводитель: {self.producer} \tтип принтера: {self.type_printer}"

      
class Scanner(OfficeEquipment):
    amount_scanner = 0
    
    def __init__(self, price, color, producer, speed_scanner):
        super().__init__(price, color, producer)
        self.speed_scanner = speed_scanner
        Scanner.amount_scanner += 1
        
    @staticmethod
    def name():
        return "<<Сканер>>"

    def speed_scanner(self):
        return self.speed_scanner

    def __str__(self):
         return f" цена: {self.price} \tцвет: {self.color} \tпроизводитель: {self.producer} \tскорость сканирования: {self.speed_scanner}"
        
class Copier(OfficeEquipment):
    amount_copier = 0
    
    def __init__(self, price, color, producer, wi_fi_copier):
        super().__init__(price, color, producer)
        self.wi_fi_copier = wi_fi_copier
        Copier.amount_copier += 1
        
    @staticmethod
    def name():
        return "<<Ксерокс>>"

    def wi_fi_copier(self):
        return self.wi_fi_copier

    def __str__(self):
        return f" цена: {self.price} \tцвет: {self.color} \tпроизводитель: {self.producer} \twi_fi_copier: {self.wi_fi_copier}"


p = Printer('2000', 'белый', 'Canon','струйный')
p2 = Printer('3000', 'черный', 'Canon','лазерный')
print(p.name(), p.amount_printer, "шт")
print(p.__str__())
print(p2.__str__())


s = Scanner('1500', 'белый', 'Epson','100')
s2 = Scanner('3000', 'черный', 'Kodak','75')
print(s.name(), s.amount_scanner, "шт")
print(s.__str__())
print(s2.__str__())

с = Copier('1500', 'белый', 'Phaser','отсутствует')
с2 = Copier('3000', 'черный', 'Pantum','есть')
print(с.name(), с.amount_copier, "шт")
print(с.__str__())
print(с2.__str__())

###############################################################################
# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения 
# и умножения комплексных чисел. Проверьте работу проекта. 
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и 
# умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex_number:
    
    def __init__(self, number1, number2, *args):
        self.number1=number1
        self.number2=number2
        self.complex_number='number1 + number2*i'
        
    def __add__(self, other):
        return f'Сложение. Сумма равна: {self.number1 + other.number1} + {self.number2 + other.number2}*i'
    
    def __mul__(self, other):
        return f'Умножение. Произведение равно: {self.number1 * other.number1 - (self.number2 * other.number2)} + {self.number2 * other.number1} * i'
   
    def __str__(self):
        return f'z = {self.number1} + {self.number2} * i'    

a = Complex_number(1, -2)
b = Complex_number(3, 4)
print(a)
print(a + b)
print(a * b)



































