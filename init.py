from BubbleSort import *

def listToString(inList):
	string = ""
	for i in inList:
		string += str(i) + " "
	return string.strip()


if __name__ == "__main__":
	while True:
		# choose sorting type
		sortingType = input("What type of sorting algorithm would you like to do?\n\
			Choose from: MERGE, INSERTION, BUBBLE, QUICK, or HEAP. ")
		# Check their response is correct
		while sortingType.upper() not in ["MERGE", "INSERTION", "BUBBLE", "QUICK", "HEAP"]:
			sortingType = input("What type of sorting algorithm would you like to do?\n\
			Choose from: MERGE, INSERTION, BUBBLE, QUICK, or HEAP. ")

		# create list of numbers to sort
		numsToSort = input("Enter in a list of integers to be sorted separated by spaces. ")
		# check the input to make sure it is all ints
		numsToSort = numsToSort.strip().split(" ")
		badInput = False
		for num_index in range(len(numsToSort)):
			try:
				numsToSort[num_index] = int(numsToSort[num_index].strip())
			except ValueError:
				print("The following CANNOT be sorted: %s. " % (numsToSort[num_index].strip()))
				badInput = True
				break

		if badInput == False:
			# if no comma is in the string and the string can be turned into an int,
			# then it is already sorted
			if len(numsToSort) == 1:
				print("The sorted list is: %s." % (numsToSort.strip()))
			else:
				# call the sorting function
				if sortingType.upper() == "MERGE":
					None
				elif sortingType.upper() == "INSERTION":
					None
				elif sortingType.upper() == "BUBBLE":
					bubbleSort(numsToSort)
				elif sortingType.upper() == "QUICK":
					None
				else:
					None
				print("The sorted list is: %s." % (listToString(numsToSort)))

		runLoop = input("Would you like to do another sort?\n Enter YES or NO. ")
		while runLoop.upper() not in ["Y", "YES","N", "NO"]:
			runLoop = input("Would you like to do another sort?\n Enter YES or NO. ")
		if runLoop.upper() in ["N", "NO"]:
			break

