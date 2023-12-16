current_version = '1.2.2'

import requests


def download_update(url, file_path, text_code):
    try:
        with open(file_path, 'wb') as file:
            file.write(text_code)

            print("Обновление загружено успешно.")
            return True
    except BaseException as err:
        print(err)
        print("Ошибка загрузки обновления.")
        return False


def check_for_updates(repo_owner, repo_name, file_path, current_version):
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    response = requests.get(api_url)

    if response.status_code == 200:
        content = response.json()
        download_url = content['download_url']
        response = requests.get(download_url)
        for line in response.content.decode('utf-8').split('\n'):
            print(line)
            if line.startswith('current_version ='):
                version = sum([int(i) for i in current_version.split('.')])
                github_version = sum([int(i) for i in line.replace('current_version =', '').replace('\'', '').replace('"', '').replace(' ', '').split('.')])
                print(github_version)
                print(version)

                if version < github_version:

                    print("Найдено новое обновление.")
                    update_downloaded = download_update(download_url, file_path, response.content)

                    if update_downloaded:
                        # После успешной загрузки обновления
                        # можно добавить код для применения обновления, например:
                        # перезапуск приложения или обновление файлов
                        # ...
                        print("Обновление успешно применено.")
                    else:
                        print("Не удалось применить обновление.")
                break
            else:
                print("Установлена последняя версия.")
    else:
        print("Ошибка при получении информации с GitHub.")


# Пример вызова функции для проверки обновлений
repo_owner = "FayChik"
repo_name = "Updates"
file_path = "main.py"


def main():
    print(2, 3)
    print('Vuaaaaaa')
    print('Foeewf')


if __name__ == '__main__':
    check_for_updates(repo_owner, repo_name, file_path, current_version)
    main()


