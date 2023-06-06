from dataclasses import dataclass


class ExceptionName(Exception):
    ...


class ExceptionAgeInt(Exception):
    ...


class ExceptionAge(Exception):
    ...


class ExceptionEmail(Exception):
    ...


@dataclass
class User:
    name: str
    mail: str
    age: int


users = [User('1', '1@mail.ru', 20), User('2', '1mail.ru', 20), User('3', '3@mail.ru', 14), User('1', '4@mail.ru', 20)]
new_users = []
usernames = []
for i in users:
    try:
        if i.name in usernames:
            raise ExceptionName()
        usernames.append(i.name)
        if i.age < 16:
            raise ExceptionAge()
        if not str(i.age).isdigit() or not type(i.age) == int:
            raise ExceptionAgeInt()
        if i.mail.count('@') != 1 or i.mail[0] == '@' or i.mail[-1] == "@":
            raise ExceptionEmail()
        new_users.append([i.name, i.mail])

    except ExceptionName:
        print("Имя пользователя не уникально")
    except ExceptionAgeInt:
        print("Возраст не является положительным целым числом")
    except ExceptionAge:
        print("Пользователю меньше 16 лет")
    except ExceptionEmail:
        print("Адрес электронной почты недействителен")

print(new_users)