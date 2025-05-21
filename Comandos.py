✅ LISTAS (list)
Las listas son mutables, ordenadas y permiten elementos duplicados.
📌 Métodos comunes:
lista.append(x)       # Agrega un elemento al final
lista.extend(iter)    # Agrega todos los elementos de un iterable
lista.insert(i, x)    # Inserta x en la posición i
lista.remove(x)       # Elimina el primer valor x
lista.pop([i])        # Elimina y retorna el elemento en la posición i (por defecto el último)
lista.clear()         # Elimina todos los elementos
lista.index(x)        # Retorna el índice del primer valor x
lista.count(x)        # Cuenta cuántas veces aparece x
lista.sort()          # Ordena la lista en orden ascendente
lista.reverse()       # Invierte el orden de los elementos
lista.copy()          # Retorna una copia superficial de la lista
📌 Funciones útiles:
len(lista)            # Longitud
max(lista)            # Valor máximo
min(lista)            # Valor mínimo
sum(lista)            # Suma total
sorted(lista)         # Retorna una nueva lista ordenada
✅ TUPLAS (tuple)
Las tuplas son inmutables, ordenadas y permiten duplicados.
📌 Métodos:
tupla.index(x)        # Retorna el índice de x
tupla.count(x)        # Cuenta cuántas veces aparece x
📌 Funciones útiles:
len(tupla)
max(tupla)
min(tupla)
sum(tupla)
sorted(tupla)         # Retorna una lista ordenada
✅ CONJUNTOS (set)
Los conjuntos son no ordenados, no permiten duplicados y son mutables.
📌 Métodos:
conjunto.add(x)             # Agrega un elemento
conjunto.update(iter)       # Agrega múltiples elementos
conjunto.remove(x)          # Elimina x (error si no existe)
conjunto.discard(x)         # Elimina x (no error si no existe)
conjunto.pop()              # Elimina un elemento aleatorio
conjunto.clear()            # Vacía el conjunto
conjunto.copy()             # Copia del conjunto
📌 Operaciones:
A.union(B)                  # Unión
A.intersection(B)           # Intersección
A.difference(B)             # Diferencia (A - B)
A.symmetric_difference(B)   # Diferencia simétrica
A.issubset(B)               # A es subconjunto de B
A.issuperset(B)             # A es superconjunto de B
A.isdisjoint(B)             # A y B no tienen elementos en común
✅ DICCIONARIOS (dict)
Los diccionarios son mutables, no ordenados hasta Python 3.6, y usan pares clave:valor.
📌 Métodos:
dic.get(clave)               # Retorna el valor de la clave (None si no existe)
dic.keys()                   # Retorna las claves
dic.values()                 # Retorna los valores
dic.items()                  # Retorna pares (clave, valor)
dic.update(otro_dic)         # Actualiza con otro diccionario
dic.pop(clave)               # Elimina y retorna el valor de la clave
dic.popitem()                # Elimina y retorna el último par agregado
dic.clear()                  # Elimina todos los elementos
dic.copy()                   # Retorna una copia
dic.setdefault(clave, valor)# Retorna valor si existe, sino lo crea con valor
📌 Acceso y asignación:
dic[clave] = valor           # Asigna valor a una clave
valor = dic[clave]           # Accede al valor (error si no existe)

Tipo         	Métodos clave
Lista        	append, pop, insert, remove, sort
Tupla        	index, count
Conjunto    	add, remove, union, intersection, pop
Diccionario	    get, keys, values, items, update
