class Limit:
    def __init__(self, a: float, b: float, path: list) -> None:
        self.a: float = a
        self.b: float = b
        self.path = path

def max_a(old: Limit, new: Limit) -> Limit:
    if (old.a < new.a):
        return new 
    elif old.a == new.a and old.b < new.b:
        return new
    else:
        return old

def max_b(old: Limit, new: Limit) -> Limit:
    if (old.b < new.b):
        return new 
    elif old.b == new.b and old.a < new.a:
        return new
    else:
        return old
