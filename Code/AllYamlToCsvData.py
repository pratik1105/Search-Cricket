import yamlToCsvData
import sys
import os

if __name__ == "__main__":

	baseAddress = sys.argv[1];
	outputDirectory = sys.argv[2];
	for filename in os.listdir(baseAddress):
		if filename == 'README.txt':
			continue;
		print("Converting "+ filename);
		yamlToCsvData.yamlToCsvData(baseAddress+'/'+filename,outputDirectory);

