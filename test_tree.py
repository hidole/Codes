class Node:
    def __init__(self,left,right,data):
        self.left = None
        self.right = None
        self.data = data

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def print_tree(self):
            if self.left:
                self.left.print_tree()

            print(self.data)

            if self.right:
                self.right.print_tree()



Node a, b, c

#def insert(head, node):
#    if head == None:
#        return node
#    if node.get_data() <= head.get_data():
#        head.set_left_child(insert(head.get_left_child(), node)
#    elif :
#        head.set_right_child(insert(head.get_right_child(),node)
#    return head
