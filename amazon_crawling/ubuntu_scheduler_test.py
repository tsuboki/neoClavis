import datetime
import csv
import os.path

#testoutputfile = "/home/tsuboki.y/neoClavis/ubuntuScheudlerTest/TestResults.csv"
testoutputfile = "TestResults.csv"

output_file = open(testoutputfile, "a", encoding="utf-8")
writer = csv.writer(output_file, lineterminator='\n')
writer.writerow([str(datetime.datetime.now().strftime("%Y%m%d")), str(datetime.datetime.now().strftime("%H:%M:%S"))])
output_file.close()
