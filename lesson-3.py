lst = [6, 9, 3, 8, 5, "python", "1234", "app"]
a = input("як увійти?(user/admin)")
if a == 'user':
    print(lst)
elif a == 'admin':
    b = input('введіть логін та пароль:').split()
    if b[0] == 'admin' and b[1] == '1234':
        print("hello admin")
    while True:
        c = input('виберіть дію(добавити/забрати/сортувати)')
        if c == "добавити":
            d = input("ведіть елемент:")
            n = input("виберіть тип елемента:")
            if n == "int":
                if int(d) in lst:
                    element = input("такий елемент вже присутній,добавити ще (Yes/No)?")
                    if element == "Yes":
                        lst.append(int(d))
                        print(lst)
                if int(d) not in lst:
                    lst.append(int(d))
            elif n == "str":
                if d in lst:
                    element = input("такий елемент вже присутній,добавити ще (Yes/No)?")
                    if element == "Yes":
                        lst.append(d)
                        print(lst)
                if d not in lst:
                    lst.append(d)
            h = input("завершити сенс(так/ввести заново)")
            if h == "ввести заново":
                continue
            if h == "так":
                print(lst)
                break
        while c == "забрати":
            j = int(input("виберіть індекс:"))
            if j >= len(lst) or j < 0:
                print("на цьому індексі немає елементу")
            else:
                lst.pop(j)
            h = input("завершити сенс(так/ввести заново)")
            if h == "ввести заново":
                continue
            if h == "так":
                print(lst)
                break
        while True:
         if c == "сортувати":
            lst_new = []
            lst_for_int = [i for i in lst if type(i) == int]
            lst_for_str = [i for i in lst if type(i) == str]
            lst_for_int.sort()
            lst_for_str.sort()
            lst_new.extend(lst_for_int)
            lst_new.extend(lst_for_str)
         h = input("завершити сенс(так)")
         if h == "так":
            print("test")
            print(lst_new)
         break