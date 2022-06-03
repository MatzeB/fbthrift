// Autogenerated by Thrift Compiler (facebook)
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
// @generated

package module

import (
	"bytes"
	"context"
	"sync"
	"fmt"
	thrift "github.com/facebook/fbthrift/thrift/lib/go/thrift"
	hack0 "thrift/annotation/hack"

)

// (needed to ensure safety because of naive import list construction.)
var _ = thrift.ZERO
var _ = fmt.Printf
var _ = sync.Mutex{}
var _ = bytes.Equal
var _ = context.Background

var _ = hack0.GoUnusedProtection__
type FB303Service interface {
  // Parameters:
  //  - IntParameter
  SimpleRPC(int_parameter int32) (_r *ReservedKeyword, err error)
}

type FB303ServiceClientInterface interface {
  thrift.ClientInterface
  // Parameters:
  //  - IntParameter
  SimpleRPC(int_parameter int32) (_r *ReservedKeyword, err error)
}

type FB303ServiceClient struct {
  FB303ServiceClientInterface
  CC thrift.ClientConn
}

func(client *FB303ServiceClient) Open() error {
  return client.CC.Open()
}

func(client *FB303ServiceClient) Close() error {
  return client.CC.Close()
}

func(client *FB303ServiceClient) IsOpen() bool {
  return client.CC.IsOpen()
}

func NewFB303ServiceClientFactory(t thrift.Transport, f thrift.ProtocolFactory) *FB303ServiceClient {
  return &FB303ServiceClient{ CC: thrift.NewClientConn(t, f) }
}

func NewFB303ServiceClient(t thrift.Transport, iprot thrift.Protocol, oprot thrift.Protocol) *FB303ServiceClient {
  return &FB303ServiceClient{ CC: thrift.NewClientConnWithProtocols(t, iprot, oprot) }
}

func NewFB303ServiceClientProtocol(prot thrift.Protocol) *FB303ServiceClient {
  return NewFB303ServiceClient(prot.Transport(), prot, prot)
}

// Parameters:
//  - IntParameter
func (p *FB303ServiceClient) SimpleRPC(int_parameter int32) (_r *ReservedKeyword, err error) {
  args := FB303ServiceSimpleRpcArgs{
    IntParameter : int_parameter,
  }
  err = p.CC.SendMsg("simple_rpc", &args, thrift.CALL)
  if err != nil { return }
  return p.recvSimpleRPC()
}


func (p *FB303ServiceClient) recvSimpleRPC() (value *ReservedKeyword, err error) {
  var __result FB303ServiceSimpleRpcResult
  err = p.CC.RecvMsg("simple_rpc", &__result)
  if err != nil { return }

  return __result.GetSuccess(), nil
}


type FB303ServiceThreadsafeClient struct {
  FB303ServiceClientInterface
  CC thrift.ClientConn
  Mu sync.Mutex
}

func(client *FB303ServiceThreadsafeClient) Open() error {
  client.Mu.Lock()
  defer client.Mu.Unlock()
  return client.CC.Open()
}

func(client *FB303ServiceThreadsafeClient) Close() error {
  client.Mu.Lock()
  defer client.Mu.Unlock()
  return client.CC.Close()
}

func(client *FB303ServiceThreadsafeClient) IsOpen() bool {
  client.Mu.Lock()
  defer client.Mu.Unlock()
  return client.CC.IsOpen()
}

func NewFB303ServiceThreadsafeClientFactory(t thrift.Transport, f thrift.ProtocolFactory) *FB303ServiceThreadsafeClient {
  return &FB303ServiceThreadsafeClient{ CC: thrift.NewClientConn(t, f) }
}

func NewFB303ServiceThreadsafeClient(t thrift.Transport, iprot thrift.Protocol, oprot thrift.Protocol) *FB303ServiceThreadsafeClient {
  return &FB303ServiceThreadsafeClient{ CC: thrift.NewClientConnWithProtocols(t, iprot, oprot) }
}

func NewFB303ServiceThreadsafeClientProtocol(prot thrift.Protocol) *FB303ServiceThreadsafeClient {
  return NewFB303ServiceThreadsafeClient(prot.Transport(), prot, prot)
}

// Parameters:
//  - IntParameter
func (p *FB303ServiceThreadsafeClient) SimpleRPC(int_parameter int32) (_r *ReservedKeyword, err error) {
  p.Mu.Lock()
  defer p.Mu.Unlock()
  args := FB303ServiceSimpleRpcArgs{
    IntParameter : int_parameter,
  }
  err = p.CC.SendMsg("simple_rpc", &args, thrift.CALL)
  if err != nil { return }
  return p.recvSimpleRPC()
}


func (p *FB303ServiceThreadsafeClient) recvSimpleRPC() (value *ReservedKeyword, err error) {
  var __result FB303ServiceSimpleRpcResult
  err = p.CC.RecvMsg("simple_rpc", &__result)
  if err != nil { return }

  return __result.GetSuccess(), nil
}


type FB303ServiceChannelClient struct {
  RequestChannel thrift.RequestChannel
}

func (c *FB303ServiceChannelClient) Close() error {
  return c.RequestChannel.Close()
}

func (c *FB303ServiceChannelClient) IsOpen() bool {
  return c.RequestChannel.IsOpen()
}

func (c *FB303ServiceChannelClient) Open() error {
  return c.RequestChannel.Open()
}

func NewFB303ServiceChannelClient(channel thrift.RequestChannel) *FB303ServiceChannelClient {
  return &FB303ServiceChannelClient{RequestChannel: channel}
}

// Parameters:
//  - IntParameter
func (p *FB303ServiceChannelClient) SimpleRPC(ctx context.Context, int_parameter int32) (_r *ReservedKeyword, err error) {
  args := FB303ServiceSimpleRpcArgs{
    IntParameter : int_parameter,
  }
  var __result FB303ServiceSimpleRpcResult
  err = p.RequestChannel.Call(ctx, "simple_rpc", &args, &__result)
  if err != nil { return }

  return __result.GetSuccess(), nil
}


type FB303ServiceProcessor struct {
  processorMap map[string]thrift.ProcessorFunction
  functionServiceMap map[string]string
  handler FB303Service
}

func (p *FB303ServiceProcessor) AddToProcessorMap(key string, processor thrift.ProcessorFunction) {
  p.processorMap[key] = processor
}

func (p *FB303ServiceProcessor) AddToFunctionServiceMap(key, service string) {
  p.functionServiceMap[key] = service
}

func (p *FB303ServiceProcessor) GetProcessorFunction(key string) (processor thrift.ProcessorFunction, err error) {
  if processor, ok := p.processorMap[key]; ok {
    return processor, nil
  }
  return nil, nil // generic error message will be sent
}

func (p *FB303ServiceProcessor) ProcessorMap() map[string]thrift.ProcessorFunction {
  return p.processorMap
}

func (p *FB303ServiceProcessor) FunctionServiceMap() map[string]string {
  return p.functionServiceMap
}

func NewFB303ServiceProcessor(handler FB303Service) *FB303ServiceProcessor {
  self5 := &FB303ServiceProcessor{handler:handler, processorMap:make(map[string]thrift.ProcessorFunction), functionServiceMap:make(map[string]string)}
  self5.processorMap["simple_rpc"] = &fB303ServiceProcessorSimpleRPC{handler:handler}
  self5.functionServiceMap["simple_rpc"] = "FB303Service"
  return self5
}

type fB303ServiceProcessorSimpleRPC struct {
  handler FB303Service
}

func (p *FB303ServiceSimpleRpcResult) Exception() thrift.WritableException {
  if p == nil { return nil }
  return nil
}

func (p *fB303ServiceProcessorSimpleRPC) Read(iprot thrift.Protocol) (thrift.Struct, thrift.Exception) {
  args := FB303ServiceSimpleRpcArgs{}
  if err := args.Read(iprot); err != nil {
    return nil, err
  }
  iprot.ReadMessageEnd()
  return &args, nil
}

func (p *fB303ServiceProcessorSimpleRPC) Write(seqId int32, result thrift.WritableStruct, oprot thrift.Protocol) (err thrift.Exception) {
  var err2 error
  messageType := thrift.REPLY
  switch result.(type) {
  case thrift.ApplicationException:
    messageType = thrift.EXCEPTION
  }
  if err2 = oprot.WriteMessageBegin("simple_rpc", messageType, seqId); err2 != nil {
    err = err2
  }
  if err2 = result.Write(oprot); err == nil && err2 != nil {
    err = err2
  }
  if err2 = oprot.WriteMessageEnd(); err == nil && err2 != nil {
    err = err2
  }
  if err2 = oprot.Flush(); err == nil && err2 != nil {
    err = err2
  }
  return err
}

func (p *fB303ServiceProcessorSimpleRPC) Run(argStruct thrift.Struct) (thrift.WritableStruct, thrift.ApplicationException) {
  args := argStruct.(*FB303ServiceSimpleRpcArgs)
  var __result FB303ServiceSimpleRpcResult
  if retval, err := p.handler.SimpleRPC(args.IntParameter); err != nil {
    switch err.(type) {
    default:
      x := thrift.NewApplicationExceptionCause(thrift.INTERNAL_ERROR, "Internal error processing simple_rpc: " + err.Error(), err)
      return x, x
    }
  } else {
    __result.Success = retval
  }
  return &__result, nil
}


// HELPER FUNCTIONS AND STRUCTURES

// Attributes:
//  - IntParameter
type FB303ServiceSimpleRpcArgs struct {
  thrift.IRequest
  IntParameter int32 `thrift:"int_parameter,1" db:"int_parameter" json:"int_parameter"`
}

func NewFB303ServiceSimpleRpcArgs() *FB303ServiceSimpleRpcArgs {
  return &FB303ServiceSimpleRpcArgs{}
}


func (p *FB303ServiceSimpleRpcArgs) GetIntParameter() int32 {
  return p.IntParameter
}
type FB303ServiceSimpleRpcArgsBuilder struct {
  obj *FB303ServiceSimpleRpcArgs
}

func NewFB303ServiceSimpleRpcArgsBuilder() *FB303ServiceSimpleRpcArgsBuilder{
  return &FB303ServiceSimpleRpcArgsBuilder{
    obj: NewFB303ServiceSimpleRpcArgs(),
  }
}

func (p FB303ServiceSimpleRpcArgsBuilder) Emit() *FB303ServiceSimpleRpcArgs{
  return &FB303ServiceSimpleRpcArgs{
    IntParameter: p.obj.IntParameter,
  }
}

func (f *FB303ServiceSimpleRpcArgsBuilder) IntParameter(intParameter int32) *FB303ServiceSimpleRpcArgsBuilder {
  f.obj.IntParameter = intParameter
  return f
}

func (f *FB303ServiceSimpleRpcArgs) SetIntParameter(intParameter int32) *FB303ServiceSimpleRpcArgs {
  f.IntParameter = intParameter
  return f
}

func (p *FB303ServiceSimpleRpcArgs) Read(iprot thrift.Protocol) error {
  if _, err := iprot.ReadStructBegin(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T read error: ", p), err)
  }


  for {
    _, fieldTypeId, fieldId, err := iprot.ReadFieldBegin()
    if err != nil {
      return thrift.PrependError(fmt.Sprintf("%T field %d read error: ", p, fieldId), err)
    }
    if fieldTypeId == thrift.STOP { break; }
    switch fieldId {
    case 1:
      if err := p.ReadField1(iprot); err != nil {
        return err
      }
    default:
      if err := iprot.Skip(fieldTypeId); err != nil {
        return err
      }
    }
    if err := iprot.ReadFieldEnd(); err != nil {
      return err
    }
  }
  if err := iprot.ReadStructEnd(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T read struct end error: ", p), err)
  }
  return nil
}

func (p *FB303ServiceSimpleRpcArgs)  ReadField1(iprot thrift.Protocol) error {
  if v, err := iprot.ReadI32(); err != nil {
    return thrift.PrependError("error reading field 1: ", err)
  } else {
    p.IntParameter = v
  }
  return nil
}

func (p *FB303ServiceSimpleRpcArgs) Write(oprot thrift.Protocol) error {
  if err := oprot.WriteStructBegin("simple_rpc_args"); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", p), err) }
  if err := p.writeField1(oprot); err != nil { return err }
  if err := oprot.WriteFieldStop(); err != nil {
    return thrift.PrependError("write field stop error: ", err) }
  if err := oprot.WriteStructEnd(); err != nil {
    return thrift.PrependError("write struct stop error: ", err) }
  return nil
}

func (p *FB303ServiceSimpleRpcArgs) writeField1(oprot thrift.Protocol) (err error) {
  if err := oprot.WriteFieldBegin("int_parameter", thrift.I32, 1); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field begin error 1:int_parameter: ", p), err) }
  if err := oprot.WriteI32(int32(p.IntParameter)); err != nil {
  return thrift.PrependError(fmt.Sprintf("%T.int_parameter (1) field write error: ", p), err) }
  if err := oprot.WriteFieldEnd(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field end error 1:int_parameter: ", p), err) }
  return err
}

func (p *FB303ServiceSimpleRpcArgs) String() string {
  if p == nil {
    return "<nil>"
  }

  intParameterVal := fmt.Sprintf("%v", p.IntParameter)
  return fmt.Sprintf("FB303ServiceSimpleRpcArgs({IntParameter:%s})", intParameterVal)
}

// Attributes:
//  - Success
type FB303ServiceSimpleRpcResult struct {
  thrift.IResponse
  Success *ReservedKeyword `thrift:"success,0,optional" db:"success" json:"success,omitempty"`
}

func NewFB303ServiceSimpleRpcResult() *FB303ServiceSimpleRpcResult {
  return &FB303ServiceSimpleRpcResult{}
}

var FB303ServiceSimpleRpcResult_Success_DEFAULT *ReservedKeyword
func (p *FB303ServiceSimpleRpcResult) GetSuccess() *ReservedKeyword {
  if !p.IsSetSuccess() {
    return FB303ServiceSimpleRpcResult_Success_DEFAULT
  }
return p.Success
}
func (p *FB303ServiceSimpleRpcResult) IsSetSuccess() bool {
  return p != nil && p.Success != nil
}

type FB303ServiceSimpleRpcResultBuilder struct {
  obj *FB303ServiceSimpleRpcResult
}

func NewFB303ServiceSimpleRpcResultBuilder() *FB303ServiceSimpleRpcResultBuilder{
  return &FB303ServiceSimpleRpcResultBuilder{
    obj: NewFB303ServiceSimpleRpcResult(),
  }
}

func (p FB303ServiceSimpleRpcResultBuilder) Emit() *FB303ServiceSimpleRpcResult{
  return &FB303ServiceSimpleRpcResult{
    Success: p.obj.Success,
  }
}

func (f *FB303ServiceSimpleRpcResultBuilder) Success(success *ReservedKeyword) *FB303ServiceSimpleRpcResultBuilder {
  f.obj.Success = success
  return f
}

func (f *FB303ServiceSimpleRpcResult) SetSuccess(success *ReservedKeyword) *FB303ServiceSimpleRpcResult {
  f.Success = success
  return f
}

func (p *FB303ServiceSimpleRpcResult) Read(iprot thrift.Protocol) error {
  if _, err := iprot.ReadStructBegin(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T read error: ", p), err)
  }


  for {
    _, fieldTypeId, fieldId, err := iprot.ReadFieldBegin()
    if err != nil {
      return thrift.PrependError(fmt.Sprintf("%T field %d read error: ", p, fieldId), err)
    }
    if fieldTypeId == thrift.STOP { break; }
    switch fieldId {
    case 0:
      if err := p.ReadField0(iprot); err != nil {
        return err
      }
    default:
      if err := iprot.Skip(fieldTypeId); err != nil {
        return err
      }
    }
    if err := iprot.ReadFieldEnd(); err != nil {
      return err
    }
  }
  if err := iprot.ReadStructEnd(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T read struct end error: ", p), err)
  }
  return nil
}

func (p *FB303ServiceSimpleRpcResult)  ReadField0(iprot thrift.Protocol) error {
  p.Success = NewReservedKeyword()
  if err := p.Success.Read(iprot); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T error reading struct: ", p.Success), err)
  }
  return nil
}

func (p *FB303ServiceSimpleRpcResult) Write(oprot thrift.Protocol) error {
  if err := oprot.WriteStructBegin("simple_rpc_result"); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", p), err) }
  if err := p.writeField0(oprot); err != nil { return err }
  if err := oprot.WriteFieldStop(); err != nil {
    return thrift.PrependError("write field stop error: ", err) }
  if err := oprot.WriteStructEnd(); err != nil {
    return thrift.PrependError("write struct stop error: ", err) }
  return nil
}

func (p *FB303ServiceSimpleRpcResult) writeField0(oprot thrift.Protocol) (err error) {
  if p.IsSetSuccess() {
    if err := oprot.WriteFieldBegin("success", thrift.STRUCT, 0); err != nil {
      return thrift.PrependError(fmt.Sprintf("%T write field begin error 0:success: ", p), err) }
    if err := p.Success.Write(oprot); err != nil {
      return thrift.PrependError(fmt.Sprintf("%T error writing struct: ", p.Success), err)
    }
    if err := oprot.WriteFieldEnd(); err != nil {
      return thrift.PrependError(fmt.Sprintf("%T write field end error 0:success: ", p), err) }
  }
  return err
}

func (p *FB303ServiceSimpleRpcResult) String() string {
  if p == nil {
    return "<nil>"
  }

  var successVal string
  if p.Success == nil {
    successVal = "<nil>"
  } else {
    successVal = fmt.Sprintf("%v", p.Success)
  }
  return fmt.Sprintf("FB303ServiceSimpleRpcResult({Success:%s})", successVal)
}


