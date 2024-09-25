import zython as mz


class ModelBuilder(mz.Model):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def constraint(self):
        self.constraints = [self.a * self.x ** 2 + self.b * self.x + self.c == 0]

print(ModelBuilder(1, 2, 3))

m = ModelBuilder(1, 4, 3)
m.__dict__['x'] = mz.var(range(-2, 10))
m.constraint()
result = m.solve_satisfy()
print(result.original['x'])