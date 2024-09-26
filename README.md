# Запуск

Для запуска необходимо запустить файл **main.py**


# Входные данные

Входные данные записываются в текстовый файл **dependencies.txt** в следующем формате:

```
root <root version>: <dependency name 1> <dependency version 1> ... <dependency name n> <dependency version n>
<package name> <package version>: <dependency name 1> <dependency version 1> ... <dependency name n> <dependency version n>
...
```

### Пример входных данных:

```
root 1.0.0: foo ^1.0.0 target ^2.0.0
foo 1.1.0: left ^1.0.0 right ^1.0.0
left 1.0.0: shared >=1.0.0
right 1.0.0: shared <2.0.0
shared 1.0.0: target ^1.0.0
```

### Вывод для данных из примера:

```
root: 1.0.0
target: 2.0.0
right: any
left: any
foo: 1.0.0
shared: any
```
