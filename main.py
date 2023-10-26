from calculadora import soma

# print(soma(10,20))
# print(soma(-110,50))
# print(soma(-110.5,20.5))

# try:
#     print(soma('10',20))
# except TypeError as e:
#     print('\nTypeError - Erro de tipo de dado')
#     print(e, '\n')

try:
    print(soma('10',20))
except AssertionError as e:
    print(f'conta invalida: {e}')
    
    # desfazer assertion -O no terminal antes de rodar o programa