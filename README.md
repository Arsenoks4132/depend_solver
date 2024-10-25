# О проекте

Консольное приложение, позволяющее при помощи SMT/SAT решателей разрешить задачу выборки версий пакетов для установки с учетом их зависимостей.

# 1. Клонирование репозитория

Склонируйте репозиторий с исходным кодом и тестами:

```bash
git clone <URL репозитория>
cd <директория проекта>
```

# 2. Виртуальное окружение

```shell
python -m venv venv
venv\Scripts\activate
```

# 3. Установка зависимостей

```shell
pip install -r requirements.txt
```

# 4. Установка компилятора

Необходимо скачать с официального сайта компилятор **minizinc** и добавить его в **PATH**

# 5. Запуск программы

```shell
py main.py
```

# 6. Конфигурация входных файлов

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
