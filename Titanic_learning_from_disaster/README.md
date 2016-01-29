# Drafting a machine learning solution 

This is the code skeleton on how to define a machine learning draft solution.  
study case: kaggle competition - Titanic learning from disaster
Link: https://www.kaggle.com/c/titanic 

Folder structure:

	 $tree 
	.
	├── data
	│   ├── test.csv
	│   └── train.csv
	├── prediction.csv
	├── README.md
	└── scripts
	    └── worksript.py

	2 directories, 5 files
	 
How to run the script: 
	
	$time python scripts/worksript.py -td data/train.csv -tsd data/test.csv 
	
The output is a file called prediction.csv 