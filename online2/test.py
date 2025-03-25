def id_generator(prefix: str):
    counter = -1

    def generate(count=10):
        nonlocal counter
        if count < 1:
            raise ValueError("1")

        start = counter + 1
        counter += count
        ids = [f"{prefix}{i}" for i in range(start, start + count)]

        return "\n".join(ids) if count > 1 else ids[0]

    return generate



item_id = id_generator("ID")
user_id = id_generator("USER")


print(item_id())
print(user_id())