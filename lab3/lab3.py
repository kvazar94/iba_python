# Вариант 7	Создать класс Book: id, Название, Автор (ы), Издательство,
# Год издания, Количество страниц, Цена, Тип переплета.
# Функции-члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов. Вывести:
# a)	список книг заданного автора;
# b)	список книг, выпущенных после заданного года.



class Book:
    """"
    __Id = 0
    __Name = "Unknown"
    __Author = "Unknown"
    __Publisher = "Unknown"
    __Year = 0
    __NumberOfPages = 0
    __Price = 0
    __BindingType = "Unknown"
"""
    def __init__(self, Id, Name, Author, Publisher, Year, NumberOfPages, Price, BindingType):
        self.__Id = Id
        self.__Name = Name
        self.__Author = Author
        self.__Publisher = Publisher
        self.__Year = Year
        self.__NumberOfPages = NumberOfPages
        self.__Price = Price
        self.__BindingType = BindingType

    def set_Id(self, Id):
        self.__Id = Id

    def get_Id(self):
        return self.__Id

    def set_Name(self, Name):
        self.__Name = Name

    def get_Name(self):
        return self.__Name

    def set_Author(self, Author):
        self.__Author = Author

    def get_Author(self):
        return self.__Author

    def set_Publisher(self, Publisher):
        self.__Publisher = Publisher

    def get_Publisher(self):
        return self.__Publisher

    def set_Year(self, Year):
        self.__Year = Year

    def get_Year(self):
        return self.__Year

    def set_NumberOfPages(self, NumberOfPages):
        self.__NumberOfPages = NumberOfPages

    def get_NumberOfPages(self):
        return self.__NumberOfPages

    def set_Price(self, Price):
        self.__Price = Price

    def get_Price(self):
        return self.__Price

    def set_BindingType(self, BindingType):
        self.__BindingType = BindingType

    def get_BindingType(self):
        return self.__BindingType

    def display_info(self):
        print(self.__str__())

    def __str__(self):
        return "Название книги: {}".format(self.__Name)




list_of_books = []

list_of_books.append(Book(0, "Задча трех тел", "Лю Цысинь", "Эксмо", 2017, 464, 25.54, "твердая"))
list_of_books.append(Book(1, "Темный лес", "Лю Цысинь", "Эксмо", 2018, 640, 24.31, "твердая"))
list_of_books.append(Book(2, "Вечная жизнь смерти", "Лю Цысинь", "Эксмо", 2018, 688, 21.18, "твердая"))
list_of_books.append(Book(3, "Дэнс, дэнс, дэнс", "Харуки Мураками", "Эксмо", 2020, 608, 8.06, "мягкая"))
list_of_books.append(Book(4, "Охота на овец", "Харуки Мураками", "Эксмо", 2009, 446, 18.56, "твердая"))
list_of_books.append(Book(5, "Норвежский лес", "Харуки Мураками", "Эксмо", 2020, 384, 9.72, "мягкая"))
list_of_books.append(Book(6, "Мексиканская готика", "Сильвия Гарсия", "Рипол", 2020, 352, 20.67, "твердая"))
list_of_books.append(Book(7, "Вы, конечно, шутите, мистер Фейнман", "Ричард Фейнман", "Аст", 2019, 480, 13.05, "твердая"))
list_of_books.append(Book(8, "Не все ли равно, что думают другие?", "Ричард Фейнман", "Аст", 2019, 480, 7.24, "мягкая"))
list_of_books.append(Book(9, "Послемрак", "Харуки Мураками", "Эксмо", 2020, 224, 6.63, "мягкая"))
"""
inp_author = str(input("Введите автора:\n"))
i = 0


while i < len(list_of_books):
    if str(list_of_books[i].get_Author()) in inp_author:
        print(list_of_books[i], "\n")
    i += 1
"""
inp_a = str(input("Ведите автора:"))
def find_author(inp_author):
    i = 0
    while i < len(list_of_books):
        if inp_author in str(list_of_books[i].get_Author()):
            print(list_of_books[i])
        i+=1

find_author(inp_a)

inp_y = int(input("Ведите год:"))


def find_year(inp_year):
    j = 0

    while j < len(list_of_books):
        if inp_year <= int(list_of_books[j].get_Year()):
            print(list_of_books[j])
        j+=1

find_year(inp_y)
