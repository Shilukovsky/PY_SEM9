# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
# между ними в 2D пространстве.
ax = float(input('введите координату х первой точки'))
ay = float(input('введите координату y первой точки'))
bx = float(input('введите координату х второй точки'))
by = float(input('введите координату y второй точки'))
print(round(((bx - ax)**2 + (by - by)**2)**1/2, 3))