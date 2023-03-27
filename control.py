import model

pb = model.PhoneBook('Lib.txt')


while True:
    print(pb.main_menu())
    choice = int(input("Выберите пункт меню:"))
    match choice:
        case 1:
            print(pb)
        case 2:
            name = input("Ведите имя:")
            phone = input("Ведите номер телефона:")
            comment = input("Ведите комментарий:")
            pb.new_contact(name, phone, comment)
        case 3:
            word = input("Ведите поисковый запросЖ")
            print(pb.serch(word))
        case 4:
            print(pb)
            index = int(input("Ведите номер контакта:"))
            name = input("Ведите имя или нажмите Enter для пропуска:")
            phone = input("Ведите номер телефона или нажмите Enter для пропуска:")
            comment = input("Ведите комментарий или нажмите Enter для пропуска:")
            pb.change(index-1, name, phone, comment)
        case 5:
            print(pb)
            index = int(input("Ведите номер контакта"))
            pb.delete((index-1))
        case 6:
            pb.save()
            break