from prediction.prediction_pb2_grpc import EdgifyServiceStub
from samples.samples_pb2_grpc import SamplesServiceStub
from analytics.analytics_pb2_grpc import AnalyticsServiceStub
from prediction.prediction_pb2 import *
from analytics.analytics_pb2 import *
from samples.samples_pb2 import *
import grpc

class EdgifySDK(object):

    def __init__(self, host, port):
        grpc_channel = grpc.insecure_channel(host + ':' + str(port))
        self.client = EdgifyServiceStub(grpc_channel)
        self.analytics_client = AnalyticsServiceStub(grpc_channel)
        self.samples_client = SamplesServiceStub(grpc_channel)

    def GetPrediction(self):
        req = PredictionRequest()
        return self.client.GetPrediction(req).prediction

    def CreateGroundTruth(self, prediction, label, source=None):
        req = GroundTruthRequest()
        req.ground_truth.prediction.MergeFrom(prediction)
        req.ground_truth.label = label
        if source is not None:
            req.ground_truth.source = source
        self.client.CreateGroundTruth(req)

    def DeleteSample(self, uuid=None):
        if uuid is not None:
            req = DeleteSampleRequest()
            req.uuid = uuid
            self.samples_client.DeleteSample(req)

    def StartCustomerTransaction(self):
        req = CreateAnalyticsEventRequest()
        req.name = 'TransactionCustomerStart'
        self.analytics_client.CreateEvent(req)

    def EndCustomerTransaction(self):
        req = CreateAnalyticsEventRequest()
        req.name = 'TransactionCustomerEnd'
        self.analytics_client.CreateEvent(req)
