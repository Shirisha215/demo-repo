class stack:
    def push(k,i,n):
        if(len(k)==n):
            print("Stack is full",i,"is unable to push")
        else:
            k.append(i)
            print(i,"is pushed")
    def pop(k):
        if(len(k)==0):
            print("Stack is empty")
        else:
            print("popped element: ",k.pop())
    def isempty(k):
        if(len(k)==0):
            print("Stack is empty")
        else:
            print("Stack is not empty")
k=[]
n=int(input("Enter the size of stack: "))
stack.isempty(k)
while(1):
    print("1.push")
    print("2.pop")
    print("choice")
    ch=int(input("(1/2): "))
    if(ch==1):
        p=int(input("no to be pushed: "))
        stack.push(k,p,n)
    elif(ch==2):
        stack.pop(k)
    else:
        break
