def print_message(message):
    name = input("Введите ваше имя: ")
    """Выводит переданное сообщение на экран."""
    print(message + name)

def main():
    msg = "Hello world from "
    print_message(msg)

if __name__ == "__main__":
    main()