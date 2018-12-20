# README

The purpose of this system is the prediction api. This is supplied by the prediction server. It makes predictions using a model produced by the training server. The training server trains on the bases of annotations supplied by the annotator server.

They interact through the following files:

- /mnt/nfs/projects/trash_recognition/models/predict/output_inference_graph/ - The folder with the trained model used by the prediction server, produced by the training server.
- /mnt/nfs/projects/trash_recognition/data/examples/annotations/label_map.pbtxt - The file with the labels the prediction server must predict. It is also read by the annotator tool and the training server.

- /mnt/nfs/projects/trash_recognition/data/examples/annotations/xmls/ - the annotation xmls produced by the annotator server, and used by the training server to train.
- /mnt/nfs/projects/trash_recognition/data/examples/images/ - the input images used by the training server for training the model

## Important files
- /annotation/startup.sh - the startup script for the annotation server
- /image_recognition/training_server/startup.sh - the startup script for the training server
- /image_recognition/prediction_server/startup.sh - the startup script for the training server
- /control/serverManagement/retrain_if_new.py - script that starts up the training server if there are modifications to the images The idea is that this script is run in a cron job.
- /control/serverManagement/config.py - Configuration for retrain_if_new.py:

OLD_IMAGE_DICT_FILE_PATH = 'file path to json file that tracks the last known state of the images'
IMAGE_PATH = 'path to the location of the images'
TRAINING_INSTANCE_ID = 'AWS instance id of the training server'

## TODO
annotation xml changes should also trigger retraining.
