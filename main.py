import requests


def download_update(url, file_path, github_version):
    response = requests.get(url)
    if response.status_code == 200:
        text_code = response.content.decode('utf-8')
        with open(file_path, 'wb') as file:
            text_code += f"\ncurrent_version = '{github_version}'\n"
            print(text_code)
            file.write(text_code.encode('utf-8'))

        print("Обновление загружено успешно.")
        return True
    else:
        print("Ошибка загрузки обновления.")
        return False


def check_for_updates(repo_owner, repo_name, file_path, current_version):
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    response = requests.get(api_url)

    if response.status_code == 200:
        content = response.json()
        github_version = content['sha']  # Пример использования хэша SHA файла как версии
        print(github_version)
        if github_version != current_version:
            print("Найдено новое обновление.")
            download_url = content['download_url']
            update_downloaded = download_update(download_url, file_path, github_version)

            if update_downloaded:
                # После успешной загрузки обновления
                # можно добавить код для применения обновления, например:
                # перезапуск приложения или обновление файлов
                # ...
                print("Обновление успешно применено.")
            else:
                print("Не удалось применить обновление.")
        else:
            print("Установлена последняя версия.")
    else:
        print("Ошибка при получении информации с GitHub.")


# Пример вызова функции для проверки обновлений
repo_owner = "FayChik"
repo_name = "Updates"
file_path = "main.py"
current_version = "d97338cd2e637e6aca1bec2c8c08138126230622"
check_for_updates(repo_owner, repo_name, file_path, current_version)
