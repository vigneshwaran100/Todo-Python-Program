todo_list=[]

while True:
    user_action= input("Enter Your Option ADD,REMOVE,REPLACE,SHOW and Exit: ")

    match user_action:
        case 'add':
            todo_add=input("Enter Your Todo Task: ") + "\n"
            todo_list.append(todo_add)
            file=open("Todo.txt",'w')
            file.writelines(todo_list)
            file.close( )

        case 'remove':
            todo_remove=int(input("Enter Your Option To Remove Task: "))
            remove=todo_list[todo_remove+1]
            todo_list.remove(remove)
         
        case 'show':
            file=open("todo.txt",'r')
            todo_list=file.readline()
            #print(todo_list)
            file.close()

            new_list=[]
            for i in todo_list:
                new_i=i.strip("\n")
                new_list.append(new_i)
            print(new_list)

            for index,i in enumerate(todo_list,1):
                print(index,i)


        case 'replace':
            word_index=int(input("Enter your word replace number: "))
            word_index=word_index-1
            new_word=input("Enter Your Replace Word: ")
            todo_list[word_index]=new_word

        case 'read':
            file=open("todo.txt",'r')
            todo_list=file.readline()
            print(todo_list)
            file.close()
        
        case 'exit':
            break
print("Quit") 
