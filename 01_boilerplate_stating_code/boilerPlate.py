"""
@author: Mohamed Ali Jamaoui 
@description: starter code for data science projects  

"""

import pandas as pd 
import argparse 
import sys 
import logging 
import json 

class BoilerPlate():
	def __init__(self):
		pass

	def readConfigurationFile(self, configuration_file_name):
		"""
		@description: read a json configuration file 
		@param : configuration file name 
		@return : the configuration object  
		"""
		with open(configuration_file_name, "r") as config_file:
			configuration_info = json.load(config_file)

		return configuration_info


	def processInputArguments(self,args):
		parser = argparse.ArgumentParser(description="Starter code for data science projects")

		#train data file name 
		parser.add_argument('-td',
							'--training-data',
							type=str,
							dest='training_data',
							help='training data file'
							)

		#test data file name 
		parser.add_argument('-tsd',
							'--test-data',
							type=str,
							dest='test_data',
							help='test data file'
							)
		
		#test data file name 
		parser.add_argument('-jc',
							'--json-configuration-file',
							type=str,
							dest='json_configuration_file',
							help='json configuration file'
							)

		## show help if no arguments passed 
		if len(sys.argv)==1:
			parser.print_help()
			sys.exit(1)

		#apply the parser to the argument list 
		options = parser.parse_args(args)
		return vars(options)

	def main(self):

		##### Set up python logging format ###### 
		log_format='%(asctime)s %(levelname)s %(message)s'
		logging.basicConfig(format=log_format, level=logging.INFO)


		##### Set up command command line parsing config ###### 
		options = self.processInputArguments(sys.argv[1:])
		training_data = options["training_data"]
		test_data = options["test_data"]
		json_configuration_file = options["json_configuration_file"]

		##### loading json configuration parameters ###### 
		json_configs = self.readConfigurationFile(json_configuration_file)


		##### load training data ###### 
		logging.info("loading training data")
		train = pd.read_csv(training_data, delimiter=",")
		print(train.head())
		

		logging.info("loading test data")
		test = pd.read_csv(test_data, delimiter=",")

		print(train.head())
		
		logging.info("doing some data cleansing stuff")
		logging.info("doing some cool machine learning ")		

		logging.info("finishing and writing out results")

		return 


if __name__ == '__main__':
	bp = BoilerPlate()
	bp.main()