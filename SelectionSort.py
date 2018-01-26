def selectionSort(inList):
	# loop through the indices finding the lowest number 
	# which will be placed at that index
	for i in range(len(inList)):
		lowestIndex = findLowest(inList,i)
		temp = inList[i]
		inList[i] = inList[lowestIndex]
		inList[lowestIndex] = temp


def findLowest(inList,startIndex):
	# helper function that returns that index of the number with the lowest value
	# without including already sorted values
	lowestIndex = startIndex
	for i in range(startIndex, len(inList)):
		if inList[lowestIndex] > inList[i]:
			lowestIndex = i
	return lowestIndex

