# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/tools/sensor_calibration/proto/extractor_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/tools/sensor_calibration/proto/extractor_config.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=modules/tools/sensor_calibration/proto/extractor_config.proto\"\xa2\x01\n\x08IoConfig\x12\x16\n\ttask_name\x18\x01 \x02(\t:\x03tmp\x12#\n\x0boutput_path\x18\x02 \x02(\t:\x0e\x65xtracted_data\x12\"\n\x0fstart_timestamp\x18\x03 \x01(\t:\tFLOAT_MIN\x12 \n\rend_timestamp\x18\x04 \x01(\t:\tFLOAT_MAX\x12\x13\n\x0bmain_sensor\x18\x05 \x01(\t\"P\n\rChannelConfig\x12\x15\n\x0b\x64\x65scription\x18\x01 \x01(\t:\x00\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x1a\n\x0f\x65xtraction_rate\x18\x03 \x02(\r:\x01\x31\"+\n\x08\x43hannels\x12\x1f\n\x07\x63hannel\x18\x01 \x03(\x0b\x32\x0e.ChannelConfig\"\x1e\n\x07Records\x12\x13\n\x0brecord_path\x18\x01 \x03(\t\"l\n\x14\x44\x61taExtractionConfig\x12\x1c\n\tio_config\x18\x01 \x02(\x0b\x32\t.IoConfig\x12\x1b\n\x08\x63hannels\x18\x02 \x02(\x0b\x32\t.Channels\x12\x19\n\x07records\x18\x03 \x02(\x0b\x32\x08.Records'
)




_IOCONFIG = _descriptor.Descriptor(
  name='IoConfig',
  full_name='IoConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_name', full_name='IoConfig.task_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=b"tmp".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_path', full_name='IoConfig.output_path', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=b"extracted_data".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='IoConfig.start_timestamp', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"FLOAT_MIN".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_timestamp', full_name='IoConfig.end_timestamp', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"FLOAT_MAX".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='main_sensor', full_name='IoConfig.main_sensor', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=228,
)


_CHANNELCONFIG = _descriptor.Descriptor(
  name='ChannelConfig',
  full_name='ChannelConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='ChannelConfig.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='ChannelConfig.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extraction_rate', full_name='ChannelConfig.extraction_rate', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=310,
)


_CHANNELS = _descriptor.Descriptor(
  name='Channels',
  full_name='Channels',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='Channels.channel', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=312,
  serialized_end=355,
)


_RECORDS = _descriptor.Descriptor(
  name='Records',
  full_name='Records',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='record_path', full_name='Records.record_path', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=357,
  serialized_end=387,
)


_DATAEXTRACTIONCONFIG = _descriptor.Descriptor(
  name='DataExtractionConfig',
  full_name='DataExtractionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='io_config', full_name='DataExtractionConfig.io_config', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channels', full_name='DataExtractionConfig.channels', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='records', full_name='DataExtractionConfig.records', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=389,
  serialized_end=497,
)

_CHANNELS.fields_by_name['channel'].message_type = _CHANNELCONFIG
_DATAEXTRACTIONCONFIG.fields_by_name['io_config'].message_type = _IOCONFIG
_DATAEXTRACTIONCONFIG.fields_by_name['channels'].message_type = _CHANNELS
_DATAEXTRACTIONCONFIG.fields_by_name['records'].message_type = _RECORDS
DESCRIPTOR.message_types_by_name['IoConfig'] = _IOCONFIG
DESCRIPTOR.message_types_by_name['ChannelConfig'] = _CHANNELCONFIG
DESCRIPTOR.message_types_by_name['Channels'] = _CHANNELS
DESCRIPTOR.message_types_by_name['Records'] = _RECORDS
DESCRIPTOR.message_types_by_name['DataExtractionConfig'] = _DATAEXTRACTIONCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IoConfig = _reflection.GeneratedProtocolMessageType('IoConfig', (_message.Message,), {
  'DESCRIPTOR' : _IOCONFIG,
  '__module__' : 'modules.tools.sensor_calibration.proto.extractor_config_pb2'
  # @@protoc_insertion_point(class_scope:IoConfig)
  })
_sym_db.RegisterMessage(IoConfig)

ChannelConfig = _reflection.GeneratedProtocolMessageType('ChannelConfig', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELCONFIG,
  '__module__' : 'modules.tools.sensor_calibration.proto.extractor_config_pb2'
  # @@protoc_insertion_point(class_scope:ChannelConfig)
  })
_sym_db.RegisterMessage(ChannelConfig)

Channels = _reflection.GeneratedProtocolMessageType('Channels', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELS,
  '__module__' : 'modules.tools.sensor_calibration.proto.extractor_config_pb2'
  # @@protoc_insertion_point(class_scope:Channels)
  })
_sym_db.RegisterMessage(Channels)

Records = _reflection.GeneratedProtocolMessageType('Records', (_message.Message,), {
  'DESCRIPTOR' : _RECORDS,
  '__module__' : 'modules.tools.sensor_calibration.proto.extractor_config_pb2'
  # @@protoc_insertion_point(class_scope:Records)
  })
_sym_db.RegisterMessage(Records)

DataExtractionConfig = _reflection.GeneratedProtocolMessageType('DataExtractionConfig', (_message.Message,), {
  'DESCRIPTOR' : _DATAEXTRACTIONCONFIG,
  '__module__' : 'modules.tools.sensor_calibration.proto.extractor_config_pb2'
  # @@protoc_insertion_point(class_scope:DataExtractionConfig)
  })
_sym_db.RegisterMessage(DataExtractionConfig)


# @@protoc_insertion_point(module_scope)
