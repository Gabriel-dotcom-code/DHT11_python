import serial                                   # Importando pyserial lib
import time
import matplotlib.pyplot as plt          # Importando lib matplotlib
from drawnow import *                     # Importando lib drawnow (allows dynamic plotting)

Temp = []       # Lista de valores de temperatura
Humd = []       # Lista de valores de umidade
Dist = []           # Lista de valores com a distancia

arduinoData = serial.Serial('com4', 115200)         # porta de comunicação com arduino e velocidade de comunicação
plt.ion()       # Indica que irá plotar dados simultâneos

cont=0

# Construir função para plotar gráficos
def plot_T_H():
    
    #Ferramentas visuais da Temperatura
    plt.subplot(2,1,1)                                                          # primeiro plot
    plt.ylim(20,90)                                                              # Limites de leitura
    plt.ylabel('Temperatura ºC')                                            # Nome do eixo
    plt.plot(Temp, 'ro-', linewidth=0.5, label='Temperatura')     # Cores e labels
    plt.legend(loc="upper left")                                            # Localização da legenda
    plt.grid()    # Mostrar grid

    #Ferramentas visuais da umidade
    plt2 = plt.twinx()                                      # Cria segundo eixo para colocar umidade
    plt.ylim(20,100)                                       # Limites de leitura
    plt2.set_ylabel('Umidade (%)')                  # Nome do eixo
    plt2.plot(Humd, 'g^-', label='Umidade')        # Cores e labels
    plt2.legend(loc="upper right")                   # Localização da legenda
    plt2.ticklabel_format(useOffset=False)      # Ferramenta para impedir que o maplotlib refaça escala do gráfico automaticamente (questão de legibilidade)
    plt.grid()    # Mostrar grid
    
    # Ferramentas visuais da distancia
    plt.subplot(2,1,2)                                                          # segundo plot
    plt.ylim(0, 40)                                                               # Limites de leitura
    plt.ylabel('Distância (cm)')                                             # Nome do eixo
    plt.plot(Dist, 'c:', linewidth=2, label='Distância')               # Cores e labels
    plt.legend(loc="upper right")                                         # Localização da legenda
    plt.grid()   # Mostrar grid

while True:       # loop que funciona enquanto arduino estiver ligado
    while (arduinoData.inWaiting()==0):   # enquanto não houver dados a serem lidos
        pass  # fazer absolutamente nada
    
    # se houver dados...
    arduinoString = arduinoData.readline().decode("utf-8")        # Em python3 é necessário usar o decode par evitar dados 'b', recomenda-se fazer o teste sem decode
                                                                                        # em decode é possível usar também "utf-8", ou apenas decode
    # Faz leitura do objeto já declarado
    
    #print (arduinoString)                                                       # Verificando como os dados estão sendo enviados
    
    vec_dados = arduinoString.split(',')                                   # Armazenando os dados em vec_dados, separando na vírgula mandada pelo arduíno
    
    #print(vec_dados[0])                                                        # Visualizando como estão sendo armazenados os dados do vetor, AINDA ESTÃO COMO STRINGS!
    #print(vec_dados[1])                                                        # Visualizando como estão sendo armazenados os dados do vetor, AINDA ESTÃO COMO STRINGS!
    #print(vec_dados[2])                                                        # Visualizando como estão sendo armazenados os dados do vetor, AINDA ESTÃO COMO STRINGS!

    T = float(vec_dados[0])                                                    # Convertendo as strings em valores numéricos
    H = float(vec_dados[1])                                                   # Convertendo as strings em valores numéricos
    D = float(vec_dados[2])                                                   # Convertendo as strings em valores numéricos

    #print(T)                                                                        # Visualizando os dados
    #print(H)                                                                       # Visualizando os dados
    #print(D)

    Temp.append(T)                                                           # Armazenando dados de temperatura em lista
    Humd.append(H)                                                          # Armazenando dados de umidade em lista
    Dist.append(D)                                                            # Armazenando dados de distancia em lista
    

    #print(Temp)                                                                 # Visualizando a lista de temperatura
    #print(Humd)                                                                # Visualizando a lista de umidade
    
    drawnow(plot_T_H)                                                       # Chama a função e constrói gráfico pela lib 'drawnow'

    ''' A função draw() poderia ser substituída por plt.pause(coloca_o_intervalo_de_t_desejado) '''
    plt.pause(0.000001)
    
    # É ilegível plotar absolutamente todos os pontos, por isso definimos um contador para plotar apenas os dados mais recentes
    cont+=1

    if (cont>60):           # Delimitamos armazenamento até 60 dados
        Temp.pop(0)      # Eliminamos dados mais 'antigos' de Temp
        Humd.pop(0)      # Eliminamos dados mais 'antigos' de Humd
        Dist.pop(0)        # Eliminamos dados mais 'antigos' de Dist
