class Worker:
    def work(self):
        print("Человек работает")


class RobotWorker:
    def work(self):
        print("Робот работает")


class WorkerService:
    def __init__(self, worker: Worker):
        self.worker = worker

    def manage(self):
        self.worker.work()