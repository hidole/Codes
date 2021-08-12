class ListN:
	def __init__(self, data):
		self.data = data
		



#linked list creation loop

head = ListN("head")
start = head

for i in range(1,10):
	temp = ListN(i)
	start.next = temp
	start = start.next


	
	


