# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Cmd.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Cmd.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tCmd.proto\"7\n\x07Vehicle\x12\x0c\n\x04\x44uty\x18\x01 \x01(\x05\x12\x1e\n\tDirection\x18\x02 \x01(\x0e\x32\x0b.EDirection\"5\n\tImuAngles\x12\x0c\n\x04Roll\x18\x01 \x01(\x05\x12\r\n\x05Pitch\x18\x02 \x01(\x05\x12\x0b\n\x03Yaw\x18\x03 \x01(\x05\"L\n\x03Msg\x12\x1b\n\x07Vehicle\x18\x01 \x01(\x0b\x32\x08.VehicleH\x00\x12\x1f\n\tImuAngles\x18\x02 \x01(\x0b\x32\n.ImuAnglesH\x00\x42\x07\n\x05Types*5\n\nEDirection\x12\x08\n\x04Idle\x10\x00\x12\x08\n\x04Move\x10\x01\x12\x08\n\x04Left\x10\x02\x12\t\n\x05Right\x10\x03\x62\x06proto3')
)

_EDIRECTION = _descriptor.EnumDescriptor(
  name='EDirection',
  full_name='EDirection',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Idle', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Move', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Left', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Right', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=203,
  serialized_end=256,
)
_sym_db.RegisterEnumDescriptor(_EDIRECTION)

EDirection = enum_type_wrapper.EnumTypeWrapper(_EDIRECTION)
Idle = 0
Move = 1
Left = 2
Right = 3



_VEHICLE = _descriptor.Descriptor(
  name='Vehicle',
  full_name='Vehicle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Duty', full_name='Vehicle.Duty', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Direction', full_name='Vehicle.Direction', index=1,
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
  serialized_start=13,
  serialized_end=68,
)


_IMUANGLES = _descriptor.Descriptor(
  name='ImuAngles',
  full_name='ImuAngles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Roll', full_name='ImuAngles.Roll', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Pitch', full_name='ImuAngles.Pitch', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Yaw', full_name='ImuAngles.Yaw', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=70,
  serialized_end=123,
)


_MSG = _descriptor.Descriptor(
  name='Msg',
  full_name='Msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Vehicle', full_name='Msg.Vehicle', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ImuAngles', full_name='Msg.ImuAngles', index=1,
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
    _descriptor.OneofDescriptor(
      name='Types', full_name='Msg.Types',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=125,
  serialized_end=201,
)

_VEHICLE.fields_by_name['Direction'].enum_type = _EDIRECTION
_MSG.fields_by_name['Vehicle'].message_type = _VEHICLE
_MSG.fields_by_name['ImuAngles'].message_type = _IMUANGLES
_MSG.oneofs_by_name['Types'].fields.append(
  _MSG.fields_by_name['Vehicle'])
_MSG.fields_by_name['Vehicle'].containing_oneof = _MSG.oneofs_by_name['Types']
_MSG.oneofs_by_name['Types'].fields.append(
  _MSG.fields_by_name['ImuAngles'])
_MSG.fields_by_name['ImuAngles'].containing_oneof = _MSG.oneofs_by_name['Types']
DESCRIPTOR.message_types_by_name['Vehicle'] = _VEHICLE
DESCRIPTOR.message_types_by_name['ImuAngles'] = _IMUANGLES
DESCRIPTOR.message_types_by_name['Msg'] = _MSG
DESCRIPTOR.enum_types_by_name['EDirection'] = _EDIRECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vehicle = _reflection.GeneratedProtocolMessageType('Vehicle', (_message.Message,), dict(
  DESCRIPTOR = _VEHICLE,
  __module__ = 'Cmd_pb2'
  # @@protoc_insertion_point(class_scope:Vehicle)
  ))
_sym_db.RegisterMessage(Vehicle)

ImuAngles = _reflection.GeneratedProtocolMessageType('ImuAngles', (_message.Message,), dict(
  DESCRIPTOR = _IMUANGLES,
  __module__ = 'Cmd_pb2'
  # @@protoc_insertion_point(class_scope:ImuAngles)
  ))
_sym_db.RegisterMessage(ImuAngles)

Msg = _reflection.GeneratedProtocolMessageType('Msg', (_message.Message,), dict(
  DESCRIPTOR = _MSG,
  __module__ = 'Cmd_pb2'
  # @@protoc_insertion_point(class_scope:Msg)
  ))
_sym_db.RegisterMessage(Msg)


# @@protoc_insertion_point(module_scope)
