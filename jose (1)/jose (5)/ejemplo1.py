# If
""" x = 10
if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual a 5") """

# Switch
""" y = 2
if y == 1:
    print("y es 1")
elif y == 2:
    print("y es 2")
elif y == 3:
    print("y es 3")
else:
    print("y no es 1, 2, ni 3") """

# Diccionarios 
diccionario = {'a':1, 'b': 2, 'c': 3}
if 'b' in diccionario:
    print("La clave 'b' esta en el diccionario")
else:
    print("La clave 'b' no esta en el diccionario")

for clave, valor in diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")

keys = list(diccionario.keys())    
index = 0
while index < len(keys):
    key = keys[index]
    print(f"Clave: {key}, Valor: {diccionario[key]}")
    index += 1