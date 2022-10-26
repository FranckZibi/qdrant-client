# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: points.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import json_with_int_pb2 as json__with__int__pb2
from . import collections_pb2 as collections__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cpoints.proto\x12\x06qdrant\x1a\x13json_with_int.proto\x1a\x11\x63ollections.proto\"<\n\x07PointId\x12\r\n\x03num\x18\x01 \x01(\x04H\x00\x12\x0e\n\x04uuid\x18\x02 \x01(\tH\x00\x42\x12\n\x10point_id_options\"\x16\n\x06Vector\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x02\"h\n\x0cUpsertPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x11\n\x04wait\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12#\n\x06points\x18\x03 \x03(\x0b\x32\x13.qdrant.PointStructB\x07\n\x05_wait\"k\n\x0c\x44\x65letePoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x11\n\x04wait\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12&\n\x06points\x18\x03 \x01(\x0b\x32\x16.qdrant.PointsSelectorB\x07\n\x05_wait\"\xc4\x01\n\tGetPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x1c\n\x03ids\x18\x02 \x03(\x0b\x32\x0f.qdrant.PointId\x12\x31\n\x0cwith_payload\x18\x04 \x01(\x0b\x32\x1b.qdrant.WithPayloadSelector\x12\x36\n\x0cwith_vectors\x18\x05 \x01(\x0b\x32\x1b.qdrant.WithVectorsSelectorH\x00\x88\x01\x01\x42\x0f\n\r_with_vectorsJ\x04\x08\x03\x10\x04\"\xdf\x01\n\x10SetPayloadPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x11\n\x04wait\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x36\n\x07payload\x18\x03 \x03(\x0b\x32%.qdrant.SetPayloadPoints.PayloadEntry\x12\x1f\n\x06points\x18\x04 \x03(\x0b\x32\x0f.qdrant.PointId\x1a=\n\x0cPayloadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.qdrant.Value:\x02\x38\x01\x42\x07\n\x05_wait\"y\n\x13\x44\x65letePayloadPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x11\n\x04wait\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x0c\n\x04keys\x18\x03 \x03(\t\x12\x1f\n\x06points\x18\x04 \x03(\x0b\x32\x0f.qdrant.PointIdB\x07\n\x05_wait\"q\n\x12\x43learPayloadPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x11\n\x04wait\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12&\n\x06points\x18\x03 \x01(\x0b\x32\x16.qdrant.PointsSelectorB\x07\n\x05_wait\"\xf4\x01\n\x1a\x43reateFieldIndexCollection\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x11\n\x04wait\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x12\n\nfield_name\x18\x03 \x01(\t\x12*\n\nfield_type\x18\x04 \x01(\x0e\x32\x11.qdrant.FieldTypeH\x01\x88\x01\x01\x12;\n\x12\x66ield_index_params\x18\x05 \x01(\x0b\x32\x1a.qdrant.PayloadIndexParamsH\x02\x88\x01\x01\x42\x07\n\x05_waitB\r\n\x0b_field_typeB\x15\n\x13_field_index_params\"e\n\x1a\x44\x65leteFieldIndexCollection\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x11\n\x04wait\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x12\n\nfield_name\x18\x03 \x01(\tB\x07\n\x05_wait\"(\n\x16PayloadIncludeSelector\x12\x0e\n\x06\x66ields\x18\x01 \x03(\t\"(\n\x16PayloadExcludeSelector\x12\x0e\n\x06\x66ields\x18\x01 \x03(\t\"\xa1\x01\n\x13WithPayloadSelector\x12\x10\n\x06\x65nable\x18\x01 \x01(\x08H\x00\x12\x31\n\x07include\x18\x02 \x01(\x0b\x32\x1e.qdrant.PayloadIncludeSelectorH\x00\x12\x31\n\x07\x65xclude\x18\x03 \x01(\x0b\x32\x1e.qdrant.PayloadExcludeSelectorH\x00\x42\x12\n\x10selector_options\"\x82\x01\n\x0cNamedVectors\x12\x32\n\x07vectors\x18\x01 \x03(\x0b\x32!.qdrant.NamedVectors.VectorsEntry\x1a>\n\x0cVectorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.qdrant.Vector:\x02\x38\x01\"g\n\x07Vectors\x12 \n\x06vector\x18\x01 \x01(\x0b\x32\x0e.qdrant.VectorH\x00\x12\'\n\x07vectors\x18\x02 \x01(\x0b\x32\x14.qdrant.NamedVectorsH\x00\x42\x11\n\x0fvectors_options\" \n\x0fVectorsSelector\x12\r\n\x05names\x18\x01 \x03(\t\"g\n\x13WithVectorsSelector\x12\x10\n\x06\x65nable\x18\x01 \x01(\x08H\x00\x12*\n\x07include\x18\x02 \x01(\x0b\x32\x17.qdrant.VectorsSelectorH\x00\x42\x12\n\x10selector_options\"N\n\x0cSearchParams\x12\x14\n\x07hnsw_ef\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x12\n\x05\x65xact\x18\x02 \x01(\x08H\x01\x88\x01\x01\x42\n\n\x08_hnsw_efB\x08\n\x06_exact\"\x8a\x03\n\x0cSearchPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x0e\n\x06vector\x18\x02 \x03(\x02\x12\x1e\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x0e.qdrant.Filter\x12\r\n\x05limit\x18\x04 \x01(\x04\x12\x31\n\x0cwith_payload\x18\x06 \x01(\x0b\x32\x1b.qdrant.WithPayloadSelector\x12$\n\x06params\x18\x07 \x01(\x0b\x32\x14.qdrant.SearchParams\x12\x1c\n\x0fscore_threshold\x18\x08 \x01(\x02H\x00\x88\x01\x01\x12\x13\n\x06offset\x18\t \x01(\x04H\x01\x88\x01\x01\x12\x18\n\x0bvector_name\x18\n \x01(\tH\x02\x88\x01\x01\x12\x36\n\x0cwith_vectors\x18\x0b \x01(\x0b\x32\x1b.qdrant.WithVectorsSelectorH\x03\x88\x01\x01\x42\x12\n\x10_score_thresholdB\t\n\x07_offsetB\x0e\n\x0c_vector_nameB\x0f\n\r_with_vectorsJ\x04\x08\x05\x10\x06\"Y\n\x11SearchBatchPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12+\n\rsearch_points\x18\x02 \x03(\x0b\x32\x14.qdrant.SearchPoints\"\x98\x02\n\x0cScrollPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x1e\n\x06\x66ilter\x18\x02 \x01(\x0b\x32\x0e.qdrant.Filter\x12$\n\x06offset\x18\x03 \x01(\x0b\x32\x0f.qdrant.PointIdH\x00\x88\x01\x01\x12\x12\n\x05limit\x18\x04 \x01(\rH\x01\x88\x01\x01\x12\x31\n\x0cwith_payload\x18\x06 \x01(\x0b\x32\x1b.qdrant.WithPayloadSelector\x12\x36\n\x0cwith_vectors\x18\x07 \x01(\x0b\x32\x1b.qdrant.WithVectorsSelectorH\x02\x88\x01\x01\x42\t\n\x07_offsetB\x08\n\x06_limitB\x0f\n\r_with_vectorsJ\x04\x08\x05\x10\x06\"\xb7\x03\n\x0fRecommendPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12!\n\x08positive\x18\x02 \x03(\x0b\x32\x0f.qdrant.PointId\x12!\n\x08negative\x18\x03 \x03(\x0b\x32\x0f.qdrant.PointId\x12\x1e\n\x06\x66ilter\x18\x04 \x01(\x0b\x32\x0e.qdrant.Filter\x12\r\n\x05limit\x18\x05 \x01(\x04\x12\x31\n\x0cwith_payload\x18\x07 \x01(\x0b\x32\x1b.qdrant.WithPayloadSelector\x12$\n\x06params\x18\x08 \x01(\x0b\x32\x14.qdrant.SearchParams\x12\x1c\n\x0fscore_threshold\x18\t \x01(\x02H\x00\x88\x01\x01\x12\x13\n\x06offset\x18\n \x01(\x04H\x01\x88\x01\x01\x12\x12\n\x05using\x18\x0b \x01(\tH\x02\x88\x01\x01\x12\x36\n\x0cwith_vectors\x18\x0c \x01(\x0b\x32\x1b.qdrant.WithVectorsSelectorH\x03\x88\x01\x01\x42\x12\n\x10_score_thresholdB\t\n\x07_offsetB\x08\n\x06_usingB\x0f\n\r_with_vectorsJ\x04\x08\x06\x10\x07\"b\n\x14RecommendBatchPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x31\n\x10recommend_points\x18\x02 \x03(\x0b\x32\x17.qdrant.RecommendPoints\"d\n\x0b\x43ountPoints\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x1e\n\x06\x66ilter\x18\x02 \x01(\x0b\x32\x0e.qdrant.Filter\x12\x12\n\x05\x65xact\x18\x03 \x01(\x08H\x00\x88\x01\x01\x42\x08\n\x06_exact\"M\n\x17PointsOperationResponse\x12$\n\x06result\x18\x01 \x01(\x0b\x32\x14.qdrant.UpdateResult\x12\x0c\n\x04time\x18\x02 \x01(\x01\"J\n\x0cUpdateResult\x12\x14\n\x0coperation_id\x18\x01 \x01(\x04\x12$\n\x06status\x18\x02 \x01(\x0e\x32\x14.qdrant.UpdateStatus\"\xf5\x01\n\x0bScoredPoint\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.qdrant.PointId\x12\x31\n\x07payload\x18\x02 \x03(\x0b\x32 .qdrant.ScoredPoint.PayloadEntry\x12\r\n\x05score\x18\x03 \x01(\x02\x12\x0f\n\x07version\x18\x05 \x01(\x04\x12%\n\x07vectors\x18\x06 \x01(\x0b\x32\x0f.qdrant.VectorsH\x00\x88\x01\x01\x1a=\n\x0cPayloadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.qdrant.Value:\x02\x38\x01\x42\n\n\x08_vectorsJ\x04\x08\x04\x10\x05\"C\n\x0eSearchResponse\x12#\n\x06result\x18\x01 \x03(\x0b\x32\x13.qdrant.ScoredPoint\x12\x0c\n\x04time\x18\x02 \x01(\x01\"2\n\x0b\x42\x61tchResult\x12#\n\x06result\x18\x01 \x03(\x0b\x32\x13.qdrant.ScoredPoint\"H\n\x13SearchBatchResponse\x12#\n\x06result\x18\x01 \x03(\x0b\x32\x13.qdrant.BatchResult\x12\x0c\n\x04time\x18\x02 \x01(\x01\"B\n\rCountResponse\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.qdrant.CountResult\x12\x0c\n\x04time\x18\x02 \x01(\x01\"\x8b\x01\n\x0eScrollResponse\x12.\n\x10next_page_offset\x18\x01 \x01(\x0b\x32\x0f.qdrant.PointIdH\x00\x88\x01\x01\x12&\n\x06result\x18\x02 \x03(\x0b\x32\x16.qdrant.RetrievedPoint\x12\x0c\n\x04time\x18\x03 \x01(\x01\x42\x13\n\x11_next_page_offset\"\x1c\n\x0b\x43ountResult\x12\r\n\x05\x63ount\x18\x01 \x01(\x04\"\xdb\x01\n\x0eRetrievedPoint\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.qdrant.PointId\x12\x34\n\x07payload\x18\x02 \x03(\x0b\x32#.qdrant.RetrievedPoint.PayloadEntry\x12%\n\x07vectors\x18\x04 \x01(\x0b\x32\x0f.qdrant.VectorsH\x00\x88\x01\x01\x1a=\n\x0cPayloadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.qdrant.Value:\x02\x38\x01\x42\n\n\x08_vectorsJ\x04\x08\x03\x10\x04\"C\n\x0bGetResponse\x12&\n\x06result\x18\x01 \x03(\x0b\x32\x16.qdrant.RetrievedPoint\x12\x0c\n\x04time\x18\x02 \x01(\x01\"F\n\x11RecommendResponse\x12#\n\x06result\x18\x01 \x03(\x0b\x32\x13.qdrant.ScoredPoint\x12\x0c\n\x04time\x18\x02 \x01(\x01\"K\n\x16RecommendBatchResponse\x12#\n\x06result\x18\x01 \x03(\x0b\x32\x13.qdrant.BatchResult\x12\x0c\n\x04time\x18\x02 \x01(\x01\"q\n\x06\x46ilter\x12!\n\x06should\x18\x01 \x03(\x0b\x32\x11.qdrant.Condition\x12\x1f\n\x04must\x18\x02 \x03(\x0b\x32\x11.qdrant.Condition\x12#\n\x08must_not\x18\x03 \x03(\x0b\x32\x11.qdrant.Condition\"\xc2\x01\n\tCondition\x12\'\n\x05\x66ield\x18\x01 \x01(\x0b\x32\x16.qdrant.FieldConditionH\x00\x12,\n\x08is_empty\x18\x02 \x01(\x0b\x32\x18.qdrant.IsEmptyConditionH\x00\x12(\n\x06has_id\x18\x03 \x01(\x0b\x32\x16.qdrant.HasIdConditionH\x00\x12 \n\x06\x66ilter\x18\x04 \x01(\x0b\x32\x0e.qdrant.FilterH\x00\x42\x12\n\x10\x63ondition_one_of\"\x1f\n\x10IsEmptyCondition\x12\x0b\n\x03key\x18\x01 \x01(\t\"1\n\x0eHasIdCondition\x12\x1f\n\x06has_id\x18\x01 \x03(\x0b\x32\x0f.qdrant.PointId\"\xdd\x01\n\x0e\x46ieldCondition\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05match\x18\x02 \x01(\x0b\x32\r.qdrant.Match\x12\x1c\n\x05range\x18\x03 \x01(\x0b\x32\r.qdrant.Range\x12\x30\n\x10geo_bounding_box\x18\x04 \x01(\x0b\x32\x16.qdrant.GeoBoundingBox\x12%\n\ngeo_radius\x18\x05 \x01(\x0b\x32\x11.qdrant.GeoRadius\x12)\n\x0cvalues_count\x18\x06 \x01(\x0b\x32\x13.qdrant.ValuesCount\"_\n\x05Match\x12\x11\n\x07keyword\x18\x01 \x01(\tH\x00\x12\x11\n\x07integer\x18\x02 \x01(\x03H\x00\x12\x11\n\x07\x62oolean\x18\x03 \x01(\x08H\x00\x12\x0e\n\x04text\x18\x04 \x01(\tH\x00\x42\r\n\x0bmatch_value\"k\n\x05Range\x12\x0f\n\x02lt\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x0f\n\x02gt\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12\x10\n\x03gte\x18\x03 \x01(\x01H\x02\x88\x01\x01\x12\x10\n\x03lte\x18\x04 \x01(\x01H\x03\x88\x01\x01\x42\x05\n\x03_ltB\x05\n\x03_gtB\x06\n\x04_gteB\x06\n\x04_lte\"\\\n\x0eGeoBoundingBox\x12\"\n\x08top_left\x18\x01 \x01(\x0b\x32\x10.qdrant.GeoPoint\x12&\n\x0c\x62ottom_right\x18\x02 \x01(\x0b\x32\x10.qdrant.GeoPoint\"=\n\tGeoRadius\x12 \n\x06\x63\x65nter\x18\x01 \x01(\x0b\x32\x10.qdrant.GeoPoint\x12\x0e\n\x06radius\x18\x02 \x01(\x02\"q\n\x0bValuesCount\x12\x0f\n\x02lt\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x0f\n\x02gt\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x10\n\x03gte\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12\x10\n\x03lte\x18\x04 \x01(\x04H\x03\x88\x01\x01\x42\x05\n\x03_ltB\x05\n\x03_gtB\x06\n\x04_gteB\x06\n\x04_lte\"u\n\x0ePointsSelector\x12\'\n\x06points\x18\x01 \x01(\x0b\x32\x15.qdrant.PointsIdsListH\x00\x12 \n\x06\x66ilter\x18\x02 \x01(\x0b\x32\x0e.qdrant.FilterH\x00\x42\x18\n\x16points_selector_one_of\"-\n\rPointsIdsList\x12\x1c\n\x03ids\x18\x01 \x03(\x0b\x32\x0f.qdrant.PointId\"\xd5\x01\n\x0bPointStruct\x12\x1b\n\x02id\x18\x01 \x01(\x0b\x32\x0f.qdrant.PointId\x12\x31\n\x07payload\x18\x03 \x03(\x0b\x32 .qdrant.PointStruct.PayloadEntry\x12%\n\x07vectors\x18\x04 \x01(\x0b\x32\x0f.qdrant.VectorsH\x00\x88\x01\x01\x1a=\n\x0cPayloadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.qdrant.Value:\x02\x38\x01\x42\n\n\x08_vectorsJ\x04\x08\x02\x10\x03\"$\n\x08GeoPoint\x12\x0b\n\x03lon\x18\x01 \x01(\x01\x12\x0b\n\x03lat\x18\x02 \x01(\x01*p\n\tFieldType\x12\x14\n\x10\x46ieldTypeKeyword\x10\x00\x12\x14\n\x10\x46ieldTypeInteger\x10\x01\x12\x12\n\x0e\x46ieldTypeFloat\x10\x02\x12\x10\n\x0c\x46ieldTypeGeo\x10\x03\x12\x11\n\rFieldTypeText\x10\x04*H\n\x0cUpdateStatus\x12\x17\n\x13UnknownUpdateStatus\x10\x00\x12\x10\n\x0c\x41\x63knowledged\x10\x01\x12\r\n\tCompleted\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'points_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SETPAYLOADPOINTS_PAYLOADENTRY._options = None
  _SETPAYLOADPOINTS_PAYLOADENTRY._serialized_options = b'8\001'
  _NAMEDVECTORS_VECTORSENTRY._options = None
  _NAMEDVECTORS_VECTORSENTRY._serialized_options = b'8\001'
  _SCOREDPOINT_PAYLOADENTRY._options = None
  _SCOREDPOINT_PAYLOADENTRY._serialized_options = b'8\001'
  _RETRIEVEDPOINT_PAYLOADENTRY._options = None
  _RETRIEVEDPOINT_PAYLOADENTRY._serialized_options = b'8\001'
  _POINTSTRUCT_PAYLOADENTRY._options = None
  _POINTSTRUCT_PAYLOADENTRY._serialized_options = b'8\001'
  _FIELDTYPE._serialized_start=6294
  _FIELDTYPE._serialized_end=6406
  _UPDATESTATUS._serialized_start=6408
  _UPDATESTATUS._serialized_end=6480
  _POINTID._serialized_start=64
  _POINTID._serialized_end=124
  _VECTOR._serialized_start=126
  _VECTOR._serialized_end=148
  _UPSERTPOINTS._serialized_start=150
  _UPSERTPOINTS._serialized_end=254
  _DELETEPOINTS._serialized_start=256
  _DELETEPOINTS._serialized_end=363
  _GETPOINTS._serialized_start=366
  _GETPOINTS._serialized_end=562
  _SETPAYLOADPOINTS._serialized_start=565
  _SETPAYLOADPOINTS._serialized_end=788
  _SETPAYLOADPOINTS_PAYLOADENTRY._serialized_start=718
  _SETPAYLOADPOINTS_PAYLOADENTRY._serialized_end=779
  _DELETEPAYLOADPOINTS._serialized_start=790
  _DELETEPAYLOADPOINTS._serialized_end=911
  _CLEARPAYLOADPOINTS._serialized_start=913
  _CLEARPAYLOADPOINTS._serialized_end=1026
  _CREATEFIELDINDEXCOLLECTION._serialized_start=1029
  _CREATEFIELDINDEXCOLLECTION._serialized_end=1273
  _DELETEFIELDINDEXCOLLECTION._serialized_start=1275
  _DELETEFIELDINDEXCOLLECTION._serialized_end=1376
  _PAYLOADINCLUDESELECTOR._serialized_start=1378
  _PAYLOADINCLUDESELECTOR._serialized_end=1418
  _PAYLOADEXCLUDESELECTOR._serialized_start=1420
  _PAYLOADEXCLUDESELECTOR._serialized_end=1460
  _WITHPAYLOADSELECTOR._serialized_start=1463
  _WITHPAYLOADSELECTOR._serialized_end=1624
  _NAMEDVECTORS._serialized_start=1627
  _NAMEDVECTORS._serialized_end=1757
  _NAMEDVECTORS_VECTORSENTRY._serialized_start=1695
  _NAMEDVECTORS_VECTORSENTRY._serialized_end=1757
  _VECTORS._serialized_start=1759
  _VECTORS._serialized_end=1862
  _VECTORSSELECTOR._serialized_start=1864
  _VECTORSSELECTOR._serialized_end=1896
  _WITHVECTORSSELECTOR._serialized_start=1898
  _WITHVECTORSSELECTOR._serialized_end=2001
  _SEARCHPARAMS._serialized_start=2003
  _SEARCHPARAMS._serialized_end=2081
  _SEARCHPOINTS._serialized_start=2084
  _SEARCHPOINTS._serialized_end=2478
  _SEARCHBATCHPOINTS._serialized_start=2480
  _SEARCHBATCHPOINTS._serialized_end=2569
  _SCROLLPOINTS._serialized_start=2572
  _SCROLLPOINTS._serialized_end=2852
  _RECOMMENDPOINTS._serialized_start=2855
  _RECOMMENDPOINTS._serialized_end=3294
  _RECOMMENDBATCHPOINTS._serialized_start=3296
  _RECOMMENDBATCHPOINTS._serialized_end=3394
  _COUNTPOINTS._serialized_start=3396
  _COUNTPOINTS._serialized_end=3496
  _POINTSOPERATIONRESPONSE._serialized_start=3498
  _POINTSOPERATIONRESPONSE._serialized_end=3575
  _UPDATERESULT._serialized_start=3577
  _UPDATERESULT._serialized_end=3651
  _SCOREDPOINT._serialized_start=3654
  _SCOREDPOINT._serialized_end=3899
  _SCOREDPOINT_PAYLOADENTRY._serialized_start=718
  _SCOREDPOINT_PAYLOADENTRY._serialized_end=779
  _SEARCHRESPONSE._serialized_start=3901
  _SEARCHRESPONSE._serialized_end=3968
  _BATCHRESULT._serialized_start=3970
  _BATCHRESULT._serialized_end=4020
  _SEARCHBATCHRESPONSE._serialized_start=4022
  _SEARCHBATCHRESPONSE._serialized_end=4094
  _COUNTRESPONSE._serialized_start=4096
  _COUNTRESPONSE._serialized_end=4162
  _SCROLLRESPONSE._serialized_start=4165
  _SCROLLRESPONSE._serialized_end=4304
  _COUNTRESULT._serialized_start=4306
  _COUNTRESULT._serialized_end=4334
  _RETRIEVEDPOINT._serialized_start=4337
  _RETRIEVEDPOINT._serialized_end=4556
  _RETRIEVEDPOINT_PAYLOADENTRY._serialized_start=718
  _RETRIEVEDPOINT_PAYLOADENTRY._serialized_end=779
  _GETRESPONSE._serialized_start=4558
  _GETRESPONSE._serialized_end=4625
  _RECOMMENDRESPONSE._serialized_start=4627
  _RECOMMENDRESPONSE._serialized_end=4697
  _RECOMMENDBATCHRESPONSE._serialized_start=4699
  _RECOMMENDBATCHRESPONSE._serialized_end=4774
  _FILTER._serialized_start=4776
  _FILTER._serialized_end=4889
  _CONDITION._serialized_start=4892
  _CONDITION._serialized_end=5086
  _ISEMPTYCONDITION._serialized_start=5088
  _ISEMPTYCONDITION._serialized_end=5119
  _HASIDCONDITION._serialized_start=5121
  _HASIDCONDITION._serialized_end=5170
  _FIELDCONDITION._serialized_start=5173
  _FIELDCONDITION._serialized_end=5394
  _MATCH._serialized_start=5396
  _MATCH._serialized_end=5491
  _RANGE._serialized_start=5493
  _RANGE._serialized_end=5600
  _GEOBOUNDINGBOX._serialized_start=5602
  _GEOBOUNDINGBOX._serialized_end=5694
  _GEORADIUS._serialized_start=5696
  _GEORADIUS._serialized_end=5757
  _VALUESCOUNT._serialized_start=5759
  _VALUESCOUNT._serialized_end=5872
  _POINTSSELECTOR._serialized_start=5874
  _POINTSSELECTOR._serialized_end=5991
  _POINTSIDSLIST._serialized_start=5993
  _POINTSIDSLIST._serialized_end=6038
  _POINTSTRUCT._serialized_start=6041
  _POINTSTRUCT._serialized_end=6254
  _POINTSTRUCT_PAYLOADENTRY._serialized_start=718
  _POINTSTRUCT_PAYLOADENTRY._serialized_end=779
  _GEOPOINT._serialized_start=6256
  _GEOPOINT._serialized_end=6292
# @@protoc_insertion_point(module_scope)