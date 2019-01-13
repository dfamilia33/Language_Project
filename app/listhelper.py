
import math

def slice_list(mylist, num):
	if(len(mylist) > (num * 25)):
		return mylist[(num *25)-25:(num *25)]
	else:
		return mylist[(num*25)-25:]

def page_ind( num, dblen):
	mylist = list()
	last_ind = math.ceil(dblen/25)

	if(dblen <=75):
		for i in range(last_ind):
			mylist.append(i+1)
	else:
		if(num == 1):
			return [1,2,3]
		elif num == last_ind:
			return [last_ind -2, last_ind -1, last_ind]
		else:
			return [num-1, num, num+1]

	return mylist


