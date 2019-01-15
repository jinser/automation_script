import sys
import os
import configparser as cfp
import logging
import csv
import xml.etree.cElementTree as ET

sys.path.append('common')
import send_mail as mail
import xml_to_dict as xmlToDict
import database_connect as database
import logging_level as loglevel


def db_select_call(sql,db_conn):
	#Connect to database  date_modified = \'' + str(time_now) + '\'
	db_init=database.MySQLConn( host=db_conn['db_host'],
								port=db_conn['db_port'],
								user=db_conn['db_user'],
								pw=db_conn['db_pw'],
								schema=db_conn['db_schema']
							  )
	finalquery=db_init.SelectQuery(sql)
	return finalquery

#convert csv files to dict
#csv headers can be retrieved by reader.fieldnames
def read_csv_file(file_loc):
	with open(file_loc,'r',encoding='UTF-8') as csvFile:
		reader = csv.DictReader(open(file_loc))
		return reader;

#convert xml files to dict
def read_xml_file(file_loc):
	tree=ET.parse(file_loc)
	root=tree.getroot()
	xmldict = xmlToDict.XmlDictConfig(root)
	return xmldict

#content is a string object
def save_temp_file(file_loc,content):	
	with open(file_loc,"a") as output_file:
		output_file.write(content)
		
def send_email(from_users,to_users,subject,message):
	mail.function(from_users,to_users,subject,message)
	return true

def initialize():
	#Read the properties file and define the variables
	config = cfp.ConfigParser()
	config.read("properties.ini")
	
	#get all property keys in a dict
	property_config = {}
	for section in config.sections():
		for (key,value) in config.items(section):
			property_config[key] = value
		
	#Set logging level based on properties file
	log_level = config.get('Properties','LogLevel')
	log_file = config.get('Properties','LogFile')
	logging.basicConfig(filename=property_config['logfile'], level=loglevel.getLoggingLevel(property_config['loglevel']),format="%(asctime)s:%(levelname)s:%(message)s")
	
	return property_config

def main(properties):
	#DB queries
	sql_query = 'SELECT count(*) FROM TABLE where status=\'PROCESSED\';'
	query_results = db_select_call(sql=sql_query,db_conn=properties);
	num_inserted=query_results[0].get('count(*)')
	logging.info("query: " + str(num_inserted))
	
	#Read from XML file
	xmlDict = read_xml_file(properties['xml_input_location'] + properties['xml_input_filename'])
	
	#Extract lines from a csv file
	input_file_abs_location = properties['file_input_location'] + properties['file_input_filename']
	read_csv_file(file_loc=input_file_abs_location)
	
	#Sending Email notifications
	#send_email(from_users="from@example.com",to_users="to@example.com,to2@example.com",subject="This is a python email",message="this email was sent.")

	
if __name__ == "__main__":
	properties = initialize();
	
	#Run the main code
	main(properties);