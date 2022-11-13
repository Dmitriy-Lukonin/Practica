from Polymorphism import Rectangle, Square, Circle

#создаем два прямоугольника

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print('выводим площади прямоугольников')
print(rect_1.get_area())
print(rect_2.get_area())

#создаем два квадрата
square_1 = Square(5)
square_2 = Square(10)

print('выводим площади квадратов')
print(square_1.get_area_square(),
      square_2.get_area_square())

# функция isinstance, поддерживающая наследование.
# Она проверяет, является ли аргумент объекта экземпляром класса
# или экземпляром класса из кортежа. В случае если является,
# функция возвращает True, если не является — False

print('выводим площади квадратов и прямоугольников')
figures = [rect_1, rect_2, square_1, square_2]
for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())

#создаем два круга
circle_1 = Circle(5)
circle_2 = Circle(10)

print('выводим площади кругов')
print(circle_1.get_area_circle(),
      circle_2.get_area_circle())

print('выводим площади квадратов, прямоугольников и кругов')
figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())