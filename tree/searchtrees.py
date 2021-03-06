class Node(object):
    def __init__(self, num):
        self.n = num
        self.left = None
        self.right = None

    def insert(self, num):
        if num > self.n:
            if not self.right:
                self.right = Node(num)
            else:
                self.right.insert(num)
        else:
            if not self.left:
                self.left = Node(num)
            else:
                self.left.insert(num)

    def find(self, num, parent=None):
        if self.n == num:
            return self, parent
        elif num > self.n and self.right:
            return self.right.find(num, self)
        elif num < self.n and self.left:
            return self.left.find(num, self)
        return False, None

    def child_count(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    def delete(self, num):
        node, parent = self.find(num)
        if not node:
            return None
        child_count = node.child_count()
        if child_count == 0:
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None
        elif child_count == 1:  # either right or left child is present
            if node.left:
                child = node.left
            else:
                child = node.right
            if parent:
                if parent.left is node:
                    parent.left = child
                else:
                    parent.right = child
        else:  # both the children are present
            parent = node
            next = node.right  # find smallest node in right sub tree
            while next.left:
                parent = next
                next = next.left
            node.n = next.n  # last node falls under zero or 1 child
            if parent.left == next:
                parent.left = next.right
            else:
                parent.right = next.right

    def find_min(self):
        if not self.left:
            return self.n
        else:
            return self.left.find_min()

    def find_max(self):
        if not self.right:
            return self.n
        else:
            return self.right.find_max()

    def in_order(self):
        if not self.n:
            return None
        if self.left:
            self.left.in_order()
        print self.n
        if self.right:
            self.right.in_order()

    def pre_order(self):
        if not self.n:
            return None
        print self.n
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def post_order(self):
        if not self.n:
            return None
        if self.right:
            self.right.post_order()
        if self.left:
            self.left.post_order()

    def mirror(self):
        if not self:
            return
        self.mirror(self.left)
        self.mirror(self.right)

        temp = self.left
        self.left = self.right
        self.right = temp

    def __str__(self):
        return str(self.n)


if __name__ == '__main__':
    root = Node(10)
    root.insert(15)
    root.insert(25)
    root.insert(4)
    root.insert(5)

    print "In order traversal"
    print root.in_order()
    print "-----------------"
    root.delete(10)

    print root

    found_node, root_node = root.find(5)
    print "found>> ", found_node.n, "root>> ", root_node.n

    print "Min value " + str(root.find_min())
    print "Max value " + str(root.find_max())
