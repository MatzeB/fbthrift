#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import __static__


import typing as _typing

import enum

import folly.iobuf as _fbthrift_iobuf
import fbcode.thrift.python.types as _fbthrift_python_types
import fbcode.thrift.python.exceptions as _fbthrift_python_exceptions


class AnEnum(_fbthrift_python_types.Enum, enum.Enum):
    NOTSET: AnEnum = ...
    ONE: AnEnum = ...
    TWO: AnEnum = ...
    THREE: AnEnum = ...
    FOUR: AnEnum = ...
    def _to_python(self) -> AnEnum: ...
    def _to_py3(self) -> "module.types.AnEnum": ...  # type: ignore
    def _to_py_deprecated(self) -> int: ...


class AnEnumRenamed(_fbthrift_python_types.Enum, enum.Enum):
    name_: AnEnumRenamed = ...
    value_: AnEnumRenamed = ...
    renamed_: AnEnumRenamed = ...
    def _to_python(self) -> AnEnumRenamed: ...
    def _to_py3(self) -> "module.types.AnEnumRenamed": ...  # type: ignore
    def _to_py_deprecated(self) -> int: ...


class Flags(_fbthrift_python_types.Enum, enum.Flag):
    flag_A: Flags = ...
    flag_B: Flags = ...
    flag_C: Flags = ...
    flag_D: Flags = ...
    def _to_python(self) -> Flags: ...
    def _to_py3(self) -> "module.types.Flags": ...  # type: ignore
    def _to_py_deprecated(self) -> int: ...


class SimpleException(_fbthrift_python_exceptions.GeneratedError):
    err_code: _typing.Final[int] = ...
    def __init__(
        self, *,
        err_code: _typing.Optional[int]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int]]]: ...
    def _to_python(self) -> SimpleException: ...
    def _to_py3(self) -> "module.types.SimpleException": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.SimpleException": ...  # type: ignore


class OptionalRefStruct(_fbthrift_python_types.Struct):
    optional_blob: _typing.Final[_typing.Optional[_fbthrift_iobuf.IOBuf]] = ...
    def __init__(
        self, *,
        optional_blob: _typing.Optional[_fbthrift_iobuf.IOBuf]=...
    ) -> None: ...

    def __call__(
        self, *,
        optional_blob: _typing.Optional[_fbthrift_iobuf.IOBuf]=...
    ) -> OptionalRefStruct: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_fbthrift_iobuf.IOBuf]]]: ...
    def _to_python(self) -> OptionalRefStruct: ...
    def _to_py3(self) -> "module.types.OptionalRefStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.OptionalRefStruct": ...  # type: ignore


class SimpleStruct(_fbthrift_python_types.Struct):
    is_on: _typing.Final[bool] = ...
    tiny_int: _typing.Final[int] = ...
    small_int: _typing.Final[int] = ...
    nice_sized_int: _typing.Final[int] = ...
    big_int: _typing.Final[int] = ...
    real: _typing.Final[float] = ...
    smaller_real: _typing.Final[float] = ...
    hidden_field: _typing.Final[int] = ...
    def __init__(
        self, *,
        is_on: _typing.Optional[bool]=...,
        tiny_int: _typing.Optional[int]=...,
        small_int: _typing.Optional[int]=...,
        nice_sized_int: _typing.Optional[int]=...,
        big_int: _typing.Optional[int]=...,
        real: _typing.Optional[float]=...,
        smaller_real: _typing.Optional[float]=...,
        hidden_field: _typing.Optional[int]=...
    ) -> None: ...

    def __call__(
        self, *,
        is_on: _typing.Optional[bool]=...,
        tiny_int: _typing.Optional[int]=...,
        small_int: _typing.Optional[int]=...,
        nice_sized_int: _typing.Optional[int]=...,
        big_int: _typing.Optional[int]=...,
        real: _typing.Optional[float]=...,
        smaller_real: _typing.Optional[float]=...,
        hidden_field: _typing.Optional[int]=...
    ) -> SimpleStruct: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[bool, int, int, int, int, float, float, int]]]: ...
    def _to_python(self) -> SimpleStruct: ...
    def _to_py3(self) -> "module.types.SimpleStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.SimpleStruct": ...  # type: ignore


class ComplexStruct(_fbthrift_python_types.Struct):
    structOne: _typing.Final[SimpleStruct] = ...
    structTwo: _typing.Final[SimpleStruct] = ...
    an_integer: _typing.Final[int] = ...
    name: _typing.Final[str] = ...
    an_enum: _typing.Final[AnEnum] = ...
    some_bytes: _typing.Final[bytes] = ...
    sender: _typing.Final[str] = ...
    cdef_: _typing.Final[str] = ...
    bytes_with_cpp_type: _typing.Final[bytes] = ...
    def __init__(
        self, *,
        structOne: _typing.Optional[SimpleStruct]=...,
        structTwo: _typing.Optional[SimpleStruct]=...,
        an_integer: _typing.Optional[int]=...,
        name: _typing.Optional[str]=...,
        an_enum: _typing.Optional[AnEnum]=...,
        some_bytes: _typing.Optional[bytes]=...,
        sender: _typing.Optional[str]=...,
        cdef_: _typing.Optional[str]=...,
        bytes_with_cpp_type: _typing.Optional[bytes]=...
    ) -> None: ...

    def __call__(
        self, *,
        structOne: _typing.Optional[SimpleStruct]=...,
        structTwo: _typing.Optional[SimpleStruct]=...,
        an_integer: _typing.Optional[int]=...,
        name: _typing.Optional[str]=...,
        an_enum: _typing.Optional[AnEnum]=...,
        some_bytes: _typing.Optional[bytes]=...,
        sender: _typing.Optional[str]=...,
        cdef_: _typing.Optional[str]=...,
        bytes_with_cpp_type: _typing.Optional[bytes]=...
    ) -> ComplexStruct: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[SimpleStruct, SimpleStruct, int, str, AnEnum, bytes, str, str, bytes]]]: ...
    def _to_python(self) -> ComplexStruct: ...
    def _to_py3(self) -> "module.types.ComplexStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.ComplexStruct": ...  # type: ignore


class BinaryUnion(_fbthrift_python_types.Union):
    iobuf_val: _typing.Final[_fbthrift_iobuf.IOBuf] = ...
    def __init__(
        self, *,
        iobuf_val: _typing.Optional[_fbthrift_iobuf.IOBuf]=...
    ) -> None: ...


    class Type(enum.Enum):
        EMPTY: BinaryUnion.Type = ...
        iobuf_val: BinaryUnion.Type = ...

    @classmethod
    def fromValue(cls, value: _typing.Union[None, _fbthrift_iobuf.IOBuf]) -> BinaryUnion: ...
    value: _typing.Final[_typing.Union[None, _fbthrift_iobuf.IOBuf]]
    type: Type
    def get_type(self) -> Type:...
    def _to_python(self) -> BinaryUnion: ...
    def _to_py3(self) -> "module.types.BinaryUnion": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.BinaryUnion": ...  # type: ignore


class BinaryUnionStruct(_fbthrift_python_types.Struct):
    u: _typing.Final[BinaryUnion] = ...
    def __init__(
        self, *,
        u: _typing.Optional[BinaryUnion]=...
    ) -> None: ...

    def __call__(
        self, *,
        u: _typing.Optional[BinaryUnion]=...
    ) -> BinaryUnionStruct: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[BinaryUnion]]]: ...
    def _to_python(self) -> BinaryUnionStruct: ...
    def _to_py3(self) -> "module.types.BinaryUnionStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.BinaryUnionStruct": ...  # type: ignore


A_BOOL: bool = ...

A_BYTE: int = ...

THE_ANSWER: int = ...

A_NUMBER: int = ...

A_BIG_NUMBER: int = ...

A_REAL_NUMBER: float = ...

A_FAKE_NUMBER: float = ...

A_WORD: str = ...

SOME_BYTES: bytes = ...

A_STRUCT: SimpleStruct = ...

WORD_LIST: _typing.List[str] = ...

SOME_MAP: _typing.List[_typing.Mapping[int, float]] = ...

DIGITS: _typing.Set[int] = ...

A_CONST_MAP: _typing.Dict[str, SimpleStruct] = ...

ANOTHER_CONST_MAP: _typing.Dict[AnEnumRenamed, int] = ...

IOBufPtr = _fbthrift_iobuf.IOBuf
IOBuf = _fbthrift_iobuf.IOBuf
foo_bar = bytes


class _fbthrift_SimpleService_get_five_args(_fbthrift_python_types.Struct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_SimpleService_get_five_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SimpleService_add_five_args(_fbthrift_python_types.Struct):
    num: _typing.Final[int] = ...

    def __init__(
        self, *,
        num: _typing.Optional[int]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, int]]]: ...


class _fbthrift_SimpleService_add_five_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SimpleService_do_nothing_args(_fbthrift_python_types.Struct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_SimpleService_do_nothing_result(_fbthrift_python_types.Struct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_SimpleService_concat_args(_fbthrift_python_types.Struct):
    first: _typing.Final[str] = ...
    second: _typing.Final[str] = ...

    def __init__(
        self, *,
        first: _typing.Optional[str]=...,
        second: _typing.Optional[str]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, str, str]]]: ...


class _fbthrift_SimpleService_concat_result(_fbthrift_python_types.Struct):
    success: _typing.Final[str]

    def __init__(
        self, *, success: _typing.Optional[str] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            str,
        ]]]: ...


class _fbthrift_SimpleService_get_value_args(_fbthrift_python_types.Struct):
    simple_struct: _typing.Final[SimpleStruct] = ...

    def __init__(
        self, *,
        simple_struct: _typing.Optional[SimpleStruct]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, SimpleStruct]]]: ...


class _fbthrift_SimpleService_get_value_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SimpleService_negate_args(_fbthrift_python_types.Struct):
    input: _typing.Final[bool] = ...

    def __init__(
        self, *,
        input: _typing.Optional[bool]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, bool]]]: ...


class _fbthrift_SimpleService_negate_result(_fbthrift_python_types.Struct):
    success: _typing.Final[bool]

    def __init__(
        self, *, success: _typing.Optional[bool] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            bool,
        ]]]: ...


class _fbthrift_SimpleService_tiny_args(_fbthrift_python_types.Struct):
    input: _typing.Final[int] = ...

    def __init__(
        self, *,
        input: _typing.Optional[int]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, int]]]: ...


class _fbthrift_SimpleService_tiny_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SimpleService_small_args(_fbthrift_python_types.Struct):
    input: _typing.Final[int] = ...

    def __init__(
        self, *,
        input: _typing.Optional[int]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, int]]]: ...


class _fbthrift_SimpleService_small_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SimpleService_big_args(_fbthrift_python_types.Struct):
    input: _typing.Final[int] = ...

    def __init__(
        self, *,
        input: _typing.Optional[int]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, int]]]: ...


class _fbthrift_SimpleService_big_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SimpleService_two_args(_fbthrift_python_types.Struct):
    input: _typing.Final[float] = ...

    def __init__(
        self, *,
        input: _typing.Optional[float]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, float]]]: ...


class _fbthrift_SimpleService_two_result(_fbthrift_python_types.Struct):
    success: _typing.Final[float]

    def __init__(
        self, *, success: _typing.Optional[float] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            float,
        ]]]: ...


class _fbthrift_SimpleService_expected_exception_args(_fbthrift_python_types.Struct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_SimpleService_expected_exception_result(_fbthrift_python_types.Struct):
    success: _typing.Final[None]
    se: _typing.Final[SimpleException]

    def __init__(
        self, *, success: _typing.Optional[None] = ..., se: _typing.Optional[SimpleException]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
            SimpleException,
        ]]]: ...


class _fbthrift_SimpleService_unexpected_exception_args(_fbthrift_python_types.Struct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_SimpleService_unexpected_exception_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SimpleService_sum_i16_list_args(_fbthrift_python_types.Struct):
    numbers: _typing.Final[_typing.Sequence[int]] = ...

    def __init__(
        self, *,
        numbers: _typing.Optional[_typing.Sequence[int]]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.Sequence[int]]]]: ...


class _fbthrift_SimpleService_sum_i16_list_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SimpleService_sum_i32_list_args(_fbthrift_python_types.Struct):
    numbers: _typing.Final[_typing.Sequence[int]] = ...

    def __init__(
        self, *,
        numbers: _typing.Optional[_typing.Sequence[int]]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.Sequence[int]]]]: ...


class _fbthrift_SimpleService_sum_i32_list_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SimpleService_sum_i64_list_args(_fbthrift_python_types.Struct):
    numbers: _typing.Final[_typing.Sequence[int]] = ...

    def __init__(
        self, *,
        numbers: _typing.Optional[_typing.Sequence[int]]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.Sequence[int]]]]: ...


class _fbthrift_SimpleService_sum_i64_list_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SimpleService_concat_many_args(_fbthrift_python_types.Struct):
    words: _typing.Final[_typing.Sequence[str]] = ...

    def __init__(
        self, *,
        words: _typing.Optional[_typing.Sequence[str]]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.Sequence[str]]]]: ...


class _fbthrift_SimpleService_concat_many_result(_fbthrift_python_types.Struct):
    success: _typing.Final[str]

    def __init__(
        self, *, success: _typing.Optional[str] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            str,
        ]]]: ...


class _fbthrift_SimpleService_count_structs_args(_fbthrift_python_types.Struct):
    items: _typing.Final[_typing.Sequence[SimpleStruct]] = ...

    def __init__(
        self, *,
        items: _typing.Optional[_typing.Sequence[SimpleStruct]]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.Sequence[SimpleStruct]]]]: ...


class _fbthrift_SimpleService_count_structs_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SimpleService_sum_set_args(_fbthrift_python_types.Struct):
    numbers: _typing.Final[_typing.AbstractSet[int]] = ...

    def __init__(
        self, *,
        numbers: _typing.Optional[_typing.AbstractSet[int]]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.AbstractSet[int]]]]: ...


class _fbthrift_SimpleService_sum_set_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SimpleService_contains_word_args(_fbthrift_python_types.Struct):
    words: _typing.Final[_typing.AbstractSet[str]] = ...
    word: _typing.Final[str] = ...

    def __init__(
        self, *,
        words: _typing.Optional[_typing.AbstractSet[str]]=...,
        word: _typing.Optional[str]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.AbstractSet[str], str]]]: ...


class _fbthrift_SimpleService_contains_word_result(_fbthrift_python_types.Struct):
    success: _typing.Final[bool]

    def __init__(
        self, *, success: _typing.Optional[bool] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            bool,
        ]]]: ...


class _fbthrift_SimpleService_get_map_value_args(_fbthrift_python_types.Struct):
    words: _typing.Final[_typing.Mapping[str, str]] = ...
    key: _typing.Final[str] = ...

    def __init__(
        self, *,
        words: _typing.Optional[_typing.Mapping[str, str]]=...,
        key: _typing.Optional[str]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.Mapping[str, str], str]]]: ...


class _fbthrift_SimpleService_get_map_value_result(_fbthrift_python_types.Struct):
    success: _typing.Final[str]

    def __init__(
        self, *, success: _typing.Optional[str] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            str,
        ]]]: ...


class _fbthrift_SimpleService_map_length_args(_fbthrift_python_types.Struct):
    items: _typing.Final[_typing.Mapping[str, SimpleStruct]] = ...

    def __init__(
        self, *,
        items: _typing.Optional[_typing.Mapping[str, SimpleStruct]]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.Mapping[str, SimpleStruct]]]]: ...


class _fbthrift_SimpleService_map_length_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SimpleService_sum_map_values_args(_fbthrift_python_types.Struct):
    items: _typing.Final[_typing.Mapping[str, int]] = ...

    def __init__(
        self, *,
        items: _typing.Optional[_typing.Mapping[str, int]]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.Mapping[str, int]]]]: ...


class _fbthrift_SimpleService_sum_map_values_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SimpleService_complex_sum_i32_args(_fbthrift_python_types.Struct):
    counter: _typing.Final[ComplexStruct] = ...

    def __init__(
        self, *,
        counter: _typing.Optional[ComplexStruct]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, ComplexStruct]]]: ...


class _fbthrift_SimpleService_complex_sum_i32_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SimpleService_repeat_name_args(_fbthrift_python_types.Struct):
    counter: _typing.Final[ComplexStruct] = ...

    def __init__(
        self, *,
        counter: _typing.Optional[ComplexStruct]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, ComplexStruct]]]: ...


class _fbthrift_SimpleService_repeat_name_result(_fbthrift_python_types.Struct):
    success: _typing.Final[str]

    def __init__(
        self, *, success: _typing.Optional[str] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            str,
        ]]]: ...


class _fbthrift_SimpleService_get_struct_args(_fbthrift_python_types.Struct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_SimpleService_get_struct_result(_fbthrift_python_types.Struct):
    success: _typing.Final[SimpleStruct]

    def __init__(
        self, *, success: _typing.Optional[SimpleStruct] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            SimpleStruct,
        ]]]: ...


class _fbthrift_SimpleService_fib_args(_fbthrift_python_types.Struct):
    n: _typing.Final[int] = ...

    def __init__(
        self, *,
        n: _typing.Optional[int]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, int]]]: ...


class _fbthrift_SimpleService_fib_result(_fbthrift_python_types.Struct):
    success: _typing.Final[_typing.Sequence[int]]

    def __init__(
        self, *, success: _typing.Optional[_typing.Sequence[int]] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            _typing.Sequence[int],
        ]]]: ...


class _fbthrift_SimpleService_unique_words_args(_fbthrift_python_types.Struct):
    words: _typing.Final[_typing.Sequence[str]] = ...

    def __init__(
        self, *,
        words: _typing.Optional[_typing.Sequence[str]]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.Sequence[str]]]]: ...


class _fbthrift_SimpleService_unique_words_result(_fbthrift_python_types.Struct):
    success: _typing.Final[_typing.AbstractSet[str]]

    def __init__(
        self, *, success: _typing.Optional[_typing.AbstractSet[str]] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            _typing.AbstractSet[str],
        ]]]: ...


class _fbthrift_SimpleService_words_count_args(_fbthrift_python_types.Struct):
    words: _typing.Final[_typing.Sequence[str]] = ...

    def __init__(
        self, *,
        words: _typing.Optional[_typing.Sequence[str]]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.Sequence[str]]]]: ...


class _fbthrift_SimpleService_words_count_result(_fbthrift_python_types.Struct):
    success: _typing.Final[_typing.Mapping[str, int]]

    def __init__(
        self, *, success: _typing.Optional[_typing.Mapping[str, int]] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            _typing.Mapping[str, int],
        ]]]: ...


class _fbthrift_SimpleService_set_enum_args(_fbthrift_python_types.Struct):
    in_enum: _typing.Final[AnEnum] = ...

    def __init__(
        self, *,
        in_enum: _typing.Optional[AnEnum]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, AnEnum]]]: ...


class _fbthrift_SimpleService_set_enum_result(_fbthrift_python_types.Struct):
    success: _typing.Final[AnEnum]

    def __init__(
        self, *, success: _typing.Optional[AnEnum] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            AnEnum,
        ]]]: ...


class _fbthrift_SimpleService_list_of_lists_args(_fbthrift_python_types.Struct):
    num_lists: _typing.Final[int] = ...
    num_items: _typing.Final[int] = ...

    def __init__(
        self, *,
        num_lists: _typing.Optional[int]=...,
        num_items: _typing.Optional[int]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, int, int]]]: ...


class _fbthrift_SimpleService_list_of_lists_result(_fbthrift_python_types.Struct):
    success: _typing.Final[_typing.Sequence[_typing.Sequence[int]]]

    def __init__(
        self, *, success: _typing.Optional[_typing.Sequence[_typing.Sequence[int]]] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            _typing.Sequence[_typing.Sequence[int]],
        ]]]: ...


class _fbthrift_SimpleService_word_character_frequency_args(_fbthrift_python_types.Struct):
    sentence: _typing.Final[str] = ...

    def __init__(
        self, *,
        sentence: _typing.Optional[str]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, str]]]: ...


class _fbthrift_SimpleService_word_character_frequency_result(_fbthrift_python_types.Struct):
    success: _typing.Final[_typing.Mapping[str, _typing.Mapping[str, int]]]

    def __init__(
        self, *, success: _typing.Optional[_typing.Mapping[str, _typing.Mapping[str, int]]] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            _typing.Mapping[str, _typing.Mapping[str, int]],
        ]]]: ...


class _fbthrift_SimpleService_list_of_sets_args(_fbthrift_python_types.Struct):
    some_words: _typing.Final[str] = ...

    def __init__(
        self, *,
        some_words: _typing.Optional[str]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, str]]]: ...


class _fbthrift_SimpleService_list_of_sets_result(_fbthrift_python_types.Struct):
    success: _typing.Final[_typing.Sequence[_typing.AbstractSet[str]]]

    def __init__(
        self, *, success: _typing.Optional[_typing.Sequence[_typing.AbstractSet[str]]] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            _typing.Sequence[_typing.AbstractSet[str]],
        ]]]: ...


class _fbthrift_SimpleService_nested_map_argument_args(_fbthrift_python_types.Struct):
    struct_map: _typing.Final[_typing.Mapping[str, _typing.Sequence[SimpleStruct]]] = ...

    def __init__(
        self, *,
        struct_map: _typing.Optional[_typing.Mapping[str, _typing.Sequence[SimpleStruct]]]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.Mapping[str, _typing.Sequence[SimpleStruct]]]]]: ...


class _fbthrift_SimpleService_nested_map_argument_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_SimpleService_make_sentence_args(_fbthrift_python_types.Struct):
    word_chars: _typing.Final[_typing.Sequence[_typing.Sequence[str]]] = ...

    def __init__(
        self, *,
        word_chars: _typing.Optional[_typing.Sequence[_typing.Sequence[str]]]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.Sequence[_typing.Sequence[str]]]]]: ...


class _fbthrift_SimpleService_make_sentence_result(_fbthrift_python_types.Struct):
    success: _typing.Final[str]

    def __init__(
        self, *, success: _typing.Optional[str] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            str,
        ]]]: ...


class _fbthrift_SimpleService_get_union_args(_fbthrift_python_types.Struct):
    sets: _typing.Final[_typing.Sequence[_typing.AbstractSet[int]]] = ...

    def __init__(
        self, *,
        sets: _typing.Optional[_typing.Sequence[_typing.AbstractSet[int]]]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.Sequence[_typing.AbstractSet[int]]]]]: ...


class _fbthrift_SimpleService_get_union_result(_fbthrift_python_types.Struct):
    success: _typing.Final[_typing.AbstractSet[int]]

    def __init__(
        self, *, success: _typing.Optional[_typing.AbstractSet[int]] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            _typing.AbstractSet[int],
        ]]]: ...


class _fbthrift_SimpleService_get_keys_args(_fbthrift_python_types.Struct):
    string_map: _typing.Final[_typing.Sequence[_typing.Mapping[str, str]]] = ...

    def __init__(
        self, *,
        string_map: _typing.Optional[_typing.Sequence[_typing.Mapping[str, str]]]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.Sequence[_typing.Mapping[str, str]]]]]: ...


class _fbthrift_SimpleService_get_keys_result(_fbthrift_python_types.Struct):
    success: _typing.Final[_typing.AbstractSet[str]]

    def __init__(
        self, *, success: _typing.Optional[_typing.AbstractSet[str]] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            _typing.AbstractSet[str],
        ]]]: ...


class _fbthrift_SimpleService_lookup_double_args(_fbthrift_python_types.Struct):
    key: _typing.Final[int] = ...

    def __init__(
        self, *,
        key: _typing.Optional[int]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, int]]]: ...


class _fbthrift_SimpleService_lookup_double_result(_fbthrift_python_types.Struct):
    success: _typing.Final[float]

    def __init__(
        self, *, success: _typing.Optional[float] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            float,
        ]]]: ...


class _fbthrift_SimpleService_retrieve_binary_args(_fbthrift_python_types.Struct):
    something: _typing.Final[bytes] = ...

    def __init__(
        self, *,
        something: _typing.Optional[bytes]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, bytes]]]: ...


class _fbthrift_SimpleService_retrieve_binary_result(_fbthrift_python_types.Struct):
    success: _typing.Final[bytes]

    def __init__(
        self, *, success: _typing.Optional[bytes] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            bytes,
        ]]]: ...


class _fbthrift_SimpleService_contain_binary_args(_fbthrift_python_types.Struct):
    binaries: _typing.Final[_typing.Sequence[bytes]] = ...

    def __init__(
        self, *,
        binaries: _typing.Optional[_typing.Sequence[bytes]]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.Sequence[bytes]]]]: ...


class _fbthrift_SimpleService_contain_binary_result(_fbthrift_python_types.Struct):
    success: _typing.Final[_typing.AbstractSet[bytes]]

    def __init__(
        self, *, success: _typing.Optional[_typing.AbstractSet[bytes]] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            _typing.AbstractSet[bytes],
        ]]]: ...


class _fbthrift_SimpleService_contain_enum_args(_fbthrift_python_types.Struct):
    the_enum: _typing.Final[_typing.Sequence[AnEnum]] = ...

    def __init__(
        self, *,
        the_enum: _typing.Optional[_typing.Sequence[AnEnum]]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _typing.Sequence[AnEnum]]]]: ...


class _fbthrift_SimpleService_contain_enum_result(_fbthrift_python_types.Struct):
    success: _typing.Final[_typing.Sequence[AnEnum]]

    def __init__(
        self, *, success: _typing.Optional[_typing.Sequence[AnEnum]] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            _typing.Sequence[AnEnum],
        ]]]: ...


class _fbthrift_SimpleService_get_binary_union_struct_args(_fbthrift_python_types.Struct):
    u: _typing.Final[BinaryUnion] = ...

    def __init__(
        self, *,
        u: _typing.Optional[BinaryUnion]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, BinaryUnion]]]: ...


class _fbthrift_SimpleService_get_binary_union_struct_result(_fbthrift_python_types.Struct):
    success: _typing.Final[BinaryUnionStruct]

    def __init__(
        self, *, success: _typing.Optional[BinaryUnionStruct] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            BinaryUnionStruct,
        ]]]: ...


class _fbthrift_DerivedService_get_six_args(_fbthrift_python_types.Struct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_DerivedService_get_six_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...


class _fbthrift_RederivedService_get_seven_args(_fbthrift_python_types.Struct):

    def __init__(
        self,
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None]]]: ...


class _fbthrift_RederivedService_get_seven_result(_fbthrift_python_types.Struct):
    success: _typing.Final[int]

    def __init__(
        self, *, success: _typing.Optional[int] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            int,
        ]]]: ...
