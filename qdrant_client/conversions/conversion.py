from qdrant_client import grpc
from qdrant_client.http.models import models as http


class GrpcToRest:

    @classmethod
    def convert_condition(cls, model: grpc.Condition) -> http.Condition:
        if model.field:
            return cls.convert_field_condition(model.field)
        if model.filter:
            return cls.convert_filter(model.filter)
        if model.has_id:
            return cls.convert_has_id_condition(model.has_id)
        if model.is_empty:
            return cls.convert_is_empty_condition(model.is_empty)

    @classmethod
    def convert_filter(cls, model: grpc.Filter) -> http.Filter:
        return http.Filter(
            must=[cls.convert_condition(condition) for condition in model.must],
            should=[cls.convert_condition(condition) for condition in model.should],
            must_not=[cls.convert_condition(condition) for condition in model.must_not]
        )

    @classmethod
    def convert_range(cls, model: grpc.Range) -> http.Range:
        return http.Range(
            gt=model.gt,
            gte=model.gte,
            lt=model.lt,
            lte=model.lte,
        )

    @classmethod
    def convert_geo_radius(cls, model: grpc.GeoRadius) -> http.GeoRadius:
        return http.GeoRadius(
            center=cls.convert_geo_point(model.center),
            radius=model.radius
        )

    @classmethod
    def convert_collection_description(cls, model: grpc.CollectionDescription) -> http.CollectionDescription:
        return http.CollectionDescription(name=model.name)

    @classmethod
    def convert_collection_info(cls, model: grpc.CollectionInfo) -> http.CollectionInfo:
        return http.CollectionInfo(config=cls.convert_collection_config(model.config),
        disk_data_size=model.disk_data_size,
        optimizer_status=cls.convert_optimizer_status(model.optimizer_status),
        payload_schema=cls.convert_payload_schema(model.payload_schema),
        ram_data_size=model.ram_data_size,
        segments_count=model.segments_count,
        status=cls.convert_collection_status(model.status),
        vectors_count=model.vectors_count
        )

    @classmethod
    def convert_collection_config(cls, model: grpc.CollectionConfig) -> http.CollectionConfig:
        return http.CollectionConfig(
            hnsw_config=cls.convert_hnsw_config(model.hnsw_config),
        optimizer_config=cls.convert_optimizer_config(model.optimizer_config),
        params=cls.convert_collection_params(model.params),
        wal_config=cls.convert_wal_config(model.wal_config)
        )

    @classmethod
    def convert_hnsw_config(cls, model: grpc.HnswConfigDiff) -> http.HnswConfig:
        return http.HnswConfig(ef_construct=model.ef_construct, m=model.m, full_scan_threshold=model.full_scan_threshold)

    @classmethod
    def convert_optimizer_config(cls, model: grpc.OptimizersConfigDiff) -> http.OptimizersConfig:
        return http.OptimizersConfig(
            default_segment_number=model.default_segment_number,
            deleted_threshold=model.deleted_threshold,
            flush_interval_sec=model.flush_interval_sec,
            indexing_threshold=model.indexing_threshold,
            max_optimization_threads=model.max_optimization_threads,
            max_segment_size=model.max_segment_size,
            memmap_threshold=model.memmap_threshold,
            payload_indexing_threshold=model.payload_indexing_threshold,
            vacuum_min_vector_number=model.vacuum_min_vector_number
        )

    @classmethod
    def convert_collection_params(cls, model: grpc.CollectionParams) -> http.CollectionParams:
        return http.CollectionParams(
            distance=cls.convert_distance(model.distance),
            shard_number=model.shard_number,
            vector_size=model.vector_sie
        )

    @classmethod
    def convert_distance(cls, model: grpc.Distance) -> http.Distance:
        if model == grpc.Distance.Cosine:
            return http.Distance.COSINE
        elif model == grpc.Distance.Euclid:
            return http.Distance.EUCLID
        elif model == grpc.Distance.Dot:
            return http.Distance.DOT
        else:
            raise NotImplementedError()


        
    @classmethod
    def convert_update_result(cls, model: grpc.UpdateResult) -> http.UpdateResult:
        return http.UpdateResult(operation_id=model.operation_id, status=cls.convert_update_status(model.status))

    @classmethod
    def convert_update_status(cls, model: grpc.UpdateStatus) -> http.UpdateStatus:
        if model == grpc.UpdateStatus.Acknowledged:
            return http.UpdateStatus.ACKNOWLEDGED
        elif model == grpc.UpdateStatus.Completed:
            return http.UpdateStatus.COMPLETED
        else:
            raise NotImplementedError()

    @classmethod
    def convert_has_id_condition(cls, model: grpc.HasIdCondition) -> http.HasIdCondition:
        return http.HasIdCondition(
            has_id=[cls.convert_point_id(idx) for idx in model.has_id]
        )

    @classmethod
    def convert_point_id(cls, model: grpc.PointId) -> http.ExtendedPointId:
        if model.num:
            return model.num
        if model.uuid:
            return model.uuid
        raise ValueError(f"invalid PointId model: {model}")

    @classmethod
    def convert_delete_alias(cls, model: grpc.DeleteAlias) -> http.DeleteAlias:
        raise NotImplementedError()

    @classmethod
    def convert_rename_alias(cls, model: grpc.RenameAlias) -> http.RenameAlias:
        raise NotImplementedError()

    @classmethod
    def convert_is_empty_condition(cls, model: grpc.IsEmptyCondition) -> http.IsEmptyCondition:
        return http.IsEmptyCondition(is_empty=http.PayloadField(key=model.key))

    @classmethod
    def convert_search_params(cls, model: grpc.SearchParams) -> http.SearchParams:
        raise NotImplementedError()

    @classmethod
    def convert_create_alias(cls, model: grpc.CreateAlias) -> http.CreateAlias:
        raise NotImplementedError()

    @classmethod
    def convert_create_collection(cls, model: grpc.CreateCollection) -> http.CreateCollection:
        raise NotImplementedError()

    @classmethod
    def convert_scored_point(cls, model: grpc.ScoredPoint) -> http.ScoredPoint:
        raise NotImplementedError()

    @classmethod
    def convert_values_count(cls, model: grpc.ValuesCount) -> http.ValuesCount:
        return http.ValuesCount(
            gt=model.gt,
            gte=model.gte,
            lt=model.lt,
            lte=model.lte,
        )

    @classmethod
    def convert_geo_bounding_box(cls, model: grpc.GeoBoundingBox) -> http.GeoBoundingBox:
        return http.GeoBoundingBox(
            bottom_right=cls.convert_geo_point(model.bottom_right),
            top_left=cls.convert_geo_point(model.top_left)
        )

    @classmethod
    def convert_point_struct(cls, model: grpc.PointStruct) -> http.PointStruct:
        raise NotImplementedError()

    @classmethod
    def convert_hnsw_config_diff(cls, model: grpc.HnswConfigDiff) -> http.HnswConfigDiff:
        raise NotImplementedError()

    @classmethod
    def convert_field_condition(cls, model: grpc.FieldCondition) -> http.FieldCondition:
        geo_bounding_box = cls.convert_geo_bounding_box(model.geo_bounding_box) if model.geo_bounding_box else None
        geo_radius = cls.convert_geo_radius(model.geo_radius) if model.geo_radius else None
        match = cls.convert_match(model.match) if model.match else None
        range_ = cls.convert_range(model.range) if model.range else None
        values_count = cls.convert_values_count(model.values_count) if model.values_count else None
        return http.FieldCondition(
            key=model.key,
            geo_bounding_box=geo_bounding_box,
            geo_radius=geo_radius,
            match=match,
            range=range_,
            values_count=values_count,
        )

    @classmethod
    def convert_match(cls, model: grpc.Match) -> http.Match:
        if model.integer:
            return http.MatchValue(value=model.integer)
        if model.boolean:
            return http.MatchValue(value=model.boolean)
        if model.keyword:
            return http.MatchValue(value=model.keyword)
        raise ValueError(f"invalid Match model: {model}")

    @classmethod
    def convert_wal_config_diff(cls, model: grpc.WalConfigDiff) -> http.WalConfigDiff:
        raise NotImplementedError()

    @classmethod
    def convert_collection_config(cls, model: grpc.CollectionConfig) -> http.CollectionConfig:
        raise NotImplementedError()

    @classmethod
    def convert_collection_params(cls, model: grpc.CollectionParams) -> http.CollectionParams:
        raise NotImplementedError()

    @classmethod
    def convert_optimizers_config_diff(cls, model: grpc.OptimizersConfigDiff) -> http.OptimizersConfigDiff:
        raise NotImplementedError()

    @classmethod
    def convert_update_collection(cls, model: grpc.UpdateCollection) -> http.UpdateCollection:
        raise NotImplementedError()

    @classmethod
    def convert_geo_point(cls, model: grpc.GeoPoint) -> http.GeoPoint:
        return http.GeoPoint(
            lat=model.lat,
            lon=model.lon,
        )

    @classmethod
    def convert_alias_operations(cls, model: grpc.AliasOperations) -> http.AliasOperations:
        raise NotImplementedError()

    @classmethod
    def convert_points_selector(cls, model: grpc.PointsSelector) -> http.PointsSelector:
        raise NotImplementedError()


class RestToGrpc:
    @classmethod
    def convert_filter(cls, model: http.Filter) -> grpc.Filter:
        raise NotImplementedError()

    @classmethod
    def convert_range(cls, model: http.Range) -> grpc.Range:
        raise NotImplementedError()

    @classmethod
    def convert_geo_radius(cls, model: http.GeoRadius) -> grpc.GeoRadius:
        raise NotImplementedError()

    @classmethod
    def convert_collection_description(cls, model: http.CollectionDescription) -> grpc.CollectionDescription:
        raise NotImplementedError()

    @classmethod
    def convert_collection_info(cls, model: http.CollectionInfo) -> grpc.CollectionInfo:
        raise NotImplementedError()

    @classmethod
    def convert_update_result(cls, model: http.UpdateResult) -> grpc.UpdateResult:
        raise NotImplementedError()

    @classmethod
    def convert_has_id_condition(cls, model: http.HasIdCondition) -> grpc.HasIdCondition:
        raise NotImplementedError()

    @classmethod
    def convert_delete_alias(cls, model: http.DeleteAlias) -> grpc.DeleteAlias:
        raise NotImplementedError()

    @classmethod
    def convert_rename_alias(cls, model: http.RenameAlias) -> grpc.RenameAlias:
        raise NotImplementedError()

    @classmethod
    def convert_is_empty_condition(cls, model: http.IsEmptyCondition) -> grpc.IsEmptyCondition:
        raise NotImplementedError()

    @classmethod
    def convert_search_params(cls, model: http.SearchParams) -> grpc.SearchParams:
        raise NotImplementedError()

    @classmethod
    def convert_create_alias(cls, model: http.CreateAlias) -> grpc.CreateAlias:
        raise NotImplementedError()

    @classmethod
    def convert_create_collection(cls, model: http.CreateCollection) -> grpc.CreateCollection:
        raise NotImplementedError()

    @classmethod
    def convert_scored_point(cls, model: http.ScoredPoint) -> grpc.ScoredPoint:
        raise NotImplementedError()

    @classmethod
    def convert_values_count(cls, model: http.ValuesCount) -> grpc.ValuesCount:
        raise NotImplementedError()

    @classmethod
    def convert_geo_bounding_box(cls, model: http.GeoBoundingBox) -> grpc.GeoBoundingBox:
        raise NotImplementedError()

    @classmethod
    def convert_point_struct(cls, model: http.PointStruct) -> grpc.PointStruct:
        raise NotImplementedError()

    @classmethod
    def convert_hnsw_config_diff(cls, model: http.HnswConfigDiff) -> grpc.HnswConfigDiff:
        raise NotImplementedError()

    @classmethod
    def convert_field_condition(cls, model: http.FieldCondition) -> grpc.FieldCondition:
        raise NotImplementedError()

    @classmethod
    def convert_wal_config_diff(cls, model: http.WalConfigDiff) -> grpc.WalConfigDiff:
        raise NotImplementedError()

    @classmethod
    def convert_collection_config(cls, model: http.CollectionConfig) -> grpc.CollectionConfig:
        raise NotImplementedError()

    @classmethod
    def convert_collection_params(cls, model: http.CollectionParams) -> grpc.CollectionParams:
        raise NotImplementedError()

    @classmethod
    def convert_optimizers_config_diff(cls, model: http.OptimizersConfigDiff) -> grpc.OptimizersConfigDiff:
        raise NotImplementedError()

    @classmethod
    def convert_update_collection(cls, model: http.UpdateCollection) -> grpc.UpdateCollection:
        raise NotImplementedError()

    @classmethod
    def convert_geo_point(cls, model: http.GeoPoint) -> grpc.GeoPoint:
        raise NotImplementedError()

    @classmethod
    def convert_match(cls, model: http.Match) -> grpc.Match:
        raise NotImplementedError()

    @classmethod
    def convert_alias_operations(cls, model: http.AliasOperations) -> grpc.AliasOperations:
        raise NotImplementedError()

    @classmethod
    def convert_points_selector(cls, model: http.PointsSelector) -> grpc.PointsSelector:
        raise NotImplementedError()

    @classmethod
    def convert_condition(cls, model: http.Condition) -> grpc.Condition:
        raise NotImplementedError()