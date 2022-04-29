# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/prediction/proto/offline_features.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.common.proto import pnc_point_pb2 as modules_dot_common_dot_proto_dot_pnc__point__pb2
from modules.prediction.proto import feature_pb2 as modules_dot_prediction_dot_proto_dot_feature__pb2
from modules.prediction.proto import prediction_conf_pb2 as modules_dot_prediction_dot_proto_dot_prediction__conf__pb2
from modules.prediction.proto import scenario_pb2 as modules_dot_prediction_dot_proto_dot_scenario__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/prediction/proto/offline_features.proto',
  package='apollo.prediction',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/modules/prediction/proto/offline_features.proto\x12\x11\x61pollo.prediction\x1a$modules/common/proto/pnc_point.proto\x1a&modules/prediction/proto/feature.proto\x1a.modules/prediction/proto/prediction_conf.proto\x1a\'modules/prediction/proto/scenario.proto\"\xb1\x01\n\x0f\x44\x61taForLearning\x12\x10\n\x08\x63\x61tegory\x18\x05 \x01(\t\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x12\x1d\n\x15\x66\x65\x61tures_for_learning\x18\x03 \x03(\x01\x12$\n\x1cstring_features_for_learning\x18\x07 \x03(\t\x12\x0e\n\x06labels\x18\x04 \x03(\x01\x12\x18\n\x10lane_sequence_id\x18\x06 \x01(\x05\"T\n\x13ListDataForLearning\x12=\n\x11\x64\x61ta_for_learning\x18\x01 \x03(\x0b\x32\".apollo.prediction.DataForLearning\"\xcb\x01\n\x10PredictionResult\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x12\x31\n\ntrajectory\x18\x03 \x03(\x0b\x32\x1d.apollo.prediction.Trajectory\x12\x36\n\robstacle_conf\x18\x04 \x01(\x0b\x32\x1f.apollo.prediction.ObstacleConf\x12-\n\x08scenario\x18\x05 \x01(\x0b\x32\x1b.apollo.prediction.Scenario\"V\n\x14ListPredictionResult\x12>\n\x11prediction_result\x18\x01 \x03(\x0b\x32#.apollo.prediction.PredictionResult\">\n\x0cListFrameEnv\x12.\n\tframe_env\x18\x01 \x03(\x0b\x32\x1b.apollo.prediction.FrameEnv\"\xcc\x01\n\rDataForTuning\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x11\n\ttimestamp\x18\x03 \x01(\x01\x12\x19\n\x11values_for_tuning\x18\x04 \x03(\x01\x12\x17\n\x0freal_cost_value\x18\x05 \x03(\x01\x12\x18\n\x10lane_sequence_id\x18\x06 \x01(\x05\x12<\n\x14\x61\x64\x63_trajectory_point\x18\x07 \x03(\x0b\x32\x1e.apollo.common.TrajectoryPoint\"N\n\x11ListDataForTuning\x12\x39\n\x0f\x64\x61ta_for_tuning\x18\x01 \x03(\x0b\x32 .apollo.prediction.DataForTuning\"7\n\x08\x46\x65\x61tures\x12+\n\x07\x66\x65\x61ture\x18\x01 \x03(\x0b\x32\x1a.apollo.prediction.Feature'
  ,
  dependencies=[modules_dot_common_dot_proto_dot_pnc__point__pb2.DESCRIPTOR,modules_dot_prediction_dot_proto_dot_feature__pb2.DESCRIPTOR,modules_dot_prediction_dot_proto_dot_prediction__conf__pb2.DESCRIPTOR,modules_dot_prediction_dot_proto_dot_scenario__pb2.DESCRIPTOR,])




_DATAFORLEARNING = _descriptor.Descriptor(
  name='DataForLearning',
  full_name='apollo.prediction.DataForLearning',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='apollo.prediction.DataForLearning.category', index=0,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.prediction.DataForLearning.id', index=1,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='apollo.prediction.DataForLearning.timestamp', index=2,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='features_for_learning', full_name='apollo.prediction.DataForLearning.features_for_learning', index=3,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_features_for_learning', full_name='apollo.prediction.DataForLearning.string_features_for_learning', index=4,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='apollo.prediction.DataForLearning.labels', index=5,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_sequence_id', full_name='apollo.prediction.DataForLearning.lane_sequence_id', index=6,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=238,
  serialized_end=415,
)


_LISTDATAFORLEARNING = _descriptor.Descriptor(
  name='ListDataForLearning',
  full_name='apollo.prediction.ListDataForLearning',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_for_learning', full_name='apollo.prediction.ListDataForLearning.data_for_learning', index=0,
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
  serialized_start=417,
  serialized_end=501,
)


_PREDICTIONRESULT = _descriptor.Descriptor(
  name='PredictionResult',
  full_name='apollo.prediction.PredictionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.prediction.PredictionResult.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='apollo.prediction.PredictionResult.timestamp', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trajectory', full_name='apollo.prediction.PredictionResult.trajectory', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='obstacle_conf', full_name='apollo.prediction.PredictionResult.obstacle_conf', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scenario', full_name='apollo.prediction.PredictionResult.scenario', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=504,
  serialized_end=707,
)


_LISTPREDICTIONRESULT = _descriptor.Descriptor(
  name='ListPredictionResult',
  full_name='apollo.prediction.ListPredictionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='prediction_result', full_name='apollo.prediction.ListPredictionResult.prediction_result', index=0,
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
  serialized_start=709,
  serialized_end=795,
)


_LISTFRAMEENV = _descriptor.Descriptor(
  name='ListFrameEnv',
  full_name='apollo.prediction.ListFrameEnv',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_env', full_name='apollo.prediction.ListFrameEnv.frame_env', index=0,
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
  serialized_start=797,
  serialized_end=859,
)


_DATAFORTUNING = _descriptor.Descriptor(
  name='DataForTuning',
  full_name='apollo.prediction.DataForTuning',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='apollo.prediction.DataForTuning.category', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.prediction.DataForTuning.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='apollo.prediction.DataForTuning.timestamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values_for_tuning', full_name='apollo.prediction.DataForTuning.values_for_tuning', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='real_cost_value', full_name='apollo.prediction.DataForTuning.real_cost_value', index=4,
      number=5, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_sequence_id', full_name='apollo.prediction.DataForTuning.lane_sequence_id', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adc_trajectory_point', full_name='apollo.prediction.DataForTuning.adc_trajectory_point', index=6,
      number=7, type=11, cpp_type=10, label=3,
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
  serialized_start=862,
  serialized_end=1066,
)


_LISTDATAFORTUNING = _descriptor.Descriptor(
  name='ListDataForTuning',
  full_name='apollo.prediction.ListDataForTuning',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_for_tuning', full_name='apollo.prediction.ListDataForTuning.data_for_tuning', index=0,
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
  serialized_start=1068,
  serialized_end=1146,
)


_FEATURES = _descriptor.Descriptor(
  name='Features',
  full_name='apollo.prediction.Features',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature', full_name='apollo.prediction.Features.feature', index=0,
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
  serialized_start=1148,
  serialized_end=1203,
)

_LISTDATAFORLEARNING.fields_by_name['data_for_learning'].message_type = _DATAFORLEARNING
_PREDICTIONRESULT.fields_by_name['trajectory'].message_type = modules_dot_prediction_dot_proto_dot_feature__pb2._TRAJECTORY
_PREDICTIONRESULT.fields_by_name['obstacle_conf'].message_type = modules_dot_prediction_dot_proto_dot_prediction__conf__pb2._OBSTACLECONF
_PREDICTIONRESULT.fields_by_name['scenario'].message_type = modules_dot_prediction_dot_proto_dot_scenario__pb2._SCENARIO
_LISTPREDICTIONRESULT.fields_by_name['prediction_result'].message_type = _PREDICTIONRESULT
_LISTFRAMEENV.fields_by_name['frame_env'].message_type = modules_dot_prediction_dot_proto_dot_feature__pb2._FRAMEENV
_DATAFORTUNING.fields_by_name['adc_trajectory_point'].message_type = modules_dot_common_dot_proto_dot_pnc__point__pb2._TRAJECTORYPOINT
_LISTDATAFORTUNING.fields_by_name['data_for_tuning'].message_type = _DATAFORTUNING
_FEATURES.fields_by_name['feature'].message_type = modules_dot_prediction_dot_proto_dot_feature__pb2._FEATURE
DESCRIPTOR.message_types_by_name['DataForLearning'] = _DATAFORLEARNING
DESCRIPTOR.message_types_by_name['ListDataForLearning'] = _LISTDATAFORLEARNING
DESCRIPTOR.message_types_by_name['PredictionResult'] = _PREDICTIONRESULT
DESCRIPTOR.message_types_by_name['ListPredictionResult'] = _LISTPREDICTIONRESULT
DESCRIPTOR.message_types_by_name['ListFrameEnv'] = _LISTFRAMEENV
DESCRIPTOR.message_types_by_name['DataForTuning'] = _DATAFORTUNING
DESCRIPTOR.message_types_by_name['ListDataForTuning'] = _LISTDATAFORTUNING
DESCRIPTOR.message_types_by_name['Features'] = _FEATURES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataForLearning = _reflection.GeneratedProtocolMessageType('DataForLearning', (_message.Message,), {
  'DESCRIPTOR' : _DATAFORLEARNING,
  '__module__' : 'modules.prediction.proto.offline_features_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.DataForLearning)
  })
_sym_db.RegisterMessage(DataForLearning)

ListDataForLearning = _reflection.GeneratedProtocolMessageType('ListDataForLearning', (_message.Message,), {
  'DESCRIPTOR' : _LISTDATAFORLEARNING,
  '__module__' : 'modules.prediction.proto.offline_features_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.ListDataForLearning)
  })
_sym_db.RegisterMessage(ListDataForLearning)

PredictionResult = _reflection.GeneratedProtocolMessageType('PredictionResult', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTIONRESULT,
  '__module__' : 'modules.prediction.proto.offline_features_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.PredictionResult)
  })
_sym_db.RegisterMessage(PredictionResult)

ListPredictionResult = _reflection.GeneratedProtocolMessageType('ListPredictionResult', (_message.Message,), {
  'DESCRIPTOR' : _LISTPREDICTIONRESULT,
  '__module__' : 'modules.prediction.proto.offline_features_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.ListPredictionResult)
  })
_sym_db.RegisterMessage(ListPredictionResult)

ListFrameEnv = _reflection.GeneratedProtocolMessageType('ListFrameEnv', (_message.Message,), {
  'DESCRIPTOR' : _LISTFRAMEENV,
  '__module__' : 'modules.prediction.proto.offline_features_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.ListFrameEnv)
  })
_sym_db.RegisterMessage(ListFrameEnv)

DataForTuning = _reflection.GeneratedProtocolMessageType('DataForTuning', (_message.Message,), {
  'DESCRIPTOR' : _DATAFORTUNING,
  '__module__' : 'modules.prediction.proto.offline_features_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.DataForTuning)
  })
_sym_db.RegisterMessage(DataForTuning)

ListDataForTuning = _reflection.GeneratedProtocolMessageType('ListDataForTuning', (_message.Message,), {
  'DESCRIPTOR' : _LISTDATAFORTUNING,
  '__module__' : 'modules.prediction.proto.offline_features_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.ListDataForTuning)
  })
_sym_db.RegisterMessage(ListDataForTuning)

Features = _reflection.GeneratedProtocolMessageType('Features', (_message.Message,), {
  'DESCRIPTOR' : _FEATURES,
  '__module__' : 'modules.prediction.proto.offline_features_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.Features)
  })
_sym_db.RegisterMessage(Features)


# @@protoc_insertion_point(module_scope)
