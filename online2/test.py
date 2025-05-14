class Bird:
    def fly(self):
        print("летит")

class Sparrow(Bird): # Sparrow - воробей
    pass

class Ostrich(Bird): # Ostrich - страус
    pass


birds = [Sparrow(), Ostrich()]
for bird in birds:
    bird.fly()

"""
что будет, если у класса Bird вызвать метод fly(), а потмо подставить туда Ostrich()?
Как повлияет добавление новых типов птиц на текущую реализацию?
почему страус не должен наследоваться от класса Bird, если Bird требует умения летать?
как избежать подобных нарушений в будущем?

"""