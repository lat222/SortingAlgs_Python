from BubbleSort import *
from MergeSort import *
from InsertionSort import *
from SelectionSort import *

def listToString(inList):
	string = ""
	for i in inList:
		string += str(i) + " "
	return string.strip()


if __name__ == "__main__":
	while True:
		# choose sorting type
		sortingType = input("What type of sorting algorithm would you like to do?\n\
			Choose from: INSERTION, BUBBLE, SELECTION, or MERGE. ")
		# Check their response is correct
		while sortingType.upper() not in ["MERGE", "INSERTION", "BUBBLE", "QUICK", "HEAP", "SELECTION"]:
			sortingType = input("What type of sorting algorithm would you like to do?\n\
			Choose from: INSERTION, BUBBLE, SELECTION, or MERGE. ")

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
				print("The sorted list is: %s." % (numsToSort[0]))
			else:
				# call the sorting function
				if sortingType.upper() == "MERGE":
					inList = mergeSort(numsToSort)
				elif sortingType.upper() == "INSERTION":
					insertionSort(numsToSort)
				elif sortingType.upper() == "BUBBLE":
					bubbleSort(numsToSort)
				elif sortingType.upper() == "SELECTION":
					selectionSort(numsToSort)
				elif sortingType.upper() == "QUICK":
					None
				else:
					None
				print("The sorted list is: %s." % (listToString(numsToSort)))

		runLoop = input("Would you like to do another sort?\n Enter YES or NO. ")
		while runLoop.upper() not in ["Y", "YES","N", "NO"]:
			runLoop = input("Would you like to do another sort?\n Enter YES or NO. ")
		print()
		if runLoop.upper() in ["N", "NO"]:
			break

