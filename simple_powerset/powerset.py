def get_powerset(list):
	powers = []
	total = 2**len(list)

	for i in range(total):
		temp_set = []
		num = ("{0:0%db}" % (len(list))).format(i)
		
		for j in range(len(num)):
			if num[j] == '1':
				temp_set.append(list[int(j)])

		powers.append(temp_set)

	return powers

def powerset(ip):
	"""
	Returns the powerset of the given input.

	Supported input formats: int, str, list, tuple.

	"""
	if isinstance(ip, int):
		lst = [int(x) for x in str(ip)]
		return get_powerset(lst)
	elif isinstance(ip, (str, list, tuple)):
		return get_powerset(ip)
	else:
		raise TypeError("Cannot find the powerset for a {} type.".format(type(ip)))
