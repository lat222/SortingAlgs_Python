def mergeSort(inList):
	if len(inList) > 1:
		middleIndex = len(inList)//2
		firstHalf = inList[:middleIndex]
		secondHalf = inList[middleIndex:]
		mergeSort(firstHalf)
		mergeSort(secondHalf)

		# merge the two now
		merge(inList, firstHalf, secondHalf)


def merge(inList, firstHalf,secondHalf):
	firstIndex = 0
	secondIndex = 0
	listIndex = 0
	while firstIndex < len(firstHalf) and secondIndex < len(secondHalf):
		if firstHalf[firstIndex] < secondHalf[secondIndex]:
			inList[listIndex] = firstHalf[firstIndex]
			firstIndex += 1
		else:
			inList[listIndex] = secondHalf[secondIndex]
			secondIndex += 1
		listIndex += 1

	
	while firstIndex < len(firstHalf):
		inList[listIndex] = firstHalf[firstIndex]
		firstIndex += 1
		listIndex += 1

	while secondIndex < len(secondHalf):
		inList[listIndex] = secondHalf[secondIndex]
		secondIndex += 1
		listIndex += 1