#1. Add a task
#2. Remove task
#3. Edit task
#4. Edit description
#5. Add description

# Create a function 'addTask' and pass a list of tasks that already 
# have been created by users as argument.

#Initial task list
tasks = []

# Auxiliary function => to display the task => Task displayer function
def displayTasks(all_tasks):
    print('\nYour tasks: ')
    if len(all_tasks) <= 0:
        print('No Tasks yet..!!')
    else:
        for index, task in enumerate(all_tasks):
            print(f'{index+1} : {task}')

# Choose operation to perform
def newOperation(all_tasks):
    operation = input("Press 'A' to add a task, 'E' to edit a task, 'R' to remove a task or 'F' to quit the application: ")
    if operation == 'A':
        addTask(all_tasks)
    elif operation == 'E':
        editTask(all_tasks)
    elif operation == 'R':
        removeTask(all_tasks)
    elif operation == 'F':
        return
    else:
        newOperation(all_tasks)
        
# Edit a task
def editTask(all_tasks):
    task_number = int(input("Enter the task number of task's you want to edit: "))
    new_task = input('Edit task: ')
    
    all_tasks[task_number-1] = new_task
    print(f'Item with {task_number} has been edited.!')
    
    displayTasks(all_tasks)
    newOperation(all_tasks)

# Remove a task
def removeTask(all_tasks):
    task_number = int(input("Enter the task's number you want to remove: "))
    all_tasks.remove(all_tasks[task_number-1])
    print(f'Item with {task_number} has been removed from the task list.')
    
    displayTasks(all_tasks)
    newOperation(all_tasks)

# Add a task
def addTask(all_tasks):
    new_task = input('Add task: ')
    all_tasks.append(new_task)
    
    # print tasks
    displayTasks(all_tasks)
    
    
    newOperation(all_tasks) # Ask for the new operation

# Start Application        
addTask(tasks)     

