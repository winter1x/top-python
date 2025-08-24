async def hello():
    print("Привет из асинхронной функции!")

# Вызов функции
result = hello()
print(result)  # Выведет что-то вроде: <coroutine object hello at 0x...>