# Types in Python
{id: types}

## mypy
{id: mypy}
{i: mypy}

* [mypy](http://mypy-lang.org/)
* [Type Checking](https://realpython.com/python-type-checking/)
* [type hints](https://docs.python.org/library/typing.html)

```
pip install mypy
```

## Types of variables
{id: types-of-variables}

![](examples/types/variables.py)

`python variables.py`

![](examples/types/variables.out)

`mypy variables.py`

![](examples/types/variables.mypy)

## Types of function parameters
{id: types-of-function-parameters}

![](examples/types/function.py)
![](examples/types/function.out)
![](examples/types/function.mypy)


## Types function returns None or bool
{id: mypy-to-check-function-returns}

{aside}
-> bool means the function returns a boolean. Either True or False.

-> None means the function returns None. Explicitely, or implicitely.
{/aside}

![](examples/types/function_bool.py)
![](examples/types/function_bool.out)

## Types used properly
{id: types-used-properly}


![](examples/types/good.py)
![](examples/types/good.out)
![](examples/types/good.mypy)

## TODO: mypy
{id: mypy-todo}

* Complex data structures?
* My types/classes?
* Allow None (or not) for a variable.
