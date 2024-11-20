def hash_function(value, table_size):
    return value % table_size

def insert_to_hash_table(values, table_size):
    hash_table = [None] * table_size  # Inicializar a tabela hash
    for value in values:
        index = hash_function(value, table_size)
        print(f"Valor {value} é mapeado para o índice {index}")
        if hash_table[index] is None:
            hash_table[index] = value
        else:
            print(f"Colisão detectada! Índice {index} já ocupado por {hash_table[index]}")
    
    return hash_table

# Valores fornecidos
values = [2341, 4234, 2839, 430, 22, 397, 3920]

# Tamanho da tabela hash
table_size = 7

# Inserir valores na tabela hash
resultant_table = insert_to_hash_table(values, table_size)

print("\nTabela hash final:")
for i, value in enumerate(resultant_table):
    print(f"Índice {i}: {value}")
