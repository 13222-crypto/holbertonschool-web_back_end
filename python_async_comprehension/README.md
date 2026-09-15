# Python - Async Comprehension

This project covers asynchronous generators and comprehensions in Python 3 using `asyncio`.

## Resources
* [PEP 530 -- Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
* [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#pep-530-asynchronous-comprehensions)
* [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)

## Learning Objectives
By the end of this project, you should be able to explain:
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements
- Ubuntu 20.04 LTS with Python 3.8
- Code style: `pycodestyle` (version 2.5.x)
- All files must be executable (`chmod +x`)
- First line of all files must be `#!/usr/bin/env python3`
- Full type annotations for all functions and coroutines

## Tasks Summary

| File | Description |
| --- | --- |
| `0-async_generator.py` | Asynchronous generator yielding random floats. |
| `1-async_comprehension.py` | Async comprehension collecting values from the generator. |
| `2-measure_runtime.py` | Parallel execution measurement using `asyncio.gather`. |

## Author
* **Emmanuel Turlay** - Staff Software Engineer at Cruise
