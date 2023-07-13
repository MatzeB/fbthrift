#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from libc.stdint cimport (
    int8_t as cint8_t,
    int16_t as cint16_t,
    int32_t as cint32_t,
    int64_t as cint64_t,
    uint16_t as cuint16_t,
    uint32_t as cuint32_t,
)
from libcpp.string cimport string
from libcpp cimport bool as cbool, nullptr, nullptr_t
from cpython cimport bool as pbool
from libcpp.memory cimport shared_ptr, unique_ptr
from libcpp.utility cimport move as cmove
from libcpp.vector cimport vector
from libcpp.set cimport set as cset
from libcpp.map cimport map as cmap
from libcpp.unordered_map cimport unordered_map as cumap
from thrift.py3.exceptions cimport cTException
cimport folly.iobuf as _fbthrift_iobuf
cimport thrift.py3.exceptions
cimport thrift.py3.types
from thrift.py3.common cimport Protocol as __Protocol
from thrift.py3.std_libcpp cimport string_view as __cstring_view
from thrift.py3.types cimport (
    bstring,
    bytes_to_string,
    field_ref as __field_ref,
    optional_field_ref as __optional_field_ref,
    required_field_ref as __required_field_ref,
    terse_field_ref as __terse_field_ref,
    StructFieldsSetter as __StructFieldsSetter
)
from folly.optional cimport cOptional as __cOptional


cimport module.types as _module_types



ctypedef void (*__MyField_FieldsSetterFunc)(__MyField_FieldsSetter, object) except *

cdef class __MyField_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cMyField* _struct_cpp_obj
    cdef cumap[__cstring_view, __MyField_FieldsSetterFunc] _setters

    @staticmethod
    cdef __MyField_FieldsSetter _fbthrift_create(_module_types.cMyField* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *
    cdef void _set_field_1(self, _fbthrift_value) except *
    cdef void _set_field_2(self, _fbthrift_value) except *
    cdef void _set_field_3(self, _fbthrift_value) except *
    cdef void _set_field_4(self, _fbthrift_value) except *
    cdef void _set_field_5(self, _fbthrift_value) except *
    cdef void _set_field_6(self, _fbthrift_value) except *
    cdef void _set_field_7(self, _fbthrift_value) except *
    cdef void _set_field_8(self, _fbthrift_value) except *


ctypedef void (*__MyStruct_FieldsSetterFunc)(__MyStruct_FieldsSetter, object) except *

cdef class __MyStruct_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cMyStruct* _struct_cpp_obj
    cdef cumap[__cstring_view, __MyStruct_FieldsSetterFunc] _setters

    @staticmethod
    cdef __MyStruct_FieldsSetter _fbthrift_create(_module_types.cMyStruct* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *
    cdef void _set_field_1(self, _fbthrift_value) except *
    cdef void _set_field_2(self, _fbthrift_value) except *


ctypedef void (*__StructWithUnion_FieldsSetterFunc)(__StructWithUnion_FieldsSetter, object) except *

cdef class __StructWithUnion_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cStructWithUnion* _struct_cpp_obj
    cdef cumap[__cstring_view, __StructWithUnion_FieldsSetterFunc] _setters

    @staticmethod
    cdef __StructWithUnion_FieldsSetter _fbthrift_create(_module_types.cStructWithUnion* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *
    cdef void _set_field_1(self, _fbthrift_value) except *
    cdef void _set_field_2(self, _fbthrift_value) except *


ctypedef void (*__RecursiveStruct_FieldsSetterFunc)(__RecursiveStruct_FieldsSetter, object) except *

cdef class __RecursiveStruct_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cRecursiveStruct* _struct_cpp_obj
    cdef cumap[__cstring_view, __RecursiveStruct_FieldsSetterFunc] _setters

    @staticmethod
    cdef __RecursiveStruct_FieldsSetter _fbthrift_create(_module_types.cRecursiveStruct* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *


ctypedef void (*__StructWithContainers_FieldsSetterFunc)(__StructWithContainers_FieldsSetter, object) except *

cdef class __StructWithContainers_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cStructWithContainers* _struct_cpp_obj
    cdef cumap[__cstring_view, __StructWithContainers_FieldsSetterFunc] _setters

    @staticmethod
    cdef __StructWithContainers_FieldsSetter _fbthrift_create(_module_types.cStructWithContainers* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *
    cdef void _set_field_1(self, _fbthrift_value) except *
    cdef void _set_field_2(self, _fbthrift_value) except *
    cdef void _set_field_3(self, _fbthrift_value) except *
    cdef void _set_field_4(self, _fbthrift_value) except *
    cdef void _set_field_5(self, _fbthrift_value) except *


ctypedef void (*__StructWithSharedConst_FieldsSetterFunc)(__StructWithSharedConst_FieldsSetter, object) except *

cdef class __StructWithSharedConst_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cStructWithSharedConst* _struct_cpp_obj
    cdef cumap[__cstring_view, __StructWithSharedConst_FieldsSetterFunc] _setters

    @staticmethod
    cdef __StructWithSharedConst_FieldsSetter _fbthrift_create(_module_types.cStructWithSharedConst* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *
    cdef void _set_field_1(self, _fbthrift_value) except *
    cdef void _set_field_2(self, _fbthrift_value) except *


ctypedef void (*__Empty_FieldsSetterFunc)(__Empty_FieldsSetter, object) except *

cdef class __Empty_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cEmpty* _struct_cpp_obj
    cdef cumap[__cstring_view, __Empty_FieldsSetterFunc] _setters

    @staticmethod
    cdef __Empty_FieldsSetter _fbthrift_create(_module_types.cEmpty* struct_cpp_obj)


ctypedef void (*__StructWithRef_FieldsSetterFunc)(__StructWithRef_FieldsSetter, object) except *

cdef class __StructWithRef_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cStructWithRef* _struct_cpp_obj
    cdef cumap[__cstring_view, __StructWithRef_FieldsSetterFunc] _setters

    @staticmethod
    cdef __StructWithRef_FieldsSetter _fbthrift_create(_module_types.cStructWithRef* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *
    cdef void _set_field_1(self, _fbthrift_value) except *
    cdef void _set_field_2(self, _fbthrift_value) except *


ctypedef void (*__StructWithBox_FieldsSetterFunc)(__StructWithBox_FieldsSetter, object) except *

cdef class __StructWithBox_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cStructWithBox* _struct_cpp_obj
    cdef cumap[__cstring_view, __StructWithBox_FieldsSetterFunc] _setters

    @staticmethod
    cdef __StructWithBox_FieldsSetter _fbthrift_create(_module_types.cStructWithBox* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *
    cdef void _set_field_1(self, _fbthrift_value) except *
    cdef void _set_field_2(self, _fbthrift_value) except *


ctypedef void (*__StructWithInternBox_FieldsSetterFunc)(__StructWithInternBox_FieldsSetter, object) except *

cdef class __StructWithInternBox_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cStructWithInternBox* _struct_cpp_obj
    cdef cumap[__cstring_view, __StructWithInternBox_FieldsSetterFunc] _setters

    @staticmethod
    cdef __StructWithInternBox_FieldsSetter _fbthrift_create(_module_types.cStructWithInternBox* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *
    cdef void _set_field_1(self, _fbthrift_value) except *


ctypedef void (*__StructWithTerseInternBox_FieldsSetterFunc)(__StructWithTerseInternBox_FieldsSetter, object) except *

cdef class __StructWithTerseInternBox_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cStructWithTerseInternBox* _struct_cpp_obj
    cdef cumap[__cstring_view, __StructWithTerseInternBox_FieldsSetterFunc] _setters

    @staticmethod
    cdef __StructWithTerseInternBox_FieldsSetter _fbthrift_create(_module_types.cStructWithTerseInternBox* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *
    cdef void _set_field_1(self, _fbthrift_value) except *


ctypedef void (*__AdaptedStructWithInternBox_FieldsSetterFunc)(__AdaptedStructWithInternBox_FieldsSetter, object) except *

cdef class __AdaptedStructWithInternBox_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cAdaptedStructWithInternBox* _struct_cpp_obj
    cdef cumap[__cstring_view, __AdaptedStructWithInternBox_FieldsSetterFunc] _setters

    @staticmethod
    cdef __AdaptedStructWithInternBox_FieldsSetter _fbthrift_create(_module_types.cAdaptedStructWithInternBox* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *
    cdef void _set_field_1(self, _fbthrift_value) except *


ctypedef void (*__AdaptedStructWithTerseInternBox_FieldsSetterFunc)(__AdaptedStructWithTerseInternBox_FieldsSetter, object) except *

cdef class __AdaptedStructWithTerseInternBox_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cAdaptedStructWithTerseInternBox* _struct_cpp_obj
    cdef cumap[__cstring_view, __AdaptedStructWithTerseInternBox_FieldsSetterFunc] _setters

    @staticmethod
    cdef __AdaptedStructWithTerseInternBox_FieldsSetter _fbthrift_create(_module_types.cAdaptedStructWithTerseInternBox* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *
    cdef void _set_field_1(self, _fbthrift_value) except *


ctypedef void (*__StructWithRefTypeUnique_FieldsSetterFunc)(__StructWithRefTypeUnique_FieldsSetter, object) except *

cdef class __StructWithRefTypeUnique_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cStructWithRefTypeUnique* _struct_cpp_obj
    cdef cumap[__cstring_view, __StructWithRefTypeUnique_FieldsSetterFunc] _setters

    @staticmethod
    cdef __StructWithRefTypeUnique_FieldsSetter _fbthrift_create(_module_types.cStructWithRefTypeUnique* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *
    cdef void _set_field_1(self, _fbthrift_value) except *
    cdef void _set_field_2(self, _fbthrift_value) except *


ctypedef void (*__StructWithRefTypeShared_FieldsSetterFunc)(__StructWithRefTypeShared_FieldsSetter, object) except *

cdef class __StructWithRefTypeShared_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cStructWithRefTypeShared* _struct_cpp_obj
    cdef cumap[__cstring_view, __StructWithRefTypeShared_FieldsSetterFunc] _setters

    @staticmethod
    cdef __StructWithRefTypeShared_FieldsSetter _fbthrift_create(_module_types.cStructWithRefTypeShared* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *
    cdef void _set_field_1(self, _fbthrift_value) except *
    cdef void _set_field_2(self, _fbthrift_value) except *


ctypedef void (*__StructWithRefTypeSharedConst_FieldsSetterFunc)(__StructWithRefTypeSharedConst_FieldsSetter, object) except *

cdef class __StructWithRefTypeSharedConst_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cStructWithRefTypeSharedConst* _struct_cpp_obj
    cdef cumap[__cstring_view, __StructWithRefTypeSharedConst_FieldsSetterFunc] _setters

    @staticmethod
    cdef __StructWithRefTypeSharedConst_FieldsSetter _fbthrift_create(_module_types.cStructWithRefTypeSharedConst* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *
    cdef void _set_field_1(self, _fbthrift_value) except *
    cdef void _set_field_2(self, _fbthrift_value) except *


ctypedef void (*__StructWithRefAndAnnotCppNoexceptMoveCtor_FieldsSetterFunc)(__StructWithRefAndAnnotCppNoexceptMoveCtor_FieldsSetter, object) except *

cdef class __StructWithRefAndAnnotCppNoexceptMoveCtor_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cStructWithRefAndAnnotCppNoexceptMoveCtor* _struct_cpp_obj
    cdef cumap[__cstring_view, __StructWithRefAndAnnotCppNoexceptMoveCtor_FieldsSetterFunc] _setters

    @staticmethod
    cdef __StructWithRefAndAnnotCppNoexceptMoveCtor_FieldsSetter _fbthrift_create(_module_types.cStructWithRefAndAnnotCppNoexceptMoveCtor* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *


ctypedef void (*__StructWithString_FieldsSetterFunc)(__StructWithString_FieldsSetter, object) except *

cdef class __StructWithString_FieldsSetter(__StructFieldsSetter):
    cdef _module_types.cStructWithString* _struct_cpp_obj
    cdef cumap[__cstring_view, __StructWithString_FieldsSetterFunc] _setters

    @staticmethod
    cdef __StructWithString_FieldsSetter _fbthrift_create(_module_types.cStructWithString* struct_cpp_obj)
    cdef void _set_field_0(self, _fbthrift_value) except *
    cdef void _set_field_1(self, _fbthrift_value) except *
    cdef void _set_field_2(self, _fbthrift_value) except *
    cdef void _set_field_3(self, _fbthrift_value) except *
    cdef void _set_field_4(self, _fbthrift_value) except *

