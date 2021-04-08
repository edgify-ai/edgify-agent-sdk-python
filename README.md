Usage:

from edgify_sdk import EdgifySDK

sdk = EdgifySDK('localhost', 50051)

# take a prediction
prediction = sdk.GetPrediction()

# Autobuy flag
if prediction.certain:
print("using Autobuy")

print('Uuid: ' + prediction.uuid)
print('Predictions: ', prediction.predictions)

# create the ground truth
label = 'Banana'
source = 'RegularMenuSelection'
sdk.CreateGroundTruth(prediction, label, source)

# if you need to delete a sample
sdk.DeleteSample(prediction.uuid)

# inform edgify on transaction start
sdk.StartCustomerTransaction()

# inform edgify on transaction end
sdk.EndCustomerTransaction()
