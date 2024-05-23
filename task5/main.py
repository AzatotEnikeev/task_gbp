# -*- coding: utf-8 -*-
from typing import Dict, List


def create_dict_from_file(file_local_path: str) -> Dict[str, List[str]]:
	"""
	Возвращает словарь где ключ, первая буква слова
	:param file_local_path: Путь до файла
	"""
	dict_words = dict()
	with open(file_local_path, encoding='utf-8') as f:
		for line in f.readlines():
			word = line.strip()
			try:
				dict_words[word[0]].append(word)
			except KeyError:
				dict_words[word[0]] = [word]
	return dict_words


def find_combine_second_word(first_word: str, dict_words: Dict[str, List[str]]) -> List[str]:
	"""
	Перебираем с конца первого слова возможные буквы и ищем сооветствие в словаре
	:param first_word: Слово которое будет первым в комбинации
	:param dict_words: Словарь по которому ищем возможные вторые слова
	:return:
	"""
	cur_position_from_end = len(first_word) - 1
	length = 1
	result_list = []
	while cur_position_from_end > -1:
		# перебираем возможные "первые буквы с конца"
		key = first_word[cur_position_from_end]
		if key in dict_words:
			for second_word in dict_words[key]:
				# проверяем чтобы не тоже самое слово либо аннаграмма
				if second_word != first_word:
					start_second_word = second_word[0:length]
					last_first_word = first_word[cur_position_from_end:cur_position_from_end+length]
					if start_second_word == last_first_word:
						result_list.append(first_word+second_word[length:])
		length = length + 1
		cur_position_from_end = cur_position_from_end - 1
	return result_list


if __name__ == "__main__":
	dict_words = create_dict_from_file("test.txt")
	continue_words = True
	while continue_words:
		first_word = input("Введите \"первое\" слово: ")
		res_list = find_combine_second_word(first_word, dict_words)

		if len(res_list) > 0:
			for word in res_list:
				print(f'{word}')
		else:
			print(f'Невозможно найти комбинацию')

		symb = input("\n Желаете продолжить? y - следующее слово, иначе выход")
		if symb != 'y':
			continue_words = False
