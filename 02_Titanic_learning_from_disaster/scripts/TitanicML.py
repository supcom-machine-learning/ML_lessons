"""
@author: Mohamed Ali Jamaoui 
@description: submission script for "Titanic: machine learning from disaster" competition

"""

import pandas as pd 
import argparse 
import sys 
from sklearn.preprocessing import LabelEncoder 
from sklearn.ensemble import RandomForestClassifier

class TitanicML():
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

	def encodeLabels(self, data, columns_to_encode):
		"""
		@param data: original dataframe 
		@param columns_to_encode: list of column names to encode 
		"""
		data[columns_to_encode] = data[columns_to_encode].apply(LabelEncoder().fit_transform)
		return data

	def removeColumns(self, data, columns_to_remove):
		return data[data.columns.difference(columns_to_remove)]

	def fillingMissingValues(self, data): 
		return data.fillna(data.mean(), inplace=True)

	def applyRandomForestClassifier(self, train, test):
		#init algorithm 
		RFC = RandomForestClassifier()

		#training target 
		y_train = train[["Survived"]]
		x_train = train[train.columns.difference(["PassengerId","Survived"])]

		#fitting 
		RFC.fit(x_train, y_train)

		result = RFC.predict(test[test.columns.difference(["PassengerId"])])

		self.writeMessage("current training score")
		print RFC.score(x_train, y_train)
		
		test["Survived"] = result 

		return test 


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
		
		self.writeMessage("remove irrelevant columns", "D")
		columns_to_remove = ["Name","Ticket","Cabin","Fare"]
		train = self.removeColumns(train, columns_to_remove)
		test = self.removeColumns(test, columns_to_remove)

		self.writeMessage("encoding categorical variables","D")
		train = self.encodeLabels(train, ["Sex","Embarked"])
		test = self.encodeLabels(test, ["Sex","Embarked"])

		self.writeMessage("data after preprocessing")
		print "train"
		print train.head()
		print "shape", train.shape


		print "nulls in train"
		print train.isnull().sum()
		print "nulls in test"
		print test.isnull().sum()

		self.fillingMissingValues(train)
		self.fillingMissingValues(test)
		

		print "nulls in train"
		print train.isnull().sum()
		print "nulls in test"
		print test.isnull().sum()


		self.writeMessage("Prediction")
		rs = self.applyRandomForestClassifier(train ,test)

		self.writeMessage("writing results")
		rs[["PassengerId","Survived"]].to_csv("prediction.csv", index=False)


if __name__ == '__main__':
	TML = TitanicML()
	TML.main()