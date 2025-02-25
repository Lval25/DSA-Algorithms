class Treenode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def append_child(self, child):
        child.parent = self
        # self will become a parent of child
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    # Creating parent node
    root = Treenode("Electronics")


    # Initiate sub categories of root node or creating child nodes
    ###
    laptop = Treenode("Laptop")
    laptop.append_child(Treenode("Mac"))
    laptop.append_child(Treenode("PC"))
    laptop.append_child(Treenode("Thinkpad"))

    cellphone = Treenode("Cellphone")
    cellphone.append_child(Treenode("Iphone"))
    cellphone.append_child(Treenode("Galaxy"))
    cellphone.append_child(Treenode("Vivo"))

    tablet = Treenode("Tablet")
    tablet.append_child(Treenode("Ipad"))
    tablet.append_child(Treenode("Thinkpad"))
    tablet.append_child(Treenode("Mypad"))
    ###

    # Creating Child nodes of the parent and their respective elements
    root.append_child(laptop)
    root.append_child(cellphone)
    root.append_child(tablet)

    return root


    # Creating the child nodes hence append child
    #root.append_child(laptop)




if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    pass
