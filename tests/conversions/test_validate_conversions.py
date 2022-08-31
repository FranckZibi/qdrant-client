import inspect
import re
from inspect import getmembers

from google.protobuf.json_format import MessageToDict
from loguru import logger

from tests.conversions.fixtures import get_grpc_fixture, fixtures as class_fixtures


def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def test_conversion_completeness():
    from qdrant_client.conversions.conversion import GrpcToRest, RestToGrpc

    grpc_to_rest_convert = dict(
        (method_name, method) for method_name, method
        in getmembers(GrpcToRest) if method_name.startswith("convert_")
    )

    rest_to_grpc_convert = dict(
        (method_name, method) for method_name, method
        in getmembers(RestToGrpc) if method_name.startswith("convert_")
    )

    for model_class_name in class_fixtures:
        convert_function_name = f"convert_{camel_to_snake(model_class_name)}"

        fixtures = get_grpc_fixture(model_class_name)
        for fixture in fixtures:
            if fixture is ...:
                logger.warning(f"Fixture for {model_class_name} skipped")
                continue

            try:
                result = list(inspect.signature(grpc_to_rest_convert[convert_function_name]).parameters.keys())
                if 'collection_name' in result:
                    rest_fixture = grpc_to_rest_convert[convert_function_name](
                        fixture,
                        collection_name=fixture.collection_name
                    )
                else:
                    rest_fixture = grpc_to_rest_convert[convert_function_name](fixture)

                back_convert_function_name = convert_function_name

                result = list(inspect.signature(rest_to_grpc_convert[back_convert_function_name]).parameters.keys())
                if 'collection_name' in result:
                    grpc_fixture = rest_to_grpc_convert[back_convert_function_name](
                        rest_fixture,
                        collection_name=fixture.collection_name
                    )
                else:
                    grpc_fixture = rest_to_grpc_convert[back_convert_function_name](rest_fixture)
            except Exception as e:
                logger.warning(f"Error with {fixture}")
                raise e

            assert MessageToDict(grpc_fixture) == MessageToDict(fixture), f"{model_class_name} conversion is broken"


def test_vector_batch_conversion():
    from qdrant_client import grpc

    from qdrant_client.conversions.conversion import RestToGrpc
    batch = []
    res = RestToGrpc.convert_batch_vector_struct(batch, 1)
    assert len(res) == 0

    batch = {}
    res = RestToGrpc.convert_batch_vector_struct(batch, 1)
    assert len(res) == 1
    assert res == [grpc.Vectors(vectors=grpc.NamedVectors(vectors={}))]

    batch = []
    res = RestToGrpc.convert_batch_vector_struct(batch, 1)
    assert len(res) == 0

    batch = [[]]
    res = RestToGrpc.convert_batch_vector_struct(batch, 1)
    assert len(res) == 1
    assert res == [grpc.Vectors(vector=grpc.Vector(data=[]))]

    batch = [[1, 2, 3]]
    res = RestToGrpc.convert_batch_vector_struct(batch, 1)
    assert len(res) == 1
    assert res == [grpc.Vectors(vector=grpc.Vector(data=[1, 2, 3]))]

    batch = [[1, 2, 3]]
    res = RestToGrpc.convert_batch_vector_struct(batch, 1)
    assert len(res) == 1
    assert res == [grpc.Vectors(vector=grpc.Vector(data=[1, 2, 3]))]

    batch = [[1, 2, 3], [3, 4, 5]]
    res = RestToGrpc.convert_batch_vector_struct(batch, 0)
    assert len(res) == 2
    assert res == [grpc.Vectors(vector=grpc.Vector(data=[1, 2, 3])), grpc.Vectors(vector=grpc.Vector(data=[3, 4, 5]))]

    batch = {"image": [[1, 2, 3]]}
    res = RestToGrpc.convert_batch_vector_struct(batch, 1)
    assert len(res) == 1
    assert res == [grpc.Vectors(vectors=grpc.NamedVectors(vectors={"image": grpc.Vector(data=[1, 2, 3])}))]

    batch = {"image": [[1, 2, 3], [3, 4, 5]]}
    res = RestToGrpc.convert_batch_vector_struct(batch, 2)
    assert len(res) == 2
    assert res == [grpc.Vectors(vectors=grpc.NamedVectors(vectors={"image": grpc.Vector(data=[1, 2, 3])})),
                   grpc.Vectors(vectors=grpc.NamedVectors(vectors={"image": grpc.Vector(data=[3, 4, 5])}))]

    batch = {"image": [[1, 2, 3], [3, 4, 5]],
             "restaurants": [[6, 7, 8], [9, 10, 11]]}
    res = RestToGrpc.convert_batch_vector_struct(batch, 2)
    assert len(res) == 2
    assert res == [grpc.Vectors(vectors=grpc.NamedVectors(vectors={"image": grpc.Vector(data=[1, 2, 3]), "restaurants": grpc.Vector(data=[6, 7, 8])})),
                   grpc.Vectors(vectors=grpc.NamedVectors(vectors={"image": grpc.Vector(data=[3, 4, 5]), "restaurants": grpc.Vector(data=[9, 10, 11])}))]

