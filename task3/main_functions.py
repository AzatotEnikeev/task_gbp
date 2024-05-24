
def convert_list_of_lists_to_list_of_dict_with_zip(list_of_lists):
    """
    :param list_of_lists: list[list] входной список списков
    :return: list[dict] список словарей
    """
    return [dict(zip(['k' + str(x) for x in a[0]], elem)) for elem in a]


def convert_list_of_lists_to_list_of_dict(list_of_lists):
    """
    :param list_of_lists: list[list] входной список списков
    :return: list[dict] список словарей
    """
    return [{f"k{count + 1}": num for count, num in enumerate(elem)} for elem in a]
a = [[1,2,3], [4,5,6]]
print(convert_list_of_lists_to_list_of_dict_with_zip(a))
print(convert_list_of_lists_to_list_of_dict(a))