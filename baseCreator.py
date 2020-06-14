#Abre um arquivo já existente em modo de append
arqEnderecos = open('enderecos.txt', 'a')

texto = ('09560-650') #Texto a ser colocado

#for para colocar os dados
for linha in range(100001):
    arqEnderecos.write(texto + ';' + '\n')

print('Concluído')

arqEnderecos.close

