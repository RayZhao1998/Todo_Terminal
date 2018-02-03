import os 
import time

class TodoItem():
    
    def __init__(self, title, endTime):
        self.title = title
        self.createdTime = int(time.time())
        self.endTime = endTime
        self.haveDone = False

    def Done(self):
        self.haveDone = True

    def unDone(self):
        self.haveDone = False

    def editTitle(self, newTitle):
        self.title = newTitle
        
    def editEndTime(self, newEndTime):
        self.endTime = newEndTime
        
class TodoList():
    
    def __init__(self):
        self.todoItems = []

    def addItem(self, newTodoItem):
        self.todoItems.append(newTodoItem)

    

def Welcome():
    os.system('clear')
    print("\n\n\n")
    print("|ˉˉˉˉˉˉˉˉˉˉˉ|ˉ| /ˉˉˉˉˉˉˉˉ\ˉ\ |ˉˉˉˉˉˉˉˉ\ˉ\   /ˉˉˉˉˉˉˉˉ\ˉ\ |ˉ|ˉ|         |ˉˉˉˉˉˉˉˉˉˉ|ˉ| /ˉˉˉˉˉˉˉˉˉ|ˉ||ˉˉˉˉˉˉˉˉˉˉˉ|ˉ|")
    print("ˉˉˉˉˉ| |ˉ|ˉˉˉˉˉ/ /ˉTˉˉˉˉ\ \ \| |ˉ|ˉˉˉ\ \ \ / /ˉTˉˉˉˉ\ \ \| | |          ˉˉˉ|  |ˉ|ˉ ˉ / /ˉ/ˉˉˉˉˉˉˉˉˉˉˉˉˉˉ| |ˉ|ˉˉˉˉˉ")
    print("     | | |     | | |    | | || | |    | | || | |    | | || | |             |  | |    \ ˉˉˉˉˉˉˉˉ\ˉ\      | | |     ")
    print("     | | |     | | |    | | || | |    / | || | |    | | || | |             |  | |     ˉˉˉˉˉˉˉˉ\ \ \     | | |     ")
    print("     | | |     \ \ \    / / /| | |   / / / \ \ \    / / /| | |             |  | |    \ˉ\ˉ\    / / /     | | |     ")
    print("     | | |      \ ˉˉˉˉˉˉ / / |  ˉˉˉˉˉ / /   \ ˉˉˉˉˉˉ / / |  ˉˉˉˉˉˉˉˉ|ˉ||ˉˉˉ    ˉˉˉ|ˉ| \ ˉˉˉˉˉˉ / /      | | |     ")
    print("     ˉˉˉˉˉ       ˉˉˉˉˉˉˉˉˉˉ  ˉˉˉˉˉˉˉˉˉˉˉ     ˉˉˉˉˉˉˉˉˉˉ  ˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉˉ  ˉˉˉˉˉˉˉˉˉˉ       ˉˉˉˉˉ     ")
    print("                                                                                                   version beta0.1")

def ShowMenu():
    print("\n\n")
    print("1. add a todo item")
    print("2. show todolist")
    print("0. quit")
    

def AddTodoItem(todoList):
    Welcome();
    newTodoItemTitle = input("title:")
    newTodoItemEndTime = input("end-time:")
    newTodoItem = TodoItem(newTodoItemTitle, newTodoItemEndTime)
    todoList.addItem(newTodoItem)
    print(newTodoItem.title + "   " + str(newTodoItem.createdTime) + "   " + newTodoItemEndTime + "   " + str(newTodoItem.haveDone))

def ShowTodolist():
    print("show todolist")


def select(selectedId, todoList):
    if selectedId == 0:
        print("exit")
    elif selectedId == 1:
        AddTodoItem(todoList)
        isNext = "yes"
        while True:
            isNext = input("Do you want to add another one?(yes or no)")
            if isNext == "yes":
                continue
                AddTodoItem(todoList)
            else:
                break
        if isNext == "no":
            Home()
            
    elif selectedId == 2:
        ShowTodolist()
    else:
        print("wrong command! Please select the correct one!")

def Home():
    Welcome()
    ShowMenu()
    inputSelectedId = int(input())
    select(inputSelectedId, todoList)

if __name__ == '__main__':
    todoList = TodoList()
    Home()
        