# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import prediction.prediction_pb2 as prediction__pb2


class EdgifyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPrediction = channel.unary_unary(
                '/edgify.EdgifyService/GetPrediction',
                request_serializer=prediction__pb2.PredictionRequest.SerializeToString,
                response_deserializer=prediction__pb2.PredictionResponse.FromString,
                )
        self.CreateGroundTruth = channel.unary_unary(
                '/edgify.EdgifyService/CreateGroundTruth',
                request_serializer=prediction__pb2.GroundTruthRequest.SerializeToString,
                response_deserializer=prediction__pb2.GroundTruthResponse.FromString,
                )
        self.GetCurrentModelDeployment = channel.unary_unary(
                '/edgify.EdgifyService/GetCurrentModelDeployment',
                request_serializer=prediction__pb2.GetCurrentModelDeploymentRequest.SerializeToString,
                response_deserializer=prediction__pb2.GetCurrentModelDeploymentResponse.FromString,
                )


class EdgifyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPrediction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateGroundTruth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCurrentModelDeployment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EdgifyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPrediction': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPrediction,
                    request_deserializer=prediction__pb2.PredictionRequest.FromString,
                    response_serializer=prediction__pb2.PredictionResponse.SerializeToString,
            ),
            'CreateGroundTruth': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateGroundTruth,
                    request_deserializer=prediction__pb2.GroundTruthRequest.FromString,
                    response_serializer=prediction__pb2.GroundTruthResponse.SerializeToString,
            ),
            'GetCurrentModelDeployment': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCurrentModelDeployment,
                    request_deserializer=prediction__pb2.GetCurrentModelDeploymentRequest.FromString,
                    response_serializer=prediction__pb2.GetCurrentModelDeploymentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'edgify.EdgifyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EdgifyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPrediction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/edgify.EdgifyService/GetPrediction',
            prediction__pb2.PredictionRequest.SerializeToString,
            prediction__pb2.PredictionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateGroundTruth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/edgify.EdgifyService/CreateGroundTruth',
            prediction__pb2.GroundTruthRequest.SerializeToString,
            prediction__pb2.GroundTruthResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCurrentModelDeployment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/edgify.EdgifyService/GetCurrentModelDeployment',
            prediction__pb2.GetCurrentModelDeploymentRequest.SerializeToString,
            prediction__pb2.GetCurrentModelDeploymentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
