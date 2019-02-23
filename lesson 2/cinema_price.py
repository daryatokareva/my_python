print("При покупке билетов за день до сеанса: скидка 5%\nПри покупке более 20 билетов: скидка 20%")
film=str(input("Выберите фильм: Пятница, Чемпионы, Пернатая банда "))
if film=="Пятница":
    date=str(input("Сегодня или завтра пойдете в кино? "))
    if date=="сегодня":
        print("Сеансы: 12:00\n16:00\n20:00")
        seans=int(input("Выберите сеанс: "))
        if seans==12:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",250*0.8*pers)
            else:
                print("Общая стоимость: ",250*pers)
        if seans==16:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",350*0.8*pers)
            else:
                print("Общая стоимость: ",350*pers)
        if seans==20:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",450*0.8*pers)
            else:
                print("Общая стоимость: ",450*pers)
    if date=="завтра":
        print("Сеансы: 12:00\n16:00\n20:00")
        seans=int(input("Выберите сеанс: "))
        if seans==12:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",250*0.8*0.95*pers)
            else:
                print("Общая стоимость: ",250*0.95*pers)
        if seans==16:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",350*0.8*0.95*pers)
            else:
                print("Общая стоимость: ",350*0.95*pers)
        if seans==20:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",450*0.8*0.95*pers)
            else:
                print("Общая стоимость: ",450*0.95*pers)
if film=="Чемпионы":
    date=str(input("Сегодня или завтра пойдете в кино? "))
    if date=="сегодня":
        print("Сеансы: 10:00\n13:00\n16:00")
        seans=int(input("Выберите сеанс: "))
        if seans==10:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",250*0.8*pers)
            else:
                print("Общая стоимость: ",250*pers)
        if seans==13:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",350*0.8*pers)
            else:
                print("Общая стоимость: ",350*pers)
        if seans==16:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",350*0.8*pers)
            else:
                print("Общая стоимость: ",350*pers)
    if date=="завтра":
        print("Сеансы: 10:00\n13:00\n16:00")
        seans=int(input("Выберите сеанс: "))
        if seans==10:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",250*0.8*0.95*pers)
            else:
                print("Общая стоимость: ",250*0.95*pers)
        if seans==13:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",350*0.8*0.95*pers)
            else:
                print("Общая стоимость: ",350*0.95*pers)
        if seans==16:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",350*0.8*0.95*pers)
            else:
                print("Общая стоимость: ",350*0.95*pers)
if film=="Пернатая банда":
    date=str(input("Сегодня или завтра пойдете в кино? "))
    if date=="сегодня":
        print("Сеансы: 10:00\n14:00\n18:00")
        seans=int(input("Выберите сеанс: "))
        if seans==10:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",350*0.8*pers)
            else:
                print("Общая стоимость: ",350*pers)
        if seans==14:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",450*0.8*pers)
            else:
                print("Общая стоимость: ",450*pers)
        if seans==18:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",450*0.8*pers)
            else:
                print("Общая стоимость: ",450*pers)
    if date=="завтра":
        print("Сеансы: 10:00\n14:00\n18:00")
        seans=int(input("Выберите сеанс: "))
        if seans==10:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",450*0.8*0.95*pers)
            else:
                print("Общая стоимость: ",450*0.95*pers)
        if seans==14:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",450*0.8*0.95*pers)
            else:
                print("Общая стоимость: ",450*0.95*pers)
        if seans==18:
            pers=int(input("Сколько билетов? "))
            if pers>=20:
                print("Общая стоимость: ",450*0.8*0.95*pers)
            else:
                print("Общая стоимость: ",450*0.95*pers)


