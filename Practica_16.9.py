

# Задание 16.9.1

# Создайте метод, который возвращает атрибуты прямоугольника как строку
# (постарайтесь применить магический метод __str__). Для объекта прямоугольника со значениями
# атрибута x = 5, y = 10, width = 50, height = 100 метод должен вернуть строку Rectangle : 5, 10, 50, 100.


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle : {self.x}, {self.y}, {self.width}, {self.height}.'


r1 = Rectangle (5, 10, 50, 100)
r2 = Rectangle (5, 10, 25, 50)


print(r1.x, r1.y, r1.width, r1.height) # выводит без метода __str__
print(r2)


#-----------------------------------------------------------------------------------------------------------------------


# Задание 16.9.2

# Напишите код для описания геометрической фигуры.
# Создайте класс «прямоугольник» с помощью метода init().
# На выходе в консоли вам необходимо получить площадь данной фигуры.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def figure_area(self):
        return self.width * self.height


r1 = Rectangle(50, 100)
r2 = Rectangle(25, 50)

print(r1.figure_area())
print(r2.figure_area())


#-----------------------------------------------------------------------------------------------------------------------


# Задание 16.9.3
# В проекте «Дом питомца» добавим новую услугу — электронный кошелек.
# Необходимо создать класс «Клиент», который будет содержать данные о клиентах и их финансовых операциях.
# О клиенте известна следующая информация: имя, фамилия, город, баланс.

# Далее сделайте вывод о клиентах в консоль в формате:
# «Иван Петров. Москва. Баланс: 50 руб.»

class User:
    def __init__(self, first_name, last_name, city, cash):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.cash = (round(cash, 2))

    def __str__(self):
        return f'<<{self.first_name} {self.last_name}. {self.city}. Баланс: {self.cash} руб.>>'

user1 = User('Roman', 'Ibramovich', 'Saratov', 100000000.00)
user2 = User('Elvira', 'Nibulina', 'Ufa', 10000000.00)
user3 = User('Aleksandr', 'Ivanov', 'Ulan-Ude', 1.546)

print(user1)
print(user2)
print(user3)


#-----------------------------------------------------------------------------------------------------------------------


# Задание 16.9.4
# Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов.
# Вам необходимо написать программу, которая позволит составить список гостей.
# В класс «Клиент» добавьте метод, который будет возвращать информацию только об имени, фамилии и городе клиента.

# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

class User:
    def __init__(self, first_name, last_name, city, cash):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.cash = (round(cash, 2))

    def __str__(self):
        return f'<<{self.first_name} {self.last_name}. {self.city}. Баланс: {self.cash} руб.>>'

    def get_guest(self):
        return f'{self.first_name} {self.last_name}. {self.city}'

user1 = User('Roman', 'Ibramovich', 'Saratov', 100000000.00)
user2 = User('Elvira', 'Nibulina', 'Ufa', 10000000.00)
user3 = User('Aleksandr', 'Ivanov', 'Ulan-Ude', 1.546)

guest_list = [user1, user2, user3]

for guest in guest_list:
    print(guest.get_guest())


#-----------------------------------------------------------------------------------------------------------------------