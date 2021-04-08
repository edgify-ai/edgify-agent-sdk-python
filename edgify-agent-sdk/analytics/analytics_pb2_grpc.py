# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import analytics.analytics_pb2 as analytics__pb2


class AnalyticsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateEvent = channel.unary_unary(
                '/edgify.AnalyticsService/CreateEvent',
                request_serializer=analytics__pb2.CreateAnalyticsEventRequest.SerializeToString,
                response_deserializer=analytics__pb2.CreateAnalyticsEventResponse.FromString,
                )


class AnalyticsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AnalyticsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateEvent,
                    request_deserializer=analytics__pb2.CreateAnalyticsEventRequest.FromString,
                    response_serializer=analytics__pb2.CreateAnalyticsEventResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'edgify.AnalyticsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AnalyticsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/edgify.AnalyticsService/CreateEvent',
            analytics__pb2.CreateAnalyticsEventRequest.SerializeToString,
            analytics__pb2.CreateAnalyticsEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)