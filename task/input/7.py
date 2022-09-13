n = 0
h = 0
while n!=2:
    a = int(input('Введите количество часов '))
    b = int(input('Введите количество минут '))
    c = int(input('Введите количество секунд '))
    h = a*3600 + b *60 + c - h
    n=n+1
    if n==1:
        print('Вторая метка')
if h<0:
    h=-h
print(h)

