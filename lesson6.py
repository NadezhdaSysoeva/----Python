#1. Создать класс  (светофор).
#определить у него один атрибут color (цвет) и метод running (запуск);
#атрибут реализовать как приватный;
# рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#продолжительность первого состояния (красный) составляет 7 секунд, 
#второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#переключение между режимами должно осуществляться только в указанном порядке 
#(красный, жёлтый, зелёный);
#проверить работу примера, создав экземпляр и вызвав описанный метод.

from itertools import cycle
from time import sleep

class TrafficLight:
    __color = cycle([
        {'режим': 'красный', 'период': 7},
        {'режим': 'желтый', 'период': 2},
        {'режим': 'зеленый', 'период': 5},
        ])

    def running(self):
        light = next(self.__color)
        print(f"Сигнал {light['режим']}, пауза {light['период']} сек.")
        sleep(light['период'])

traffic_light = TrafficLight()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()


###############################################################################
#2. Реализовать класс Road (дорога).
#определить атрибуты: length (длина), width (ширина);
#значения атрибутов должны передаваться при создании экземпляра класса;
#атрибуты сделать защищёнными;
#определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#использовать формулу: длина*ширина*масса асфальта для покрытия 
#одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
#проверить работу метода.

class Road():

    __weight = float(input('Введите вес асфальта в тоннах для 1 кв.м. полотна толщиной в 1 см\n '))

    def __init__(self, length, width):
        self._length = length
        self._width = width
       
    def get_weight(self, thickness):
        ret_val = self._length * self._width * thickness * self.__weight
        print(f'Вес асфальта, требуемый для укладки полотна толщиной {thickness} см, равен {ret_val} т')

        return ret_val

r = Road(100, 5)
w = r.get_weight(10)

##############################################################################
#3. Реализовать базовый класс Worker (работник).
#определить атрибуты: name, surname, position (должность), income (доход);
#последний атрибут должен быть защищённым и ссылаться на словарь, содержащий 
#элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
#создать класс Position (должность) на базе класса Worker;
#в классе Position реализовать методы получения полного имени сотрудника 
#(get_full_name) и дохода с учётом премии (get_total_income);
#проверить работу примера на реальных данных: создать экземпляры класса Position, 
#  передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name:str, surname:str, position:str, wage:int, bonus:int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'оклад': wage, 'премия': bonus}
        
class Position(Worker):
    def get_full_name(self):
        full_name=f"{self.name} {self.surname}"
        return full_name
    def get_total_income(self):
        total_income=sum(self._income.values())
        return total_income   

nadya=Position("Надежда","Сысоева","ведущий эксперт", 100000, 30000)
print(nadya.get_full_name())
print(nadya.position)
print(nadya.get_total_income())
    
      
##############################################################################
#4. Реализуйте базовый класс Car.
#у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
#А также методы: go, stop, turn(direction), которые должны сообщать, 
#что машина поехала, остановилась, повернула (куда);
#опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#добавьте в базовый класс метод show_speed, который должен показывать текущую 
#скорость автомобиля;
#для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
#сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. 
#Выполните доступ к атрибутам, выведите результат. 
#Вызовите методы и покажите результат.

class Car:
    def __init__(self, color:str, name:str, is_police:bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self, speed):
        self.speed = speed
        print(f' разгоняемся до {speed} км/ч') 
    
    def stop(self):
        self.speed = 0
        print('Останавливаемся')
        
    def turn(self, direction:str):
        if self.speed > 0:
          print(f'Поворачиваем {direction}')
        else:
          print('Не можем повернуть - мы стоим на месте')
          
    def show_speed(self):
        print(f"Скорость равна {self.speed}")

class TownCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False
    def show_speed(self):
        if self.speed > 60:
            print('Внимание!!! Скорость превышена!!!')
        else:
            print(f'Скорость равна {self.speed} км/ч')

class SportCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

class WorkCar(Car):
    
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False
    
    def show_speed(self):
        if self.speed > 40:
            print('Внимание!!! Скорость превышена!!!')
        else:
            print(f'Скорость равна {self.speed} км/ч')
            
class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True

def test_drive(model):
    print(f"Тест-драйв {'полицейского' if model.is_police else 'гражданского'} автомобиля {model.name}, цвет {model.color}")
    model.go(40)
    model.show_speed()
    model.turn('направо')
    model.stop()
    model.show_speed()
    model.turn('налево')
    model.go(60)
    model.show_speed()
    model.go(120)
    model.show_speed()
    model.stop()
    print("Тест-драйв окончен")

car = Car('белый', 'Kia Optima', False)
test_drive(car)

polo = TownCar('коричневый', 'Volkswagen Polo')
test_drive(polo)

veyron = SportCar('желтый', 'Bugatti Veyron')
test_drive(veyron)

largus = WorkCar('красный', 'Lada Largus')
test_drive(largus)

mondeo = PoliceCar('синий', 'Ford Mondeo')
test_drive(mondeo)


###############################################################################
#5. Реализовать класс Stationery (канцелярская принадлежность).
#определить в нём атрибут title (название) и метод draw (отрисовка). 
#Метод выводит сообщение «Запуск отрисовки»;
#создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#в каждом классе реализовать переопределение метода draw. 
#Для каждого класса метод должен выводить уникальное сообщение;
#создать экземпляры классов и проверить, что выведет описанный метод для 
#каждого экземпляра.


class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}')
        
class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}')
        
class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}')

st=Stationery('Гусиное перо')
st.draw()

pen = Pen('Гелевая')
pen.draw()

pencil = Pencil('Простой')
pencil.draw()

handle = Handle('Черный')
handle.draw()














