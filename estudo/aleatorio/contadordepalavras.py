
# fobj = open('tabacaria1', 'r')
# for line in fobj:
#     print(line.rstrip())
# fobj.close()

# fobj = open('tabacaria1', 'r')
# fobj.write('Uma cobra verde escreveu aqui e \n NotreDame pegou fogo!')

# with open('tabacaria1', 'w') as cobra_verde:
#     cobra_verde.write('A cobra entrou no arquivo novamente... \n e escreveu \n ' \
#         'mais duas groselhas \n' \
#         'bem escritas!')

# with open('tabacaria2', 'r') as nova_tabacaria:
#     for line in nova_tabacaria:
#         print(line.rstrip())


tabacaria_entrada = open('tabacaria2')
tabacaria_saida = open('tabacaria_editada2.txt', 'w')

i= 0
for line in tabacaria_entrada:
    # print(line.rstrip())
    tabacaria_saida.write(str(i) + ': ' + line)
    i = i + 1


tabacaria_saida.close()
tabacaria_entrada.close()

