import csv

#basic code to parse a tsv file 
#can access column data by row['value'] where 'value' is the column name

with open('mydata.tsv') as tsvfile:
	reader = csv.DictReader(tsvfile, dialect='excel-tab')
	for row in reader:
		print(row)