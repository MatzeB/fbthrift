/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

#include "thrift/annotation/gen-py3/hack/metadata.h"

namespace facebook {
namespace thrift {
namespace annotation {
namespace hack {
::apache::thrift::metadata::ThriftMetadata hack_getThriftModuleMetadata() {
  ::apache::thrift::metadata::ThriftServiceMetadataResponse response;
  ::apache::thrift::metadata::ThriftMetadata& metadata = *response.metadata_ref();
  ::apache::thrift::detail::md::StructMetadata<FieldWrapper>::gen(metadata);
  ::apache::thrift::detail::md::StructMetadata<Adapter>::gen(metadata);
  ::apache::thrift::detail::md::StructMetadata<SkipCodegen>::gen(metadata);
  ::apache::thrift::detail::md::StructMetadata<Name>::gen(metadata);
  return metadata;
}
} // namespace facebook
} // namespace thrift
} // namespace annotation
} // namespace hack
