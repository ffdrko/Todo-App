print('--- Home ---')
print("""1- Add Todo
2- show Todo
3- Edit Todo
4- Complete Todo
5- Exit""")
print("-----------------")

todo_list = []

while True:
    user_action = input("Enter your option: ").strip()

    match user_action:
        case 'add':
            todo_task = input("Enter a Todo task: ") + '\n'
            todo_list.append(todo_task)
            print("Task is added in the list.")
        case 'show':
            for index, task in enumerate(todo_list):
                print(f'{index + 1} - {task.strip("\n")}')
        case 'edit':
            todo_num = int(input("Enter todo number: ")) - 1
            todo_list[todo_num] = input("Enter edited task: ") + "\n"
        case 'complete':
            todo_num = int(input("Enter todo number: ")) - 1
            com_task = todo_list.pop(todo_num)
            print(f"[{com_task}]this task is complete.")
        case 'exit':
            break