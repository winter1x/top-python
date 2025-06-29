"""
asyncio - асинхронный цикл событий

event loop цикл событий
    ищет задачи для выполнения
    запускает задачу до ближайшего await
    переключается на следующую задачу
    возвращается к приостановленной задаче, когда данные готовы

корутины coroutine
    async def
    await

create_task - создает задачу и регистрирует ее в цикле событий

gather - запускает задачи и ожидает их завершения
    return_exceptions=True - возвращает исключения

wait - ожидает завершения задач
    return_when=ALL_COMPLETED - все задачи завершены
    return_when=FIRST_COMPLETED - первая задача завершена
    return_when=FIRST_EXCEPTION - первая задача завершена с ошибкой

cancel - отменяет задачу
    asyncio.CancelledError

asyncio.shield - защита от отмены
"""
import asyncio
async def hello():
    print("hello")
    await asyncio.sleep(1)
    #await some_coroutine()
    print('пока')

"""coro = hello()
asyncio.run(hello())"""


async def func1():
    print("func1 start")
    await asyncio.sleep(1)
    print("func1 end")

async def func2():
    print("func2 start")
    await func1()
    print("func2 end")


async def bad_task():
    while True:
        pass


async def fetch_data():
    await asyncio.sleep(1)
    return "some data"

async def process():
    data = await fetch_data()
    print(data)

#asyncio.run(process())

async def add(a, b):
    return a + b

async def main():
    result = await add(1, 2)
    print(result)

#asyncio.run(main())

async def job(n):
    await asyncio.sleep(1)
    print(f"готово: {n}")

async def main():
    tasks = [asyncio.create_task(job(n)) for n in range(10)]
    await asyncio.gather(*tasks)

#asyncio.run(main())

async def risky():
    raise ValueError("ошибка")

async def main():
    try:
        await risky()
    except ValueError as e:
        print(e)

#asyncio.run(main())

async def say_hello():
    print("hello")
    await asyncio.sleep(1)
    raise Exception
    print("world")
    

async def main():
    task = asyncio.create_task(say_hello())
    print("корутина запущена")
    await task


#asyncio.run(main())

async def say(word, delay):
    await asyncio.sleep(delay)
    return word

async def main():
    results = await asyncio.gather(
        say("hello", 1),
        say("world", 2),
        say("asyncio", 3)
    )
    print(results)


#asyncio.run(main())

async def task(name, delay):
    await asyncio.sleep(delay)
    return f"{name} завершен"

async def main():
    tasks = [asyncio.create_task(task(f"задача {i}", i)) for i in range(5)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for d in done:
        print(d.result())

#asyncio.run(main())

async def do_work(n):
    await asyncio.sleep(n)
    return f"задача {n} завершена"

async def main():
    tasks = [asyncio.create_task(do_work(n)) for n in range(1, 4)]
    results = await asyncio.gather(*tasks)
    print(results)


#asyncio.run(main())

async def bad():
    raise ValueError("ошибка")

async def main():
    try:
        await asyncio.gather(hello(), say_hello(), return_exceptions=True)
    except ValueError as e:
        print(e)

#asyncio.run(main())

async def first():
    await asyncio.sleep(1)
    print("first")

async def second():
    await asyncio.sleep(3)
    print("second")

async def main():
    tasks = [asyncio.create_task(first()), asyncio.create_task(second())]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for task in pending:
        task.cancel()

    for task in done:
        print("завершена задача", task.result())


asyncio.run(main())
"""


ручное создание
loop = asyncio.get_event_loop()
asyncio.set_event_loop(loop)

loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()

asyncio.create_task(my_coroutine())


loop.call_later(3, print, "прошло 3 секунды")

task = asyncio.create_task(some_coroutine())
task.cancel()
"""

"""
список серверов - асинхронные функции. ждет случайное время
некоторые падают с ошибкой

запустить опрос всех серверов одновременно
собрать все успешные ответы
обработать ошибки
показать время выполения
"""