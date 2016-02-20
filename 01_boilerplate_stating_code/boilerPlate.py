"""
@author: Mohamed Ali Jamaoui 
@description: boilerplate code structure for the machine learning club 

"""

import pandas as pd 
import argparse 
import sys 

class BoilerPlate():
	def __init__(self):
		pass 

	def writeMessage(self, message, mode="D"):
		"""
		a wrapper function to write debug messages
		@param message: a string that is the message to write 
		@param mode: the mode in which to yield the message 
		@return None 
		"""
		#dictionary to hold all possible debug modes 
		#3 modes, names are self expanatory 
		debug_modes = {"D":"DEBUG:", "W":"WARNING:", "E":"ERROR:"}
		print debug_modes[mode],message
		return

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
		options = self.processInputArguments(sys.argv[1:])
		training_data = options["training_data"]
		test_data = options["test_data"]

		self.writeMessage("loading training data","D")
		train = pd.read_csv(training_data, delimiter=",")

		self.writeMessage("loading test data","D")
		test = pd.read_csv(test_data, delimiter=",")
		
		self.writeMessage("doing some data cleansing stuff")
		self.writeMessage("doing some cool machine learning ")		

		self.writeMessage("finishing and writing out results")

		return 


if __name__ == '__main__':
	bp = BoilerPlate()
	bp.main()