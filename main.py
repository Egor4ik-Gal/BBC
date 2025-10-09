def lvl1():
    m = input("Выбери метод: 1)upper 2)lower 3)capitalize ")
    print("Напиши текст!")
    text = input()
    if m == "1":
        print("Я сделаю все буквы заглавными")
        print(text.upper())
    elif m == "2":
        print("Я сделаю все буквы маленькими")
        print(text.lower())
    elif m == "3":
        print("Я сделаю первую букву предложения заглавной")
        print(text.capitalize())

def lvl2():
    print("Выбери метод: 1)find 2)replace 3)count 4)index")
    m = input()
    if m == "1":
        text = input("Введи строчку в которой нужно найти индекс первого вхождения элемента ")
        text2 = input("Введи подстроку которую нужно найти ")
        if text.find(text2) != -1:
            print(f"Первая подстрока {text2} находится по индексу {text.find(text2)}")
        else:
            print("Данная подстрока не встречается в твоей (((")
    elif m == "2":
        text = input("Введи свою срочку ")
        text2 = input("А теперь символ, который хочешь заменить ")
        text3 = input("А теперь то, на что хочешь заменить ")
        if text2 in text:
            print(text.replace(text2, text3))
        else:
            print("У тебя нет такого символа для замены")
    elif m == "3":
        text = input("Введи свою строчку ")
        text2 = input("Введи какой символ (-ы) подсчитать ")
        print(text.count(text2)) #метод .cont() принимает на переменную,
        # а также индекс начала и конца для подсчета символа в строке, возвращает количество символов на данном промежутке
    elif m == "4":
        text = input("Введи строчку в которой нужно найти индекс первого вхождения элемента,"
                     " но будь осторожен, она обязательно должна быть в твоей 1 строке ")
        text2 = input("Введи подстроку которую нужно найти ")
        if text2 in text:
            print(text.index(text2)) # Все тоже самое что .find(), но при подстроке, которая не содержится в строке, выдает ошибку


def lvl3():
    print("Выбери метод: 1)split 2)join")
    m = input()
    if m == "1":
        text = input("Введи свою строчку, которую хочешь перевести в list ")
        text2 = input("Введи разделитель для разбития по элементам списка ")
        print(text.split(text2))
    elif m == "2":
        text = input("Введи текст через пробел ").split()
        text2 = input("Введи через какой разделитель хочешь его видеть ")
        print(text2.join(text))


def lvl4():
    print("Выбери метод: 1)isdigit 2)isalpha 3)strip() 4)format()")
    m = input()
    if m == "1":
        text = input("Введи строку и я проверю только ли цифры в ней ")
        print(text.isdigit())
    elif m == "2":
        text = input("Введи строку и я проверю только ли в ней буквы ")
        print(text.isalpha())
    elif m == "3":
        text = input("Введи строку и я удалю лишный символ с двух сторон ")
        text2 = input("Введи какой символ нужно удалить по бокам строки ")
        print(text.strip(text2))
    elif m == "4":
        text = input("Введи строчку с 1 пустой внутри {} и внутри этого я выведи тебе 13 ")
        print(text.format("13"))



def lvl5():
    text = "                     pYtHon;is;AWESome;               "
    text = text.split(';')
    text[0] = text[0].capitalize()
    text[1] = text[1].lower()
    text[2] = text[2].lower()
    print(' '.join(text).strip())





print("Выбери уровень: 1, 2, 3, 4, 5")
lvl = input()
if lvl == "1":
    lvl1()
elif lvl == "2":
    lvl2()
elif lvl == "3":
    lvl3()
elif lvl == "4":
    lvl4()
elif lvl == "5":
    lvl5()



