# az.py
# Falowing the equation azi = pi + arctan(tan(satSiteDif)/sin(siteLon))

import numpy as np
import csv

# Getting the sat name and lon from the user to pass on to the script.

satName = input('What is the sat name?: ')
satLon = input('What is the Sat Lon?: ')
satLon2 = np.float(satLon)
print("Working")

# Opening the output file
outputFile = open("az_output_" + satName + ".csv", 'a')

# Adding blank cols to the CSV
outputFile.write(",,,,Azimuth,," '\n')

# Opening the .csv with the city lat - lon data
with open('book2.csv', 'r') as cityData:
	reader = csv.reader(cityData)

# Getting data from the CSV and setting var's
	for row in reader:
		cityName = row[0]
		stateName = row[1]
		siteLon = np.float(row[3])
		siteLat = np.float(row[2])
		siteLon2 = siteLon * -1
		satSiteDif = satLon2 - siteLon2

#Converting to Radians
		satSiteDifRad = np.deg2rad(satSiteDif)
		siteLatRad = np.deg2rad(siteLat)

#getting the tan and sin of satSiteDifRad and siteLatRad
		satSiteDifRadTan = np.tan(satSiteDifRad)
		siteLatRadSin = np.sin(siteLatRad)
# The Actual math for the equation, or whatever
		azi1 = satSiteDifRadTan / siteLatRadSin
		azi2 = np.arctan(azi1)
		azi3 = azi2 + np.pi
		
		# writing to the CSV file
		outputVar = cityName + ',' + stateName + ',' + satName + ',' + satLon + ',' + str(np.rad2deg(azi3))
		outputFile.write(outputVar + '\n')

outputFile.close()
print("Done")
#EOF