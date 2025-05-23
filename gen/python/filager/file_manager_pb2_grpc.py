# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from filager import file_manager_pb2 as filager_dot_file__manager__pb2

GRPC_GENERATED_VERSION = '1.72.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in filager/file_manager_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class FileManagerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartSending = channel.unary_unary(
                '/filager.FileManagerService/StartSending',
                request_serializer=filager_dot_file__manager__pb2.StartWriteRequest.SerializeToString,
                response_deserializer=filager_dot_file__manager__pb2.StartResponse.FromString,
                _registered_method=True)
        self.SendChunk = channel.unary_unary(
                '/filager.FileManagerService/SendChunk',
                request_serializer=filager_dot_file__manager__pb2.WriteChunk.SerializeToString,
                response_deserializer=filager_dot_file__manager__pb2.WriteResponse.FromString,
                _registered_method=True)
        self.ReadChunk = channel.unary_unary(
                '/filager.FileManagerService/ReadChunk',
                request_serializer=filager_dot_file__manager__pb2.ReadRequest.SerializeToString,
                response_deserializer=filager_dot_file__manager__pb2.GetChunk.FromString,
                _registered_method=True)
        self.CloseSending = channel.unary_unary(
                '/filager.FileManagerService/CloseSending',
                request_serializer=filager_dot_file__manager__pb2.EndRequest.SerializeToString,
                response_deserializer=filager_dot_file__manager__pb2.EndResponse.FromString,
                _registered_method=True)
        self.StartReading = channel.unary_unary(
                '/filager.FileManagerService/StartReading',
                request_serializer=filager_dot_file__manager__pb2.StartReadRequest.SerializeToString,
                response_deserializer=filager_dot_file__manager__pb2.StartResponse.FromString,
                _registered_method=True)


class FileManagerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartSending(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendChunk(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadChunk(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseSending(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartReading(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileManagerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartSending': grpc.unary_unary_rpc_method_handler(
                    servicer.StartSending,
                    request_deserializer=filager_dot_file__manager__pb2.StartWriteRequest.FromString,
                    response_serializer=filager_dot_file__manager__pb2.StartResponse.SerializeToString,
            ),
            'SendChunk': grpc.unary_unary_rpc_method_handler(
                    servicer.SendChunk,
                    request_deserializer=filager_dot_file__manager__pb2.WriteChunk.FromString,
                    response_serializer=filager_dot_file__manager__pb2.WriteResponse.SerializeToString,
            ),
            'ReadChunk': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadChunk,
                    request_deserializer=filager_dot_file__manager__pb2.ReadRequest.FromString,
                    response_serializer=filager_dot_file__manager__pb2.GetChunk.SerializeToString,
            ),
            'CloseSending': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseSending,
                    request_deserializer=filager_dot_file__manager__pb2.EndRequest.FromString,
                    response_serializer=filager_dot_file__manager__pb2.EndResponse.SerializeToString,
            ),
            'StartReading': grpc.unary_unary_rpc_method_handler(
                    servicer.StartReading,
                    request_deserializer=filager_dot_file__manager__pb2.StartReadRequest.FromString,
                    response_serializer=filager_dot_file__manager__pb2.StartResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'filager.FileManagerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('filager.FileManagerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FileManagerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartSending(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/filager.FileManagerService/StartSending',
            filager_dot_file__manager__pb2.StartWriteRequest.SerializeToString,
            filager_dot_file__manager__pb2.StartResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SendChunk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/filager.FileManagerService/SendChunk',
            filager_dot_file__manager__pb2.WriteChunk.SerializeToString,
            filager_dot_file__manager__pb2.WriteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReadChunk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/filager.FileManagerService/ReadChunk',
            filager_dot_file__manager__pb2.ReadRequest.SerializeToString,
            filager_dot_file__manager__pb2.GetChunk.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CloseSending(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/filager.FileManagerService/CloseSending',
            filager_dot_file__manager__pb2.EndRequest.SerializeToString,
            filager_dot_file__manager__pb2.EndResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def StartReading(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/filager.FileManagerService/StartReading',
            filager_dot_file__manager__pb2.StartReadRequest.SerializeToString,
            filager_dot_file__manager__pb2.StartResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
