from typing import final


print ("--------- \U0001f680 \U0001f680 \U0001f680 \U0001f680 \U0001f680 \U0001f680 \U0001f680 \U0001f680 ---------------- ") 
print("hello World!")
print("=D")

a = 1
print("O valor de a eh: ")
print(a)

b = 3
print(" O valor de b é: ")
print(b)

print("Se eu somo a+ b então: ")
soma = a + b 
print(soma)

print("Se eu subtrair a - b então: ")
subtração = a - b 
print(subtração)

print ("Se multiplicar a * b então: ")
multiplicação = a * b 
print (multiplicação)

print ("Se eu dividir a / b então: ")
divisão = a / b
print (divisão)
print ("--------- \U0001f680 \U0001f680 \U0001f680 \U0001f680 \U0001f680 \U0001f680 \U0001f680 \U0001f680 ----------------")

print ("--- Strings (textos como Variaveis) ---")
N = "Walisson"
print (N)
N_outro_jeito = 'walisson'
print (N_outro_jeito)
parte_final = ' do Constela Digital \U0001f680 \U0001f680'
final_com_tudo = N + parte_final
print(final_com_tudo)
final_com_tudo_com_e_caixa_alta = final_com_tudo.replace("a", "A")
print(final_com_tudo_com_e_caixa_alta)


print("--------------------------------------------------------")
print(" \U0001f680 ---------------- LISTAS ----------------- \U0001f680 ")
# LISTAS DE NUMEROS ...
minha_lista = [2, 1, 6, 3, 80, 12312266]
print("conteudo da minha lista: ")
primeiro_elemento = minha_lista[0]
print( primeiro_elemento )
print("segundo elemento da minha lita: ")
segundo_elemento = minha_lista[1]
print( segundo_elemento )
print("terceiro elemento da minha lita: ")
terceiro_elemento = minha_lista[2]
print( terceiro_elemento )
print("quarto_elemento da minha lita: ")
quarto_elemento = minha_lista[3]
print( quarto_elemento )
print("quinto elemento da minha lita: ")
quinto_elemento = minha_lista[4]
print( quinto_elemento )
print("sexto elemento da minha lita: ")
sexto_elemento = minha_lista[5]
print( sexto_elemento )

# LISTA DE PALAVRAS 
minha_lista_palavras = ['walisson', 'Constela', 'Digital', 'Sol']
print('conteudo da minha lista de palavras: ')
print(minha_lista_palavras)
terceiro_elemento_lista_palavras = minha_lista_palavras[2]
print('terceiro elemento da minha lista de palavras: ')
print(terceiro_elemento_lista_palavras)



print("--------------------------------------------------------")
print(" \U0001f680 ---------------- if e else ----------------- \U0001f680 ")
saldo_conta_bancaria = -1
print('wait..... your process is in progress')
if saldo_conta_bancaria > 0:
    print('Give the cash')
else:
        print("I'm Sorry but you don't have money, you nedd work more =) ") 

print(" \U0001f680 ---------------- CHECANDO BALCONISTAS  ----------------- \U0001f680 ")
minha_lista_de_presenca_de_balconista = ['presente', 'nao ta presente', 'presente' ]
if len (minha_lista_de_presenca_de_balconista) == 3:
    print('Estamos funcionando a todo vapor.')
else: 
    print('Esta faltando gente pra trabalhar.')

print(" \U0001f680 \U0001f680 ---------------- FOR LOOP ----------------- \U0001f680 \U0001f680 ")

for i in range(3):
    print(i)
    print('HELLO WORLD!')


print('printando elementos da minha lista de palavras:')
for elemento in minha_lista_palavras:
    print(elemento)

print('printando elementos da minha lista de palavras com modificacao: ')
for elemento in minha_lista_palavras: 
    elemento_modificado = " \U0001f680 " +  elemento + " \U0001f680 "
    print(elemento_modificado)

    print('Vamos saber quantas palavras na minha lista que tem mais de 3 letras: ')
    total_palavras_com_mais_3_letras = 0  
    for palavra in minha_lista_palavras:
        if len(palavra) > 3:
            total_palavras_com_mais_3_letras += 1
        else:
            print('elemento com 3 letras ou menos ')
print('quantidade de palavras que tem mais de 3 letras: ')
print('total_palavras_com_mais_de_3_letras')

print(" \U0001f680 \U0001f680 ---------------- FUNCOES  ----------------- \U0001f680 \U0001f680 ")
def imprimir_hello_world ():
    print("Hello world!")

imprimir_hello_world()

def checar_se_tem_grana(saldo_conta_bancaria):
     print('Tentando Sacar Dinheiro')
     if saldo_conta_bancaria >0:
         print('solta a grana')
     else:
         print('nao tem grana, nao da pra soltar dinheiro para voce!!!')
checar_se_tem_grana(-100)
checar_se_tem_grana(2000)
saldo_da_minha_conta = 4000 
checar_se_tem_grana(saldo_da_minha_conta)

def somar_todos_os_valores_da_minha_lista_de_numeros(minha_lista):
    valor_total = 0
    for valor in minha_lista:
        #valor_total += valor 
        valor_total = valor_total + valor
    return valor_total 

# minha_lista = [2, 1, 6, 80, 12312266]       
# RESULTADO = 12312358 
valor_total= somar_todos_os_valores_da_minha_lista_de_numeros(minha_lista)
print('Valor total (12312358):')
print('Valor total (esperamos2312358): ')
print(valor_total)

print("--------------------------------------------------------")
print(" \U0001f680 ---------------- Algoritimo de ordenacao bubble sort ----------------- \U0001f680 ")

def algoritmo_bubble_sort(minha_lista):
    # Python program for implementation of Bubble Sort
    n = len(minha_lista)
    # Traverse through all array elements
    for i in range(n-1):
    #range (n) also work but outer loop will

        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if minha_lista[j] > minha_lista[j + 1] :
                minha_lista[j], minha_lista[j + 1] = minha_lista[j + 1], minha_lista[j]
    return minha_lista


print('minha lista antes: ')
print(minha_lista)
print('minha lista depois: ')
minha_lista_depois = algoritmo_bubble_sort(minha_lista)
print(minha_lista_depois)

print("--------------------------------------------------------")
print(" \U0001f680 ---------------- LEITURA E ESCRITA DE ARQUIVOS ----------------- \U0001f680 ")

arquivo_para_ler = open('minha_movimentacao_bancaria.txt', 'r')
dados_do_arquivo = arquivo_para_ler.read()
lista_dados_dp_arquivo = dados_do_arquivo.split('\n')
saldo_total = 0
for valor in lista_dados_dp_arquivo:
    saldo_total += float(valor)
print('O SALDO TOTAL e (ESPERAMOS ANSIOSAMENTE QUE SEJA 733)')
print(saldo_total)
arquivo_para_guardar_o_saldo = open('meu_saldo_total.txt', 'w')
arquivo_para_guardar_o_saldo.write(str(saldo_total))
arquivo_para_guardar_o_saldo.close()


print("--------------------------------------------------------")
print(" \U0001f680 ---------------- COMO DEBUGAR ----------------- \U0001f680 ")
import pdb; pdb.set_trace()

        #CONCLUSAO DO DESAFIO PART 1
# 1-REPRODUZIR  ESSE TUTORIAL PASSO A PASSO E LINHA POR LINHA 
# 2 - CRIAR UM REPOSITORIO NO GITHUB E USANDO OS COMANDOS GIT VOCE VAI COLOCAR O CODIGO LA.

print("\U0001f680 MUITO BOM! \U0001f680")