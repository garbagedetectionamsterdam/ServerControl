import json
import config
import os

def compute_current_image_dict():
	current_image_list = list(filter(lambda x: x.endswith('.jpg'), os.listdir(config.IMAGE_PATH)))
	creation_dates = list(map(lambda x: os.path.getmtime(os.path.join(config.IMAGE_PATH, x)), current_image_list))
	current_image_dict = dict(zip(current_image_list, creation_dates))

	return current_image_dict

def retrieve_old_image_dict():
	old_image_dict = None
	if os.path.isfile(config.OLD_IMAGE_DICT_FILE_PATH):
		with open(config.OLD_IMAGE_DICT_FILE_PATH, 'r') as f:
			old_image_dict = json.load(f)

	return old_image_dict

def new_images_exist():

	old_image_dict = retrieve_old_image_dict()

	current_image_dict = compute_current_image_dict()

	return current_image_dict != old_image_dict

def start_training():
	os.system("aws ec2 start-instances --instance-ids " + config.TRAINING_INSTANCE_ID)

def save_current_images_as_old():
	with open(config.OLD_IMAGE_DICT_FILE_PATH, 'w') as f:
		json.dump(compute_current_image_dict(), f)

def run():
	if new_images_exist():
		start_training()

	save_current_images_as_old()

if __name__ == '__main__':
	run()
