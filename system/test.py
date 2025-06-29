import asyncio


async def task(name, delay):
    await asyncio.sleep(delay)
    return f"{name} завершен"

async def main():
    tasks = [asyncio.create_task(task(f"задача {i}", i)) for i in range(5)]
    done, pending = await asyncio.wait(tasks)

    for d in done:
        print(d.result())

asyncio.run(main())