# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import samples.samples_pb2 as samples__pb2


class SamplesServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSamples = channel.unary_unary(
                '/edgify.SamplesService/GetSamples',
                request_serializer=samples__pb2.GetSamplesRequest.SerializeToString,
                response_deserializer=samples__pb2.GetSamplesResponse.FromString,
                )
        self.AddSample = channel.unary_unary(
                '/edgify.SamplesService/AddSample',
                request_serializer=samples__pb2.AddSampleRequest.SerializeToString,
                response_deserializer=samples__pb2.AddSampleResponse.FromString,
                )
        self.UpdateSample = channel.unary_unary(
                '/edgify.SamplesService/UpdateSample',
                request_serializer=samples__pb2.UpdateSampleRequest.SerializeToString,
                response_deserializer=samples__pb2.UpdateSampleResponse.FromString,
                )
        self.Sync = channel.unary_unary(
                '/edgify.SamplesService/Sync',
                request_serializer=samples__pb2.SyncRequest.SerializeToString,
                response_deserializer=samples__pb2.SyncResponse.FromString,
                )
        self.DeleteAllSamples = channel.unary_unary(
                '/edgify.SamplesService/DeleteAllSamples',
                request_serializer=samples__pb2.DeleteAllSamplesRequest.SerializeToString,
                response_deserializer=samples__pb2.DeleteAllSamplesResponse.FromString,
                )
        self.DeleteSamples = channel.unary_unary(
                '/edgify.SamplesService/DeleteSamples',
                request_serializer=samples__pb2.DeleteSamplesRequest.SerializeToString,
                response_deserializer=samples__pb2.DeleteSamplesResponse.FromString,
                )
        self.DeleteSample = channel.unary_unary(
                '/edgify.SamplesService/DeleteSample',
                request_serializer=samples__pb2.DeleteSampleRequest.SerializeToString,
                response_deserializer=samples__pb2.DeleteSampleResponse.FromString,
                )


class SamplesServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSamples(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddSample(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSample(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sync(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAllSamples(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSamples(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSample(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SamplesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSamples': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSamples,
                    request_deserializer=samples__pb2.GetSamplesRequest.FromString,
                    response_serializer=samples__pb2.GetSamplesResponse.SerializeToString,
            ),
            'AddSample': grpc.unary_unary_rpc_method_handler(
                    servicer.AddSample,
                    request_deserializer=samples__pb2.AddSampleRequest.FromString,
                    response_serializer=samples__pb2.AddSampleResponse.SerializeToString,
            ),
            'UpdateSample': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSample,
                    request_deserializer=samples__pb2.UpdateSampleRequest.FromString,
                    response_serializer=samples__pb2.UpdateSampleResponse.SerializeToString,
            ),
            'Sync': grpc.unary_unary_rpc_method_handler(
                    servicer.Sync,
                    request_deserializer=samples__pb2.SyncRequest.FromString,
                    response_serializer=samples__pb2.SyncResponse.SerializeToString,
            ),
            'DeleteAllSamples': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAllSamples,
                    request_deserializer=samples__pb2.DeleteAllSamplesRequest.FromString,
                    response_serializer=samples__pb2.DeleteAllSamplesResponse.SerializeToString,
            ),
            'DeleteSamples': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteSamples,
                    request_deserializer=samples__pb2.DeleteSamplesRequest.FromString,
                    response_serializer=samples__pb2.DeleteSamplesResponse.SerializeToString,
            ),
            'DeleteSample': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteSample,
                    request_deserializer=samples__pb2.DeleteSampleRequest.FromString,
                    response_serializer=samples__pb2.DeleteSampleResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'edgify.SamplesService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SamplesService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSamples(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/edgify.SamplesService/GetSamples',
            samples__pb2.GetSamplesRequest.SerializeToString,
            samples__pb2.GetSamplesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddSample(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/edgify.SamplesService/AddSample',
            samples__pb2.AddSampleRequest.SerializeToString,
            samples__pb2.AddSampleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateSample(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/edgify.SamplesService/UpdateSample',
            samples__pb2.UpdateSampleRequest.SerializeToString,
            samples__pb2.UpdateSampleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sync(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/edgify.SamplesService/Sync',
            samples__pb2.SyncRequest.SerializeToString,
            samples__pb2.SyncResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAllSamples(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/edgify.SamplesService/DeleteAllSamples',
            samples__pb2.DeleteAllSamplesRequest.SerializeToString,
            samples__pb2.DeleteAllSamplesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteSamples(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/edgify.SamplesService/DeleteSamples',
            samples__pb2.DeleteSamplesRequest.SerializeToString,
            samples__pb2.DeleteSamplesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteSample(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/edgify.SamplesService/DeleteSample',
            samples__pb2.DeleteSampleRequest.SerializeToString,
            samples__pb2.DeleteSampleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
