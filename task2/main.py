from functools import reduce
# в наличии список множеств. внутри множества целые числа
# посчитать
#  1. общее количество чисел
#  2. общую сумму чисел
#  3. посчитать среднее значение
#  4. собрать все числа из множеств в один кортеж
# *написать решения в одну строку
m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
print(m)
all_count = sum(map(lambda x: len(x), [elem for elem in m]))
print(all_count)
all_sum = sum(map(lambda x: sum(x), [x for x in m]))
print(all_sum)
average = sum(map(lambda x: sum(x), [x for x in m]))/sum(map(lambda x: len(x), [elem for elem in m]))
print(average)
to_tuple = reduce(lambda a, b: a + b,tuple(map(lambda x: tuple(x), [x for x in m])))
print(to_tuple)
