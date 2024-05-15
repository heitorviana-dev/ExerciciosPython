from collections import deque

fila = deque(['A', 'B', 'C'])
print(fila)

# Inserindo o elemento D
fila.append('D')
print(fila)

# Removendo o elemento A
elementoRemovido = fila.popleft()
print(fila, elementoRemovido)



