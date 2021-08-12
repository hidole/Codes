#double linked list
class ListN:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
		self.num = 0



#travel linked list
def travel_Next(pstart):
	print("starting of the list Next")
	while(pstart.next!=None):
		print("list number:", pstart.num)
		print("List data:", pstart.data)
		pstart = pstart.next

	print("list number:", pstart.num)
	print("List data:", pstart.data)
	print("end of the travel_Next list")
	return 0	

def travel_Prev(pstart):
	print("starting of the list Prev")

	while(pstart.prev!=None):
		print('list number:', pstart.num)
		print("List data:", pstart.data)
		pstart = pstart.prev


	print('list number:', pstart.num)
	print("List data:", pstart.data)	
	print("end of the travel_Prev list")
	return 0 
		

def listCnt(alist):
	temp = alist
	i=0

	while(temp.next!=None):
		temp = temp.next
		i=i+1

	return i+1
		


def ScanFromHead(listA, Node):
#Scan from head
	temp = listA
	while(temp.next !=None):
		if temp.data == Node.data:
			return temp.num
		else:
			temp= temp.next
	
	print("not found")		
	return 0  


#adding nodes
def addNode2First(listA, iNode):
	temp = listA

#adding node to after the head
	while(temp.prev !=None):
			temp = temp.prev

	if temp.data !="head":
			print ("No Head in the list")
			return 0	

	tempNext = temp.next
	temp.next = iNode
	iNode.prev = temp

	iNode.next = tempNext
	tempNext.prev = iNode
	temp= None
	tempNext =None

	return 0

#adding node to the tail
def addNode2Last(listA, iNode):
	temp = listA
	while(temp.next!=None):
			temp = temp.next

	print(temp.num, temp.data)


#adding node to before the tail
	tempPrev = temp.prev
	temp.prev = iNode
	iNode.next = temp

	iNode.prev = tempPrev
	tempPrev.next = iNode

	temp =None
	tempPrev = None
	return 0


#adding node to among the nodes 










#removing nodes



#sorting 




# single linked list creation loop

head = ListN("head")
tail = ListN("tail")

start = head

for i in range(0,30):
	temp = ListN(i)
	temp.num = i
	start.next = temp
	temp.prev  = start

	start = start.next

start.next = tail
tail.prev = start

	
	
print (head.data)
print (tail.data)

#travel_Next(head)
#travel_Prev(tail)

#find = ListN(26)
#print ("scan result", ScanFromHead(head, find ))
#print("linked list length:",listCnt(head))

iinput =ListN(9999)

addNode2First(head, iinput)

travel_Next(head)

ilast = ListN(1111)
addNode2First(head, iinput)
#addNode2Last(head, ilast)
#addNode2Last(head, ilast)

travel_Next(head)

listCnt(head)










