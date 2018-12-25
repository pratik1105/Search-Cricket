import yamlToCsvData
import sys
import os

if __name__ == "__main__":

	try:
		baseAddress = sys.argv[1];
		outputDirectory = sys.argv[2];
	except IndexError:
		print("Usage: <python-command> <path-to-this-file> <absolute-path-to-base-address-storing-all-yaml-files> <absolute-path-to-output-directory> ");
		sys.exit(1);
	
	for filename in os.listdir(baseAddress):
		if filename == 'README.txt':
			continue;
		print("Converting "+ filename);
		yamlToCsvData.yamlToCsvData(baseAddress+'/'+filename,outputDirectory);

