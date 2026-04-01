todo_list =[] 
while True:
          print("1. add task")
          print("2. view task")
          print("3. delete task")
          print("4. exit")
          choice=int(input("enter your choice :"))
          if choice==1:
               task= input("enter task:")
               todo_list.append(task)
               print("task added successfully!")
          elif choice==2:
               if len(todo_list)==0:
                    print("no tasks available.")
               else:
                    print("\nyour tasks:")
                    for i in range(len(todo_list)):
                         print(i+1, todo_list[i])  
          elif choice==3:
               if len((todo_list))==0:
                    print("no task to delete.")
               else:
                    for i in range(len(todo_list)):
                         print(i+1, todo_list[i])  
                    num = int(input("enter task number to delete:"))
                    if 0 < num<=len(todo_list):
                         removed = todo_list.pop(num-1)
                         print("deleted task:",removed)
                    else:
                         print("invalid task number.")       
          elif choice==4:
               print("exiting the application")
               break
          else:
               print("invalid choice! try again>")
            