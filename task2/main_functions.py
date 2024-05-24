from functools import reduce
# в наличии список множеств. внутри множества целые числа
# посчитать
#  1. общее количество чисел
#  2. общую сумму чисел
#  3. посчитать среднее значение
#  4. собрать все числа из множеств в один кортеж
# *написать решения в одну строку


def calc_count_in_list_of_sets(value):
    """
    Функция расчета количество чисел в списке множеств. внутри множества целые числа
    :param value: список множеств, внутри множества целые числа
    :return: общее количество чисел
    """
    return sum(map(lambda x: len(x), [elem for elem in value]))


def calc_sum_in_list_of_sets(value):
    """
    Функция расчета общей суммы чисел в списке множеств. внутри множества целые числа
    :param value: список множеств, внутри множества целые числа
    :return: общая сумма чисел в списке множеств
    """
    return sum(map(lambda x: sum(x), [x for x in value]))


def calc_average_in_list_of_sets(value):
    """
    Функция расчета среднего в списке множеств. внутри множества целые числа
    :param value:  список множеств, внутри множества целые числа
    :return: среднее значение
    """
    return calc_sum_in_list_of_sets(value)/calc_count_in_list_of_sets(value)

def convert_list_of_sets_to_tuple(value):
    """
    Функция расчета среднего в списке множеств. внутри множества целые числа
    :param value:  список множеств, внутри множества целые числа
    :return: собирает числа в кортеж
    """
    return reduce(lambda a, b: a + b, tuple(map(lambda x: tuple(x), [x for x in m])))


m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
print(calc_count_in_list_of_sets(m))
print(calc_sum_in_list_of_sets(m))
print(calc_average_in_list_of_sets(m))
print(convert_list_of_sets_to_tuple(m))
