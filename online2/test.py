#uuid

"""
замыкание

генерирует последовательные идентификаторы
возвращает следующий уникальный идентификатор
"""

"""
ID0
ID1
ID2
"""

"""
USER0
USER1
USER2
"""

def create_id_generator(prefix="ID"):
    current_id = 0

    def generate_id():
        nonlocal current_id
        id_value = f'{prefix}{current_id}'
        current_id += 1
        return id_value
    return generate_id

id_generator = create_id_generator()

print(id_generator())
print(id_generator())
print(id_generator())

custom_id_generator = create_id_generator('USER')
print(custom_id_generator())
print(custom_id_generator())
print(custom_id_generator())