s="У Лукоморья 123 дуб зеленый 456"
print("Буква я находится на позиции ",s.find("я"))
print("Буква у встречается в строке",s.count("у"),"раз")
m=str(s.isalpha())
if m=="False":
    print(s.upper())
r=len(s)
if r>4:
    print(s.lower())
print(s.replace("У","О"))
