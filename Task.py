"""
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
Информация о человеке:
    Фамилия, Имя, Телефон, Описание
Корректность и уникальность данных не обязательны.
Функционал программы
1) телефонный справочник хранится в памяти в процессе выполнения кода
2) CRUD: Create, Read, Update, Delete
3) Search по полю фамилия
3) экспорт данных в текстовый файл
4) импорт данных из текстового файла

Используйте функции для реализации значимых действий в программе
Сделать "автотесты" для функций
Разделить на model-view-controller


[*] В домашнем задании необходимо будет реализовать функции Update, Delete

"""


# import controller

# if __name__ == "__main__":
#     controller.menu()





# def new_rec(mode="new")->tuple:
#     if mode=="new":
#         print("Режим ввода новой записи")
#     elif mode=="update":
#         print("Ввод новых данных для записи {surname}")
#         print("Пустая строка означает оставить данные без изменений")
#     else:
#         raise ValueError("Недопустимый файл: {mode}")
#     surname=input("Введите фамилию: ")
#     name=input("Введите имя: ")
#     tel=input("Введите номер телефона: ")
#     desc=input("Введите описание: ")
    
#     return surname, name, tel, desc

# def file_name()->str:
#     return input("Введите имя файла: ")

# def surname():
#     return input("Введите фамилию: ")

# def show_recs(recs:list):
#     for rec in recs:
#         show_recs(rec)
        
# def show_rec(rec:dict):
#     for val in rec.values():
#         print(val,end=" ")
#         print(" ")  
        
# def show_all_recs(phone_book:list):
#  print("Записи в справочнике: ")
#  for rec in phone_book:
#      show_rec(rec)
     
# def show_menu()->str:
#     print("\t(c)reat - Ввод новой записи: ")
#     print("\t(r)ead - Поиск записи по фамилии: ")
#     print("\t(u)date - Изменение записи по фамилии: ")
#     print("\t(i)mport - импорт из файла: ")
#     print("\t(e)xport - Экспорт в файл: ")
#     print("\t(d)elete - Удаление записи по фамилии: ")
#     print("\t(s)how - Вывод на экран содержимого справочника")
    
#     return input("Выберите нужный пункт")
                      
"""        
import view
import model


def menu():
    phone_book_main = []
    while True:
        choice = view.show_menu()
        if choice == "":
            print("до новых встреч")
            break
        elif choice == "c":
            rec = model.create_rec(*view.new_rec(mode = "new"))
            phone_book_main.append(rec)
        elif choice == "r":
            surname = view.surname()
            recs = model.select(phone_book_main, surname)
            view.show_recs(recs)
        elif choice == "u":
            surname = view.surname()
            recs = model.select(phone_book_main, surname)
            if recs:
                idx = phone_book_main.index(recs[0])
                rec = model.create_rec(*view.new_rec(mode = "update"))
                rec = model.merge(rec, recs[0])
                phone_book_main[idx] = rec
        elif choice == "d":
            surname = view.surname()
            recs = model.select(phone_book_main, surname)
            if recs:
                idx = phone_book_main.index(recs[0])
                phone_book_main.pop(idx)
        elif choice == "i":
            filename = view.file_name()
            recs = model.import_file(filename)
            phone_book_main.extend(recs)
        elif choice == "e":
            filename = view.file_name()
            model.export_file(filename, phone_book_main)
        elif choice == "s":
            view.show_all_recs(phone_book_main)
        else:
            print("Недопустимый пункт меню")
   
"""        
        
         