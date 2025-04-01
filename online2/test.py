"""
next iter yield StopIteration send

умный счетчик
с 0
inc + 1
dec - 1
reset в 0
stop
"""

def smart_counter():
    count = 0
    while True:
        command = yield count
        if command == "inc":
            count += 1
        elif command == "dec":
            count -= 1
        elif command == "reset":
            count = 0
        elif command == "stop":
            raise StopIteration("остановлен")

counter = smart_counter()
next(counter)




try:
    print(next(counter))
    print(counter.send("inc"))
    counter.send("stop")
except StopIteration as e:
    print(e)