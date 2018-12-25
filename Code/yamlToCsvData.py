import yaml
import csv
import sys

def defaultValues(data,inning):
	Dictionary = {'innings': inning+1,'ball': 0.0, 'batsman': 'NA', 'bowler': 'NA', 'extras': 'NA', 'non_striker': 'NA' , 'batsman_run': 0, 'extras_run': 0, 'total_run': 0, 'wicket': 0, 'fielders': 'NA', 'wicket_kind': 'NA', 'player_out': 'NA'};
	return Dictionary;	

def writeDelivery(Dictionary,delivery):
	for keys, values in delivery.items():
		Dictionary['ball']=keys;
		for key, value in values.items():
			if key == 'batsman' or key == 'bowler' or key == 'non_striker' :
				Dictionary[key]=value;
			if key == 'extras' :
				for kind , run in value.items():
					Dictionary[key]=str(run)+kind;
			if key == 'runs' :
				Dictionary['batsman_run']=value['batsman'];
				Dictionary['extras_run']=value['extras'];
				Dictionary['total_run']=value['total'];	
			if key == 'wicket' :
				Dictionary['wicket']=1;
				if 'fielders' in value:
					Dictionary['fielders']=value['fielders'][0];
				Dictionary['wicket_kind']=value['kind'];
				Dictionary['player_out']=value['player_out'];


def writeAllDeliveries(writer,data,inning):
	if inning==0:
		innings='1st innings';
	elif inning==1:
		innings='2nd innings';
	elif inning ==2:
		innings= data["innings"][1]['2nd innings']['team']+ " Super Over";
	elif inning ==3:
		innings= data["innings"][0]['1st innings']['team']+ " Super Over";


	for delivery in data["innings"][inning][innings]["deliveries"]:
		Dictionary = defaultValues(data,inning);
		writeDelivery(Dictionary,delivery);
		writer.writerow(Dictionary);

def writeToCsv(data,outputFileName,outputDirectory):
	fieldnames = ['innings','ball','batsman','bowler','extras','non_striker','batsman_run','extras_run','total_run','wicket','fielders','wicket_kind','player_out'];
	with open(outputDirectory + '/' + outputFileName,mode='w') as csv_file:	
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader();
		for inning in range(len(data["innings"])):
			writeAllDeliveries(writer,data,inning);

def yamlToCsvData(filename,outputDirectory):
	with open(filename,'r') as stream:
		data=(yaml.load(stream));
	team1=data['info']['teams'][0];
	team2=data['info']['teams'][1];
	date=str(data['info']['dates'][0]);
	outputFileName=team1+'_'+team2+'_'+date+'.csv';
	writeToCsv(data,outputFileName,outputDirectory);
			
			
if __name__ == "__main__":

	try:
		filename = sys.argv[1];
		outputDirectory = sys.argv[2];
	except IndexError:
		print("Usage: <python-command> <path-to-this-file> <absolute-path-to-yaml-file> <absolute-path-to-output-directory> ");
		sys.exit(1);

	yamlToCsvData(filename,outputDirectory);