/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

package test.fixtures.basic;

import com.facebook.nifty.client.RequestChannel;
import com.facebook.swift.codec.*;
import com.facebook.swift.service.*;
import com.facebook.swift.service.metadata.*;
import com.facebook.thrift.client.*;
import com.facebook.thrift.util.FutureUtil;
import java.io.*;
import java.lang.reflect.Method;
import java.util.*;
import org.apache.thrift.ProtocolId;
import reactor.core.publisher.Mono;

@SwiftGenerated
@Deprecated
public class FooServiceClientImpl extends AbstractThriftClient implements FooService {

    // Method Handlers
    private ThriftMethodHandler simpleRpcMethodHandler;

    // Method Exceptions
    private static final Class[] simpleRpcExceptions = new Class[] {
        org.apache.thrift.TException.class};

    public FooServiceClientImpl(
        RequestChannel channel,
        Map<Method, ThriftMethodHandler> methods,
        Map<String, String> headers,
        Map<String, String> persistentHeaders,
        List<? extends ThriftClientEventHandler> eventHandlers) {
      super(channel, headers, persistentHeaders, eventHandlers);

      Map<String, ThriftMethodHandler> methodHandlerMap = new HashMap<>();
      methods.forEach(
          (key, value) -> {
            methodHandlerMap.put(key.getName(), value);
          });

      // Set method handlers
      simpleRpcMethodHandler = methodHandlerMap.get("simpleRpc");
    }

    public FooServiceClientImpl(
        Map<String, String> headers,
        Map<String, String> persistentHeaders,
        Mono<? extends RpcClient> rpcClient,
        ThriftServiceMetadata serviceMetadata,
        ThriftCodecManager codecManager,
        ProtocolId protocolId,
        Map<Method, ThriftMethodHandler> methods) {
      super(headers, persistentHeaders, rpcClient, serviceMetadata, codecManager, protocolId);

      Map<String, ThriftMethodHandler> methodHandlerMap = new HashMap<>();
      methods.forEach(
          (key, value) -> {
            methodHandlerMap.put(key.getName(), value);
          });

      // Set method handlers
      simpleRpcMethodHandler = methodHandlerMap.get("simpleRpc");
    }

    @java.lang.Override
    public void close() {
        super.close();
    }


    @java.lang.Override
    public void simpleRpc() throws org.apache.thrift.TException {
      simpleRpcWrapper(RpcOptions.EMPTY).getData();
    }

    @java.lang.Override
    public void simpleRpc(
        RpcOptions rpcOptions) throws org.apache.thrift.TException {
      simpleRpcWrapper(rpcOptions).getData();
    }

    @java.lang.Override
    public ResponseWrapper<Void> simpleRpcWrapper(
        RpcOptions rpcOptions) throws org.apache.thrift.TException {
      try {
        return FutureUtil.get(executeWrapperWithOptions(simpleRpcMethodHandler, simpleRpcExceptions, rpcOptions));
      } catch (Throwable t) {
        if (t instanceof org.apache.thrift.TException) {
          throw (org.apache.thrift.TException) t;
        }
        throw new org.apache.thrift.TException(t);
      }
    }
}
