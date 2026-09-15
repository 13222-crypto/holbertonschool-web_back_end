# Python - Variable Annotations

This project covers type annotations in Python 3, using `mypy` for static type checking, duck typing, and function signature specifications.

## Resources
* [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
* [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Learning Objectives
By the end of this project, you should be able to explain:
- Type annotations in Python 3
- How to specify function signatures and variable types using type annotations
- Duck typing concepts
- How to validate code using `mypy`

## Requirements
- Ubuntu 20.04 LTS with Python 3.9
- Code style: `pycodestyle` (version 2.5.x)
- All files must be executable (`chmod +x`)
- The first line of all files must be `#!/usr/bin/env python3`
- Full type annotations for all variables, parameters, and return values
- Documentation required for all modules, classes, and functions

## Tasks Summary

| File | Description |
| --- | --- |
| `0-add.py` | Type-annotated function `add` returning the sum of two floats. |
| `1-concat.py` | Type-annotated function `concat` returning concatenated strings. |
| `2-floor.py` | Type-annotated function `floor` returning the floor of a float. |
| `3-to_str.py` | Type-annotated function `to_str` returning string representation of a float. |
| `4-define_variables.py` | Type-annotated variable declarations with specified values. |
| `5-sum_list.py` | Type-annotated function `sum_list` returning sum of floats in a list. |
| `6-sum_mixed_list.py` | Type-annotated function `sum_mixed_list` summing integers and floats. |
| `7-to_kv.py` | Type-annotated function `to_kv` returning a tuple of string and squared number. |
| `8-make_multiplier.py` | Type-annotated function `make_multiplier` returning a multiplier function. |
| `9-element_length.py` | Duck typing an iterable to return a list of tuples with element lengths. |
| `100-safe_first_element.py` | Duck typing to safely return the first element of a sequence. |
| `101-safely_get_value.py` | Type annotations using `TypeVar` and `Mapping` for safe dictionary retrieval. |
| `102-type_checking.py` | Applying `mypy` type validation and correcting annotations in array zooming. |

## Author
* **Emmanuel Turlay** - Staff Software Engineer at Cruise
