#########################
######## IMPORTS ########
#########################

import sim
import os

################################################
############### GLOBAL CONSTANTS ###############
################################################

DAYS = 16						# The number of days in our simulation(MUST MATCH SIM)
RUNS = 1000						# The number of iteration the simulation will be running for. 


def main():
	initialFileSetup()
	simulationLoop()
	fileReformat()
	printFile()




def initialFileSetup():

	avgF = open("AvgFilled.txt", "w+")
	fullBinsF = open("fullBins.txt", "w+")
	excessF = open("excess.txt", "w+")
	totalF = open("total.txt", "w+")

	for line in range(DAYS):
		avgF.write("0\r\n")
		fullBinsF.write("0\r\n")
		excessF.write("0\r\n")
		totalF.write("0\r\n")

	avgF.close()
	fullBinsF.close()
	excessF.close()
	totalF.close()


def simulationLoop():
	for iteration in range(RUNS):
		#print(iteration)
		sim.main()


def fileReformat():
	avgF = open("AvgFilled.txt", "r")
	lines = avgF.readlines()
	avgF.close()
	outAvgF = open("AvgFilled.txt", "w")
	for line in lines:
		outAvgF.write(str(float(line) / RUNS) + '\n')



	fullBinsF = open("fullBins.txt", "r")
	lines = fullBinsF.readlines()
	fullBinsF.close()
	outFullBinsF = open("fullBins.txt", "w")
	for line in lines:
		outFullBinsF.write(str(int(line) / RUNS) + '\n')



	excessF = open("excess.txt", "r")
	lines = excessF.readlines()
	excessF.close()
	outExcessF = open("excess.txt", "w")
	for line in lines:
		outExcessF.write(str(float(line) / RUNS) + '\n')



	totalF = open("total.txt", "r")
	lines = totalF.readlines()
	totalF.close()
	outTotalF = open("total.txt", "w")
	for line in lines:
		outTotalF.write(str(float(line) / RUNS) + '\n')


def printFile():
	avgF = open("AvgFilled.txt", "r")
	fullBinsF = open("fullBins.txt", "r")
	excessF = open("excess.txt", "r")
	totalF = open("total.txt", "r")

	if avgF.mode == "r":
		print("average percent full: \n")
		contents = avgF.read()
		print(contents)

	if fullBinsF.mode == "r":
		print("Number of full bins: \n")
		contents = fullBinsF.read()
		print(contents)

	if excessF.mode == "r":
		print("Amount of excess garbage (KG): \n")
		contents = excessF.read()
		print(contents)

	if totalF.mode == "r":
		print("Amount of total garbage (KG): \n")
		contents = totalF.read()
		print(contents)

	avgF.close()
	fullBinsF.close()
	excessF.close()
	totalF.close()


main()