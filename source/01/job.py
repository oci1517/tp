from a_list import a_list
from n_list import n_list

from power import power

def job(alist, nlist):
	assert len(alist) == len(nlist)

	result = [0] * len(alist)

	for i in range(len(alist)):
		result[i] = power(alist[i], nlist[i])

power_list = job(a_list, n_list)
print(power_list[:10])
