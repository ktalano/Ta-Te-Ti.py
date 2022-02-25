from random import randint
import os
#Fabrizio Julian Catalano DNI: 42242909

# La función mostrar imprime en pantalla el tablero del tatetí
def mostrar(tab):
    for contador in range(0,9,3):
        print(tab[contador]," | ",tab[contador+1]," | ",tab[contador+2])
        
# Dado un tablero la función hayGanador determina si hay un ganador
# hayGanador : [String] -> Bool      
def hayGanador(tab):
    #Horizontal
    for contador in range(0,9,3):
        if(tab[contador] == tab[contador+1] == tab[contador+2] and tab[contador]!=' '):
            return True
    #Verticual
    for contador in range(0,3):
        if(tab[contador] == tab[contador+3] == tab[contador+6] and tab[contador]!=' '):
            return True
    #Diagonales
    if (tab[0] == tab[4] == tab[8] and tab[0]!=' '): 
        return True
    elif (tab[2] == tab[4] == tab[6] and tab[2]!=' '):
        return True
    else:
        return False

# Una posición en el tablero va ser representada por un par de enteros
# del 1 al 3. Es decir que el tablero es visto como una matriz de 3x3
# Dado un tablero y una posición en el mismo la función libre
# determina si un casillero está libre        
def libre(tab, fila, col):
    return (tab[(fila-1)*3 + col -1]==' ')

def jugar():
    # Inicializar variables
    tab = [' ']*9
    simbolos =['O','X']
    cond=1 #Condicion Verdadera para iniciar bucle
    player=randint(0,1)#Jugador decidido aleatoriamente
    
    while cond<=9 : # cond=Cantidad de lugares vacios
        print("Jugador ",simbolos[player])
        # Pedir posición al jugador que tenga el turno
        mostrar(tab)
        print("fila:")
        fila = int(input())
        while fila>3:
            print("0 <= fila <= 3")
            fila=int(input())
        print("columna:")
        col  = int(input())
        while col>3:
            print("0 <= columna <= 3")
            col=int(input())        
        # Si la posición no está ocupada
        if libre(tab, fila, col):
            # actualizar tablero y mostrarlo
            if fila==1:
                tab[-1+col]=simbolos[player]
            if fila==2:
                tab[2+col]=simbolos[player]
            if fila==3:
                tab[5+col]=simbolos[player]
            mostrar(tab)
            # Chequear que el jugador no haya ganado
            if(hayGanador(tab)==True):
                print("Ganó el jugador ",simbolos[player])
                return 0
            # Actualizar variables para seguir jugando
            player=1-player
            cond+=1
        else:
            print ('El casillero está ocupado elija otro.')
    print("No quedan mas movimientos")
jugar()