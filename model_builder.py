import zython as mz


class ModelBuilder(mz.Model):
    def __init__(self):
        self.constraints = []
        self.deps_inds = {'root': 0}
        self.v = None

    def read_file(self, f_name):
        records = dict()
        deps_raw_list = set()
        with open(f_name, 'rt') as file:
            for line in file:
                name, vers, *deps = line.split()
                vers = vers[:-1]
                record = dict(zip(deps[::2], deps[1::2]))
                record['vers'] = vers
                deps_raw_list |= set(record.keys())
                records[name] = record

        self.v = mz.Array(mz.var(range(0, 9)), shape=(len(deps_raw_list) + 1, 3))

        for i in range(1, len(deps_raw_list) + 1):
            nm = deps_raw_list.pop()
            if nm != 'vers':
                self.deps_inds[nm] = i

        for rd in records.keys():
            version = records[rd].pop('vers')
            self.add_constraint(rd, version, records[rd])

    def add_constraint(self, name, vers, dependency: dict):
        main_ind = self.deps_inds[name]
        a, b, c = map(int, vers.split('.'))
        if name == 'root':
            self.constraints += [
                self.v[0, 0] == a,
                self.v[0, 1] == b,
                self.v[0, 2] == c
            ]

        for dp in dependency.keys():
            ind = self.deps_inds[dp]
            value = dependency[dp]
            r = value.find('.') - 1
            op = value[:r]
            x, y, z = map(int, value[r:].split('.'))

            if op == '^':
                expression = ((self.v[ind, 0] == x) & (self.v[ind, 1] * 10 + self.v[ind, 2] >= y * 10 + z))
            elif op == "~":
                expression = ((self.v[ind, 0] == x) & (self.v[ind, 1] == y) & (self.v[ind, 2] >= z))
            elif op == ">":
                expression = ((self.v[ind, 0] * 100 + self.v[ind, 1] * 10 + self.v[ind, 2]) > (x * 100 + y * 10 + z))
            elif op == ">=":
                expression = ((self.v[ind, 0] * 100 + self.v[ind, 1] * 10 + self.v[ind, 2]) >= (x * 100 + y * 10 + z))
            elif op == "<":
                expression = ((self.v[ind, 0] * 100 + self.v[ind, 1] * 10 + self.v[ind, 2]) < (x * 100 + y * 10 + z))
            elif op == "<=":
                expression = ((self.v[ind, 0] * 100 + self.v[ind, 1] * 10 + self.v[ind, 2]) <= (x * 100 + y * 10 + z))
            else:
                expression = ((self.v[ind, 0] == x) & (self.v[ind, 1] == y) & (self.v[ind, 2] == z))

            self.constraints += [
                ~((self.v[main_ind, 0] == a) & (self.v[main_ind, 1] == b) & (self.v[main_ind, 2] == c))
                | expression
            ]

    def solution(self):
        result = self.solve_satisfy()['v']
        message = ''
        for name, ind in self.deps_inds.items():
            version = '.'.join(map(str, result[ind]))
            if version == '0.0.0':
                version = 'any'
            message += f'{name}: {version}\n'
        return message
