def hash_function(value, table_size):
    return value % table_size

# Lista de valores
values = [120, 123, 145, 90, 39, 45, 23, 220]

# Tamanho da tabela hash
table_size = 10

# Valor para calcular o índice
value_to_find = 145

# Cálculo do índice
index = hash_function(value_to_find, table_size)

print(f"O índice para o valor {value_to_find} na tabela hash é: {index}")
