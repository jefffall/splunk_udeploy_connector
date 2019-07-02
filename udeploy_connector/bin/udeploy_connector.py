import subprocess, sys, os, datetime
import xml.etree.ElementTree as ET
import gzip
import shutil
import csv

print >>sys.stderr, "udeploy_connector script running.."


alert_xml = []

def log(msg):
	f = open("D:/splunk/var/log/splunk/udeploy_connector.log", "w")
#    print >> f, str(datetime.datetime.now().isoformat()), msg
	print >> f, msg
	f.close()


def logappend(msg):
        f = open("D:/splunk/var/log/splunk/udeploy_connector.log", "a")
        print >> f, msg
        f.close()




#log("got arguments %s" % sys.argv)
#log("got payload: %s" % sys.stdin.read())
alert_xml = sys.stdin.read()
#log(alert_xml)



root = ET.fromstring(alert_xml)

#xmldict = XmlDictConfig(root)

for results in root.iter('results_file'):
	results_csv_gz = results.text

for results in root.iter('field k="host"'):
	host_string = results.txt


results_csv = results_csv_gz[:-3]


with gzip.open(results_csv_gz, 'rb') as f_in:
	with open(results_csv, 'wb') as f_out:
		shutil.copyfileobj(f_in, f_out)




for results in root.iter('param'):
	search_string = results.text


	print >>sys.stderr, "udeploy_connector: Alert search string below"

	print >>sys.stderr, search_string

	print >>sys.stderr, "udeploy_connector - alert search string above"


dict = {} 
with open(results_csv) as f:
    records = csv.DictReader(f)
    for row in records:
        dict = row 

#print ("\n\n\n")

#print dict['_raw']



#alert_output = "Is not present"
#try:
#	alert_output = #root.find(".//field[@k='_raw']/value/text").text
#except Exception:
#	 sys.exc_clear() 

#component = "Is not present"
#try:
#	component = #root.find(".//field[@k='component']/value/text").text
#except Exception:
#	 sys.exc_clear() 

 
#environment = "Is not present"
#try:
#	environment = #root.find(".//field[@k='environment']/value/text").text 
#except Exception:
#	 sys.exc_clear() 

#host = "Is not present"
#try:
#	host = root.find(".//field[@k='host']/value/text").text 
#except Exception:
#	 sys.exc_clear() 


try:
	summary = root.find(".//field[@k='Summary']/value/text").text 

	item = summary.split()

	host = item[0]
	component = item[1]
	environment = item[2]

except Exception:
	component = 'Component is not present'
	environment = 'environment is not present'
	host = 'host is not present'
	summary = 'summary is not present'

	sys.exc_clear() 


incident_number = "incident number is not present"
try:
	incident_number = root.find(".//field[@k='Incident_Number']/value/text").text  
except Exception:
	 sys.exc_clear() 



log("----- Fields Log starts here -----")

logappend( " " )
#logappend( "alert output = " + alert_output + "\n" )
logappend( "component = " + component + "\n" )
logappend( "environment = " + environment + "\n" )
logappend( "host = " + host + "\n" )
logappend( "incident number = " + incident_number )
logappend( " " )



logappend(alert_xml)

for key, value in dict.iteritems():
    logappend ("field = " +  key  + "\t\t\t\t\t" + "value = " +  value )

print >>sys.stderr, "udeploy_connector script done"


hostname = host
incidentnumber = incident_number

try:
	p = subprocess.Popen(['powershell.exe', '-ExecutionPolicy', 'Unrestricted', '-File', 
              '.\splunk_to_uDeploy_prod.ps1', hostname, component, environment, incidentnumber], 
              stdout=sys.stdout)
except subprocess.CalledProcessError, e:
	print >>sys.stderr, "subproces CalledProcessError.output = " + e.output
	
p.communicate()




