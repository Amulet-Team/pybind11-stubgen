from __future__ import annotations

import collections.abc
import typing

__all__: list[str] = [
    "Foo",
    "accept_annotated_callable",
    "accept_callable",
    "accept_frozenset",
    "accept_py_handle",
    "accept_py_object",
    "accept_set",
    "add",
    "default_custom_arg",
    "default_int_arg",
    "default_list_arg",
    "default_optional_arg",
    "func_w_anon_args",
    "func_w_named_pos_args",
    "generic",
    "mul",
    "nested_types",
    "pass_callback",
    "passthrough1",
    "passthrough2",
    "passthrough3",
    "pos_kw_only_mix",
    "pos_kw_only_variadic_mix",
]

class Foo:
    def __init__(self, arg0: typing.SupportsInt) -> None: ...

def accept_annotated_callable(
    arg0: collections.abc.Callable[[typing.SupportsInt, typing.SupportsInt], int],
) -> typing.Any: ...
def accept_callable(arg0: collections.abc.Callable) -> typing.Any: ...
def accept_frozenset(arg0: frozenset) -> None: ...
def accept_py_handle(arg0: typing.Any) -> str: ...
def accept_py_object(arg0: typing.Any) -> str: ...
def accept_set(arg0: set) -> None: ...
def add(arg0: typing.SupportsInt, arg1: typing.SupportsInt) -> int: ...
def default_custom_arg(foo: Foo = Foo(5)) -> None: ...
def default_int_arg(n: typing.SupportsInt = 5) -> None: ...
def default_list_arg(l: list = [1, 2, 6, 18]) -> None: ...
def default_optional_arg(n: typing.SupportsInt | None = None) -> None: ...
def func_w_anon_args(
    arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: typing.SupportsInt
) -> None: ...
def func_w_named_pos_args(
    x: typing.SupportsInt, y: typing.SupportsInt, z: typing.SupportsInt
) -> None: ...
def generic(*args, **kwargs) -> None: ...
@typing.overload
def mul(x: typing.SupportsInt, y: typing.SupportsInt) -> int:
    """
    Multiply x and y (int)
    """

@typing.overload
def mul(p: typing.SupportsFloat, q: typing.SupportsFloat) -> float:
    """
    Multiply p and q (double)
    """

def nested_types(arg0: collections.abc.Sequence[Foo] | Foo) -> list[Foo] | Foo: ...
def pass_callback(arg0: collections.abc.Callable[[Foo], Foo]) -> Foo: ...
def passthrough1[T](obj: T) -> T: ...
@typing.overload
def passthrough2() -> None: ...
@typing.overload
def passthrough2[T](obj: T) -> T: ...
@typing.overload
def passthrough3() -> tuple[None, None]: ...
@typing.overload
def passthrough3[T](obj: T) -> tuple[T, None]: ...
@typing.overload
def passthrough3[T1, T2](obj1: T1, obj2: T2) -> tuple[T1, T2]: ...
def pos_kw_only_mix(
    i: typing.SupportsInt, /, j: typing.SupportsInt, *, k: typing.SupportsInt
) -> tuple: ...
def pos_kw_only_variadic_mix(
    i: typing.SupportsInt,
    /,
    j: typing.SupportsInt,
    *args,
    k: typing.SupportsInt,
    **kwargs,
) -> tuple: ...
