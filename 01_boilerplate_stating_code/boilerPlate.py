"""
@author: Mohamed Ali Jamaoui 
@description: boilerplate code structure for the machine learning club 

"""

import pandas as pd 
import argparse 
import sys 
import logging 

class BoilerPlate():
	def __init__(self):
		pass 

	def processInputArguments(self,args):
		parser = argparse.ArgumentParser(description="Titanic: machine learning from disaster")

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

		#apply the parser to the argument list 
		options = parser.parse_args(args)
		return vars(options)

	def main(self):

		##### Set up python logging format ###### 
		log_format='%(asctime)s %(levelname)s %(message)s'
		logging.basicConfig(format=log_format, level=logging.DEBUG)


		##### Set up command command line parsing config ###### 
		options = self.processInputArguments(sys.argv[1:])
		training_data = options["training_data"]
		test_data = options["test_data"]


		##### load training data ###### 
		logging.info("loading training data","D")
		train = pd.read_csv(training_data, delimiter=",")
		

		logging.info("loading test data","D")
		test = pd.read_csv(test_data, delimiter=",")
		
		logging.info("doing some data cleansing stuff")
		logging.info("doing some cool machine learning ")		

		logging.info("finishing and writing out results")

		return 


if __name__ == '__main__':
	bp = BoilerPlate()
	bp.main()