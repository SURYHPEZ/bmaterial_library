class Subject:
    def __init__(self):
        self.observers = set()

    def attach(self, observer):
        self.observers.add(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, **kwargs):
        for observer in self.observers:
            observer.update(self, **kwargs)
