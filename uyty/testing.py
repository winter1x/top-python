def get_by_index(elements, index, default):
    return elements[index] if index < len(elements) else default


get_by_index(['zero', 'one'], 2, 'value')

print('ok')