# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from cython.view cimport memoryview
from folly.iobuf cimport IOBuf
from thrift.python.exceptions cimport Error
from thrift.python.types cimport Struct, StructOrUnion, Union

import cython

Buf = cython.fused_type(IOBuf, bytes, bytearray, memoryview)

def serialize_iobuf(StructOrUnion strct not None, Protocol protocol=Protocol.COMPACT):
    return strct._serialize(protocol)

def serialize(StructOrUnion struct not None, Protocol protocol=Protocol.COMPACT):
    return b''.join(serialize_iobuf(struct, protocol))

def deserialize_with_length(klass, Buf buf, Protocol protocol=Protocol.COMPACT):
    if not issubclass(klass, StructOrUnion):
        raise TypeError("Only Struct or Union classes can be deserialized")
    cdef IOBuf iobuf = buf if isinstance(buf, IOBuf) else IOBuf(buf)
    inst = klass.__new__(klass)
    cdef uint32_t length
    try:
        length = (<Struct>inst)._deserialize(
            iobuf, protocol) if issubclass(klass, Struct) else (
            <Union>inst)._deserialize(iobuf, protocol)
    except Exception as e:
        raise Error.__new__(Error, *e.args) from None
    return inst, length

def deserialize(klass, Buf buf, Protocol protocol=Protocol.COMPACT):
    return deserialize_with_length(klass, buf, protocol)[0]
