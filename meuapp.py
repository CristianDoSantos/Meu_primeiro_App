#titulo
print('=== ANALISADOR DE MEDIDAS PARA CAMINHÕES ===')
#Banco de cores

#dados que serão inseridos
comprimentoTotal = float(input('Comprimento total: '))
entreEixo = float(input('Entre eixos: '))
balancoTraseiro = float(input('Balanço traseiro: '))
comprimentoCarroceria = int(input('Comprimento da carroceria: '))
largura = int(input('Largura: '))
#calculos
balancoDianteiro = (comprimentoTotal - entreEixo) - balancoTraseiro
calculoLimite = entreEixo * 0.6
faixaLateral = comprimentoCarroceria * 0.33
faixaLateralNumero = round(faixaLateral / 300)
faixaTraseira = largura * 0.8
faixaTraseiraNumero = round(faixaTraseira / 300)
print('')
print('=' * 40)
print('O balaço dianteiro é de {:.0f}mm. '.format(balancoDianteiro))
print('')
limiteNorma = 3500
if balancoTraseiro > limiteNorma:
    print('REPROVADO por ultrapassar 3500mm!')
elif balancoTraseiro <= calculoLimite and balancoTraseiro <= limiteNorma:
    print('Balanço traseiro APROVADO! ')
    if calculoLimite <= limiteNorma:
        print('O limite do balanço traseiro é de {:.0f}mm. '.format(calculoLimite))
    else:
        print('O limite do balanço traseiro é de {:.0f}mm. '.format(limiteNorma))
else:
    print('Balanço traseiro REPROVADO por ser maior que {:.0f}mm'.format(calculoLimite))
print('')
print('=' * 40)
print('')
print('Quantidade de faixas na lateral é de {:.0f} faixas. '.format(faixaLateralNumero))
print('A quantidade de faixas na traseira é de {:.0f} faixas. '.format(faixaTraseiraNumero))
print('')
print('============Espero que tenha ajudado!===============')
print('')
fechar = str(input('Para fechar aperte ENTER '))
print(fechar)
