from collections import deque #Importar libreria deque que permie rabajar con grafos

def bfs(grafo, inicio): #Implementar algorimo de busqueda en anchura
    visitado = set()  #Variable para guardar los nodos visitados
    cola = deque([inicio]) #Cola para manejar los nodos por visitar que incia con el noodo de inicio

    while cola:
        node = cola.popleft() #Se extrae el primer nodo de la cola
        if node not in visitado: #Si no se ha visitado el nodo
            print(node, end= " ") #Se muestra en la pantalla
            visitado.add(node) #Se agrega a los nodos visitados

            #Se agregan los nodos adyacentes a este a la cola si es que no se han visitado
            cola.extend(grafo[node]-visitado) 


# Ejemplo de uso
grafo = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

print("Busqueda en Anchura (BFS):")
bfs(grafo, 'A')
