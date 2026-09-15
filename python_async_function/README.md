# Python - Async

This project is part of the Web Back-End curriculum. It covers asynchronous programming concepts in Python 3 using `asyncio`.

## Resources
* [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
* [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
* [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Learning Objectives
By the end of this project, you should be able to explain:
- `async` and `await` syntax
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create `asyncio` tasks
- How to use the `random` module

## Requirements
- Ubuntu 20.04 LTS with Python 3.8
- Code formatted according to `pycodestyle` (version 2.5.x)
- All files must be executable (`chmod +x`)
- All files must start with `#!/usr/bin/env python3`
- All functions, coroutines, and modules must have proper documentation and type annotations

## Tasks Summary

| File | Description |
| --- | --- |
| `0-basic_async_syntax.py` | Asynchronous coroutine `wait_random` that waits for a random delay. |
| `1-concurrent_coroutines.py` | Executing multiple coroutines concurrently using `wait_n`. |
| `2-measure_runtime.py` | Measuring average execution time for `wait_n`. |
| `3-tasks.py` | Returning an `asyncio.Task` from a regular function. |
| `4-tasks.py` | Altering `wait_n` to use `task_wait_random`. |

## Author
* **Emmanuel Turlay** - Staff Software Engineer at Cruise
