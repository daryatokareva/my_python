s=int(input("Введите число:"))
def parity(s):
    if s%2==0:
        return "Число {0} четное".format(s)
    elif s%2!=0:
        return "Число {0} нечетное".format(s)
print(parity(s))  
