import cv2
import matplotlib.pyplot as plt
import os
import folder_manipulation as fm

# Загрузка предобученной модели для обнаружения лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Замените 'your_directory_path' на путь к папке, где находятся ваши изображения
directory_path = 'your_directory_path'

# Создаем уникальную папку для обработанных фотографий с помощью нашего модуля folder_manipulation
base_folder_name = 'CascadedFaces_'
new_folder_name = fm.create_unique_folder(base_folder_name)
print(f"New folder created: {new_folder_name}")

# os.listdir возвращает список, содержащий имена файлов в данной директории
for filename in os.listdir(directory_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Замените или добавьте нужные вам расширения файлов

        # Загрузка изображения
        img = cv2.imread(os.path.join(directory_path,filename))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Преобразование изображения в оттенки серого
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Обнаружение лиц на изображении
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Рисование прямоугольников вокруг лиц синим цветом
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Сохранение изображения с разметкой
        plt.imshow(img)
        new_filename = (filename + 'Rectangle.png')
        plt.savefig(new_filename)

        # Перемещаем обработанное изображение в созданную нами ранее папку
        fm.file_transfer(new_filename,new_folder_name)