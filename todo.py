tasks=[]
while True:
    print("\nTo Do List\n")
    print("1.Add")
    print("2.View")
    print("3.Remove")
    print("4.Exit")
    choice=input("Enter Your Choice: ")
    if choice=="1":
        task=input("Enter Your Task:")
        tasks.append(task)
        print("Task Added!")
    elif choice=="2":
        if len(tasks)==0:
            print("No tasks available")
        else:
            print("Your tasks:\n")
            for i in range(len(tasks)):
                print(i+1," ",tasks[i])
    elif choice=="3":
        if len(tasks)==0:
           print("No tasks to remove\n")
        else:
            print("Your tasks:\n")
            for i in range(len(tasks)):
                print(i+1," ",tasks[i])
            num=int(input("Enter the task number to be remove:"))
            if num <= len(tasks):
                removed=tasks.pop(num-1) 
                print("The task is removed sucessfully!")
            else:
                print("Invalid number")
    elif choice =="4":
        print("Thank You!")
        break
    else:
        print("Invalid choice")    
                   

