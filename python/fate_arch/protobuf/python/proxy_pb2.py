# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import basic_meta_pb2 as basic__meta__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proxy.proto',
  package='com.webank.ai.eggroll.api.networking.proxy',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0bproxy.proto\x12*com.webank.ai.eggroll.api.networking.proxy\x1a\x10\x62\x61sic-meta.proto\"&\n\x05Model\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x61taKey\x18\x02 \x01(\t\"X\n\x04Task\x12\x0e\n\x06taskId\x18\x01 \x01(\t\x12@\n\x05model\x18\x02 \x01(\x0b\x32\x31.com.webank.ai.eggroll.api.networking.proxy.Model\"p\n\x05Topic\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07partyId\x18\x02 \x01(\t\x12\x0c\n\x04role\x18\x03 \x01(\t\x12:\n\x08\x63\x61llback\x18\x04 \x01(\x0b\x32(.com.webank.ai.eggroll.api.core.Endpoint\"\x17\n\x07\x43ommand\x12\x0c\n\x04name\x18\x01 \x01(\t\"p\n\x04\x43onf\x12\x16\n\x0eoverallTimeout\x18\x01 \x01(\x03\x12\x1d\n\x15\x63ompletionWaitTimeout\x18\x02 \x01(\x03\x12\x1d\n\x15packetIntervalTimeout\x18\x03 \x01(\x03\x12\x12\n\nmaxRetries\x18\x04 \x01(\x05\"\x9a\x03\n\x08Metadata\x12>\n\x04task\x18\x01 \x01(\x0b\x32\x30.com.webank.ai.eggroll.api.networking.proxy.Task\x12>\n\x03src\x18\x02 \x01(\x0b\x32\x31.com.webank.ai.eggroll.api.networking.proxy.Topic\x12>\n\x03\x64st\x18\x03 \x01(\x0b\x32\x31.com.webank.ai.eggroll.api.networking.proxy.Topic\x12\x44\n\x07\x63ommand\x18\x04 \x01(\x0b\x32\x33.com.webank.ai.eggroll.api.networking.proxy.Command\x12\x10\n\x08operator\x18\x05 \x01(\t\x12\x0b\n\x03seq\x18\x06 \x01(\x03\x12\x0b\n\x03\x61\x63k\x18\x07 \x01(\x03\x12>\n\x04\x63onf\x18\x08 \x01(\x0b\x32\x30.com.webank.ai.eggroll.api.networking.proxy.Conf\x12\x0b\n\x03\x65xt\x18\t \x01(\x0c\x12\x0f\n\x07version\x18\x64 \x01(\t\"\"\n\x04\x44\x61ta\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"\x8e\x01\n\x06Packet\x12\x44\n\x06header\x18\x01 \x01(\x0b\x32\x34.com.webank.ai.eggroll.api.networking.proxy.Metadata\x12>\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x30.com.webank.ai.eggroll.api.networking.proxy.Data\"\xa3\x01\n\x11HeartbeatResponse\x12\x44\n\x06header\x18\x01 \x01(\x0b\x32\x34.com.webank.ai.eggroll.api.networking.proxy.Metadata\x12H\n\toperation\x18\x02 \x01(\x0e\x32\x35.com.webank.ai.eggroll.api.networking.proxy.Operation\"\xb7\x01\n\x0cPollingFrame\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0b\n\x03seq\x18\x02 \x01(\x03\x12\x46\n\x08metadata\x18\n \x01(\x0b\x32\x34.com.webank.ai.eggroll.api.networking.proxy.Metadata\x12\x42\n\x06packet\x18\x14 \x01(\x0b\x32\x32.com.webank.ai.eggroll.api.networking.proxy.Packet*O\n\tOperation\x12\t\n\x05START\x10\x00\x12\x07\n\x03RUN\x10\x01\x12\x08\n\x04STOP\x10\x02\x12\x08\n\x04KILL\x10\x03\x12\x0c\n\x08GET_DATA\x10\x04\x12\x0c\n\x08PUT_DATA\x10\x05\x32\xf6\x03\n\x13\x44\x61taTransferService\x12r\n\x04push\x12\x32.com.webank.ai.eggroll.api.networking.proxy.Packet\x1a\x34.com.webank.ai.eggroll.api.networking.proxy.Metadata(\x01\x12r\n\x04pull\x12\x34.com.webank.ai.eggroll.api.networking.proxy.Metadata\x1a\x32.com.webank.ai.eggroll.api.networking.proxy.Packet0\x01\x12s\n\tunaryCall\x12\x32.com.webank.ai.eggroll.api.networking.proxy.Packet\x1a\x32.com.webank.ai.eggroll.api.networking.proxy.Packet\x12\x81\x01\n\x07polling\x12\x38.com.webank.ai.eggroll.api.networking.proxy.PollingFrame\x1a\x38.com.webank.ai.eggroll.api.networking.proxy.PollingFrame(\x01\x30\x01\x32t\n\x0cRouteService\x12\x64\n\x05query\x12\x31.com.webank.ai.eggroll.api.networking.proxy.Topic\x1a(.com.webank.ai.eggroll.api.core.Endpointb\x06proto3'
  ,
  dependencies=[basic__meta__pb2.DESCRIPTOR,])

_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='com.webank.ai.eggroll.api.networking.proxy.Operation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='START', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KILL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_DATA', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUT_DATA', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1406,
  serialized_end=1485,
)
_sym_db.RegisterEnumDescriptor(_OPERATION)

Operation = enum_type_wrapper.EnumTypeWrapper(_OPERATION)
START = 0
RUN = 1
STOP = 2
KILL = 3
GET_DATA = 4
PUT_DATA = 5



_MODEL = _descriptor.Descriptor(
  name='Model',
  full_name='com.webank.ai.eggroll.api.networking.proxy.Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='com.webank.ai.eggroll.api.networking.proxy.Model.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataKey', full_name='com.webank.ai.eggroll.api.networking.proxy.Model.dataKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=115,
)


_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='com.webank.ai.eggroll.api.networking.proxy.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='com.webank.ai.eggroll.api.networking.proxy.Task.taskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='com.webank.ai.eggroll.api.networking.proxy.Task.model', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=205,
)


_TOPIC = _descriptor.Descriptor(
  name='Topic',
  full_name='com.webank.ai.eggroll.api.networking.proxy.Topic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='com.webank.ai.eggroll.api.networking.proxy.Topic.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partyId', full_name='com.webank.ai.eggroll.api.networking.proxy.Topic.partyId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='com.webank.ai.eggroll.api.networking.proxy.Topic.role', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callback', full_name='com.webank.ai.eggroll.api.networking.proxy.Topic.callback', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=207,
  serialized_end=319,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='com.webank.ai.eggroll.api.networking.proxy.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='com.webank.ai.eggroll.api.networking.proxy.Command.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=344,
)


_CONF = _descriptor.Descriptor(
  name='Conf',
  full_name='com.webank.ai.eggroll.api.networking.proxy.Conf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='overallTimeout', full_name='com.webank.ai.eggroll.api.networking.proxy.Conf.overallTimeout', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='completionWaitTimeout', full_name='com.webank.ai.eggroll.api.networking.proxy.Conf.completionWaitTimeout', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packetIntervalTimeout', full_name='com.webank.ai.eggroll.api.networking.proxy.Conf.packetIntervalTimeout', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxRetries', full_name='com.webank.ai.eggroll.api.networking.proxy.Conf.maxRetries', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=458,
)


_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='com.webank.ai.eggroll.api.networking.proxy.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='com.webank.ai.eggroll.api.networking.proxy.Metadata.task', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src', full_name='com.webank.ai.eggroll.api.networking.proxy.Metadata.src', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dst', full_name='com.webank.ai.eggroll.api.networking.proxy.Metadata.dst', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command', full_name='com.webank.ai.eggroll.api.networking.proxy.Metadata.command', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operator', full_name='com.webank.ai.eggroll.api.networking.proxy.Metadata.operator', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq', full_name='com.webank.ai.eggroll.api.networking.proxy.Metadata.seq', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ack', full_name='com.webank.ai.eggroll.api.networking.proxy.Metadata.ack', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conf', full_name='com.webank.ai.eggroll.api.networking.proxy.Metadata.conf', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ext', full_name='com.webank.ai.eggroll.api.networking.proxy.Metadata.ext', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='com.webank.ai.eggroll.api.networking.proxy.Metadata.version', index=9,
      number=100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=461,
  serialized_end=871,
)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='com.webank.ai.eggroll.api.networking.proxy.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.eggroll.api.networking.proxy.Data.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.eggroll.api.networking.proxy.Data.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=873,
  serialized_end=907,
)


_PACKET = _descriptor.Descriptor(
  name='Packet',
  full_name='com.webank.ai.eggroll.api.networking.proxy.Packet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='com.webank.ai.eggroll.api.networking.proxy.Packet.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='com.webank.ai.eggroll.api.networking.proxy.Packet.body', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=910,
  serialized_end=1052,
)


_HEARTBEATRESPONSE = _descriptor.Descriptor(
  name='HeartbeatResponse',
  full_name='com.webank.ai.eggroll.api.networking.proxy.HeartbeatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='com.webank.ai.eggroll.api.networking.proxy.HeartbeatResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='com.webank.ai.eggroll.api.networking.proxy.HeartbeatResponse.operation', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1055,
  serialized_end=1218,
)


_POLLINGFRAME = _descriptor.Descriptor(
  name='PollingFrame',
  full_name='com.webank.ai.eggroll.api.networking.proxy.PollingFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='com.webank.ai.eggroll.api.networking.proxy.PollingFrame.method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq', full_name='com.webank.ai.eggroll.api.networking.proxy.PollingFrame.seq', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='com.webank.ai.eggroll.api.networking.proxy.PollingFrame.metadata', index=2,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packet', full_name='com.webank.ai.eggroll.api.networking.proxy.PollingFrame.packet', index=3,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1221,
  serialized_end=1404,
)

_TASK.fields_by_name['model'].message_type = _MODEL
_TOPIC.fields_by_name['callback'].message_type = basic__meta__pb2._ENDPOINT
_METADATA.fields_by_name['task'].message_type = _TASK
_METADATA.fields_by_name['src'].message_type = _TOPIC
_METADATA.fields_by_name['dst'].message_type = _TOPIC
_METADATA.fields_by_name['command'].message_type = _COMMAND
_METADATA.fields_by_name['conf'].message_type = _CONF
_PACKET.fields_by_name['header'].message_type = _METADATA
_PACKET.fields_by_name['body'].message_type = _DATA
_HEARTBEATRESPONSE.fields_by_name['header'].message_type = _METADATA
_HEARTBEATRESPONSE.fields_by_name['operation'].enum_type = _OPERATION
_POLLINGFRAME.fields_by_name['metadata'].message_type = _METADATA
_POLLINGFRAME.fields_by_name['packet'].message_type = _PACKET
DESCRIPTOR.message_types_by_name['Model'] = _MODEL
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['Topic'] = _TOPIC
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Conf'] = _CONF
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['Packet'] = _PACKET
DESCRIPTOR.message_types_by_name['HeartbeatResponse'] = _HEARTBEATRESPONSE
DESCRIPTOR.message_types_by_name['PollingFrame'] = _POLLINGFRAME
DESCRIPTOR.enum_types_by_name['Operation'] = _OPERATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), {
  'DESCRIPTOR' : _MODEL,
  '__module__' : 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.Model)
  })
_sym_db.RegisterMessage(Model)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
  'DESCRIPTOR' : _TASK,
  '__module__' : 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.Task)
  })
_sym_db.RegisterMessage(Task)

Topic = _reflection.GeneratedProtocolMessageType('Topic', (_message.Message,), {
  'DESCRIPTOR' : _TOPIC,
  '__module__' : 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.Topic)
  })
_sym_db.RegisterMessage(Topic)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.Command)
  })
_sym_db.RegisterMessage(Command)

Conf = _reflection.GeneratedProtocolMessageType('Conf', (_message.Message,), {
  'DESCRIPTOR' : _CONF,
  '__module__' : 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.Conf)
  })
_sym_db.RegisterMessage(Conf)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.Metadata)
  })
_sym_db.RegisterMessage(Metadata)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
  'DESCRIPTOR' : _DATA,
  '__module__' : 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.Data)
  })
_sym_db.RegisterMessage(Data)

Packet = _reflection.GeneratedProtocolMessageType('Packet', (_message.Message,), {
  'DESCRIPTOR' : _PACKET,
  '__module__' : 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.Packet)
  })
_sym_db.RegisterMessage(Packet)

HeartbeatResponse = _reflection.GeneratedProtocolMessageType('HeartbeatResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATRESPONSE,
  '__module__' : 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.HeartbeatResponse)
  })
_sym_db.RegisterMessage(HeartbeatResponse)

PollingFrame = _reflection.GeneratedProtocolMessageType('PollingFrame', (_message.Message,), {
  'DESCRIPTOR' : _POLLINGFRAME,
  '__module__' : 'proxy_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.networking.proxy.PollingFrame)
  })
_sym_db.RegisterMessage(PollingFrame)



_DATATRANSFERSERVICE = _descriptor.ServiceDescriptor(
  name='DataTransferService',
  full_name='com.webank.ai.eggroll.api.networking.proxy.DataTransferService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1488,
  serialized_end=1990,
  methods=[
  _descriptor.MethodDescriptor(
    name='push',
    full_name='com.webank.ai.eggroll.api.networking.proxy.DataTransferService.push',
    index=0,
    containing_service=None,
    input_type=_PACKET,
    output_type=_METADATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='pull',
    full_name='com.webank.ai.eggroll.api.networking.proxy.DataTransferService.pull',
    index=1,
    containing_service=None,
    input_type=_METADATA,
    output_type=_PACKET,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='unaryCall',
    full_name='com.webank.ai.eggroll.api.networking.proxy.DataTransferService.unaryCall',
    index=2,
    containing_service=None,
    input_type=_PACKET,
    output_type=_PACKET,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='polling',
    full_name='com.webank.ai.eggroll.api.networking.proxy.DataTransferService.polling',
    index=3,
    containing_service=None,
    input_type=_POLLINGFRAME,
    output_type=_POLLINGFRAME,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATATRANSFERSERVICE)

DESCRIPTOR.services_by_name['DataTransferService'] = _DATATRANSFERSERVICE


_ROUTESERVICE = _descriptor.ServiceDescriptor(
  name='RouteService',
  full_name='com.webank.ai.eggroll.api.networking.proxy.RouteService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=1992,
  serialized_end=2108,
  methods=[
  _descriptor.MethodDescriptor(
    name='query',
    full_name='com.webank.ai.eggroll.api.networking.proxy.RouteService.query',
    index=0,
    containing_service=None,
    input_type=_TOPIC,
    output_type=basic__meta__pb2._ENDPOINT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROUTESERVICE)

DESCRIPTOR.services_by_name['RouteService'] = _ROUTESERVICE

# @@protoc_insertion_point(module_scope)
