first = int(input('Введите целое число: '))
second = int(input('Введите целое число: '))
third = int(input('Введите целое число: '))

print(first, second, third)

if first != second and first != third and second != third:
    print(0)
elif first == second == third:
    print(3)
elif first == second and first != third and second != third:
    print(2)
elif first != second and first == third and second != third:
    print(2)
elif first != second and first != third and second == third:
    print(2)


