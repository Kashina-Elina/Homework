class ExceptionName(Exception):
    ...


class ExceptionAgeInt(Exception):
    ...


class ExceptionAge(Exception):
    ...


class ExceptionEmail(Exception):
    ...


users = [('name1', '1@mail.ru', 18.1), ('name2', '2@mail.ru', 15), ('name3', '3@mail.ru', 21), ('name4', '@mail.ru', 19), ('name1', '5@mail.ru', 20), ('name6', '6@gmail.com', 17)]
new_users = []
usernames = []
for i in users:
    try:
        if i[0] in usernames:
            raise ExceptionName()
        usernames.append(i[0])
        if i[-1] < 16:
            raise ExceptionAge()
        if not str(i[-1]).isdigit() or not type(i[-1]) == int:
            raise ExceptionAgeInt()
        if i[1].count('@') != 1 or i[1][0] == '@' or i[1][-1] == "@":
            raise ExceptionEmail()
        new_users.append(i[:-1])

    except ExceptionName:
        print("Имя пользователя не уникально")
    except ExceptionAgeInt:
        print("Возраст не является положительным целым числом")
    except ExceptionAge:
        print("Пользователю меньше 16 лет")
    except ExceptionEmail:
        print("Адрес электронной почты недействителен")
print()
print(new_users)