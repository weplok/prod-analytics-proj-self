import requests
from bs4 import BeautifulSoup


def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content


def download_file(url, file_name):
    response = requests.get(url)
    with open(f"raw_data/{file_name}", 'wb') as file:
        file.write(response.content)

def parse_website(url):
    text = read_html_file(url)
    soup = BeautifulSoup(text, 'html.parser')

    # Пример поиска файлов по определенному селектору
    links = soup.find_all('a')  # Измените селектор в соответствии с вашим случаем

    for link in links:
        print(link)
        href = link.get('href')
        if href and href.endswith('.zip'):  # Добавьте нужные форматы
            file_name = href.split('/')[-1]
            download_file(href, file_name)
            print(f'Файл {file_name} загружен.')

if __name__ == '__main__':
    website_url = 'index.html'  # Замените на нужный URL
    parse_website(website_url)
