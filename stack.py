class stack:
    def __init__(self):
        self.stk = []
        self.top = -1

    def push(self):
        ele = float(input("Enter the value to be input"))
        self.stk.append(ele)
        if len(self.stk) == (self.top+2):
            print("Element successfully added now")
            self.top += 1
        else:
            print("Stack is fulled")

    def pop(self):
        if self.top == -1:
            print("Stack is full")
        else:
            ele = self.stk.pop()
            self.top -= 1
            print(f"the element {ele} is deleted from the stack top")


def main():
    st = stack()
    choice = 1
    while (choice):
        choice = int(
            input("Enter your choise \n 1.push \n 2.pop \n 3.peek\n 4.display \n 0. it "))
    if choice == 1:
        st.push()
    elif choice == 2:
        st.pop()
    elif choice == 3:
        if st.top != -1:
            print("Stsck top = ", st.stk[st.top])
        else:
            print("Stack is empty")
    elif choice == 4:
        if st.top != -1:
            print("Stack is \n", st.stk)
        else:
            print("Stack is empty")
    elif choice != 0:
        print("Wrong choice ")


if __name__ == "__main__":
    main()
