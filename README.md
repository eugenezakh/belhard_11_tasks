# Занятие 11. Работа с NoSQL. MongoDB

## DB

1. Создать пакет db.
2. Сделать модуль:

        client.py

   В файле описать клиента к MongoDB. Host и port должны быть прочитаны из файла конфигурации, который должен находиться
   в корне проекта
   (выбрать по своему усмотрению: .ini, .toml, .yaml. Файл конфигурации с вашими данными не должен быть в репозитории)

3. Сделать файл и описать в нем инструкции импорта пакета:

        __init__.py

## UTILS

1. Создать пакет utils.
2. Создать модуль:

        func_bench.py

   В данном модуле описать декоратор, который будет вычислять время старта, время окончания и время затрачиваемое на
   выполнение функции. Сделать запись результата в MongoDB (БД benchmarks, коллекция functions_benchmark) в следующем
   виде:

        {
            "module": <module_name>,
            "function": <function_name>,
            "args": tuple,
            "kwargs": dict,
            "start_time": str,
            "end_time": str,
            "duration": str
        }

   Получить название модуля:

    ```python
    import inspect
    
    
    def get_module_name(function):
        return inspect.getmodule(function)
    ```

3. Создать модуль:

        class_bench.py

   В данном модуле описать декоратор класса, который будет применять декоратор из п.2 ко всем публичным функциям класса.
   К выводу из п.2 добавить (в MongoDB писать в коллекцию class_functions_benchmark):

        {
            "class_name": <class_name>
        }

4. Сделать файл и описать в нем инструкции импорта пакета:

        __init__.py

## VIEW

1. Создать пакет view.
2. Создать модуль:

        my_function.py

    В данном модуле описать функцию, которая ждет 1 секунду

    Для ожидания воспользоваться:

    ```python
    import time
    
    time.sleep(1)
    ```

3. Создать модуль:

        my_class.py

   В данном классе описать одну функцию, которая будет ждать 2 секунды, и другую функцию, которая будет ждать 3 секунды.

4. Сделать файл и описать в нем инструкции импорта пакета:

        __init__.py

## ENTRYPOINT

1. Создать в корне проекта модуль, который будет демонстрировать функционал:

        run.py
