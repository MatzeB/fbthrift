/**
 * Autogenerated by Thrift for src/module.thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated @nocommit
 */
#pragma once

#include <vector>

#include <thrift/lib/cpp2/gen/module_metadata_h.h>
#include "thrift/compiler/test/fixtures/basic/gen-cpp2/module_types.h"
#include "thrift/annotation/gen-cpp2/hack_metadata.h"

namespace test {
namespace fixtures {
namespace basic {
class FooService;
}}} // namespace test::fixtures::basic
namespace test {
namespace fixtures {
namespace basic {
class FB303Service;
}}} // namespace test::fixtures::basic
namespace test {
namespace fixtures {
namespace basic {
class MyService;
}}} // namespace test::fixtures::basic
namespace test {
namespace fixtures {
namespace basic {
class DbMixedStackArguments;
}}} // namespace test::fixtures::basic

namespace apache {
namespace thrift {
namespace detail {
namespace md {

template <>
class EnumMetadata<::test::fixtures::basic::MyEnum> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class EnumMetadata<::test::fixtures::basic::HackEnum> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test::fixtures::basic::MyDataItem> {
 public:
  static const ::apache::thrift::metadata::ThriftStruct& gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test::fixtures::basic::MyStruct> {
 public:
  static const ::apache::thrift::metadata::ThriftStruct& gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test::fixtures::basic::MyUnion> {
 public:
  static const ::apache::thrift::metadata::ThriftStruct& gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test::fixtures::basic::ReservedKeyword> {
 public:
  static const ::apache::thrift::metadata::ThriftStruct& gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test::fixtures::basic::UnionToBeRenamed> {
 public:
  static const ::apache::thrift::metadata::ThriftStruct& gen(ThriftMetadata& metadata);
};
template <>
class ServiceMetadata<::apache::thrift::ServiceHandler<::test::fixtures::basic::FooService>> {
 public:
  static void gen(ThriftServiceMetadataResponse& response);
 private:
  static const ThriftServiceContextRef* genRecurse(ThriftMetadata& metadata, std::vector<ThriftServiceContextRef>& services);

  template <typename T>
  friend class ServiceMetadata;

  static void gen_simple_rpc(ThriftMetadata& metadata, ThriftService& context);
};
template <>
class ServiceMetadata<::apache::thrift::ServiceHandler<::test::fixtures::basic::FB303Service>> {
 public:
  static void gen(ThriftServiceMetadataResponse& response);
 private:
  static const ThriftServiceContextRef* genRecurse(ThriftMetadata& metadata, std::vector<ThriftServiceContextRef>& services);

  template <typename T>
  friend class ServiceMetadata;

  static void gen_simple_rpc(ThriftMetadata& metadata, ThriftService& context);
};
template <>
class ServiceMetadata<::apache::thrift::ServiceHandler<::test::fixtures::basic::MyService>> {
 public:
  static void gen(ThriftServiceMetadataResponse& response);
 private:
  static const ThriftServiceContextRef* genRecurse(ThriftMetadata& metadata, std::vector<ThriftServiceContextRef>& services);

  template <typename T>
  friend class ServiceMetadata;

  static void gen_ping(ThriftMetadata& metadata, ThriftService& context);
  static void gen_getRandomData(ThriftMetadata& metadata, ThriftService& context);
  static void gen_sink(ThriftMetadata& metadata, ThriftService& context);
  static void gen_putDataById(ThriftMetadata& metadata, ThriftService& context);
  static void gen_hasDataById(ThriftMetadata& metadata, ThriftService& context);
  static void gen_getDataById(ThriftMetadata& metadata, ThriftService& context);
  static void gen_deleteDataById(ThriftMetadata& metadata, ThriftService& context);
  static void gen_lobDataById(ThriftMetadata& metadata, ThriftService& context);
  static void gen_invalid_return_for_hack(ThriftMetadata& metadata, ThriftService& context);
  static void gen_rpc_skipped_codegen(ThriftMetadata& metadata, ThriftService& context);
};
template <>
class ServiceMetadata<::apache::thrift::ServiceHandler<::test::fixtures::basic::DbMixedStackArguments>> {
 public:
  static void gen(ThriftServiceMetadataResponse& response);
 private:
  static const ThriftServiceContextRef* genRecurse(ThriftMetadata& metadata, std::vector<ThriftServiceContextRef>& services);

  template <typename T>
  friend class ServiceMetadata;

  static void gen_getDataByKey0(ThriftMetadata& metadata, ThriftService& context);
  static void gen_getDataByKey1(ThriftMetadata& metadata, ThriftService& context);
};
} // namespace md
} // namespace detail
} // namespace thrift
} // namespace apache
