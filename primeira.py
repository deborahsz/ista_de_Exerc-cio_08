def hash_function(value, table_size):
    return value % table_size

def check_collisions(values, table_size):
    table = [None] * table_size
    collisions = []

    for value in values:
        index = hash_function(value, table_size)
        if table[index] is None:
            table[index] = value
        else:
            collisions.append((value, index))
    
    return collisions

# Valores fornecidos
values = [120, 123, 145, 90, 39, 45, 23, 220]
table_size = 10  # Defina o tamanho da tabela hash

collisions = check_collisions(values, table_size)

if collisions:
    print("Colisões detectadas:")
    for value, index in collisions:
        print(f"Valor {value} colidiu no índice {index}")
else:
    print("Nenhuma colisão detectada.")
