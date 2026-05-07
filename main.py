class Quackable:
    def quack(self):
        pass

class Duck(Quackable):
    def quack(self):
        print("Quack!")

class Turkey(Quackable):
    def quack(self):
        print("Gobble!")

def make_quackable(quackable):
    if isinstance(quackable, Quackable):
        return quackable
    else:
        raise TypeError("Quackable emas")

duck = Duck()
turkey = Turkey()

quackable_duck = make_quackable(duck)
quackable_turkey = make_quackable(turkey)

quackable_duck.quack()  # Quack!
quackable_turkey.quack()  # Gobble!
