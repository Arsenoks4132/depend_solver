import zython as mz


class Model(mz.Model):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def constraint(self):
        self.constraints = [self.a * self.x ** 2 + self.b * self.x + self.c == 0]


m = Model(1, 4, 3)
m.x = mz.var(int)
m.constraint()
result = m.solve_satisfy()
print(result.original['x'])
