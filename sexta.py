def hash_function(key):
    return (2 * key + 5) % 11

def insert_into_hash_table(keys, table_size):
    hash_table = [None] * table_size
    for key in keys:
        index = hash_function(key)
        print(f"Chave {key} mapeada para o índice {index}")
        if hash_table[index] is None:
            hash_table[index] = key
        else:
            print(f"Colisão detectada! Índice {index} já ocupado por {hash_table[index]}")
    
    return hash_table

# Chaves fornecidas
keys = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]

# Tamanho da tabela hash
table_size = 11

# Inserir chaves na tabela hash
resultant_table = insert_into_hash_table(keys, table_size)

print("\nTabela hash final:")
for i, key in enumerate(resultant_table):
    print(f"Índice {i}: {key}")
