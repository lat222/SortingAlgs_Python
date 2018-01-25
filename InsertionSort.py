def insertionSort(inList):
	for i in range(1,len(inList)): # the 0th index is already sorted
		# only move other indices when this number is smaller than the one before it
		if inList[i] < inList[i-1]:
			index = i-1
			# need to decrement the index for the smaller number only when
			# the index is not already 0  and the next lower index is less than
			# the current i index
			while index != 0 and inList[i] < inList[index-1]:
				index -= 1

			# the swap happens here
			temp = inList[i] # save the current i index value
			# move all of the larger values than that one up
			for j in range(i,index,-1):
				inList[j] = inList[j-1]
			# save the current i index value to its sorted spot
			inList[index] = temp
