def factors(n):
	k=1
	while k*k <=n:
		if n%k == 0:
			yield k
			yield n//k
		k+=1
	if k*k == n:
		yield k


def factors_list(n):
	k=1
	ali =[]
	while k*k <n:
		if n%k ==0:
			ali.append(k)
			#print (k)

		k +=1

	return ali


def fibonacci(n):
	a=0
	b=1
	while True:
		yield a
		nexts = a+b
		a = b
		b = nexts
		if (a>n): break
	


print("fibonacci")
for a in fibonacci(1000000000000000000000):
	print (a)



""" 


print("factors")
for a in factors(100):
	print (a)

print("factors_list: SQRT")
for a in factors_list(1000):
	print (a)

"""
