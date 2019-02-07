#lat.py
# Getting the Elevation of a ground satilight antenna useing the formula:
# ele = arctan((cos(siteSatDif) * sin(siteLon))/(sqrt(1-cos^2(siteSatDif) * cos^2(siteLat))))

import numpy as np
import csv

# Getting the sat name and lon from the user to pass on to the script.
satName = input('What is the sat name?: ')
satLon = input('What is the Sat Lon?: ')
satLon2 = np.float(satLon)

print("Working")

#Opening the CSV output file
outputFile = open("ele_output_" + satName + ".csv", 'a')
outputFile.write(",,,,Elevation," + '\n')

# Opening the .csv with the city lat - lon data
with open('book2.csv', 'r') as cityData:
	reader = csv.reader(cityData)
	for row in reader:

# Getting Data from the city data CSV
		cityName = row[0]
		stateName = row[1]
		siteLon = np.float(row[3])
		siteLat = np.float(row[2])

# Setting siteLot to positive, as the given data had it as a negitive value, and I
#didnt want to edit 36k rows.
		siteLon2 = siteLon * -1
		satSiteDif = satLon2 - siteLon2

#Converting to Radians
		satSiteDifRad = np.deg2rad(satSiteDif)
		siteLatRad = np.deg2rad(siteLat)

# getting the cosines 
		satSiteDifRadCos = np.cos(satSiteDifRad)
		siteLatRadCos = np.cos(siteLatRad)

# Math for the equation
		ele1 = satSiteDifRadCos * siteLatRadCos -.1512
		ele2 = 1 - (satSiteDifRadCos * satSiteDifRadCos * (siteLatRadCos * siteLatRadCos))
		ele3 = np.sqrt(ele2)
		ele4 = ele1 / ele3
		ele5 = np.arctan(ele4)

# Writing the CSV output file		
		outputVar = cityName + ',' + stateName + ',' + satName + ',' + satLon + ',' + str(np.rad2deg(ele5))
		outputFile.write(outputVar + '\n')
		
print("Done")
outputFile.close()
#eof