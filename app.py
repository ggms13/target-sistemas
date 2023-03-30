# 1) Observe o trecho de código abaixo:

# int INDICE = 13, SOMA = 0, K = 0;
# enquanto K < INDICE faça
# {
# K = K + 1;
# SOMA = SOMA + K;
# }
# imprimir(SOMA);

# Ao final do processamento, qual será o valor da variável SOMA?

i = 13
soma = 0
k = 0

while k < i:
    k = k + 1
    soma = soma + k
print("Ao final do processamento, o valor da variável SOMA é:", soma)

####################################################################################

# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre 
# será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a 
# sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE:

# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def isFibonacci():
    num = int(input("Por favor, digite um número:"))
    a = 0
    b = 1

    while a < num:
        a, b = b, a + b

    if a == num:
            print("O número", num, "pertence a sequência fibonacci.")
    else:
        print("O número", num, "não pertence a sequência fibonacci.")

isFibonacci()

############################################################################

# 3) Descubra a lógica e complete o próximo elemento:

# a) 1, 3, 5, 7, ___9

# b) 2, 4, 8, 16, 32, 64, ____128

# c) 0, 1, 4, 9, 16, 25, 36, ____49

# d) 4, 16, 36, 64, ____100

# e) 1, 1, 2, 3, 5, 8, ____13

# f) 2,10, 12, 16, 17, 18, 19, ____200

###########################################################

# 4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. 
# O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h 
# e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. 
# Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?

dist_rp_franca = 100
vel_carro = 110
vel_caminhao = 80
tempo_caminhao = dist_rp_franca / (vel_carro + vel_caminhao)
tempo_caminhao_pedagios = tempo_caminhao + 0.0833 + 0.0833  # 5 minutos em cada pedágio
distancia_cruzamento = vel_carro * tempo_caminhao
distancia_carro_rp = dist_rp_franca - distancia_cruzamento
distancia_caminhao_rp = distancia_cruzamento

# verificando qual veículo está mais próximo de Ribeirão Preto
if distancia_carro_rp < distancia_caminhao_rp:
    print("O carro está mais próximo de Ribeirão Preto.")
else:
    print("O caminhão está mais próximo de Ribeirão Preto.")

# IMPORTANTE:

# a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.

# b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar 
# em cada um deles e o carro possui tag de pedágio (Sem Parar)

# c) Explique como chegou no resultado.

# Sabemos que o carro viaja de Ribeirão Preto a Franca a uma velocidade constante de 110 km/h, o que significa que ele 
# percorre a distância de 100 km em aproximadamente 0,91 horas (100/110).
# Já o caminhão viaja de Franca a Ribeirão Preto a uma velocidade constante de 80 km/h. 
# Como perde 5 minutos em cada um dos 2 pedágios, a sua velocidade real é de (100/1,42) km/h, 
# o que significa que percorre a distância de 100 km em aproximadamente 1,25 horas (100/80 + 0,17).
# Sabendo o tempo que cada veículo leva para percorrer a distância entre as cidades, podemos calcular a distância que cada um percorre até o ponto de cruzamento. 
# O carro percorre uma distância de 100 km x 0,91 h = 91 km, enquanto o caminhão percorre uma distância de 100 km x 1,25 h = 125 km.
# Como os veículos se cruzam a uma distância de 60,9 km de Ribeirão Preto, 
# podemos subtrair essa distância da distância percorrida pelo carro (91 km - 60,9 km) 
# e da distância percorrida pelo caminhão (125 km - 60,9 km) para descobrir quem está mais próximo de Ribeirão Preto.
# Fazendo essas subtrações, chegamos à conclusão de que o carro percorreu uma distância de 30,1 km até o ponto de cruzamento, 
# enquanto o caminhão percorreu uma distância de 64,1 km. Isso significa que o carro está mais próximo de Ribeirão Preto do que o caminhão no momento do cruzamento.

#########################################################################################

# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:

# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

# b) Evite usar funções prontas, como, por exemplo, reverse;

string = input("Digite uma palavra: ")
lista_caracteres = list(string)
tamanho_lista = len(lista_caracteres)

for i in range(tamanho_lista//2):
    temp = lista_caracteres[i]
    lista_caracteres[i] = lista_caracteres[tamanho_lista-1-i]
    lista_caracteres[tamanho_lista-1-i] = temp

string_invertida = ''.join(lista_caracteres)

print(string_invertida)