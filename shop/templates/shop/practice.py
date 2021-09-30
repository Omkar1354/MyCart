class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
class linkList:
	def __init__(self):
		self.head = None
	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = None
		head = new_node
	def print(self):
		temp = head
		while temp.next != None:
			temp = temp.next
			print(temp)
link = linkList()
link.push(10)
link.push(20)
link.push(30)
link.print()
