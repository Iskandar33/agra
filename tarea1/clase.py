
###TAREA: 
# REVERTIR EL CODIGO PARA QUE SE ORDENE BUSCANDO AL DATO MÁS GRANDE
def osort(arreglo, n):
    if (n != len(arreglo)):
        idxmin = n
        for i in range(n + 1):
            if(arreglo[i] < arreglo[idxmin]):
                idxmin = i
        arreglo[idxmin], arreglo[n] = arreglo[n], arreglo[idxmin]
        osort(arreglo, n + 1)