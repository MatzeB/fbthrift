/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#pragma once
#include <thrift/conformance/if/gen-cpp2/ConformanceServiceAsyncClient.h>
#include <thrift/conformance/if/gen-cpp2/rpc_clients.h>
#include <thrift/lib/cpp2/PluggableFunction.h>

namespace apache::thrift::conformance {

THRIFT_PLUGGABLE_FUNC_DECLARE(
    std::unique_ptr<Client<ConformanceService>>,
    create_conformance_service_client_,
    std::string /*service_name or smc tier*/);

THRIFT_PLUGGABLE_FUNC_DECLARE(
    std::unique_ptr<Client<RPCConformanceService>>,
    create_rpc_conformance_service_client_,
    std::string /*service_name or smc tier*/);

THRIFT_PLUGGABLE_FUNC_DECLARE(
    std::unique_ptr<Client<BasicRPCConformanceService>>,
    create_basic_rpc_conformance_service_client_,
    std::string /*service_name or smc tier*/);
} // namespace apache::thrift::conformance