# README

## Important files
- /annotation/startup.sh - the startup script for the annotation server
- /image_recognition/training_server/startup.sh - the startup script for the training server
- /image_recognition/prediction_server/startup.sh - the startup script for the training server
- /control/serverManagement/retrain_if_new.py - script that starts up the training server if there are modifications to the image annotation xmls. The idea is that this script is run in a cron job.
