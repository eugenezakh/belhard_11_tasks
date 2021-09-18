import inspect
import time

from db import client


def get_module_name(func):
    return inspect.getmodule(func)


def function_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        benchmarks = client.benchmarks
        function_benchmark = benchmarks.function_benchmark
        function_benchmark_data = {
                                "module": get_module_name(func).__name__,
                                "function": func.__name__,
                                "args": args,
                                "kwargs": kwargs,
                                "start_time": start_time,
                                "end_time": end_time,
                                "duration": end_time - start_time}
        function_benchmark.insert_one(function_benchmark_data)
    return wrapper
