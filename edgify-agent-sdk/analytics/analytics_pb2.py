# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analytics.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='analytics.proto',
  package='edgify',
  syntax='proto3',
  serialized_options=b'Z\010edgifypb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x61nalytics.proto\x12\x06\x65\x64gify\"+\n\x1b\x43reateAnalyticsEventRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1e\n\x1c\x43reateAnalyticsEventResponse2n\n\x10\x41nalyticsService\x12Z\n\x0b\x43reateEvent\x12#.edgify.CreateAnalyticsEventRequest\x1a$.edgify.CreateAnalyticsEventResponse\"\x00\x42\nZ\x08\x65\x64gifypbb\x06proto3'
)




_CREATEANALYTICSEVENTREQUEST = _descriptor.Descriptor(
  name='CreateAnalyticsEventRequest',
  full_name='edgify.CreateAnalyticsEventRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='edgify.CreateAnalyticsEventRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=70,
)


_CREATEANALYTICSEVENTRESPONSE = _descriptor.Descriptor(
  name='CreateAnalyticsEventResponse',
  full_name='edgify.CreateAnalyticsEventResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=72,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['CreateAnalyticsEventRequest'] = _CREATEANALYTICSEVENTREQUEST
DESCRIPTOR.message_types_by_name['CreateAnalyticsEventResponse'] = _CREATEANALYTICSEVENTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateAnalyticsEventRequest = _reflection.GeneratedProtocolMessageType('CreateAnalyticsEventRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEANALYTICSEVENTREQUEST,
  '__module__' : 'analytics_pb2'
  # @@protoc_insertion_point(class_scope:edgify.CreateAnalyticsEventRequest)
  })
_sym_db.RegisterMessage(CreateAnalyticsEventRequest)

CreateAnalyticsEventResponse = _reflection.GeneratedProtocolMessageType('CreateAnalyticsEventResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEANALYTICSEVENTRESPONSE,
  '__module__' : 'analytics_pb2'
  # @@protoc_insertion_point(class_scope:edgify.CreateAnalyticsEventResponse)
  })
_sym_db.RegisterMessage(CreateAnalyticsEventResponse)


DESCRIPTOR._options = None

_ANALYTICSSERVICE = _descriptor.ServiceDescriptor(
  name='AnalyticsService',
  full_name='edgify.AnalyticsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=104,
  serialized_end=214,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateEvent',
    full_name='edgify.AnalyticsService.CreateEvent',
    index=0,
    containing_service=None,
    input_type=_CREATEANALYTICSEVENTREQUEST,
    output_type=_CREATEANALYTICSEVENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ANALYTICSSERVICE)

DESCRIPTOR.services_by_name['AnalyticsService'] = _ANALYTICSSERVICE

# @@protoc_insertion_point(module_scope)
