#criando uma funcao calcular media
#operacao rotineira de calculo de media
"""
def calcular_media(nota1, nota2, nota3, nota4):
    nota1 = float(input('Informe a nota do primeiro bimestre: '))
    nota2 = float(input('Informe a nota do segundo bimestre: '))
    nota3 = float(input('Informe a nota do terceiro bimestre: '))
    nota4 = float(input('Informe a nota do quarto bimestre: '))
    media = (float(nota1) + float(nota2) + float(nota3) + float(nota4)) / 4
    return  print('A media das notas informadas é de: {} '.format(media))
        

#Chamando a funcao
#sem essa linha de comando o pythom nem executa o codigo acima.
calcular_media(1,2,3,4)
"""
meta = 1000
vendas = { 'Joao':1350, 'Julia':1600,
           'Pedro':900, 'Paulo':950,
           'Ana':1225, 'Carlos':990,
         }
def calcular_meta(meta,vendas):
    bateu_meta = []
    for vendedor in vendas:
        if vendas[vendedor] >= meta:
            bateu_meta.append(vendedor)
    perc_bateu_meta = len(bateu_meta)/len(vendas)
    return perc_bateu_meta,bateu_meta
p_meta,vendedores_acima_meta = max.vendas(meta,vendas)
print(p_meta)
print(vendedores_acima_meta)