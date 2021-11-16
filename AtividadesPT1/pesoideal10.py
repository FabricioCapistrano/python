a= float(input('Digite sua altura:'))
b= str(input('Digite seu sexo(h para homens e m para mulher):'))

if b == 'h' :
    print('O peso ideal para sua altura é:', (72.7 * a) - 58)
else:
    print('O peso ideal para sua altura é: ', (62.1 * a) - 44.7)
