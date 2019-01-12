


def slice_list(mylist, num):
	if(len(mylist) > (num * 25)):
		return mylist[(num *25)-25:(num *25)]
	else:
		return mylist[(num*25)-25:]