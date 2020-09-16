#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#
import typing as __T

from thrift import Thrift
from thrift.protocol.TProtocol import TProtocolBase

from module.ttypes import *


class Iface:  # PubSubStreamingService
    def returnstream(self, i32_from: int, i32_to: int) -> : ...
    def streamthrows(self, foo: int) -> : ...
    def boththrows(self, foo: int) -> : ...
    def responseandstreamthrows(self, foo: int) -> : ...

class Client(Iface, __T.ContextManager[Client]):  # PubSubStreamingService
    def __init__(self, iprot: TProtocolBase, oprot: __T.Optional[TProtocolBase] = None) -> None: ...
    def send_returnstream(self, i32_from: __T.Optional[int] = ..., i32_to: __T.Optional[int] = ...) -> None: ...
    def recv_returnstream(self) -> : ...
    def send_streamthrows(self, foo: __T.Optional[int] = ...) -> None: ...
    def recv_streamthrows(self) -> : ...
    def send_boththrows(self, foo: __T.Optional[int] = ...) -> None: ...
    def recv_boththrows(self) -> : ...
    def send_responseandstreamthrows(self, foo: __T.Optional[int] = ...) -> None: ...
    def recv_responseandstreamthrows(self) -> : ...

class Processor(Iface, Thrift.TProcessor):  # PubSubStreamingService
    def __init__(self, handler: Iface) -> None:
        self._handler: Iface
        self._onewayMethods: __T.Sequence[__T.Callable]
        self._processMap: __T.Dict[str, __T.Callable]

    def process_returnstream(self, seqid: int, iprot: TProtocolBase, oprot: TProtocolBase, server_ctx: __T.Any = ...) -> None: ...
    def process_streamthrows(self, seqid: int, iprot: TProtocolBase, oprot: TProtocolBase, server_ctx: __T.Any = ...) -> None: ...
    def process_boththrows(self, seqid: int, iprot: TProtocolBase, oprot: TProtocolBase, server_ctx: __T.Any = ...) -> None: ...
    def process_responseandstreamthrows(self, seqid: int, iprot: TProtocolBase, oprot: TProtocolBase, server_ctx: __T.Any = ...) -> None: ...
    def process_main(self, iprot: TProtocolBase, oprot: TProtocolBase, server_ctx: __T.Any = ...) -> __T.Optional[bool]: ...
    def onewayMethods(self) -> __T.Tuple[__T.Callable]: ...

class returnstream_args:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self,
        i32_from: __T.Optional[int] = ...,
        i32_to: __T.Optional[int] = ...
    ) -> None:
        self.i32_from: __T.Optional[int]
        self.i32_to: __T.Optional[int]

    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...

class returnstream_result:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(self, success:  = ...) -> None:
        self.success: 

    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...

class streamthrows_args:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self,
        foo: __T.Optional[int] = ...
    ) -> None:
        self.foo: __T.Optional[int]

    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...

class streamthrows_result:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(self, success:  = ...) -> None:
        self.success: 

    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...

class boththrows_args:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self,
        foo: __T.Optional[int] = ...
    ) -> None:
        self.foo: __T.Optional[int]

    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...

class boththrows_result:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(self, success:  = ...) -> None:
        self.success: 

    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...

class responseandstreamthrows_args:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self,
        foo: __T.Optional[int] = ...
    ) -> None:
        self.foo: __T.Optional[int]

    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...

class responseandstreamthrows_result:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(self, success:  = ...) -> None:
        self.success: 

    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
