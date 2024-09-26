from model_builder import ModelBuilder

if __name__ == '__main__':
    a = ModelBuilder()
    a.read_file('dependencies.txt')

    print(a.solution())