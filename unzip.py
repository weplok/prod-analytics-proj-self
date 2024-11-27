import os
import zipfile


def unzip_csv_xlsx_files(folder_path):
    # Проходим по всем файлам в указанной папке
    for item in os.listdir(folder_path):
        # Формируем полный путь к файлу
        item_path = os.path.join(folder_path, item)

        # Проверяем, является ли файл ZIP-архивом
        if item.endswith('.zip') and os.path.isfile(item_path):
            print(f'Распаковываем {item_path}...')
            with zipfile.ZipFile(item_path, 'r') as zip_ref:
                # Проходим по всем файлам в архиве
                for file_info in zip_ref.infolist():
                    # Извлекаем только CSV и XLSX файлы
                    if file_info.filename.endswith(('.csv', '.xlsx')):
                        # Извлекаем файл
                        zip_ref.extract(file_info, folder_path)
                        print(f'Извлечен: {file_info.filename}')


if __name__ == '__main__':
    folder_path = 'raw_data'  # Укажите путь к вашей папке
    unzip_csv_xlsx_files(folder_path)
