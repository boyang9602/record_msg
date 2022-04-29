# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/transform/proto/transform.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/transform/proto/transform.proto',
  package='apollo.transform',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'modules/transform/proto/transform.proto\x12\x10\x61pollo.transform\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto\"e\n\tTransform\x12+\n\x0btranslation\x18\x01 \x01(\x0b\x32\x16.apollo.common.Point3D\x12+\n\x08rotation\x18\x02 \x01(\x0b\x32\x19.apollo.common.Quaternion\"\x81\x01\n\x10TransformStamped\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x16\n\x0e\x63hild_frame_id\x18\x02 \x01(\t\x12.\n\ttransform\x18\x03 \x01(\x0b\x32\x1b.apollo.transform.Transform\"r\n\x11TransformStampeds\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x36\n\ntransforms\x18\x02 \x03(\x0b\x32\".apollo.transform.TransformStamped'
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,modules_dot_common_dot_proto_dot_geometry__pb2.DESCRIPTOR,])




_TRANSFORM = _descriptor.Descriptor(
  name='Transform',
  full_name='apollo.transform.Transform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='translation', full_name='apollo.transform.Transform.translation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='apollo.transform.Transform.rotation', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=133,
  serialized_end=234,
)


_TRANSFORMSTAMPED = _descriptor.Descriptor(
  name='TransformStamped',
  full_name='apollo.transform.TransformStamped',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.transform.TransformStamped.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='child_frame_id', full_name='apollo.transform.TransformStamped.child_frame_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transform', full_name='apollo.transform.TransformStamped.transform', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=237,
  serialized_end=366,
)


_TRANSFORMSTAMPEDS = _descriptor.Descriptor(
  name='TransformStampeds',
  full_name='apollo.transform.TransformStampeds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.transform.TransformStampeds.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transforms', full_name='apollo.transform.TransformStampeds.transforms', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=368,
  serialized_end=482,
)

_TRANSFORM.fields_by_name['translation'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_TRANSFORM.fields_by_name['rotation'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._QUATERNION
_TRANSFORMSTAMPED.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_TRANSFORMSTAMPED.fields_by_name['transform'].message_type = _TRANSFORM
_TRANSFORMSTAMPEDS.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_TRANSFORMSTAMPEDS.fields_by_name['transforms'].message_type = _TRANSFORMSTAMPED
DESCRIPTOR.message_types_by_name['Transform'] = _TRANSFORM
DESCRIPTOR.message_types_by_name['TransformStamped'] = _TRANSFORMSTAMPED
DESCRIPTOR.message_types_by_name['TransformStampeds'] = _TRANSFORMSTAMPEDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Transform = _reflection.GeneratedProtocolMessageType('Transform', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORM,
  '__module__' : 'modules.transform.proto.transform_pb2'
  # @@protoc_insertion_point(class_scope:apollo.transform.Transform)
  })
_sym_db.RegisterMessage(Transform)

TransformStamped = _reflection.GeneratedProtocolMessageType('TransformStamped', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMSTAMPED,
  '__module__' : 'modules.transform.proto.transform_pb2'
  # @@protoc_insertion_point(class_scope:apollo.transform.TransformStamped)
  })
_sym_db.RegisterMessage(TransformStamped)

TransformStampeds = _reflection.GeneratedProtocolMessageType('TransformStampeds', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMSTAMPEDS,
  '__module__' : 'modules.transform.proto.transform_pb2'
  # @@protoc_insertion_point(class_scope:apollo.transform.TransformStampeds)
  })
_sym_db.RegisterMessage(TransformStampeds)


# @@protoc_insertion_point(module_scope)
