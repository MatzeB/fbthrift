<?hh
/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

namespace fixtures\basic;

/**
 * Original thrift service:-
 * FB303Service
 */
<<\ThriftTypeInfo(shape('uri' => 'test.dev/fixtures/basic/FB303Service'))>>
interface FB303ServiceAsyncIf extends \IThriftAsyncIf {
  /**
   * Original thrift definition:-
   * ReservedKeyword
   *   simple_rpc(1: i32 int_parameter);
   */
  public function simple_rpc(int $int_parameter): Awaitable<\fixtures\basic\ReservedKeyword>;
}

/**
 * Original thrift service:-
 * FB303Service
 */
<<\ThriftTypeInfo(shape('uri' => 'test.dev/fixtures/basic/FB303Service'))>>
interface FB303ServiceIf extends \IThriftSyncIf {
  /**
   * Original thrift definition:-
   * ReservedKeyword
   *   simple_rpc(1: i32 int_parameter);
   */
  public function simple_rpc(int $int_parameter): \fixtures\basic\ReservedKeyword;
}

/**
 * Original thrift service:-
 * FB303Service
 */
<<\ThriftTypeInfo(shape('uri' => 'test.dev/fixtures/basic/FB303Service'))>>
interface FB303ServiceAsyncClientIf extends FB303ServiceAsyncIf {
}

/**
 * Original thrift service:-
 * FB303Service
 */
<<\ThriftTypeInfo(shape('uri' => 'test.dev/fixtures/basic/FB303Service'))>>
interface FB303ServiceClientIf extends \IThriftSyncIf {
  /**
   * Original thrift definition:-
   * ReservedKeyword
   *   simple_rpc(1: i32 int_parameter);
   */
  public function simple_rpc(int $int_parameter): Awaitable<\fixtures\basic\ReservedKeyword>;
}

/**
 * Original thrift service:-
 * FB303Service
 */
trait FB303ServiceClientBase {
  require extends \ThriftClientBase;


  protected function recvImpl_simple_rpc(?int $expectedsequenceid = null, shape(?'read_options' => int) $options = shape()): \fixtures\basic\ReservedKeyword {
    try {
      $this->eventHandler_->preRecv('simple_rpc', $expectedsequenceid);
      if ($this->input_ is \TBinaryProtocolAccelerated) {
        $result = \thrift_protocol_read_binary($this->input_, '\fixtures\basic\FB303Service_simple_rpc_result', $this->input_->isStrictRead(), Shapes::idx($options, 'read_options', 0));
      } else if ($this->input_ is \TCompactProtocolAccelerated)
      {
        $result = \thrift_protocol_read_compact($this->input_, '\fixtures\basic\FB303Service_simple_rpc_result', Shapes::idx($options, 'read_options', 0));
      }
      else
      {
        $rseqid = 0;
        $fname = '';
        $mtype = 0;

        $this->input_->readMessageBegin(
          inout $fname,
          inout $mtype,
          inout $rseqid,
        );
        if ($mtype === \TMessageType::EXCEPTION) {
          $x = new \TApplicationException();
          $x->read($this->input_);
          $this->input_->readMessageEnd();
          throw $x;
        }
        $result = \fixtures\basic\FB303Service_simple_rpc_result::withDefaultValues();
        $result->read($this->input_);
        $this->input_->readMessageEnd();
        if ($expectedsequenceid !== null && ($rseqid !== $expectedsequenceid)) {
          throw new \TProtocolException("simple_rpc failed: sequence id is out of order");
        }
      }
    } catch (\THandlerShortCircuitException $ex) {
      switch ($ex->resultType) {
        case \THandlerShortCircuitException::R_EXPECTED_EX:
          $this->eventHandler_->recvException('simple_rpc', $expectedsequenceid, $ex->result);
          throw $ex->result;
        case \THandlerShortCircuitException::R_UNEXPECTED_EX:
          $this->eventHandler_->recvError('simple_rpc', $expectedsequenceid, $ex->result);
          throw $ex->result;
        case \THandlerShortCircuitException::R_SUCCESS:
        default:
          $this->eventHandler_->postRecv('simple_rpc', $expectedsequenceid, $ex->result);
          return $ex->result;
      }
    } catch (\Exception $ex) {
      $this->eventHandler_->recvError('simple_rpc', $expectedsequenceid, $ex);
      throw $ex;
    }
    if ($result->success !== null) {
      $success = $result->success;
      $this->eventHandler_->postRecv('simple_rpc', $expectedsequenceid, $success);
      return $success;
    }
    $x = new \TApplicationException("simple_rpc failed: unknown result", \TApplicationException::MISSING_RESULT);
    $this->eventHandler_->recvError('simple_rpc', $expectedsequenceid, $x);
    throw $x;
  }

}

class FB303ServiceAsyncClient extends \ThriftClientBase implements FB303ServiceAsyncClientIf {
  use FB303ServiceClientBase;

  /**
   * Original thrift definition:-
   * ReservedKeyword
   *   simple_rpc(1: i32 int_parameter);
   */
  public async function simple_rpc(int $int_parameter): Awaitable<\fixtures\basic\ReservedKeyword> {
    $hh_frame_metadata = $this->getHHFrameMetadata();
    if ($hh_frame_metadata !== null) {
      \HH\set_frame_metadata($hh_frame_metadata);
    }
    $rpc_options = $this->getAndResetOptions() ?? \ThriftClientBase::defaultOptions();
    await $this->asyncHandler_->genBefore("FB303Service", "simple_rpc");
    $args = \fixtures\basic\FB303Service_simple_rpc_args::fromShape(shape(
      'int_parameter' => $int_parameter,
    ));
    $currentseqid = $this->sendImplHelper($args, "simple_rpc", false);
    $channel = $this->channel_;
    $out_transport = $this->output_->getTransport();
    $in_transport = $this->input_->getTransport();
    if ($channel !== null && $out_transport is \TMemoryBuffer && $in_transport is \TMemoryBuffer) {
      $msg = $out_transport->getBuffer();
      $out_transport->resetBuffer();
      list($result_msg, $_read_headers) = await $channel->genSendRequestResponse($rpc_options, $msg);
      $in_transport->resetBuffer();
      $in_transport->write($result_msg);
    } else {
      await $this->asyncHandler_->genWait($currentseqid);
    }
    $response = $this->recvImpl_simple_rpc($currentseqid);
    await $this->asyncHandler_->genAfter();
    return $response;
  }

}

class FB303ServiceClient extends \ThriftClientBase implements FB303ServiceClientIf {
  use FB303ServiceClientBase;

  /**
   * Original thrift definition:-
   * ReservedKeyword
   *   simple_rpc(1: i32 int_parameter);
   */
  public async function simple_rpc(int $int_parameter): Awaitable<\fixtures\basic\ReservedKeyword> {
    $hh_frame_metadata = $this->getHHFrameMetadata();
    if ($hh_frame_metadata !== null) {
      \HH\set_frame_metadata($hh_frame_metadata);
    }
    $rpc_options = $this->getAndResetOptions() ?? \ThriftClientBase::defaultOptions();
    await $this->asyncHandler_->genBefore("FB303Service", "simple_rpc");
    $args = \fixtures\basic\FB303Service_simple_rpc_args::fromShape(shape(
      'int_parameter' => $int_parameter,
    ));
    $currentseqid = $this->sendImplHelper($args, "simple_rpc", false);
    $channel = $this->channel_;
    $out_transport = $this->output_->getTransport();
    $in_transport = $this->input_->getTransport();
    if ($channel !== null && $out_transport is \TMemoryBuffer && $in_transport is \TMemoryBuffer) {
      $msg = $out_transport->getBuffer();
      $out_transport->resetBuffer();
      list($result_msg, $_read_headers) = await $channel->genSendRequestResponse($rpc_options, $msg);
      $in_transport->resetBuffer();
      $in_transport->write($result_msg);
    } else {
      await $this->asyncHandler_->genWait($currentseqid);
    }
    $response = $this->recvImpl_simple_rpc($currentseqid);
    await $this->asyncHandler_->genAfter();
    return $response;
  }

  /* send and recv functions */
  public function send_simple_rpc(int $int_parameter): int {
    $args = \fixtures\basic\FB303Service_simple_rpc_args::fromShape(shape(
      'int_parameter' => $int_parameter,
    ));
    return $this->sendImplHelper($args, "simple_rpc", false);
  }
  public function recv_simple_rpc(?int $expectedsequenceid = null): \fixtures\basic\ReservedKeyword {
    return $this->recvImpl_simple_rpc($expectedsequenceid);
  }
}

abstract class FB303ServiceAsyncProcessorBase extends \ThriftAsyncProcessor {
  abstract const type TThriftIf as FB303ServiceAsyncIf;
  const classname<\IThriftServiceStaticMetadata> SERVICE_METADATA_CLASS = FB303ServiceStaticMetadata::class;

  protected async function process_simple_rpc(int $seqid, \TProtocol $input, \TProtocol $output): Awaitable<void> {
    $handler_ctx = $this->eventHandler_->getHandlerContext('simple_rpc');
    $reply_type = \TMessageType::REPLY;

    $this->eventHandler_->preRead($handler_ctx, 'simple_rpc', dict[]);

    if ($input is \TBinaryProtocolAccelerated) {
      $args = \thrift_protocol_read_binary_struct($input, '\fixtures\basic\FB303Service_simple_rpc_args');
    } else if ($input is \TCompactProtocolAccelerated) {
      $args = \thrift_protocol_read_compact_struct($input, '\fixtures\basic\FB303Service_simple_rpc_args');
    } else {
      $args = \fixtures\basic\FB303Service_simple_rpc_args::withDefaultValues();
      $args->read($input);
    }
    $input->readMessageEnd();
    $this->eventHandler_->postRead($handler_ctx, 'simple_rpc', $args);
    $result = \fixtures\basic\FB303Service_simple_rpc_result::withDefaultValues();
    try {
      $this->eventHandler_->preExec($handler_ctx, '\fixtures\basic\FB303Service', 'simple_rpc', $args);
      $result->success = await $this->handler->simple_rpc($args->int_parameter);
      $this->eventHandler_->postExec($handler_ctx, 'simple_rpc', $result);
    } catch (\Exception $ex) {
      $reply_type = \TMessageType::EXCEPTION;
      $this->eventHandler_->handlerError($handler_ctx, 'simple_rpc', $ex);
      $result = new \TApplicationException($ex->getMessage()."\n".$ex->getTraceAsString());
    }
    $this->eventHandler_->preWrite($handler_ctx, 'simple_rpc', $result);
    if ($output is \TBinaryProtocolAccelerated)
    {
      \thrift_protocol_write_binary($output, 'simple_rpc', $reply_type, $result, $seqid, $output->isStrictWrite());
    }
    else if ($output is \TCompactProtocolAccelerated)
    {
      \thrift_protocol_write_compact($output, 'simple_rpc', $reply_type, $result, $seqid);
    }
    else
    {
      $output->writeMessageBegin("simple_rpc", $reply_type, $seqid);
      $result->write($output);
      $output->writeMessageEnd();
      $output->getTransport()->flush();
    }
    $this->eventHandler_->postWrite($handler_ctx, 'simple_rpc', $result);
  }
  protected async function process_getThriftServiceMetadata(int $seqid, \TProtocol $input, \TProtocol $output): Awaitable<void> {
    $reply_type = \TMessageType::REPLY;

    if ($input is \TBinaryProtocolAccelerated) {
      $args = \thrift_protocol_read_binary_struct($input, '\tmeta_ThriftMetadataService_getThriftServiceMetadata_args');
    } else if ($input is \TCompactProtocolAccelerated) {
      $args = \thrift_protocol_read_compact_struct($input, '\tmeta_ThriftMetadataService_getThriftServiceMetadata_args');
    } else {
      $args = \tmeta_ThriftMetadataService_getThriftServiceMetadata_args::withDefaultValues();
      $args->read($input);
    }
    $input->readMessageEnd();
    $result = \tmeta_ThriftMetadataService_getThriftServiceMetadata_result::withDefaultValues();
    try {
      $result->success = FB303ServiceStaticMetadata::getServiceMetadataResponse();
    } catch (\Exception $ex) {
      $reply_type = \TMessageType::EXCEPTION;
      $result = new \TApplicationException($ex->getMessage()."\n".$ex->getTraceAsString());
    }
    if ($output is \TBinaryProtocolAccelerated)
    {
      \thrift_protocol_write_binary($output, 'getThriftServiceMetadata', $reply_type, $result, $seqid, $output->isStrictWrite());
    }
    else if ($output is \TCompactProtocolAccelerated)
    {
      \thrift_protocol_write_compact($output, 'getThriftServiceMetadata', $reply_type, $result, $seqid);
    }
    else
    {
      $output->writeMessageBegin("getThriftServiceMetadata", $reply_type, $seqid);
      $result->write($output);
      $output->writeMessageEnd();
      $output->getTransport()->flush();
    }
  }
}
class FB303ServiceAsyncProcessor extends FB303ServiceAsyncProcessorBase {
  const type TThriftIf = FB303ServiceAsyncIf;
}

abstract class FB303ServiceSyncProcessorBase extends \ThriftSyncProcessor {
  abstract const type TThriftIf as FB303ServiceIf;
  const classname<\IThriftServiceStaticMetadata> SERVICE_METADATA_CLASS = FB303ServiceStaticMetadata::class;

  protected function process_simple_rpc(int $seqid, \TProtocol $input, \TProtocol $output): void {
    $handler_ctx = $this->eventHandler_->getHandlerContext('simple_rpc');
    $reply_type = \TMessageType::REPLY;

    $this->eventHandler_->preRead($handler_ctx, 'simple_rpc', dict[]);

    if ($input is \TBinaryProtocolAccelerated) {
      $args = \thrift_protocol_read_binary_struct($input, '\fixtures\basic\FB303Service_simple_rpc_args');
    } else if ($input is \TCompactProtocolAccelerated) {
      $args = \thrift_protocol_read_compact_struct($input, '\fixtures\basic\FB303Service_simple_rpc_args');
    } else {
      $args = \fixtures\basic\FB303Service_simple_rpc_args::withDefaultValues();
      $args->read($input);
    }
    $input->readMessageEnd();
    $this->eventHandler_->postRead($handler_ctx, 'simple_rpc', $args);
    $result = \fixtures\basic\FB303Service_simple_rpc_result::withDefaultValues();
    try {
      $this->eventHandler_->preExec($handler_ctx, '\fixtures\basic\FB303Service', 'simple_rpc', $args);
      $result->success = $this->handler->simple_rpc($args->int_parameter);
      $this->eventHandler_->postExec($handler_ctx, 'simple_rpc', $result);
    } catch (\Exception $ex) {
      $reply_type = \TMessageType::EXCEPTION;
      $this->eventHandler_->handlerError($handler_ctx, 'simple_rpc', $ex);
      $result = new \TApplicationException($ex->getMessage()."\n".$ex->getTraceAsString());
    }
    $this->eventHandler_->preWrite($handler_ctx, 'simple_rpc', $result);
    if ($output is \TBinaryProtocolAccelerated)
    {
      \thrift_protocol_write_binary($output, 'simple_rpc', $reply_type, $result, $seqid, $output->isStrictWrite());
    }
    else if ($output is \TCompactProtocolAccelerated)
    {
      \thrift_protocol_write_compact($output, 'simple_rpc', $reply_type, $result, $seqid);
    }
    else
    {
      $output->writeMessageBegin("simple_rpc", $reply_type, $seqid);
      $result->write($output);
      $output->writeMessageEnd();
      $output->getTransport()->flush();
    }
    $this->eventHandler_->postWrite($handler_ctx, 'simple_rpc', $result);
  }
  protected function process_getThriftServiceMetadata(int $seqid, \TProtocol $input, \TProtocol $output): void {
    $reply_type = \TMessageType::REPLY;

    if ($input is \TBinaryProtocolAccelerated) {
      $args = \thrift_protocol_read_binary_struct($input, '\tmeta_ThriftMetadataService_getThriftServiceMetadata_args');
    } else if ($input is \TCompactProtocolAccelerated) {
      $args = \thrift_protocol_read_compact_struct($input, '\tmeta_ThriftMetadataService_getThriftServiceMetadata_args');
    } else {
      $args = \tmeta_ThriftMetadataService_getThriftServiceMetadata_args::withDefaultValues();
      $args->read($input);
    }
    $input->readMessageEnd();
    $result = \tmeta_ThriftMetadataService_getThriftServiceMetadata_result::withDefaultValues();
    try {
      $result->success = FB303ServiceStaticMetadata::getServiceMetadataResponse();
    } catch (\Exception $ex) {
      $reply_type = \TMessageType::EXCEPTION;
      $result = new \TApplicationException($ex->getMessage()."\n".$ex->getTraceAsString());
    }
    if ($output is \TBinaryProtocolAccelerated)
    {
      \thrift_protocol_write_binary($output, 'getThriftServiceMetadata', $reply_type, $result, $seqid, $output->isStrictWrite());
    }
    else if ($output is \TCompactProtocolAccelerated)
    {
      \thrift_protocol_write_compact($output, 'getThriftServiceMetadata', $reply_type, $result, $seqid);
    }
    else
    {
      $output->writeMessageBegin("getThriftServiceMetadata", $reply_type, $seqid);
      $result->write($output);
      $output->writeMessageEnd();
      $output->getTransport()->flush();
    }
  }
}
class FB303ServiceSyncProcessor extends FB303ServiceSyncProcessorBase {
  const type TThriftIf = FB303ServiceIf;
}
// For backwards compatibility
class FB303ServiceProcessor extends FB303ServiceSyncProcessor {}

// HELPER FUNCTIONS AND STRUCTURES

class FB303Service_simple_rpc_args implements \IThriftSyncStruct, \IThriftShapishSyncStruct {
  use \ThriftSerializationTrait;

  const dict<int, this::TFieldSpec> SPEC = dict[
    1 => shape(
      'var' => 'int_parameter',
      'type' => \TType::I32,
    ),
  ];
  const dict<string, int> FIELDMAP = dict[
    'int_parameter' => 1,
  ];

  const type TConstructorShape = shape(
    ?'int_parameter' => ?int,
  );

  const type TShape = shape(
    'int_parameter' => int,
    ...
  );
  const int STRUCTURAL_ID = 3607165688153615571;
  public int $int_parameter;

  public function __construct(?int $int_parameter = null  )[] {
    $this->int_parameter = $int_parameter ?? 0;
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
      Shapes::idx($shape, 'int_parameter'),
    );
  }

  public function getName()[]: string {
    return 'FB303Service_simple_rpc_args';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return \tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "module.simple_rpc_args",
        "fields" => vec[
          \tmeta_ThriftField::fromShape(
            shape(
              "id" => 1,
              "type" => \tmeta_ThriftType::fromShape(
                shape(
                  "t_primitive" => \tmeta_ThriftPrimitiveType::THRIFT_I32_TYPE,
                )
              ),
              "name" => "int_parameter",
            )
          ),
        ],
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[]: \TStructAnnotations {
    return shape(
      'struct' => dict[],
      'fields' => dict[
        'int_parameter' => shape(
          'field' => dict[
            '\facebook\thrift\annotation\Name' => \facebook\thrift\annotation\Name::fromShape(
              shape(
                "name" => "renamed_parameter",
              )
            ),
          ],
          'type' => dict[],
        ),
      ],
    );
  }

  public static function __fromShape(self::TShape $shape)[]: this {
    return new static(
      $shape['int_parameter'],
    );
  }

  public function __toShape()[]: self::TShape {
    return shape(
      'int_parameter' => $this->int_parameter,
    );
  }
  public function getInstanceKey()[write_props]: string {
    return \TCompactSerializer::serialize($this);
  }

  public function readFromJson(string $jsonText): void {
    $parsed = json_decode($jsonText, true);

    if ($parsed === null || !($parsed is KeyedContainer<_, _>)) {
      throw new \TProtocolException("Cannot parse the given json string.");
    }

    if (idx($parsed, 'int_parameter') !== null) {
      $_tmp0 = (int)/* HH_FIXME[4110] */ $parsed['int_parameter'];
      if ($_tmp0 > 0x7fffffff) {
        throw new \TProtocolException("number exceeds limit in field");
      } else {
        $this->int_parameter = (int)$_tmp0;
      }
    }    
  }

}

class FB303Service_simple_rpc_result implements \IThriftSyncStruct {
  use \ThriftSerializationTrait;

  const dict<int, this::TFieldSpec> SPEC = dict[
    0 => shape(
      'var' => 'success',
      'type' => \TType::STRUCT,
      'class' => \fixtures\basic\ReservedKeyword::class,
    ),
  ];
  const dict<string, int> FIELDMAP = dict[
    'success' => 0,
  ];

  const type TConstructorShape = shape(
    ?'success' => ?\fixtures\basic\ReservedKeyword,
  );

  const int STRUCTURAL_ID = 7443966475393398575;
  public ?\fixtures\basic\ReservedKeyword $success;

  public function __construct(?\fixtures\basic\ReservedKeyword $success = null  )[] {
    $this->success = $success;
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
      Shapes::idx($shape, 'success'),
    );
  }

  public function getName()[]: string {
    return 'FB303Service_simple_rpc_result';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return \tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "module.FB303Service_simple_rpc_result",
        "fields" => vec[
          \tmeta_ThriftField::fromShape(
            shape(
              "id" => 0,
              "type" => \tmeta_ThriftType::fromShape(
                shape(
                  "t_struct" => \tmeta_ThriftStructType::fromShape(
                    shape(
                      "name" => "module.ReservedKeyword",
                    )
                  ),
                )
              ),
              "name" => "success",
            )
          ),
        ],
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[]: \TStructAnnotations {
    return shape(
      'struct' => dict[],
      'fields' => dict[
        'success' => shape(
          'field' => dict[],
          'type' => dict[
            '\facebook\thrift\annotation\Name' => \facebook\thrift\annotation\Name::fromShape(
              shape(
                "name" => "MyRenamedStruct",
              )
            ),
          ],
        ),
      ],
    );
  }

  public function getInstanceKey()[write_props]: string {
    return \TCompactSerializer::serialize($this);
  }

  public function readFromJson(string $jsonText): void {
    $parsed = json_decode($jsonText, true);

    if ($parsed === null || !($parsed is KeyedContainer<_, _>)) {
      throw new \TProtocolException("Cannot parse the given json string.");
    }

    if (idx($parsed, 'success') !== null) {
      $_tmp0 = json_encode(/* HH_FIXME[4110] */ $parsed['success']);
      $_tmp1 = \fixtures\basic\ReservedKeyword::withDefaultValues();
      $_tmp1->readFromJson($_tmp0);
      $this->success = $_tmp1;
    }    
  }

}

class FB303ServiceStaticMetadata implements \IThriftServiceStaticMetadata {
  public static function getServiceMetadata()[]: \tmeta_ThriftService {
    return \tmeta_ThriftService::fromShape(
      shape(
        "name" => "module.FB303Service",
        "functions" => vec[
          \tmeta_ThriftFunction::fromShape(
            shape(
              "name" => "simple_rpc",
              "return_type" => \tmeta_ThriftType::fromShape(
                shape(
                  "t_struct" => \tmeta_ThriftStructType::fromShape(
                    shape(
                      "name" => "module.ReservedKeyword",
                    )
                  ),
                )
              ),
              "arguments" => vec[
                \tmeta_ThriftField::fromShape(
                  shape(
                    "id" => 1,
                    "type" => \tmeta_ThriftType::fromShape(
                      shape(
                        "t_primitive" => \tmeta_ThriftPrimitiveType::THRIFT_I32_TYPE,
                      )
                    ),
                    "name" => "int_parameter",
                  )
                ),
              ],
            )
          ),
        ],
      )
    );
  }

  public static function getServiceMetadataResponse()[]: \tmeta_ThriftServiceMetadataResponse {
    return \tmeta_ThriftServiceMetadataResponse::fromShape(
      shape(
        'context' => \tmeta_ThriftServiceContext::fromShape(
          shape(
            'service_info' => self::getServiceMetadata(),
            'module' => \tmeta_ThriftModuleContext::fromShape(
              shape(
                'name' => 'module',
              )
            ),
          )
        ),
        'metadata' => \tmeta_ThriftMetadata::fromShape(
          shape(
            'enums' => dict[
            ],
            'structs' => dict[
              'module.ReservedKeyword' => \fixtures\basic\ReservedKeyword::getStructMetadata(),
            ],
            'exceptions' => dict[
            ],
            'services' => dict[
            ],
          )
        ),
      )
    );
  }

  public static function getAllStructuredAnnotations()[]: \TServiceAnnotations {
    return shape(
      'service' => dict[],
      'functions' => dict[
        'simple_rpc' => dict[
          '\facebook\thrift\annotation\Name' => \facebook\thrift\annotation\Name::fromShape(
            shape(
              "name" => "renamed_rpc",
            )
          ),
        ],
      ],
    );
  }
}

