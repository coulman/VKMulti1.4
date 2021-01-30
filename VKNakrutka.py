import vk_api
import colorama
from colorama import Fore
from vk_api import VkUpload
import time
import random
colorama.init()

# Баннер
banner = ["""
Накрутка Фотографий - Накрутка Сообщений

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

Version: 1.4
"""]


print(Fore.YELLOW + banner[0])

# Введите название фото из папки в скобках
var1 = ['photo1.jpg', 'photo2.jpg', 'photo1.jpg', 'photo2.jpg', 'photo1.jpg']
token = []

# Получение токена
with open("token.txt", "r") as f1:
    printer = str(f1.readline())
    if printer == "":
        token = input("Введите Токен Страницы: ")
        print("Хотите сохранить токен? Напишите 'y' если согласны если нет 'n'\n")
        save = input("Хотите сохранить?: ").lower()
        if save == "y":
            with open("token.txt", "w") as f2:
                f2.write(token)

        else:
            pass
    else:
        pass

print()
print("VKMulti1.4\n\n1. Запустить накрутку фотографий\n2. Запустить накрутку сообщений\n3. Передать спасибо создателю скрипта\n4. Удалить токен\n5. Что нового?")
punkt = str(input("Введите пункт: "))

if punkt == "1":
    # Получение данных
    album = input('Введите ИД альбома: ')

    # Авторизация
    vk_session = vk_api.VkApi(token=token)
    upload = VkUpload(vk_session)
    vk = vk_session.get_api()
    print("Накрутка включена, для остоновки нажмите 'Ctrl + C'")


    # Функция на загрузку фотографий
    def photos(n):
        upload.photo(photos=n, album_id=album)


    vk_time = int(0)

    while True:
        try:
            vk_time = vk_time + 1
            photos(var1)
            if vk_time == 350:
                print("Обход капчи ВКонтакте, подождите '2' Минуты!")
                vk_time = int(0)
                time.sleep(120)

        except Exception as error:
            print("Внимание Возникла Ошибка!")
            print(repr(error))
            time.sleep(60)

elif punkt == "2":
    print("Выберите вариант накрутки:\n\n1. Накрутка через фейк(рекомендация)\n2. Обычная накрутка")
    print()
    punkt_ = str(input("Введите вариант: "))

    if punkt_ == "1":
        # Авторизация
        print("Для этого способа вам нужен второй аккаунт, если у вас нету второго аккаунта, то используйте второй способ!\n[WARNING]: Фейк аккаунт у вас должен быть в друзях!")
        print()
        token2 = input("Введите токен фейка: ")
        vk_session = vk_api.VkApi(token=token2)
        vk = vk_session.get_api()
        vk_time1 = int(0)
        print()
        b = input("Введите цифровой ид от основного аккаунта: ")

        while True:
            try:
                # Накрутка сообщений вариант 1
                vk_time1 = vk_time1 + 1
                vk.messages.createChat(user_ids=b, title="MSGBOOST")
                print(vk_time1)
                if vk_time1 > 4:
                    print("Обход капчи ВКонтакте подождите 40 секунд")
                    vk_time1 = int(0)
                    time.sleep(40)
                else:
                    time.sleep(10)

            except Exception as error:
                print("Внимание Возникла Ошибка!")
                print(repr(error))
                time.sleep(40)

    elif punkt_ == "2":
        # Авторизация
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()
        sender = ["Привет!", "Всмысле?", "Зачем?", "Разве?", "Что??", "Ты кто?", "Знакомы?"]
        timer = int(input("Введите задержку (Defult 30 Sek): "))
        print()
        print("Скрипт успешно запущен!")
        while True:
            try:
                # Накрутка сообщений вариант 2
                idr = random.randint(600000000, 700000000)
                check = vk.users.get(user_ids=idr)

                if "DELETE" in check:
                    continue

                vk.messages.send(user_id=idr, message=random.choice(sender), random_id=0)
                print("Байтанул")
                time.sleep(timer)

            except Exception as error:
                print("Внимание Возникла Ошибка!")
                print(repr(error))
                time.sleep(40)

elif punkt == "3":
    # Авторизация
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()

    # Отправка спасибки
    vk.messages.send(user_id=622629328, message="Спасибо тебе за VKPhoto1.4", random_id=0)
    print("Вы отправили спасибочки!")

elif punkt == "4":
    with open("token.txt", "w") as f:
        f.write("")
    print("Успешно удалили токен")

elif punkt == "5":
    print("-- Улучшенный обход капчи\n-- Накрутка стала еще быстрее\n-- Добавил накрутку сообщений 2 вариантов\n-- Приятный интерфейс\n-- Сменился мой ID в ВК")

else:
    print("Вы ввели не верный пункт")
