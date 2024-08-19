#TO DO List Coded By Akshit
def viewList(): #used to display the complete todo list
    print("ToDo Tasks Are ",mylst)
def addtask(): #used to add a task to the todo list
    mylst.append(str(input("Enter a To Do : ")))
    print("Task Added")

def completeTask(): # used to complete the last task of the todo list
    print(mylst[-1],"Completed")
    mylst.pop()

def completePtask(): # used to complete a specfic task of the todo list
    completedTask = str(input("Enter the task that is competed"))
    mylst.remove(completedTask)
    print(completedTask,"task was completed")

def completeAll():
    if str(input("Are you Sure you want to clear the list (Yes / No)")) == "Yes":
        mylst.clear()
    print("ToDo List Cleared")

def exit(): # used to exit from the code
    print("Thank you for using ToDo List")


mylst = []
options =0
while (options !=-1  ):

    options = int(input(
                " 1. View List"
                " 2. Add Task "
                " 3. Complete Last Task "
                " 4. Complete a particular task "
                " 5. Complete all tasks"
                " -1. Exit "))


    if options in range(-1,6):
        # print("you have selected :",options)
        if options==1:
            viewList()
        elif options==2:
            addtask()
        elif options==3:
            completeTask()
        elif options==4:
            completePtask()
        elif options==5:
            completeAll()
        elif options==-1:
            exit()
    else:
        print("Incorrect Selection")

