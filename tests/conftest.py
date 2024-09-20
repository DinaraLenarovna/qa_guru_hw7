import os
import shutil
import zipfile
import pytest
from script_os import FILES_DIR, FOLDER_DIR, ZIP_DIR


@pytest.fixture(scope="session", autouse=True)
def files_into_archive():
    if not os.path.exists(FOLDER_DIR):  # проверяем существует ли папка
        os.mkdir(FOLDER_DIR)  # создаем папку если её нет
    with zipfile.ZipFile(ZIP_DIR, 'w') as zf:  # создаем архив
        for file in os.listdir(FILES_DIR):  # добавляем файлы в архив
            zf.write(os.path.join(FILES_DIR, file), file)  # добавляем файл в архив

    yield
    shutil.rmtree(FOLDER_DIR)  # удаляем папку со всеми файлами и подпапками
