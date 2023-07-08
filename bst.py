from platform import node


class bst:
    def __init__(self ):
        self.root = None
        print("A tree has been initilized")
        self.root = node()
        self.root.right = None
        self.root.left = None

    def insert(self):
        pass

    def delete(self):
        pass

    def inorder_print(self, tree):
        if tree != None:
            self.inorder_print(tree.left)
            print(f"{tree.val}", end="")
            self.inorder_print(tree.right)

    def preorder_print(self, tree):
        if tree != None:
            print(f"{tree.val}", end="")
            self.preorder_print(tree.left)

            self.preorder_print(tree.right)

    def postorder_print(self, tree):
        if tree != None:
            self.postorder_print(tree.left)

            self.postorder_print(tree.right)
            print(f"{tree.val}", end="")

    def display(self):
        print("The tree element are ")
        self.inorder_print(self.root)
        self.preorder_print(self.root)
        self.postorder_print(self.root)
        print()


def main():
    tree = bst()
    choice = 1
    while choice:
        choice = int(input(
            "menu : \t 1.insert \n\t 2.delete \n\t 3.display\n\t 0 . enter 0 to exit \n"))
        if choice == 1:
            tree.insert()
        elif choice == 2:
            tree.delete()
        elif choice == 3:
            if tree.root == None:
                print("tree empty insert node ")
            else:
                tree.display()
        elif choice != 0:
            print("wrong choice ")


# main()
if __name__ == "__main__":
    main()
   

