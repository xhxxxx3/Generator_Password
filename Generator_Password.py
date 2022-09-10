from random import randint as r

simv = ('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM*')

n = int(input('Введите количество символов в пароле: '))
password = ''

for i in range(n):
    password = f'{password}{simv[r(0, len(simv)-1)]}'
input(password)
