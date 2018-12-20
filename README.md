# README

The purpose of this system is the prediction api. This is supplied by the prediction server. It makes predictions using a model produced by the training server. The training server trains on the bases of annotations supplied by the annotator server.

## Data files
They interact through the following files:

- /mnt/nfs/projects/trash_recognition/models/predict/output_inference_graph/ - The folder with the trained model used by the prediction server, produced by the training server.
- /mnt/nfs/projects/trash_recognition/data/examples/annotations/label_map.pbtxt - The file with the labels the prediction server must predict. It is also read by the annotator tool and the training server.

- /mnt/nfs/projects/trash_recognition/data/examples/annotations/xmls/ - the annotation xmls produced by the annotator server, and used by the training server to train.
- /mnt/nfs/projects/trash_recognition/data/examples/images/ - the input images used by the training server for training the model
## File formats

### label_map.pbtxt
```
item {
  id: 1 // unique int id for each tag
  name: 'the name of your first tag'
}

item {
  id: 2
  name: 'the name of your second tag'
}

item {
  id: 2
  name: 'etc.'
}
```

### Annotation xml
```
<annotation>
	<folder>less_selected</folder>
	<filename>FILE_NAME.jpg</filename>
	<size>
		<width>800</width>
		<height>597</height>
	</size>
	<segmented>0</segmented>
 	<object>
		<name>LABEL NAME (not id) SPECIFIED IN LABEL_MAP.PBTXT</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>300</xmin>
			<ymin>255</ymin>
			<xmax>345</xmax>
			<ymax>297</ymax>
		</bndbox>
	</object> 	
  	<object>
		<name>LABEL NAME (not id) SPECIFIED IN LABEL_MAP.PBTXT</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>359</xmin>
			<ymin>272</ymin>
			<xmax>408</xmax>
			<ymax>309</ymax>
		</bndbox>
	</object> 
</annotation>
```

xmin, ymin, xmax, ymax are all specified in pixel coordinates in the picture.
Note the tag texts in bold. These are important and must be specified.
the name of the object determines the tag it is assigned, the FILENAME.jpg specifies the image this xml annotates. Though the annotator links xmls and images by filename, the training script does not!!!

## Startup and server control scripts
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
