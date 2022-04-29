# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/prediction/proto/prediction_conf.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.perception.proto import perception_obstacle_pb2 as modules_dot_perception_dot_proto_dot_perception__obstacle__pb2
from modules.prediction.proto import feature_pb2 as modules_dot_prediction_dot_proto_dot_feature__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/prediction/proto/prediction_conf.proto',
  package='apollo.prediction',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.modules/prediction/proto/prediction_conf.proto\x12\x11\x61pollo.prediction\x1a\x32modules/perception/proto/perception_obstacle.proto\x1a&modules/prediction/proto/feature.proto\"\x97\x08\n\x0cObstacleConf\x12\x41\n\robstacle_type\x18\x01 \x01(\x0e\x32*.apollo.perception.PerceptionObstacle.Type\x12S\n\x0fobstacle_status\x18\x02 \x01(\x0e\x32..apollo.prediction.ObstacleConf.ObstacleStatus:\nSTATIONARY\x12\x43\n\rpriority_type\x18\x05 \x01(\x0e\x32,.apollo.prediction.ObstaclePriority.Priority\x12\x45\n\x0e\x65valuator_type\x18\x03 \x01(\x0e\x32-.apollo.prediction.ObstacleConf.EvaluatorType\x12\x45\n\x0epredictor_type\x18\x04 \x01(\x0e\x32-.apollo.prediction.ObstacleConf.PredictorType\"X\n\x0eObstacleStatus\x12\x0b\n\x07ON_LANE\x10\x00\x12\x0c\n\x08OFF_LANE\x10\x01\x12\x0e\n\nSTATIONARY\x10\x03\x12\n\n\x06MOVING\x10\x04\x12\x0f\n\x0bIN_JUNCTION\x10\x05\"\xc0\x02\n\rEvaluatorType\x12\x11\n\rMLP_EVALUATOR\x10\x00\x12\x15\n\rRNN_EVALUATOR\x10\x01\x1a\x02\x08\x01\x12\x12\n\x0e\x43OST_EVALUATOR\x10\x02\x12\x18\n\x14\x43RUISE_MLP_EVALUATOR\x10\x03\x12\x1a\n\x16JUNCTION_MLP_EVALUATOR\x10\x04\x12\x1f\n\x1b\x43YCLIST_KEEP_LANE_EVALUATOR\x10\x05\x12\x1b\n\x17LANE_SCANNING_EVALUATOR\x10\x06\x12$\n PEDESTRIAN_INTERACTION_EVALUATOR\x10\x07\x12\x1a\n\x16JUNCTION_MAP_EVALUATOR\x10\x08\x12\x1e\n\x1aLANE_AGGREGATING_EVALUATOR\x10\t\x12\x1b\n\x17SEMANTIC_LSTM_EVALUATOR\x10\n\"\xfe\x01\n\rPredictorType\x12\x1b\n\x17LANE_SEQUENCE_PREDICTOR\x10\x00\x12\x17\n\x13\x46REE_MOVE_PREDICTOR\x10\x01\x12\x1a\n\x12REGIONAL_PREDICTOR\x10\x02\x1a\x02\x08\x01\x12\x1b\n\x17MOVE_SEQUENCE_PREDICTOR\x10\x03\x12\x13\n\x0f\x45MPTY_PREDICTOR\x10\x04\x12\x19\n\x15SINGLE_LANE_PREDICTOR\x10\x05\x12\x16\n\x12JUNCTION_PREDICTOR\x10\x06\x12\x1b\n\x17\x45XTRAPOLATION_PREDICTOR\x10\x07\x12\x19\n\x15INTERACTION_PREDICTOR\x10\x08\"\xa9\x02\n\tTopicConf\x12\x1f\n\x17\x61\x64\x63\x63ontainer_topic_name\x18\x01 \x01(\t\x12\x1c\n\x14\x63ontainer_topic_name\x18\x02 \x01(\t\x12\x1c\n\x14\x65valuator_topic_name\x18\x03 \x01(\t\x12\x1a\n\x12localization_topic\x18\x04 \x01(\t\x12!\n\x19perception_obstacle_topic\x18\x05 \x01(\t\x12\'\n\x1fperception_obstacles_topic_name\x18\x06 \x01(\t\x12!\n\x19planning_trajectory_topic\x18\x07 \x01(\t\x12\x18\n\x10prediction_topic\x18\x08 \x01(\t\x12\x1a\n\x12storytelling_topic\x18\t \x01(\t\"z\n\x0ePredictionConf\x12\x30\n\ntopic_conf\x18\x01 \x01(\x0b\x32\x1c.apollo.prediction.TopicConf\x12\x36\n\robstacle_conf\x18\x02 \x03(\x0b\x32\x1f.apollo.prediction.ObstacleConf'
  ,
  dependencies=[modules_dot_perception_dot_proto_dot_perception__obstacle__pb2.DESCRIPTOR,modules_dot_prediction_dot_proto_dot_feature__pb2.DESCRIPTOR,])



_OBSTACLECONF_OBSTACLESTATUS = _descriptor.EnumDescriptor(
  name='ObstacleStatus',
  full_name='apollo.prediction.ObstacleConf.ObstacleStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ON_LANE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OFF_LANE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATIONARY', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MOVING', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IN_JUNCTION', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=541,
  serialized_end=629,
)
_sym_db.RegisterEnumDescriptor(_OBSTACLECONF_OBSTACLESTATUS)

_OBSTACLECONF_EVALUATORTYPE = _descriptor.EnumDescriptor(
  name='EvaluatorType',
  full_name='apollo.prediction.ObstacleConf.EvaluatorType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MLP_EVALUATOR', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RNN_EVALUATOR', index=1, number=1,
      serialized_options=b'\010\001',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COST_EVALUATOR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CRUISE_MLP_EVALUATOR', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JUNCTION_MLP_EVALUATOR', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CYCLIST_KEEP_LANE_EVALUATOR', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_SCANNING_EVALUATOR', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PEDESTRIAN_INTERACTION_EVALUATOR', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JUNCTION_MAP_EVALUATOR', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_AGGREGATING_EVALUATOR', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEMANTIC_LSTM_EVALUATOR', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=632,
  serialized_end=952,
)
_sym_db.RegisterEnumDescriptor(_OBSTACLECONF_EVALUATORTYPE)

_OBSTACLECONF_PREDICTORTYPE = _descriptor.EnumDescriptor(
  name='PredictorType',
  full_name='apollo.prediction.ObstacleConf.PredictorType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LANE_SEQUENCE_PREDICTOR', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FREE_MOVE_PREDICTOR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REGIONAL_PREDICTOR', index=2, number=2,
      serialized_options=b'\010\001',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MOVE_SEQUENCE_PREDICTOR', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EMPTY_PREDICTOR', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SINGLE_LANE_PREDICTOR', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JUNCTION_PREDICTOR', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXTRAPOLATION_PREDICTOR', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERACTION_PREDICTOR', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=955,
  serialized_end=1209,
)
_sym_db.RegisterEnumDescriptor(_OBSTACLECONF_PREDICTORTYPE)


_OBSTACLECONF = _descriptor.Descriptor(
  name='ObstacleConf',
  full_name='apollo.prediction.ObstacleConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='obstacle_type', full_name='apollo.prediction.ObstacleConf.obstacle_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='obstacle_status', full_name='apollo.prediction.ObstacleConf.obstacle_status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='priority_type', full_name='apollo.prediction.ObstacleConf.priority_type', index=2,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='evaluator_type', full_name='apollo.prediction.ObstacleConf.evaluator_type', index=3,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='predictor_type', full_name='apollo.prediction.ObstacleConf.predictor_type', index=4,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OBSTACLECONF_OBSTACLESTATUS,
    _OBSTACLECONF_EVALUATORTYPE,
    _OBSTACLECONF_PREDICTORTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=1209,
)


_TOPICCONF = _descriptor.Descriptor(
  name='TopicConf',
  full_name='apollo.prediction.TopicConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='adccontainer_topic_name', full_name='apollo.prediction.TopicConf.adccontainer_topic_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='container_topic_name', full_name='apollo.prediction.TopicConf.container_topic_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='evaluator_topic_name', full_name='apollo.prediction.TopicConf.evaluator_topic_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='localization_topic', full_name='apollo.prediction.TopicConf.localization_topic', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='perception_obstacle_topic', full_name='apollo.prediction.TopicConf.perception_obstacle_topic', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='perception_obstacles_topic_name', full_name='apollo.prediction.TopicConf.perception_obstacles_topic_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='planning_trajectory_topic', full_name='apollo.prediction.TopicConf.planning_trajectory_topic', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prediction_topic', full_name='apollo.prediction.TopicConf.prediction_topic', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='storytelling_topic', full_name='apollo.prediction.TopicConf.storytelling_topic', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=1212,
  serialized_end=1509,
)


_PREDICTIONCONF = _descriptor.Descriptor(
  name='PredictionConf',
  full_name='apollo.prediction.PredictionConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic_conf', full_name='apollo.prediction.PredictionConf.topic_conf', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='obstacle_conf', full_name='apollo.prediction.PredictionConf.obstacle_conf', index=1,
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
  serialized_start=1511,
  serialized_end=1633,
)

_OBSTACLECONF.fields_by_name['obstacle_type'].enum_type = modules_dot_perception_dot_proto_dot_perception__obstacle__pb2._PERCEPTIONOBSTACLE_TYPE
_OBSTACLECONF.fields_by_name['obstacle_status'].enum_type = _OBSTACLECONF_OBSTACLESTATUS
_OBSTACLECONF.fields_by_name['priority_type'].enum_type = modules_dot_prediction_dot_proto_dot_feature__pb2._OBSTACLEPRIORITY_PRIORITY
_OBSTACLECONF.fields_by_name['evaluator_type'].enum_type = _OBSTACLECONF_EVALUATORTYPE
_OBSTACLECONF.fields_by_name['predictor_type'].enum_type = _OBSTACLECONF_PREDICTORTYPE
_OBSTACLECONF_OBSTACLESTATUS.containing_type = _OBSTACLECONF
_OBSTACLECONF_EVALUATORTYPE.containing_type = _OBSTACLECONF
_OBSTACLECONF_PREDICTORTYPE.containing_type = _OBSTACLECONF
_PREDICTIONCONF.fields_by_name['topic_conf'].message_type = _TOPICCONF
_PREDICTIONCONF.fields_by_name['obstacle_conf'].message_type = _OBSTACLECONF
DESCRIPTOR.message_types_by_name['ObstacleConf'] = _OBSTACLECONF
DESCRIPTOR.message_types_by_name['TopicConf'] = _TOPICCONF
DESCRIPTOR.message_types_by_name['PredictionConf'] = _PREDICTIONCONF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObstacleConf = _reflection.GeneratedProtocolMessageType('ObstacleConf', (_message.Message,), {
  'DESCRIPTOR' : _OBSTACLECONF,
  '__module__' : 'modules.prediction.proto.prediction_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.ObstacleConf)
  })
_sym_db.RegisterMessage(ObstacleConf)

TopicConf = _reflection.GeneratedProtocolMessageType('TopicConf', (_message.Message,), {
  'DESCRIPTOR' : _TOPICCONF,
  '__module__' : 'modules.prediction.proto.prediction_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.TopicConf)
  })
_sym_db.RegisterMessage(TopicConf)

PredictionConf = _reflection.GeneratedProtocolMessageType('PredictionConf', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTIONCONF,
  '__module__' : 'modules.prediction.proto.prediction_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.PredictionConf)
  })
_sym_db.RegisterMessage(PredictionConf)


_OBSTACLECONF_EVALUATORTYPE.values_by_name["RNN_EVALUATOR"]._options = None
_OBSTACLECONF_PREDICTORTYPE.values_by_name["REGIONAL_PREDICTOR"]._options = None
# @@protoc_insertion_point(module_scope)
