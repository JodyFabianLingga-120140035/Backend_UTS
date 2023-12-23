# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: komputer.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ekomputer.proto\x12\x08komputer\"j\n\x08Komputer\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x05\x12\x11\n\timage_url\x18\x06 \x01(\t\x12\r\n\x05stock\x18\x07 \x01(\x05\"\x15\n\x13KomputerListRequest\"=\n\x14KomputerListResponse\x12%\n\tkomputers\x18\x01 \x03(\x0b\x32\x12.komputer.Komputer\"\x1d\n\x0fKomputerRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"8\n\x10KomputerResponse\x12$\n\x08komputer\x18\x01 \x01(\x0b\x32\x12.komputer.Komputer\"k\n\x15KomputerCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x05\x12\x11\n\timage_url\x18\x04 \x01(\t\x12\r\n\x05stock\x18\x05 \x01(\x05\">\n\x16KomputerCreateResponse\x12$\n\x08komputer\x18\x01 \x01(\x0b\x32\x12.komputer.Komputer\"w\n\x15KomputerUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x05\x12\x11\n\timage_url\x18\x05 \x01(\t\x12\r\n\x05stock\x18\x06 \x01(\x05\">\n\x16KomputerUpdateResponse\x12$\n\x08komputer\x18\x01 \x01(\x0b\x32\x12.komputer.Komputer\"#\n\x15KomputerDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\")\n\x16KomputerDeleteResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xfd\x02\n\x0fKomputerService\x12\x45\n\x04List\x12\x1d.komputer.KomputerListRequest\x1a\x1e.komputer.KomputerListResponse\x12<\n\x03Get\x12\x19.komputer.KomputerRequest\x1a\x1a.komputer.KomputerResponse\x12K\n\x06\x43reate\x12\x1f.komputer.KomputerCreateRequest\x1a .komputer.KomputerCreateResponse\x12K\n\x06Update\x12\x1f.komputer.KomputerUpdateRequest\x1a .komputer.KomputerUpdateResponse\x12K\n\x06\x44\x65lete\x12\x1f.komputer.KomputerDeleteRequest\x1a .komputer.KomputerDeleteResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'komputer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_KOMPUTER']._serialized_start=28
  _globals['_KOMPUTER']._serialized_end=134
  _globals['_KOMPUTERLISTREQUEST']._serialized_start=136
  _globals['_KOMPUTERLISTREQUEST']._serialized_end=157
  _globals['_KOMPUTERLISTRESPONSE']._serialized_start=159
  _globals['_KOMPUTERLISTRESPONSE']._serialized_end=220
  _globals['_KOMPUTERREQUEST']._serialized_start=222
  _globals['_KOMPUTERREQUEST']._serialized_end=251
  _globals['_KOMPUTERRESPONSE']._serialized_start=253
  _globals['_KOMPUTERRESPONSE']._serialized_end=309
  _globals['_KOMPUTERCREATEREQUEST']._serialized_start=311
  _globals['_KOMPUTERCREATEREQUEST']._serialized_end=418
  _globals['_KOMPUTERCREATERESPONSE']._serialized_start=420
  _globals['_KOMPUTERCREATERESPONSE']._serialized_end=482
  _globals['_KOMPUTERUPDATEREQUEST']._serialized_start=484
  _globals['_KOMPUTERUPDATEREQUEST']._serialized_end=603
  _globals['_KOMPUTERUPDATERESPONSE']._serialized_start=605
  _globals['_KOMPUTERUPDATERESPONSE']._serialized_end=667
  _globals['_KOMPUTERDELETEREQUEST']._serialized_start=669
  _globals['_KOMPUTERDELETEREQUEST']._serialized_end=704
  _globals['_KOMPUTERDELETERESPONSE']._serialized_start=706
  _globals['_KOMPUTERDELETERESPONSE']._serialized_end=747
  _globals['_KOMPUTERSERVICE']._serialized_start=750
  _globals['_KOMPUTERSERVICE']._serialized_end=1131
# @@protoc_insertion_point(module_scope)