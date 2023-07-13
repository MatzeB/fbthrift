/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

package test.fixtures.refs;

import com.facebook.swift.codec.*;
import com.facebook.swift.codec.ThriftField.Requiredness;
import com.facebook.swift.codec.ThriftField.Recursiveness;
import com.google.common.collect.*;
import java.util.*;
import javax.annotation.Nullable;
import org.apache.thrift.*;
import org.apache.thrift.transport.*;
import org.apache.thrift.protocol.*;
import static com.google.common.base.MoreObjects.toStringHelper;
import static com.google.common.base.MoreObjects.ToStringHelper;

@SwiftGenerated
@com.facebook.swift.codec.ThriftStruct(value="StructWithTerseInternBox", builder=StructWithTerseInternBox.Builder.class)
public final class StructWithTerseInternBox implements com.facebook.thrift.payload.ThriftSerializable {
    @ThriftConstructor
    public StructWithTerseInternBox(
        @com.facebook.swift.codec.ThriftField(value=1, name="field1", requiredness=Requiredness.TERSE) final test.fixtures.refs.Empty field1,
        @com.facebook.swift.codec.ThriftField(value=2, name="field2", requiredness=Requiredness.TERSE) final test.fixtures.refs.MyField field2
    ) {
        this.field1 = field1;
        this.field2 = field2;
    }
    
    @ThriftConstructor
    protected StructWithTerseInternBox() {
      this.field1 = test.fixtures.refs.Empty.defaultInstance();
      this.field2 = test.fixtures.refs.MyField.defaultInstance();
    }
    
    public static class Builder {
        private test.fixtures.refs.Empty field1 = test.fixtures.refs.Empty.defaultInstance();
        private test.fixtures.refs.MyField field2 = test.fixtures.refs.MyField.defaultInstance();
    
        @com.facebook.swift.codec.ThriftField(value=1, name="field1", requiredness=Requiredness.TERSE)
        public Builder setField1(test.fixtures.refs.Empty field1) {
            this.field1 = field1;
            return this;
        }
    
        public test.fixtures.refs.Empty getField1() { return field1; }
    
            @com.facebook.swift.codec.ThriftField(value=2, name="field2", requiredness=Requiredness.TERSE)
        public Builder setField2(test.fixtures.refs.MyField field2) {
            this.field2 = field2;
            return this;
        }
    
        public test.fixtures.refs.MyField getField2() { return field2; }
    
        public Builder() { }
        public Builder(StructWithTerseInternBox other) {
            this.field1 = other.field1;
            this.field2 = other.field2;
        }
    
        @ThriftConstructor
        public StructWithTerseInternBox build() {
            StructWithTerseInternBox result = new StructWithTerseInternBox (
                this.field1,
                this.field2
            );
            return result;
        }
    }
        
    public static final Map<String, Integer> NAMES_TO_IDS = new HashMap();
    public static final Map<String, Integer> THRIFT_NAMES_TO_IDS = new HashMap();
    public static final Map<Integer, TField> FIELD_METADATA = new HashMap<>();
    private static final TStruct STRUCT_DESC = new TStruct("StructWithTerseInternBox");
    private final test.fixtures.refs.Empty field1;
    public static final int _FIELD1 = 1;
    private static final TField FIELD1_FIELD_DESC = new TField("field1", TType.STRUCT, (short)1);
        private final test.fixtures.refs.MyField field2;
    public static final int _FIELD2 = 2;
    private static final TField FIELD2_FIELD_DESC = new TField("field2", TType.STRUCT, (short)2);
    static {
      NAMES_TO_IDS.put("field1", 1);
      THRIFT_NAMES_TO_IDS.put("field1", 1);
      FIELD_METADATA.put(1, FIELD1_FIELD_DESC);
      NAMES_TO_IDS.put("field2", 2);
      THRIFT_NAMES_TO_IDS.put("field2", 2);
      FIELD_METADATA.put(2, FIELD2_FIELD_DESC);
    }
    
    @Nullable
    @com.facebook.swift.codec.ThriftField(value=1, name="field1", requiredness=Requiredness.TERSE)
    public test.fixtures.refs.Empty getField1() { return field1; }
    
    
    @Nullable
    @com.facebook.swift.codec.ThriftField(value=2, name="field2", requiredness=Requiredness.TERSE)
    public test.fixtures.refs.MyField getField2() { return field2; }
    
    @java.lang.Override
    public String toString() {
        ToStringHelper helper = toStringHelper(this);
        helper.add("field1", field1);
        helper.add("field2", field2);
        return helper.toString();
    }
    
    @java.lang.Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
    
        StructWithTerseInternBox other = (StructWithTerseInternBox)o;
    
        return
            Objects.equals(field1, other.field1) &&
            Objects.equals(field2, other.field2) &&
            true;
    }
    
    @java.lang.Override
    public int hashCode() {
        return Arrays.deepHashCode(new java.lang.Object[] {
            field1,
            field2
        });
    }
    
    
    public static com.facebook.thrift.payload.Reader<StructWithTerseInternBox> asReader() {
      return StructWithTerseInternBox::read0;
    }
    
    public static StructWithTerseInternBox read0(TProtocol oprot) throws TException {
      TField __field;
      oprot.readStructBegin(StructWithTerseInternBox.NAMES_TO_IDS, StructWithTerseInternBox.THRIFT_NAMES_TO_IDS, StructWithTerseInternBox.FIELD_METADATA);
      StructWithTerseInternBox.Builder builder = new StructWithTerseInternBox.Builder();
      while (true) {
        __field = oprot.readFieldBegin();
        if (__field.type == TType.STOP) { break; }
        switch (__field.id) {
        case _FIELD1:
          if (__field.type == TType.STRUCT) {
            test.fixtures.refs.Empty field1 = test.fixtures.refs.Empty.read0(oprot);
            builder.setField1(field1);
          } else {
            TProtocolUtil.skip(oprot, __field.type);
          }
          break;
        case _FIELD2:
          if (__field.type == TType.STRUCT) {
            test.fixtures.refs.MyField field2 = test.fixtures.refs.MyField.read0(oprot);
            builder.setField2(field2);
          } else {
            TProtocolUtil.skip(oprot, __field.type);
          }
          break;
        default:
          TProtocolUtil.skip(oprot, __field.type);
          break;
        }
        oprot.readFieldEnd();
      }
      oprot.readStructEnd();
      return builder.build();
    }
    
    public void write0(TProtocol oprot) throws TException {
      oprot.writeStructBegin(STRUCT_DESC);
      int structStart = 0;
      int pos = 0;
      com.facebook.thrift.protocol.ByteBufTProtocol p = (com.facebook.thrift.protocol.ByteBufTProtocol) oprot;
      java.util.Objects.requireNonNull(field1, "field1 must not be null");
      structStart = p.mark();
        oprot.writeFieldBegin(FIELD1_FIELD_DESC);
        pos = p.mark();
        this.field1.write0(oprot);
        if (p.mark() - pos > p.getEmptyStructSize()) {
          p.writeFieldEnd();    
        } else {
          p.rollback(structStart);
        }    
      java.util.Objects.requireNonNull(field2, "field2 must not be null");
      structStart = p.mark();
        oprot.writeFieldBegin(FIELD2_FIELD_DESC);
        pos = p.mark();
        this.field2.write0(oprot);
        if (p.mark() - pos > p.getEmptyStructSize()) {
          p.writeFieldEnd();    
        } else {
          p.rollback(structStart);
        }    
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }
    
    private static class _StructWithTerseInternBoxLazy {
        private static final StructWithTerseInternBox _DEFAULT = new StructWithTerseInternBox.Builder().build();
    }
    
    public static StructWithTerseInternBox defaultInstance() {
        return  _StructWithTerseInternBoxLazy._DEFAULT;
    }
}
