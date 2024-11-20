def hash_function(char, table_size):
    return ord(char) % table_size

def check_collisions(characters, table_size):
    table = [None] * table_size
    collisions = []

    for char in characters:
        index = hash_function(char, table_size)
        if table[index] is None:
            table[index] = char
        else:
            collisions.append((char, index))
    
    return collisions

# Lista de caracteres
characters = ['U', 'N', 'I', 'E', 'S', 'P', 'F', 'A', 'C', 'U', 'L', 'D', 'A', 'D', 'E']

# Tamanho da tabela hash
table_size = 10

# Verificar colisões
collisions = check_collisions(characters, table_size)

if collisions:
    print("Colisões detectadas:")
    for char, index in collisions:
        print(f"Caractere '{char}' colidiu no índice {index}")
else:
    print("Nenhuma colisão detectada.")
