import main
import os
import time

def test_task4_delete_files_elder_n_days():
    with open('test\\test_for_del.txt', 'tw', encoding='utf-8') as f:
        pass
    # Получаем текущее время
    current_time = time.time()
    # Устанавливаем желаемую дату и время модификации
    creation_time = current_time - 3600 * 24 * 8  # Вычитаем (в секундах)
    modification_time = current_time - 3600 * 24 * 8  # Вычитаем  (в секундах)
    # Устанавливаем дату и время модификации файла
    os.utime('test\\test_for_del.txt', (creation_time, modification_time))
    assert(main.delete_files_elder_n_days(os.path.abspath(os.curdir + '\\test'), 7))


