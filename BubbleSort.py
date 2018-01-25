""" takes in a list of numbers and then bubble sorts them"""
def bubbleSort(inList):
	while True: # run the sort until all the numbers are sorted
		switchedNums = False # if no numbers are switched the sort is over

		# loops through all of the numbers in inList
		# and swaps them by checking if the lower index's number is higher
		# than the one beside it
		for i in range(len(inList)-1):
			if inList[i] > inList[i+1]:
				switchedNums = True # a number was switched so the sort needs to loop again
				# the switch
				temp = inList[i]
				inList[i] = inList[i+1]
				inList[i+1] = temp

		if switchedNums == False:
			break
