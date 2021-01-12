import vk_api
import colorama
from colorama import Fore
from vk_api import VkUpload
import time
colorama.init()

# Баннер
banner = ["""
Накрутка Фотографий

Офицальная версия

VK Автора: @vkshit

██████▄▄░░░░░░░░░░░░░░░░░░░░░░░░▄▄██████
███████▀██▄░░░░░░░░░░░░░░░░░░▄██▀███████
░█████░░░░▀█▄░░▄▄▄▄▄▄▄▄▄▄░░▄█▀░░░░█████░
░▀███▀░░░░▄███▀▀▀▀░░░░▀▀▀▀███▄░░░░▀███▀░
░░▀██░░░░░▀▀░░░░░░░░░░░░░░░░▀▀░░░░░██▀░░
░░░▀█▄▄██░░░░░░░░░░░░░░░░░░░░░░██▄▄█▀░░░
░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░
░░░░░░█▀░░░░░░░░░░░░░░░░░░░░░░░░▀█░░░░░░
░░░░░██░░▄▄██▄░░░░░░░░░░░░▄██▄▄░░██░░░░░
░░░░░██░▄█▀░███░░░░░░░░░░███░▀█▄░██░░░░░
░░░░▄█▀░▀█▄▄▄█▀░░░░▄▄░░░░▀█▄▄▄█▀░▀█▄░░░░
░░░░██▄▄▄░▀▀▀░░░░░▀██▀░░░░░▀▀▀░▄▄▄██░░░░
░░░████████░░░▀█▄▄▄██▄▄▄█▀░░░████████░░░
░░░▀████████░░░░░█░░░░█░░░░░████████▀░░░
░░░░▀██████░░░░░░█▄░░▄█░░░░░░██████▀░░░░
░░░░░▀███▀░░░░░░░▀█▄▄█▀░░░░░░░▀███▀░░░░░
░░░░░░░░▀██▄▄░░░░░░▀▀░░░░░░▄▄██▀░░░░░░░░
░░░░░░░░░░░▀▀▀███▄▄▄▄▄▄███▀▀▀░░░░░░░░░░░

Version: 1.3
"""]

print(Fore.YELLOW + banner[0])

# Введите название фото из папки в скобках
var1 = ['photo1.jpg', 'photo2.jpg', 'photo3.jpg', 'photo4.jpg', 'photo5.jpg']

var2 = ['photo6.jpg', 'photo7.jpg', 'photo8.jpg', 'photo9.jpg', 'photo10.jpg']

var3 = ['photo11.jpg', 'photo12.jpg', 'photo13.jpg', 'photo14.jpg', 'photo15.jpg']

var4 = ['photo16.jpg', 'photo17.jpg', 'photo18.jpg', 'photo19.jpg', 'photo20.jpg']

# Получение токена
token = input('Введите Токен Страницы: ')

print()
print("VKPhoto1.3\n\n1. Запустить скрипт\n2. Передать спасибо создателю скрипта\n3. Что нового")
punkt = str(input("Введите пункт: "))

if punkt == "1":
    # Получение данных
    album = input('Введите ИД альбома: ')

    # Авторизация
    vk_session = vk_api.VkApi(token=token)
    upload = VkUpload(vk_session)
    vk = vk_session.get_api()
    print("Накрутка включена, для остановки нажмите 'Ctrl + C'")


    # Функция на загрузку фотографий
    def photos(n):
        upload.photo(photos=n, album_id=album)


    vk_time = int(0)

    while True:
        try:
            vk_time = vk_time + 1
            photos(var1)
            photos(var2)
            photos(var3)
            photos(var4)
            if vk_time == 350:
                print("Обход капчи ВКонтакте, подождите 2 Минуты!")
                vk_time = int(0)
                time.sleep(120)

        except Exception as error:
            print("Внимание Возникла Ошибка!")
            print(repr(error))
            time.sleep(60)

elif punkt == "2":
    # Авторизация
    vk_session = vk_api.VkApi(token=token)
    upload = VkUpload(vk_session)
    vk = vk_session.get_api()

    vk.messages.send(user_id=622629328, message="Спасибо тебе за VKPhoto1.3", random_id=0)
    print("Вы отправили спасибочки!")

elif punkt == "3":
    print("-- Улучшенный обход капчи\n-- Накрутка стала еще быстрее\n-- Приятный интерфейс, \n-- Сменился мой ID в ВК")

else:
    print("Вы ввели не верный пункт")
