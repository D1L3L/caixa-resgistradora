limpa = '\033[m'
vermelho = '\033[31m'
verde = '\033[32m'
roxo = '\033[35m'
azul = '\033[34m'
preco = total = maior = menorpreco = cont = 0
produto = ' '
barato = ''
while True:
    produto = str(input(f'{verde}Qual o nome do produto?').strip().title())
    preco = float(input(f'{verde}Digite o preço: '))
    total += preco
    cont += 1
    r = ' '
    if preco > 1000:
        maior += 1
    if cont == 1:
        menorpreco = preco
        barato = produto
    if cont > 1 and menorpreco > preco:
        menorpreco = preco
        barato = produto
    while r not in 'SN':
        r = input(f'Digite {limpa}[S]{verde} para adicionar mais produtos ou {vermelho}[N]{verde} para finalizar compra: ')[0].upper().strip()
    if r == 'N':
        break
print(f'{azul}-='*40)
print(f'''{verde}O valor final da compra é de {vermelho}R${total:.2f}{verde}, custando mais de {vermelho}R$1000.00{verde}
há {azul}{maior}{verde}, e o produto mais barato foi {azul}{barato}{verde}. ''')
