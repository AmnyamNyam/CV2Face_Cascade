import os
import random
import shutil

def create_unique_folder(base_folder_name):
    # Генерируем случайный символ
    random_int = str(random.randint(0,1000))

    # Создаем уникальное имя папки, добавляя случайный символ
    folder_name = base_folder_name + random_int

    # Проверяем, существует ли уже папка с таким именем
    while os.path.exists(folder_name):
        # Генерируем случайный символ
        random_int = str(random.randint(0, 1000))

        # Создаем уникальное имя папки, добавляя случайный символ
        folder_name = base_folder_name + random_int

    # Создаем новую папку
    os.makedirs(folder_name)

    return folder_name

def file_transfer(new_filename,new_folder_name):
    # Создаем путь к папке, куда должен быть перемещен файл
    destination_folder = os.path.join(os.getcwd(), new_folder_name)

    # Полный путь от и до по перемещению файла
    source = os.path.join(os.getcwd(),new_filename)
    destination = os.path.join(destination_folder,new_filename)

    # Перемещение файла
    shutil.move(source,destination)