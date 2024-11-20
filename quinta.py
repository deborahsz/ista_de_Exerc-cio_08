def hash_function(key, table_size):
    return key % table_size

def insert_into_hash_table(keys, table_size):
    hash_table = [None] * table_size
    for key in keys:
        index = hash_function(key, table_size)
        print(f"Chave {key} é mapeada para o índice {index}")
        if hash_table[index] is None:
            hash_table[index] = key
        else:
            print(f"Colisão detectada! Índice {index} já ocupado por {hash_table[index]}")
    
    return hash_table

# Chaves fornecidas
keys = [2, 32, 43, 16, 77, 51, 1, 17, 42, 111]

# Tamanho da tabela hash
table_size = 17

# Inserir chaves na tabela hash
resultant_table = insert_into_hash_table(keys, table_size)

print("\nTabela hash final:")
for i, key in enumerate(resultant_table):
    print(f"Índice {i}: {key}")
