s=int(input("Введите число:"))
def parity(s):
    if s%2==0:
        print("Число ",s," четное")
    elif s%2!=0:
        print("Число ",s," нечетное")
print(parity(s))  
