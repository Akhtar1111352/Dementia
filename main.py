import dataset
import ensemble_trainer
import evaluator
import utils

from config import config

def main(config):

	# Create save directories
	utils.create_directories(config)

	# Prepare and load the data
	if 'silences' in config.model_types:
		print("SILENCES")
		# print("IFF", config.model_types)
		# print("===>> config.dataset_dir", config.dataset_dir)
		# print("CONFIGGG", config)
		data = dataset.prepare_data_new(config.dataset_dir, config)
		test_data = dataset.prepare_test_data(config.test_dataset_dir, config)
		evaluator.evaluate(data, test_data, config)
		#print(data,"DAATAAAA")
	else:
		#print("ELSE")
		data = dataset.prepare_data(config.dataset_dir, config)
		print(data)
	# return
	# Train the ensemble models
	if config.training_type == 'bagging':
		print("bagging")
		ensemble_trainer.bagging_ensemble_training(data, config)
	elif config.training_type == 'boosting':
		ensemble_trainer.boosted_ensemble_training(data, config)

	# Evaluate the model
	if 'silences' not in config.model_types:
		print("YESSS")
		test_data = dataset.prepare_test_data(config.test_dataset_dir, config)
		print(data,"DATAAAA", test_data, "TEST DAATA", config, "CONFIGGG")
		evaluator.evaluate(data, test_data, config)


if __name__ == '__main__':
	main(config)
