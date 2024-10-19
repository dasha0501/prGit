"""Функция вывода сообщения"""
def print_message(message):
    name = input("Введите ваше имя: ") #Инпут для ввода имени
    print(message + name) #Выводит переданное сообщение на экран

"""Главная функция программы"""
def main():
    msg = "Hello world from "
    print_message(msg) #Вывод сообщения

"""Запуск главной функции"""
if __name__ == "__main__":
    main()