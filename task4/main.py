from datetime import datetime
import os
import time


def delete_files_elder_n_days(root_dir_path: str, days: int):
    try:
        convert_to_sec = 60*60*24
        res = False
        files_list = os.listdir(root_dir_path)
        current_time = time.time()
        for file in files_list:
            file_path = os.path.join(root_dir_path, file)
            if os.path.isfile(file_path):
                if (current_time - os.stat(file_path).st_mtime) > days * convert_to_sec:
                    os.remove(file_path)
                    print(file_path, ' удаление прошло успешно')
                    res = True
        print('Работа функции закончена')
        return res
    except OSError as e:
        print("OSError: {} filename {}".format(e.strerror, e.filename))


