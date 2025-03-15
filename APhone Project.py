from tkinter import *
import time
import random
from tkinter import messagebox

userName = "" #placeholder for user's name

def validateInput (): #get user's name and & move to Home canvas
    global userName
    
    userName = nameEntry.get ()
    
    if userName.isalpha (): #only accept letters error otherwise 
        return homeCanvas1 ()
    
    elif userName == "":
        messagebox.showinfo ("Error", "Please enter your first name.")
    else:
        messagebox.showinfo ("Error", "Please enter a valid name.")
        
def changeWallpaper (wallpaperImage): #change wallpaper
    global phoneWallpaper
    
    homeScreen.itemconfig (wallpaper, image = wallpaperImage)
    phoneWallpaper = wallpaperImage
  
# ---------------- Close Application ---------------- #
    
def closeCalculator (): #end calculator app
    global answer, answerError 
    
    if answerError == True: #reset answer if it was an error, store otherwise
        answer = None
        answerError = False
        calculatorRoot.destroy ()
    else:
        calculatorRoot.destroy ()
        
def closeToDo (): #end to do app
    
    toDoRoot.destroy ()

def closeUberFeasts (): #end uber feasts app
    
    uberRoot.destroy ()
    
def closeCamera (): #end camera app
    
    cameraRoot.destroy ()
    
def closeSafari (): #end safari app
    
    safariRoot.destroy ()
    
def closeYoutube (): #end youtube app
    
    youtubeRoot.destroy ()
    
def closeMessenger (): #end messenger app
    
    messengerRoot.destroy ()
    
def closeFlappy (): #end flappy bird app
    
    flappyRoot.destroy ()
    
def closeSpotify (): #end spotify app
    
    spotifyRoot.destroy ()
    
def closeNotes (): #end notes app
    
    notesRoot.destroy ()

def closeReminder (): #end reminder app
    
    reminderRoot.destroy ()
   
# ---------------- Close Application ---------------- #  
        
# ---------------- Time Update ---------------- #    

def timeUpdateHome(): # Update the current time for homescreens

    currentTime = time.ctime(time.time())
    homeScreen.itemconfig (showTime, text = currentTime)# Update the displayed time
    homeRoot.after (1000, timeUpdateHome)# schedule the function to run again after 1000 ms (1 second)

def timeUpdateToDo(): # Update the current time for To Do 
    
    currentTime = time.ctime(time.time())
    toDoHome.itemconfig (toDoTime, text = currentTime)# Update the displayed time
    toDoRoot.after (1000, timeUpdateToDo)# schedule the function to run again after 1000 ms (1 second)

def timeUpdateCalculator(): # Update the current time for calculator
    
    currentTime = time.ctime(time.time())
    calculatorHome.itemconfig (calculatorTime, text = currentTime)# Update the displayed time
    calculatorRoot.after (1000, timeUpdateCalculator)# schedule the function to run again after 1000 ms (1 second)
    
def timeUpdateUberFeasts(): # Update the current time for Uber Feasts
    
    currentTime = time.ctime(time.time())
    uberHome.itemconfig (uberTime, text = currentTime)# Update the displayed time
    uberRoot.after (1000, timeUpdateUberFeasts)# schedule the function to run again after 1000 ms (1 second)

def timeUpdateCamera (): # Update the current time for Camera
    
    currentTime = time.ctime(time.time())
    cameraHome.itemconfig (cameraTime, text = currentTime)# Update the displayed time
    cameraRoot.after (1000, timeUpdateCamera)# schedule the function to run again after 1000 ms (1 second)

def timeUpdateSafari(): # Update the current time for safari
    
    currentTime = time.ctime(time.time())
    safariHome.itemconfig (safariTime, text = currentTime)# Update the displayed time
    safariRoot.after (1000, timeUpdateSafari)# schedule the function to run again after 1000 ms (1 second)

def timeUpdateYoutube(): # Update the current time for YouTube
    
    currentTime = time.ctime(time.time())
    youtubeHome.itemconfig (youtubeTime, text = currentTime)# Update the displayed time
    youtubeRoot.after (1000, timeUpdateYoutube)# schedule the function to run again after 1000 ms (1 second)

def timeUpdateMessenger(): # Update the current time for messenger
    
    currentTime = time.ctime(time.time())
    messengerHome.itemconfig (messengerTime, text = currentTime)# Update the displayed time
    messengerRoot.after (1000, timeUpdateMessenger)# schedule the function to run again after 1000 ms (1 second)

def timeUpdateFlappy(): # Update the current time for flappy bird 
    
    currentTime = time.ctime(time.time())
    flappyHome.itemconfig (flappyTime, text = currentTime)# Update the displayed time
    flappyRoot.after (1000, timeUpdateFlappy)# schedule the function to run again after 1000 ms (1 second)
    
def timeUpdateSpotify(): # Update the current time for spotify app
    
    currentTime = time.ctime(time.time())
    spotifyHome.itemconfig (spotifyTime, text = currentTime)# Update the displayed time
    spotifyRoot.after (1000, timeUpdateSpotify)# schedule the function to run again after 1000 ms (1 second)

def timeUpdateNotes(): # Update the current time for notes app
    
    currentTime = time.ctime(time.time())
    notesHome.itemconfig (notesTime, text = currentTime)# Update the displayed time
    notesRoot.after (1000, timeUpdateNotes)# schedule the function to run again after 1000 ms (1 second)
    
def timeUpdateReminder(): # Update the current time for reminder app
    
    currentTime = time.ctime(time.time())
    reminderHome.itemconfig (reminderTime, text = currentTime)# Update the displayed time
    reminderRoot.after (1000, timeUpdateReminder)# schedule the function to run again after 1000 ms (1 second)

# ---------------- Time Update ---------------- #

# ---------------- To-Do ---------------- #

tasks = [] #store tasks being added 

def scrollRegionUpdate (): #update the range of the scroll bar
    
     toDoCanvas.configure(scrollregion = toDoCanvas.bbox ("all"))
     
def selectTask (event): #switch to checkmark image when hovering on the check box
    
    checkBoxButton = event.widget
    checkBoxButton.config (image = checkMarkImage)
    
def deselectTask(event): #switch to empty check box image when on idle
    
    checkBoxButton = event.widget
    checkBoxButton.config (image = checkBoxImage)

def checkTask(listTask, checkBoxButton, taskIndex): 
    
    #delete the specific task along with its delete button 
    listTask.destroy()
    checkBoxButton.destroy()
    tasks.pop (taskIndex)
    scrollRegionUpdate()

def createTask (taskInfo):
    
    # Create the listbox for the task information
    listTask = Listbox (listFrame, width = 28, height = 1, font = ("Helvetica", 13))
    listTask.insert (END, "     " + taskInfo)
    listTask.pack (pady = 5) 

    # Create delete button for new task
    checkBoxButton = Button(listTask, image = checkBoxImage, borderwidth = 0, highlightthickness = 0, command = lambda: checkTask (listTask, checkBoxButton, tasks.index (taskInfo)))
    checkBoxButton.place (relx = 0, rely = 0.5, anchor = W)  

    #bind the button with curser control
    checkBoxButton.bind ("<Enter>", selectTask)
    checkBoxButton.bind ("<Leave>", deselectTask)

def addTask (): #get user's task information
    
    newTask = writeTasks.get ()
    
    if newTask == "": #no empty task
        messagebox.showinfo ("Error", "Please enter a task.")
    else:   
        createTask (newTask)
        tasks.append(newTask)
        writeTasks.delete(0, END)
        
        scrollRegionUpdate ()
# ---------------- To-Do ---------------- #

# ---------------- To-Do ---------------- #

def openToDo ():
    
    global toDoRoot, toDoHome, toDoTime, toDoCanvas
    global listFrame, writeTasks, taskScroll, tasks
    global checkBoxImage, checkMarkImage
    
    #create a pop-up box, canvas, and title 
    toDoRoot = Toplevel()  
    toDoRoot.title ("To Do")
    
    toDoHome = Canvas(toDoRoot, width = 360, height = 710)
    toDoHome.pack()
    
    #importing images
    checkBoxImage = PhotoImage (file = "Check Box.png")
    checkMarkImage = PhotoImage (file = "Check Mark.png")
    
    #background image
    toDoPhone = toDoHome.create_image (180, 360, image = phoneWallpaper) 
    
    #button to close the to do app
    toDoReturnB = Button (toDoRoot, image = returnImage, borderwidth = 0, highlightthickness = 0, command = closeToDo)
    toDoReturnButton = toDoHome.create_window (80, 100, window = toDoReturnB)
    
    #create a main frame for the canvas 
    toDoFrame = Frame (toDoRoot, width = 10, height = 300)
    toDoFrameBox = toDoHome.create_window (185, 350, window = toDoFrame)
    
    #create another canvas for the application area 
    toDoCanvas = Canvas (toDoFrame, width = 230, height = 430, highlightthickness = 0)
    toDoCanvas.pack (side = LEFT, fill = BOTH, expand = True)
    
    #add bacgrkound image
    toDoWallpaper = toDoCanvas.create_image (115, 225, image = phoneWallpaper)
    
    #add scrollbars to the canvas frame
    taskScroll = Scrollbar (toDoFrame, orient = VERTICAL, command = toDoCanvas.yview)
    taskScroll.place (relx = 1, rely = 0, relheight = 1, anchor = NE)
     
    textScroll = Scrollbar (toDoFrame, orient = HORIZONTAL, command = toDoCanvas.xview)
    textScroll.place (relx = 0, rely = 1, relwidth = 1, anchor = SW)
    
    #configure the scrollbar 
    toDoCanvas.config (yscrollcommand = taskScroll.set, xscrollcommand = textScroll.set)
    
    # bind mousewheel scrolling
    toDoCanvas.bind_all("<MouseWheel>", lambda event: toDoCanvas.yview_scroll (-int(event.delta / 120), "units"))
    toDoCanvas.bind_all("<Shift-MouseWheel>", lambda event: toDoCanvas.xview_scroll (-int(event.delta / 120), "units"))
    
    #create another frame inside the canvas and add to canvas 
    listFrame = Frame (toDoCanvas)
    listFrameBox = toDoCanvas.create_window (0, 0, window = listFrame, anchor = NW)
    
    #entry for tasks
    toDoTask = StringVar ()
    toDoTask.set("")
    writeTasks = Entry (toDoRoot, textvariable = toDoTask, width = 35, font = ("Helvetica", 10))
    showTasks = toDoHome.create_window (182.5, 600, window = writeTasks)
    
    #add task buttons
    newTaskB = Button (toDoRoot, width = 30, height = 2, text = "Add Task", font = ("Helvetica", 10), fg = "white", bg = "#488cb4", command = addTask)
    newTaskButton = toDoHome.create_window (182.5, 640, window = newTaskB)
    
    #display the time 
    currentTime = time.ctime (time.time())
    toDoTime = toDoHome.create_text (230, 100, text = currentTime, font = ("Helvetica", 10), fill = "white") 
    
    timeUpdateToDo () #keep the time updated
    
    if tasks != []: #regenreate previous incomplete tasks
        for i in range (0, len (tasks)):
            createTask (tasks [i])
    
    toDoRoot.mainloop ()
     
# ---------------- To-Do ---------------- #
  
# ---------------- Calculator ---------------- #

#store variables as default for the code
answer = None
decimalAnswer = 0
operation = ""
appliedDecimal = False
answerError = False

def getNumber (digit): #get user's number and features from entry 
    
    global current, number, appliedDecimal, answer, answerError, decimalAnswer
    
    current = number.get ()
    
    if answerError == True: #clear if there is an exististing error 
        number.delete(0, END)
        number.insert(0, "Error: Clear the Error")
        answerError = True 
    
    elif digit == answer and answerError == False: #check if there is a value stored for answer
        for i in range (0, len(current)): #ensure no repeating decimal answer
            if current [i] == ".":
                decimalAnswer = decimalAnswer + 1
                if decimalAnswer == 1:
                    answerError = True
                    
        if answerError == True or answer == None:  
            number.delete(0, END)
            number.insert(0, "Error: Invalid Input")
            answerError = True
            
        else: 
            number.delete(0, END) #clear the entry
            
            number.insert(0, str(current) + str(digit)) #add the new number or feature to the current entry 
            
    elif digit == ".": 
        if appliedDecimal == True or answerError == True: #no repeating decimal for 1 number
            number.delete(0, END)
            number.insert(0, "Error: Invalid Input")
            answerError = True 
        else:
            appliedDecimal = True
            
            number.delete(0, END) #clear the entry
    
            number.insert(0, str(current) + str(digit)) #add the new number or feature to the current
    
    elif digit == "-": #changing the current to a negative or a positive number
        number.delete(0, END)
        
        if (current == "") or (current == "."): #no sign changes for empty or decimal
            number.insert(0, "Error: Invalid Input")
            answerError = True 
        
        elif appliedDecimal == True or (answer != None and answer % 1 != 0): 
            
            number.insert(0, str(-1 * float(current))) 
            
        elif appliedDecimal == False:
            number.insert(0, str(-1 * int(current)))
        
    else:
        number.delete(0, END) #clear the entry
    
        number.insert(0, str(current) + str(digit)) #add the new number or feature to the current
            
        
def clearCalculator (): #clear existing numbers, features, and operations
    global appliedDecimal, answerError, answer
    number.delete(0, END)
    
    if answerError == True: #reset answer to none if there was an error 
        answerError = False
        answer = None
        
    appliedDecimal = False
    
def performOperation (operationType): #collect 1st number and assign the selected operation 
    
    global firstNum, appliedDecimal, answer, answerError, operation
    
    numValue1 = number.get ()
    
    if answer != None and answerError == False: #check if it is decimal 
        if answer % 1 != 0: 
            appliedDecimal = True
    
    if numValue1 == "" or answerError == True or current == ".": #check conditions of error
        number.delete (0, END)
        if numValue1 == "":
            number.insert (0, "Error: No Value Inserted")
        else:
            number.insert (0, "Error: Clear the Error")
        answerError = True 
        
        return 
    
    #determine if the number is a decimal or whole number
    if appliedDecimal == True:
        firstNum = float(numValue1)
    else:
        firstNum = int(numValue1)
        
    #determine the selected operation
    if operationType == 1: 
        operation = "Addition"
        
    elif operationType == 2:
        operation = "Subtraction"
        
    elif operationType == 3:
        operation = "Multiplication"
        
    else:
        operation = "Division"
        
    number.delete (0, END)
    
    appliedDecimal = False 

def calculation (): #collect 2nd number and calculate the result 
    global answer, appliedDecimal, firstNum, secondNum, answerError
    
    numValue2 = number.get ()
        
    #check if it is a decimal number
    if answer != None and answerError == False: 
        if answer % 1 != 0: 
            appliedDecimal = True
    
    elif numValue2 == "" or numValue2 == ".":
        number.delete (0, END)
        number.insert (0, "Error: No Value Inserted")
        answerError = True
        
        return
    
    #determine if the number is a decimal or whole number
    if appliedDecimal == True and answerError == False:
        secondNum = float(numValue2)
        
    elif appliedDecimal == False and answerError == False:
        secondNum = int(numValue2)
    
    number.delete (0, END)
    
    #check which operation was selected, calculate, and show
    if answerError == False: 
    
        if operation == "Addition":  # addition
            answer = firstNum + secondNum
            if answer % 1 == 0:
                answer = int (answer)
            else:
                answer = float (answer)
                
        elif operation == "Subtraction":  # subtraction
            answer = firstNum - secondNum
            if answer % 1 == 0:
                answer = int(answer)
            else:
                answer = float (answer)
        
        elif operation == "Multiplication":  # multiplication
            answer = firstNum * secondNum
            if answer % 1 == 0:
                answer = int(answer)
            else:
                answer = float (answer)
    
        elif operation == "Division":  # division
            if secondNum != 0 and answer != 0:
                answer = firstNum / secondNum
                if answer % 1 == 0:
                    answer = int(answer)
            else: #ensure no division by zero 
                answer = "Error: Division by Zero"
                answerError = True 
        else: #ensure an operation is selected
            answer = "Error: No Operation Selected"
            answerError = True
        
        number.delete(0, END)
        number.insert(0, answer)
    
    else:
        number.insert(0,"Error: Clear the Error")

# ---------------- Calculator ---------------- #

# ---------------- Calculator ---------------- #
def openCalculator ():
    global clearImage, calculatorRoot, calculatorHome
    global number, calculatorTime
    
    #create a pop-up box, canvas, and title 
    calculatorRoot = Toplevel()
    calculatorRoot.title ("Calculator") 
    
    calculatorHome = Canvas(calculatorRoot, width = 360, height = 710)
    calculatorHome.pack()  
    
    #background image
    calculatorPhone = calculatorHome.create_image (180, 360, image = phoneWallpaper)
    
    #display the time 
    currentTime = time.ctime (time.time())
    calculatorTime = calculatorHome.create_text (120, 70, text = currentTime, font = ("Helvetica", 10), fill = "white")
    
    #button to close the calculator app 
    calculatorReturnB = Button (calculatorRoot, image = returnImage, borderwidth = 0, highlightthickness = 0,  command = closeCalculator)
    calculatorReturnButton = calculatorHome.create_window (55, 130, window = calculatorReturnB)
    
    #entry for numbers and operation
    intValue = StringVar ()
    intValue.set("")
    number = Entry (calculatorRoot, textvariable = intValue, width = 8, font = ("Helvetica", "48"))
    numberBox = calculatorHome.create_window (180, 215, window = number)
    
    #importing number images
    zeroImage = PhotoImage (file = "0.png")
    oneImage = PhotoImage (file = "1.png")
    twoImage = PhotoImage (file = "2.png")
    threeImage = PhotoImage (file = "3.png")
    fourImage = PhotoImage (file = "4.png")
    fiveImage = PhotoImage (file = "5.png")
    sixImage = PhotoImage (file = "6.png")
    sevenImage = PhotoImage (file = "7.png")
    eightImage = PhotoImage (file = "8.png")
    nineImage = PhotoImage (file = "9.png")
     
    #importing operation and feature images
    addImage = PhotoImage (file = "Add.png")
    minusImage = PhotoImage (file = "Minus.png")
    multiplyImage = PhotoImage (file = "Multiply.png")
    divideImage = PhotoImage (file = "Divide.png")
    negPosImage = PhotoImage (file = "Sign.png")
    equalImage = PhotoImage (file = "Equal.png")
    decimalImage = PhotoImage (file = "Decimal.png")
    clearImage = PhotoImage (file = "C.png")
    ansImage = PhotoImage (file = "Ans.png")
    
    #create calculator buttons
    
    #feature buttons
    addB = Button (calculatorRoot, image = addImage, command = lambda: performOperation (1))
    addButton = calculatorHome.create_window (295, 555, window = addB)
    
    minusB = Button (calculatorRoot, image = minusImage, command = lambda: performOperation (2))
    minusButton = calculatorHome.create_window (295, 470, window = minusB)
    
    multiplyB = Button (calculatorRoot, image = multiplyImage, command = lambda: performOperation (3))
    multiplyButton = calculatorHome.create_window (295, 385, window = multiplyB)
    
    divideB = Button (calculatorRoot, image = divideImage, command = lambda: performOperation (4))
    divideButton = calculatorHome.create_window (295, 300, window = divideB)
    
    clearB = Button (calculatorRoot, image = clearImage, command = clearCalculator)
    clearButton = calculatorHome.create_window (70, 300, window = clearB)
    
    negPosB = Button (calculatorRoot, image = negPosImage, command = lambda: getNumber ("-"))
    negPosButton = calculatorHome.create_window (145, 300, window = negPosB)
    
    decimalB = Button (calculatorRoot, image = decimalImage, command = lambda: getNumber ("."))
    decimalButton = calculatorHome.create_window (220, 300, window = decimalB)
    
    answerB = Button (calculatorRoot, image = ansImage, command = lambda: getNumber (answer))
    answerButton = calculatorHome.create_window (220, 640, window = answerB)
    
    equalB = Button (calculatorRoot, image = equalImage, command = calculation)
    equalButton = calculatorHome.create_window (295, 640, window = equalB)
    
    #number buttons
    button0 = Button (calculatorRoot, image = zeroImage, command = lambda: getNumber(0))
    num0  = calculatorHome.create_window (105, 640, window = button0)
    
    button1 = Button (calculatorRoot, image = oneImage, command = lambda: getNumber(1))
    num1 = calculatorHome.create_window (70, 555, window = button1)
    
    button2 = Button (calculatorRoot, image = twoImage, command = lambda: getNumber(2))
    num2 = calculatorHome.create_window (145, 555, window = button2)
    
    button3 = Button (calculatorRoot, image = threeImage, command = lambda: getNumber(3))
    num3 = calculatorHome.create_window (220, 555, window = button3)
    
    button4 = Button (calculatorRoot, image = fourImage, command = lambda: getNumber(4))
    num4 = calculatorHome.create_window (70, 470, window = button4)
    
    button5 = Button (calculatorRoot, image = fiveImage, command = lambda: getNumber(5))
    num5 = calculatorHome.create_window (145, 470, window = button5)
    
    button6 = Button (calculatorRoot, image = sixImage, command = lambda: getNumber(6))
    num6 = calculatorHome.create_window (220, 470, window = button6)
    
    button7 = Button (calculatorRoot, image = sevenImage, command = lambda: getNumber(7))
    num7 = calculatorHome.create_window (70, 385, window = button7)
    
    button8 = Button (calculatorRoot, image = eightImage, command = lambda: getNumber(8))
    num8 = calculatorHome.create_window (145, 385, window = button8)
    
    button9 = Button (calculatorRoot, image = nineImage, command = lambda: getNumber(9))
    num9 = calculatorHome.create_window (220, 385, window = button9)
    
    timeUpdateCalculator () #keep the time updated
    
    calculatorRoot.mainloop ()
# ---------------- Calculator ---------------- #

# ---------------- UberFeast ---------------- #

#store user's preference choices 
regions = ["Asia", "North America", "Europe", "Africa"]
cuisines = [[["Vietnamese"],["Japanese"], ["Indian"], ["Chinese"], ["Thai"], ["Korean"], ["Middle", "Eastern"]], [["American"],["Mexican"],["Soul","Food"]], [["Italian"], ["German"], ["French"]], [["Egyptian"], ["Moroccan"], ["South","African"]]]
meals = ["Breakfast", "Lunch", "Dinner", "Snack"]

#store images for food
preferenceImages = []
groceriesImages = []

#save a copy of cuisine lists
cuisinesList = cuisines

#groceries list for general store
groceries = [["Milk", 3.00, 5], ["Eggs", 2.00, 5], ["Cheese", 4.50, 5], ["Bread", 2.50, 5], ["Bagel", 3.00, 5], ["Bun", 2.75, 5], ["Pasta", 2.75, 5], ["Rice", 3.50, 5], ["Beans", 1.50, 5], ["Chicken", 7.25, 10], ["Beef", 10.00, 10], ["Pork", 8.50, 10], ["Apple", 5.25, 10], ["Banana", 3.00, 10], ["Spinach", 2.50, 10], ["Tissue", 6.00, 15], ["Toilet Paper", 3.15, 15], ["Towel", 5.00, 15], ["Soap", 3.00, 15], ["Shampoo", 5.25, 15], ["Body Wash", 8.25, 15], ["Tooth Paste", 2.50, 15], ["Tooth Brush", 8.50, 15], ["Flour", 3.50, 5], ["Sugar", 2.50, 5], ["Crisps", 4.99, 5], ["Cooking Oil", 4.25, 5], ["Salt", 2.75, 5], ["BBQ Sauce", 2.99, 5]]

# Vietnamese cuisine food, price, delivery time, and its images
# Vietnamese cuisine food, price, delivery time, and its images
vietnameseB = [["Phở", 20.99, 10], ["Bánh Mì", 15.50, 10], ["Xôi", 12.75, 10], ["Cà Phê", 6.50, 10], ["Trà Đá", 5.00, 10]]
vietnameseL = [["Cơm Tấm", 25.75, 15], ["Bún Thịt Nướng", 22.50, 15], ["Hủ Tiếu", 18.75, 15], ["Sinh Tố", 8.50, 15], ["Nước Mía", 7.25, 15]]
vietnameseD = [["Bánh Xèo", 35.99, 20], ["Bò Lúc Lắc", 30.25, 20], ["Bún Bò Huế", 28.50, 20], ["Nước Dừa", 6.00, 20], ["Bia", 9.75, 20]]
vietnameseS = [["Bánh Tráng Trộn", 7.00, 5], ["Gỏi Cuốn", 8.75, 5], ["Chả Giò", 7.25, 5], ["Chè", 6.00, 5], ["Trà Sữa", 6.75, 5]]

# Japanese cuisine food, price, delivery time, and its images
japaneseB = [["Tamagoyaki", 25.99, 10], ["Natto", 18.50, 10], ["Gohan", 12.75, 10], ["Green Tea", 7.50, 10], ["Miso Soup", 6.75, 10]]
japaneseL = [["Sushi", 32.50, 15], ["Ramen", 28.75, 15], ["Tempura", 24.50, 15], ["Matcha Latte", 9.25, 15], ["Miso Soup", 6.75, 15]]
japaneseD = [["Okonomiyaki", 55.99, 20], ["Yakitori", 45.25, 20], ["Shabu-Shabu", 40.50, 20], ["Sake", 12.50, 20], ["Umeshu", 9.75, 20]]
japaneseS = [["Onigiri", 7.00, 5], ["Edamame", 7.50, 5], ["Taiyaki", 6.25, 5], ["Milk Tea", 5.75, 5], ["Calpico", 5.00, 5]]

# Indian cuisine food, price, delivery time, and its images
indianB = [["Masala Chai", 22.99, 10], ["Poha", 18.50, 10], ["Idli", 14.75, 10], ["Mango Lassi", 8.50, 10], ["Chaas", 7.00, 10]]
indianL = [["Biryani", 30.50, 15], ["Chole Bhature", 27.75, 15], ["Rasam", 23.00, 15], ["Nimbu Pani", 9.25, 15], ["Thandai", 8.50, 15]]
indianD = [["Rajma Masala", 45.99, 20], ["Palak Soup", 40.25, 20], ["Dal Fry", 35.50, 20], ["Aam Panna", 10.50, 20], ["Rose Milk", 9.75, 20]]
indianS = [["Samosa", 7.00, 5], ["Bhel Puri", 8.50, 5], ["Paneer Tikka", 7.25, 5], ["Kokum Sherbet", 6.75, 5], ["Badam Milk", 5.50, 5]]

# Chinese cuisine food, price, delivery time, and its images
chineseB = [["Congee", 25.99, 10], ["Youtiao", 20.50, 10], ["Century Egg Congee", 18.75, 10], ["Soy Milk", 8.50, 10], ["Chinese Tea", 7.75, 10]]
chineseL = [["Dim Sum", 32.50, 15], ["Hot and Sour Soup", 28.75, 15], ["Stir-Fried Noodles", 24.50, 15], ["Chrysanthemum Tea", 9.25, 15], ["Winter Melon Tea", 8.50, 15]]
chineseD = [["Kung Pao Chicken", 55.99, 20], ["Peking Duck", 48.00, 20], ["Egg Drop Soup", 42.50, 20], ["Rice Wine", 13.50, 20], ["Boba", 9.00, 20]]
chineseS = [["Char Siu Bao", 9.00, 5], ["Cong You Bing", 8.50, 5], ["Cha Ye Dan", 7.25, 5], ["Boba", 6.75, 5], ["Soy Milk", 5.50, 5]]

# Thai cuisine food, price, delivery time, and its images
thaiB = [["Khao Tom", 22.99, 10], ["Kai Jeow", 18.50, 10], ["Nam Prik Ong", 14.75, 10], ["Thai Iced Tea", 8.00, 10], ["Fresh Coconut Water", 7.25, 10]]
thaiL = [["Pad Thai", 30.50, 15], ["Gaeng Keow Wan", 27.75, 15], ["Som Tum", 23.50, 15], ["Oliang", 9.25, 15], ["Cha Khiao Yen", 8.50, 15]]
thaiD = [["Tom Yum Goong", 45.99, 20], ["Pad Kra Pao", 40.25, 20], ["Massaman Curry", 35.50, 20], ["Nam Dok Anchan", 10.50, 20], ["Nam Manao", 9.00, 20]]
thaiS = [["Miang Kham", 9.00, 5], ["Tod Mun Pla", 8.50, 5], ["Khanom Krok", 7.25, 5], ["Cha Yen", 6.75, 5], ["Oliang", 5.50, 5]]

# Korean cuisine food, price, delivery time, and its images
koreanB = [["Kimchi Bokkeumbap", 25.99, 10], ["Gyeran Mari", 20.50, 10], ["Kongnamul Guk", 18.00, 10], ["Sujeonggwa", 8.50, 10], ["Yuja Cha", 7.75, 10]]
koreanL = [["Bibimbap", 32.50, 15], ["Japchae", 28.75, 15], ["Samgyeopsal", 24.50, 15], ["Sikhye", 9.00, 15], ["Boricha", 8.50, 15]]
koreanD = [["Kimchi Jjigae", 55.99, 20], ["Dak Galbi", 48.25, 20], ["Bulgogi", 42.50, 20], ["Makgeolli", 13.50, 20], ["Soju", 9.75, 20]]
koreanS = [["Twigim", 9.00, 5], ["Gimbap", 8.50, 5], ["Tteokbokki", 7.25, 5], ["Yuja Ade", 6.75, 5], ["Sikhye", 5.50, 5]]

# Middle Eastern cuisine food, price, delivery time, and its images
middleEasternB = [["Shakshuka", 20.99, 10], ["Ful Medames", 15.50, 10], ["Labneh", 12.75, 10], ["Qahwa", 6.00, 10], ["Shai bi Na'na'", 5.75, 10]]
middleEasternL = [["Falafel Wrap", 25.75, 15], ["Mujadara", 22.50, 15], ["Shawarma", 18.75, 15], ["Ayran", 8.50, 15], ["Tamr Hindi", 7.25, 15]]
middleEasternD = [["Kebabs", 35.00, 20], ["Mansaf", 30.25, 20], ["Mezze Platter", 28.50, 20], ["Pomegranate Juice", 6.50, 20], ["Rose Lemonade", 9.75, 20]]
middleEasternS = [["Pita Chips & Hummus", 9.00, 5], ["Falafel", 8.75, 5], ["Baba Ganoush", 7.25, 5], ["Cay", 5.50, 5], ["Laban Ayran", 6.75, 5]]

# American cuisine food, price, delivery time, and its images
americanB = [["Pancakes & Syrup", 11.99, 10], ["Egg Bacon Sandwich", 15.50, 10], ["Oatmeal & Fruit", 12.75, 10], ["Coffee", 6.50, 10], ["Orange Juice", 5.75, 10]]
americanL = [["Premium Cheeseburger", 15.00, 15], ["Chicken Caesar Salad", 22.50, 15], ["Grilled Cheese & Tomato Soup", 18.75, 15], ["Iced Tea", 8.50, 15], ["Lemonade", 7.00, 15]]
americanD = [["Barbecue Ribs", 35.99, 20], ["Macaroni & Cheese", 30.25, 20], ["Grilled Salmon & Vegetables", 28.50, 20], ["Red Wine", 6.50, 20], ["Craft Beer", 9.00, 20]]
americanS = [["Popcorn", 7.00, 5], ["Apple & Peanut Butter", 8.75, 5], ["Trail Mix", 7.25, 5], ["Smoothie", 5.50, 5], ["Iced Coffee", 6.75, 5]]

# Mexican cuisine food, price, delivery time, and its images
mexicanB = [["Huevos Rancheros", 20.99, 10], ["Chilaquiles", 15.50, 10], ["Breakfast Burrito", 12.75, 10], ["Horchata", 6.00, 10], ["Café de Olla", 5.75, 10]]
mexicanL = [["Tacos al Pastor", 25.75, 15], ["Chicken Quesadillas", 22.50, 15], ["Enchiladas Verdes", 18.75, 15], ["Agua Fresca", 8.50, 15], ["Michelada", 7.25, 15]]
mexicanD = [["Carne Asada Tacos", 27.99, 20], ["Chiles Rellenos", 30.25, 20], ["Mole Poblano", 28.50, 20], ["Margarita", 6.50, 20], ["Cerveza", 9.75, 20]]
mexicanS = [["Guacamole & Chips", 7.00, 5], ["Elote", 8.00, 5], ["Tostadas", 7.25, 5], ["Agua de Jamaica", 5.50, 5], ["Piña Colada", 6.75, 5]]

# Soul Food cuisine food, price, delivery time, and its images
soulFoodB = [["Shrimp & Grits", 20.99, 10], ["Chicken & Waffles", 15.50, 10], ["Biscuits and Gravy", 12.75, 10], ["Sweet Tea", 6.50, 10], ["Coffee with Cream", 5.75, 10]]
soulFoodL = [["Fried Catfish Sandwich", 25.75, 15], ["Collard Greens & Smoked Turkey", 22.50, 15], ["Jambalaya", 18.75, 15], ["Lemonade", 8.50, 15], ["Fruit Punch", 7.25, 15]]
soulFoodD = [["Fried Chicken", 26.00, 20], ["Shrimp Étouffée", 30.25, 20], ["Barbecue Ribs", 28.50, 20], ["Iced Tea with Lemon", 6.50, 20], ["Mint Julep", 9.75, 20]]
soulFoodS = [["Deviled Eggs", 9.50, 5], ["Pimento Cheese Dip with Crackers", 8.00, 5], ["Fried Green Tomatoes", 7.25, 5], ["Buttermilk", 5.50, 5], ["Southern Sweet Tea", 6.75, 5]]

# Italian cuisine food, price, delivery time, and its images
italianB = [["Cornetti", 20.99, 10], ["Frittata", 15.50, 10], ["Pane e Nutella", 12.75, 10], ["Caffè Latte", 6.00, 10], ["Espresso", 5.75, 10]]
italianL = [["Caprese Salad", 25.75, 15], ["Panini", 22.00, 15], ["Pasta Primavera", 18.75, 15], ["Aperol Spritz", 8.50, 15], ["Limoncello", 7.25, 15]]
italianD = [["Margherita Pizza", 30.99, 20], ["Risotto ai Funghi", 30.25, 20], ["Chicken Parmesan", 28.50, 20], ["Chianti", 6.50, 20], ["Prosecco", 9.75, 20]]
italianS = [["Bruschetta", 8.00, 5], ["Arancini", 8.75, 5], ["Crostini", 7.25, 5], ["Limonata", 5.50, 5], ["Gelato", 6.75, 5]]

# German cuisine food, price, delivery time, and its images
germanB = [["Brötchen", 20.99, 10], ["Bircher Müsli", 15.50, 10], ["Eierkuchen", 12.75, 10], ["Kaffee", 6.50, 10], ["Tee", 5.75, 10]]
germanL = [["Schnitzel", 25.75, 15], ["Wurstsalat", 22.50, 15], ["Kartoffelsuppe", 18.75, 15], ["Bier", 8.50, 15], ["Mineralwasser", 5.00, 15]]
germanD = [["Bratwurst & Sauerkraut", 35.00, 20], ["Rouladen & Kartoffeln", 30.25, 20], ["Käsespätzle", 28.50, 20], ["Rotwein", 6.50, 20], ["Apfelschorle", 9.75, 20]]
germanS = [["Currywurst", 9.50, 5], ["Leberkäse Semmel", 8.75, 5], ["Bienenstich", 7.25, 5], ["Mineralwasser", 5.00, 5], ["Eiskaffee", 6.75, 5]]

# French cuisine food, price, delivery time, and its images
frenchB = [["Croissant", 12.00, 10], ["Pain au Chocolat", 15.50, 10], ["Pain Perdu", 12.75, 10], ["Café au Lait", 6.50, 10], ["Chocolat Chaud", 5.75, 10]]
frenchL = [["Salade Niçoise", 25.75, 15], ["Croque Monsieur", 22.50, 15], ["Quiche Lorraine", 18.75, 15], ["Vin Rosé", 8.50, 15], ["Citron Pressé", 7.25, 15]]
frenchD = [["Coq au Vin", 32.00, 20], ["Boeuf Bourguignon", 30.25, 20], ["Ratatouille", 28.50, 20], ["Vin Rouge", 6.50, 20], ["Kir", 9.75, 20]]
frenchS = [["Quiche Lorraine", 9.50, 5], ["Tartelette aux Fruits", 8.75, 5], ["Gougères", 7.25, 5], ["Café", 5.50, 5], ["Thé", 6.75, 5]]

# Egyptian cuisine food, price, delivery time, and its images
egyptianB = [["Ful Medames", 20.99, 10], ["Ta'ameya", 15.50, 10], ["Fiteer Baladi", 12.00, 10], ["Karakade", 6.50, 10], ["Sahlab", 5.75, 10]]
egyptianL = [["Koshari", 25.75, 15], ["Mahshi", 22.50, 15], ["Mulukhiyah Soup", 18.00, 15], ["Sobia", 8.50, 15], ["Sekanjabin", 7.25, 15]]
egyptianD = [["Molokhia", 34.00, 20], ["Fattah", 30.25, 20], ["Kofta Tagine", 28.50, 20], ["Qamar al-Din", 6.50, 20], ["Erk Sous", 9.75, 20]]
egyptianS = [["Kunafa", 9.50, 5], ["Basbousa", 8.75, 5], ["Feteer Meshaltet", 7.25, 5], ["Sahlab", 5.50, 5], ["Sobia", 6.75, 5]]

# Moroccan cuisine food, price, delivery time, and its images
moroccanB = [["Baghrir", 20.00, 10], ["Msemen", 15.50, 10], ["Harira", 12.75, 10], ["Atayef", 6.50, 10], ["Amlou Smoothie", 5.75, 10]]
moroccanL = [["Tagine", 25.75, 15], ["Briouat", 22.50, 15], ["Zaalouk", 18.75, 15], ["Limonade", 8.50, 15], ["Jus d'Avocat", 7.00, 15]]
moroccanD = [["Couscous", 29.99, 20], ["Pastilla", 30.25, 20], ["Mechoui", 28.50, 20], ["Jus de Fruits", 6.50, 20], ["Lben", 9.75, 20]]
moroccanS = [["Briouat", 9.00, 5], ["Chebakia", 8.50, 5], ["Sellou", 7.25, 5], ["Atay", 5.50, 5], ["Amlou Smoothie", 6.75, 5]]

# South African cuisine food, price, delivery time, and its images
southAfricanB = [["Boerewors Roll", 20.99, 10], ["Milk Tart", 15.50, 10], ["Vetkoek", 12.75, 10], ["Rooibos Tea", 6.50, 10], ["Amarula", 5.75, 10]]
southAfricanL = [["Bunny Chow", 25.75, 15], ["Bobotie", 22.50, 15], ["Potjiekos", 18.75, 15], ["Rooibos Iced Tea", 8.50, 15], ["Soweto Gold Lager", 7.25, 15]]
southAfricanD = [["Braai", 29.99, 20], ["Pap & Wors", 30.25, 20], ["Chakalaka", 28.50, 20], ["Pinotage", 6.50, 20], ["Rooibos Tea", 9.75, 20]]
southAfricanS = [["Biltong", 9.00, 5], ["Droëwors", 8.50, 5], ["Koeksisters", 7.25, 5], ["Umqombothi", 5.50, 5], ["Cape Malay Curry", 6.75, 5]]

#store user's preference 
region = ""
cuisine = ""
meal = ""

#food list of user's preference 
foodPreference = []
foodImages = []

#store the alphabet and number 1-10 to create order code 
alphabetCode = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numberCode = ["0","1","2","3","4","5","6","7","8","9"]

#make empty list to store carts information
cart = []

def customizeFood (): #adjust food based on user's choice
    global foodPreference
    
    #pull specific list of cuisine

    #Asian cuisines 
    if region == "Asia":
        if cuisine [2:(len(cuisine) - 3)] == "Vietnamese":
            if meal == "Breakfast":
                for i in range (0, len (vietnameseB)): #add user's food preference list including images
                    foodPreference.append (vietnameseB [i])
                    foodImages.append (vietnameseBImages [i])
                    
            elif meal == "Lunch":
                for i in range (0, len (vietnameseL)):
                    foodPreference.append (vietnameseL [i])
                    foodImages.append (vietnameseLImages [i])
                    
            elif meal == "Dinner":
                for i in range (0, len (vietnameseD)):
                    foodPreference.append (vietnameseD [i])
                    foodImages.append (vietnameseDImages [i])
                    
            else:
                for i in range (0, len (vietnameseS)):
                    foodPreference.append (vietnameseS [i])
                    foodImages.append (vietnameseSImages [i])
                    
        elif cuisine [2:(len(cuisine) - 3)] == "Japanese":
            if meal == "Breakfast":
                for i in range (0, len (japaneseB)):
                    foodPreference.append (japaneseB [i])
                    foodImages.append (japaneseBImages [i])
                    
            elif meal == "Lunch":
                for i in range (0, len (japaneseL)):
                    foodPreference.append (japaneseL [i])
                    foodImages.append (japaneseLImages [i])
                    
            elif meal == "Dinner":
                for i in range (0, len (japaneseD)):
                    foodPreference.append (japaneseD [i])
                    foodImages.append (japaneseDImages [i])
                    
            else:
                for i in range (0, len (japaneseS)):
                    foodPreference.append (japaneseS [i])
                    foodImages.append (japaneseSImages [i])
                
        elif cuisine [2:(len(cuisine) - 3)] == "Indian":
            if meal == "Breakfast":
                for i in range (0, len (indianB)):
                    foodPreference.append (indianB [i])
                    foodImages.append (indianBImages [i])
                    
            elif meal == "Lunch":
                for i in range (0, len (indianL)):
                    foodPreference.append (indianL [i])
                    foodImages.append (indianLImages [i])
                    
            elif meal == "Dinner":
                for i in range (0, len (indianD)):
                    foodPreference.append (indianD [i])
                    foodImages.append (indianDImages [i])
                    
            else:
                for i in range (0, len (indianS)):
                    foodPreference.append (indianS [i])
                    foodImages.append (indianSImages [i])
                
        elif cuisine [2:(len(cuisine) - 3)] == "Chinese":
            if meal == "Breakfast":
                for i in range (0, len (chineseB)):
                    foodPreference.append (chineseB [i])
                    foodImages.append (chineseBImages [i])
                    
            elif meal == "Lunch":
                for i in range (0, len (chineseL)):
                    foodPreference.append (chineseL [i])
                    foodImages.append (chineseLImages [i])
                    
            elif meal == "Dinner":
                for i in range (0, len (chineseD)):
                    foodPreference.append (chineseD [i])
                    foodImages.append (chineseDImages [i])
                    
            else:
                for i in range (0, len (chineseS)):
                    foodPreference.append (chineseS [i])
                    foodImages.append (chineseSImages [i])
                
        elif cuisine [2:(len(cuisine) - 3)] == "Thai":
            if meal == "Breakfast":
                for i in range (0, len (thaiB)):
                    foodPreference.append (thaiB [i])
                    foodImages.append (thaiBImages [i])
                    
            elif meal == "Lunch":
                for i in range (0, len (thaiL)):
                    foodPreference.append (thaiL [i])
                    foodImages.append (thaiLImages [i])
                    
            elif meal == "Dinner":
                for i in range (0, len (thaiD)):
                    foodPreference.append (thaiD [i])
                    foodImages.append (thaiDImages [i])
                    
            else:
                for i in range (0, len (thaiS)):
                    foodPreference.append (thaiS [i])
                    foodImages.append (thaiSImages [i])
                
        elif cuisine [2:(len(cuisine) - 3)] == "Korean":
            if meal == "Breakfast":
                for i in range (0, len (koreanB)):
                    foodPreference.append (koreanB [i])
                    foodImages.append (koreanBImages [i])
                    
            elif meal == "Lunch":
                for i in range (0, len (koreanL)):
                    foodPreference.append (koreanL [i])
                    foodImages.append (koreanLImages [i])
                
            elif meal == "Dinner":
                for i in range (0, len (koreanD)):
                    foodPreference.append (koreanD [i])
                    foodImages.append (koreanDImages [i])
                    
            else:
                for i in range (0, len (koreanS)):
                    foodPreference.append (koreanS [i])
                    foodImages.append (koreanSImages [i])
                
        else:
            if meal == "Breakfast":
                for i in range (0, len (middleEasternB)):
                    foodPreference.append (middleEasternB [i])
                    foodImages.append (middleEasternBImages [i])
                    
            elif meal == "Lunch":
                for i in range (0, len (middleEasternL)):
                    foodPreference.append (middleEasternL [i])
                    foodImages.append (middleEasternLImages [i])
                    
            elif meal == "Dinner":
                for i in range (0, len (middleEasternD)):
                    foodPreference.append (middleEasternD [i])
                    foodImages.append (middleEasternDImages [i])
                    
            else:
                for i in range (0, len (middleEasternS)):
                    foodPreference.append (middleEasternS [i])
                    foodImages.append (middleEasternSImages [i])
                    
    #North American cuisines          
    elif region == "North America":
        if cuisine [2:(len(cuisine) - 3)] == "American":
            if meal == "Breakfast":
                for i in range (0, len (americanB)):
                    foodPreference.append (americanB [i])
                    foodImages.append (americanBImages [i])
                    
            elif meal == "Lunch":
                for i in range (0, len (americanL)):
                    foodPreference.append (americanL [i])
                    foodImages.append (americanLImages [i])
                    
            elif meal == "Dinner":
                for i in range (0, len (americanD)):
                    foodPreference.append (americanD [i])
                    foodImages.append (americanDImages [i])
                    
            else:
                for i in range (0, len (americanS)):
                    foodPreference.append (americanS [i])
                    foodImages.append (americanSImages [i])
                
        elif cuisine [2:(len(cuisine) - 3)] == "Mexican":
            if meal == "Breakfast":
                for i in range (0, len (mexicanB)):
                    foodPreference.append (mexicanB [i])
                    foodImages.append (mexicanBImages [i])
            elif meal == "Lunch":
                for i in range (0, len (mexicanL)):
                    foodPreference.append (mexicanL [i])
                    foodImages.append (mexicanLImages [i])
            elif meal == "Dinner":
                for i in range (0, len (mexicanD)):
                    foodPreference.append (mexicanD [i])
                    foodImages.append (mexicanDImages [i])
            else:
                for i in range (0, len (mexicanS)):
                    foodPreference.append (mexicanS [i])
                    foodImages.append (mexicanSImages [i])
                
        else:
            if meal == "Breakfast":
                for i in range (0, len (soulFoodB)):
                    foodPreference.append (soulFoodB [i])
                    foodImages.append (soulFoodBImages [i])
                    
            elif meal == "Lunch":
                for i in range (0, len (soulFoodL)):
                    foodPreference.append (soulFoodL [i])
                    foodImages.append (soulFoodLImages [i])
                    
            elif meal == "Dinner":
                for i in range (0, len (soulFoodD)):
                    foodPreference.append (soulFoodD [i])
                    foodImages.append (soulFoodDImages [i])
            else:
                for i in range (0, len (soulFoodS)):
                    foodPreference.append (soulFoodS [i])
                    foodImages.append (soulFoodSImages [i])
                    
    #European Cuisines          
    elif region == "Europe":
        if cuisine [2:(len(cuisine) - 3)] == "Italian":
            if meal == "Breakfast":
                for i in range (0, len (italianB)):
                    foodPreference.append (italianB [i])
                    foodImages.append (italianBImages [i])
                    
            elif meal == "Lunch":
                for i in range (0, len (italianL)):
                    foodPreference.append (italianL [i])
                    foodImages.append (italianLImages [i])
                    
            elif meal == "Dinner":
                for i in range (0, len (italianD)):
                    foodPreference.append (italianD [i])
                    foodImages.append (italianDImages [i])
                    
            else:
                for i in range (0, len (italianS)):
                    foodPreference.append (italianS [i])
                    foodImages.append (italianSImages [i])
                
        elif cuisine [2:(len(cuisine) - 3)] == "German":
            if meal == "Breakfast":
                for i in range (0, len (germanB)):
                    foodPreference.append (germanB [i])
                    foodImages.append (germanBImages [i])
                    
            elif meal == "Lunch":
                for i in range (0, len (germanL)):
                    foodPreference.append (germanL [i])
                    foodImages.append (germanLImages [i])
                    
            elif meal == "Dinner":
                for i in range (0, len (germanD)):
                    foodPreference.append (germanD [i])
                    foodImages.append (germanDImages [i])
                    
            else:
                for i in range (0, len (germanS)):
                    foodPreference.append (germanS [i])
                    foodImages.append (germanSImages [i])
                
        elif cuisine [2:(len(cuisine) - 3)] == "French":
            if meal == "Breakfast":
                for i in range (0, len (frenchB)):
                    foodPreference.append (frenchB [i])
                    foodImages.append (frenchBImages [i])
            elif meal == "Lunch":
                for i in range (0, len (frenchL)):
                    foodPreference.append (frenchL [i])
                    foodImages.append (frenchLImages [i])
            elif meal == "Dinner":
                for i in range (0, len (frenchD)):
                    foodPreference.append (frenchD [i])
                    foodImages.append (frenchDImages [i])
            else:
                for i in range (0, len (frenchS)):
                    foodPreference.append (frenchS [i])
                    foodImages.append (frenchSImages [i])
    
    #African cuisines
    elif region == "Africa":
                
        if cuisine [2:(len(cuisine) - 3)] == "Egyptian":
            if meal == "Breakfast":
                for i in range (0, len (egyptianB)):
                    foodPreference.append (egyptianB [i])
                    foodImages.append (egyptianBImages [i])
                    
            elif meal == "Lunch":
                for i in range (0, len (egyptianL)):
                    foodPreference.append (egyptianL [i])
                    foodImages.append (egyptianLImages [i])
                    
            elif meal == "Dinner":
                for i in range (0, len (egyptianD)):
                    foodPreference.append (egyptianD [i])
                    foodImages.append (egyptianDImages [i])
                    
            else:
                for i in range (0, len (egyptianS)):
                    foodPreference.append (egyptianS [i])
                    foodImages.append (egyptianSImages [i])
                
        elif cuisine [2:(len(cuisine) - 3)] == "Moroccan":
            if meal == "Breakfast":
                for i in range (0, len (moroccanB)):
                    foodPreference.append (moroccanB [i])
                    foodImages.append (moroccanBImages [i])
                    
            elif meal == "Lunch":
                for i in range (0, len (moroccanL)):
                    foodPreference.append (moroccanL [i])
                    foodImages.append (moroccanLImages [i])
                    
            elif meal == "Dinner":
                for i in range (0, len (moroccanD)):
                    foodPreference.append (moroccanD [i])
                    foodImages.append (moroccanDImages [i])
                    
            else:
                for i in range (0, len (moroccanS)):
                    foodPreference.append (moroccanS [i])
                    foodImages.append (moroccanSImages [i])
        else:
            if meal == "Breakfast":
                for i in range (0, len (southAfricanB)):
                    foodPreference.append (southAfricanB [i])
                    foodImages.append (southAfricanBImages [i])
                    
            elif meal == "Lunch":
                for i in range (0, len (southAfricanL)):
                    foodPreference.append (southAfricanL [i])
                    foodImages.append (southAfricanLImages [i])
                    
            elif meal == "Dinner":
                for i in range (0, len (southAfricanD)):
                    foodPreference.append (southAfricanD [i])
                    foodImages.append (southAfricanDImages [i])
            else:
                for i in range (0, len (southAfricanS)):
                    foodPreference.append (southAfricanS [i])
                    foodImages.append (southAfricanSImages [i])
                
    showFood () #display food options depending on user's choice
    
def resetCart ():
    global cart, foodPreference, foodImages, cuisines
    
    #reset cart and user's food preference 
    cart = []
    foodPreference = []
    foodImages = []
     
    #revert cuisine list back to original 
    cuisines = cuisinesList

def receiptScrollRegion (): #update the range of the scroll bar
    
     cartsCanvas.configure(scrollregion = cartsCanvas.bbox ("all"))
    
def calculateCost (): #calculate the total payment 
    
    subtotal = 0
    
    #calculate the subtotal of the cart 
    for i in range (0, len(cart)):
        subtotal = subtotal + float(cart [i][1])
        subtotal = float(format (subtotal, ".2f"))
    
    #caculate the subtotal with tax added
    taxRate = 0.13
    tax = taxRate * subtotal
    tax = float(format (tax, ".2f"))
    
    #calcualte the total payment 
    total = subtotal + tax
    total = float(format (total, ".2f"))
    
    return subtotal, tax, total

def deliveryTime (): #caculate the delivery time 

    totalTime = 0
    
    #calculate the total time it tasks to delivery items in cart
    for i in range (0, len (cart)):
        
        totalTime = totalTime + (cart [i][2])
    
    return totalTime
             
def addCart (order, price, timeCost): #add food to cart list
    
    #add items to cart
    cart.append ((order, format(price,".2f") , timeCost))
    
    orderInfo (order, price, timeCost)

def cancelItem (orderItem, cancelButton, foodIndex): 
    
    #delete the specific task along with its delete button 
    orderItem.destroy ()
    cancelButton.destroy ()
    cart.pop (foodIndex)
    
    receiptScrollRegion ()
    
def orderInfo (foodOrder, price, timeCost): #create a section for user to view their order
    
    if page == 1: #create cart items depending on store
        frame = itemsFrame
    elif page == 2:
        frame = browseCartFrame
    else:
        frame = viewFrame
   
    # Create the listbox for the item information
    orderItem = Listbox (frame, width = 50, height = 1, font = ("Helvetica", 15))
    orderItem.insert (END, "            " + foodOrder + "  " + "$" + format(price, ".2f"))
    orderItem.pack (pady = 5)
    
    # Create delete cancel for new items
    cancelButton = Button (orderItem, text = "Cancel Item", borderwidth = 0, highlightthickness = 0,  command = lambda: cancelItem (orderItem, cancelButton, cart.index ((foodOrder, format (price,".2f"), timeCost))))
    cancelButton.place (relx = 0, rely = 0.5, anchor = W)
    
def searchOptions (groceriesOptions): #update the listbox 
    
    #clear the listbox 
    groceriesList.delete (0, END)
    
    #add groceries options in the listbox
    for i in range (0, len(groceriesOptions)):
        groceriesList.insert (END, groceriesOptions [i][0])

def selectedFood (select): #update the entry box with the listbox clicked
    global cart, searchFood, cart, addSearchB
    
    cart = [] #store 1 item only
    
    # replace the selected food in the entry box
    foodSelected = groceriesList.nearest(select.y)
    searchFood = groceriesList.get (foodSelected)
    searchEntry.delete(0, END)
    searchEntry.insert(0, searchFood)
    
    for i in range (0, len(groceries)):
       
       if searchFood == groceries [i][0]:
           cart.append (groceries [i])
   
    #display button after item selected
    uberHome.itemconfig (addSearchButton, state = NORMAL)
    addSearchB.config (command = lambda foodItem = cart[0][0], price = cart[0][1], timeCost = cart[0][2]: orderInfo(foodItem, price, timeCost))
           
def check (select): #check entry and update listbox
    global searchItem
    
    # get searched grocery
    searchItem = searchEntry.get()

    if searchItem == "": #compare the search grocery with grocery's item name in grocery list
        groceriesOptions = groceries
    else:
        groceriesOptions = []
        for i in range(0, len(groceries)):
            groceriesLength = groceries[i][0]
            
            for f in range(0, len(groceriesLength) - len(searchItem) + 1):
                if groceriesLength.lower()[f : f + len(searchItem)] == searchItem.lower():
                    groceriesOptions.append(groceries[i])

    #update listbox with selected items               
    searchOptions (groceriesOptions)
        
def clearHome (): #clear home page
    
    uberHome.itemconfig (uberFrameBox, state = HIDDEN)
    uberHome.itemconfig (groceriesText, state = HIDDEN)
    uberHome.itemconfig (groceriesFrameBox, state = HIDDEN)
    uberHome.itemconfig (orderButton, state = HIDDEN)
    uberHome.itemconfig (groceriesImage, state = HIDDEN)
    groceriesScroll.place_forget ()
    viewScroll.place_forget ()
    menuScroll.place_forget ()
    
    for i in range (0, len(storeGroceries)):
        storeGroceries [i].pack_forget ()
    
def clearBrowse (): #clear browsing page
    
    uberHome.itemconfig (searchBox, state = HIDDEN)
    uberHome.itemconfig (searchFrameBox, state = HIDDEN)
    uberHome.itemconfig (addSearchButton, state = HIDDEN)
    uberHome.itemconfig (browseIntroImage, state = HIDDEN)
    uberHome.itemconfig (browseText, state = HIDDEN)
    
def clearFoodify (): #clear foodify page
    
    uberHome.itemconfig (regionPreferenceText, state = HIDDEN)
    uberHome.itemconfig (regionOptionsBox, state = HIDDEN)
    uberHome.itemconfig (confirmRegionButton, state = HIDDEN)
    uberHome.itemconfig (mealText, state = HIDDEN)
    uberHome.itemconfig (mealFrameBox, state = HIDDEN)
    uberHome.itemconfig (optionsFrameBox, state = HIDDEN)
    uberHome.itemconfig (confirmMealButton, state = HIDDEN)
    uberHome.itemconfig (cuisinePreferenceText, state = HIDDEN)
    uberHome.itemconfig (confirmCuisineButton, state = HIDDEN)
    uberHome.itemconfig (foodPreferenceText, state = HIDDEN)
    uberHome.itemconfig (placeOrderText, state = HIDDEN)
    uberHome.itemconfig (cuisineOptionsBox, state = HIDDEN)
    uberHome.itemconfig (foodifyIntroFrameBox, state = HIDDEN)
    uberHome.itemconfig (foodifyIntroButton, state = HIDDEN)
    uberHome.itemconfig (placeOrderButton, state = HIDDEN)
    uberHome.itemconfig (orderFrameBox, state = HIDDEN)
    uberHome.itemconfig (internationalImage, state = HIDDEN)
    uberHome.itemconfig (modifyText, state = HIDDEN)
    orderScroll.place_forget ()
    checkScroll.place_forget ()
    optionsScroll.place_forget ()
    
    for i in range (0, len(storeMeals)):
        storeMeals [i].pack_forget ()
    
    for i in range (0, len(storeFood)):
        storeFood [i].pack_forget ()
        
def clearCarts (): #clear cart page
        
    uberHome.itemconfig (receiptCostBackground, state = HIDDEN)
    uberHome.itemconfig (subtotalText, state = HIDDEN)
    uberHome.itemconfig (taxText, state = HIDDEN)
    uberHome.itemconfig (totalText, state = HIDDEN)
    uberHome.itemconfig (subtotalPayment, state = HIDDEN)
    uberHome.itemconfig (taxPayment, state = HIDDEN)
    uberHome.itemconfig (totalPayment, state = HIDDEN)
    
    uberHome.itemconfig (cartsFrameBox, state = HIDDEN)
    uberHome.itemconfig (emptyCart, state = HIDDEN)
    
def home (): #clear other pages and show home page
    
    homeB.config (image = selectedHomeImage)
    foodifyB.config (image = foodifyImage)
    browseB.config (image = browseImage)
    cartsB.config (image = cartsImage)
    
    clearHome ()
    
    clearBrowse ()
    
    clearFoodify ()
    
    resetCart ()
    
    clearCarts ()
    
    showHome ()
    
def browse (): #clear other pages and show browse page
    
    homeB.config (image = homeImage)
    foodifyB.config (image = foodifyImage)
    browseB.config (image = selectedBrowseImage)
    cartsB.config (image = cartsImage)

    clearHome ()
    
    clearBrowse ()
    
    clearFoodify ()
    
    resetCart ()
    
    clearCarts ()
    
    showBrowse ()
    
def foodify (): #clear other pages and show foodify page
    
    homeB.config (image = homeImage)
    foodifyB.config (image = selectedFoodifyImage)
    browseB.config (image = browseImage)
    cartsB.config (image = cartsImage)
    
    clearHome ()
    
    clearBrowse ()
    
    clearFoodify ()
    
    resetCart ()
    
    clearCarts ()
    
    showFoodify ()

def validateRegion (): 
    global cuisines, region
    
    region = selectedRegion.get () 
    
    if region != "Region": #check if user pick an option
        
        #assign region based on user's choice 
        if region == "Asia":
            cuisines = cuisines [0]
        elif region == "North America":
            cuisines = cuisines [1]
        elif region == "Europe":
            cuisines = cuisines [2]
        elif region == "Africa":
            cuisines = cuisines [3]
        
        #hide confirm button and disable option menu 
        uberHome.itemconfig (confirmRegionButton, state = HIDDEN)
        regionOptions.config (state = DISABLED)
        
        #move to next question 
        showCuisine ()
         
    else: #ensure user pick an option 
        confirmRegionB.config (state = NORMAL)
        messagebox.showinfo ("Error", "Please select a Region.")
       
def validateCuisine ():
    global cuisine
    
    cuisine = selectedCuisine.get ()
    
    if cuisine != "Cuisine": #check if user pick an option
        
        #hide confirm button and disable option menu 
        uberHome.itemconfig (confirmCuisineButton, state = HIDDEN)
        cuisineOptions.config (state = DISABLED)
        
        #move to next question
        showMeal ()
    
    else: #ensure user pick an option 
        confirmCuisineB.config (state = NORMAL)
        messagebox.showinfo ("Error", "Please select a Cuisine.")
        
def validateMeal ():
    global meal 
    
    meal = selectedMeal.get ()
    
    #assign meal based on user's choice 
    if True == True:
        if meal == 0:
            meal = "Breakfast"
        elif meal == 1:
            meal = "Lunch"
        elif meal == 2:
            meal = "Dinner"
        else:
            meal = "Snack"
        
        #hide confirm button and disable option buttons
        uberHome.itemconfig (confirmMealButton, state = HIDDEN)
        for i in range (0, len(storeMeals)):
            storeMeals [i].config (state = DISABLED)
        
        #start generating food based on the collected response 
        customizeFood ()
    
    else: #ensure user pick an option 
         confirmMealB.config (state = NORMAL)
         messagebox.showinfo ("Error", "Please select a Meal.")


def carts (): #clear other pages and show carts page
    global emptyCart
    
    homeB.config (image = homeImage)
    foodifyB.config (image = foodifyImage)
    browseB.config (image = browseImage)
    cartsB.config (image = selectedCartsImage)

    clearHome ()
    
    clearBrowse ()
    
    clearFoodify ()
    
    clearCarts ()
    
    if cart == []: #show empty cart
        showEmptyCarts ()
    else:
        showReceipt ()
# ---------------- UberFeast ---------------- #
# ---------------- UberFeast ---------------- # 
    
def openUberFeasts ():
    
    global uberRoot, uberHome, uberTime, currentTime
    global uberFrameBox, cartsFrame, cartsCanvas
    global showReceipt, showBrowse, showFoodify, showHome, showCuisine, showFood
    global showEmptyCarts, emptyCartImage, homeB, browseB, foodifyB, cartsB, homeImage, browseImage, foodifyImage, cartsImage
    global selectedHomeImage, selectedBrowseImage, selectedFoodifyImage, selectedCartsImage
    global cartsFrameBox, receiptScroll, orderCode, optionsScroll, showMeal, showRegion, groceriesImages
    
    global vietnameseBImages
    global vietnameseLImages
    global vietnameseDImages
    global vietnameseSImages

    global japaneseBImages
    global japaneseLImages
    global japaneseDImages
    global japaneseSImages

    global indianBImages
    global indianLImages
    global indianDImages
    global indianSImages

    global chineseBImages
    global chineseLImages
    global chineseDImages
    global chineseSImages

    global thaiBImages
    global thaiLImages
    global thaiDImages
    global thaiSImages

    global koreanBImages
    global koreanLImages
    global koreanDImages
    global koreanSImages

    global middleEasternBImages
    global middleEasternLImages
    global middleEasternDImages
    global middleEasternSImages

    global americanBImages
    global americanLImages
    global americanDImages
    global americanSImages

    global mexicanBImages
    global mexicanLImages
    global mexicanDImages
    global mexicanSImages

    global soulFoodBImages
    global soulFoodLImages
    global soulFoodDImages
    global soulFoodSImages

    global italianBImages
    global italianLImages
    global italianDImages
    global italianSImages

    global germanBImages
    global germanLImages
    global germanDImages
    global germanSImages

    global frenchBImages
    global frenchLImages
    global frenchDImages
    global frenchSImages

    global egyptianBImages
    global egyptianLImages
    global egyptianDImages
    global egyptianSImages
    
    global moroccanBImages
    global moroccanLImages
    global moroccanDImages
    global moroccanSImages

    global southAfricanBImages
    global southAfricanLImages
    global southAfricanDImages
    global southAfricanSImages

    #create a pop-up box, canvas, and title 
    uberRoot = Toplevel()  
    uberRoot.title ("Uber Feasts")
    
    uberHome = Canvas(uberRoot, width = 360, height = 710)
    uberHome.pack()
    
    #background image
    uberPhone = uberHome.create_image (180, 360, image = aPhoneImage)
    
    #display the time 
    currentTime = time.ctime (time.time())
    uberTime = uberHome.create_text (120, 70, text = currentTime, font = ("Helvetica", 10))
    
    #importing images for icons and buttons
    homeImage = PhotoImage (file = "Home.png")
    browseImage = PhotoImage (file = "Browse.png")
    foodifyImage = PhotoImage (file = "Foodify.png")
    cartsImage = PhotoImage (file = "Carts.png")
    
    selectedHomeImage = PhotoImage (file = "Selected Home.png")
    selectedBrowseImage = PhotoImage (file = "Selected Browse.png")
    selectedFoodifyImage = PhotoImage (file = "Selected Foodify.png")
    selectedCartsImage = PhotoImage (file = "Selected Carts.png")
    
    #importing images for carts
    emptyCartImage = PhotoImage (file = "Empty Cart.png")
    receiptFormatImage = PhotoImage (file = "Receipt Format.png")
    receiptCostImage = PhotoImage (file = "Receipt Cost.png")
    
    #importing groceries food images
    milkImage = PhotoImage(file = "Milk.png")
    eggsImage = PhotoImage(file = "Eggs.png")
    cheeseImage = PhotoImage(file = "Cheese.png")
    breadImage = PhotoImage(file = "Bread.png")
    bagelImage = PhotoImage(file = "Bagel.png")
    bunImage = PhotoImage(file = "Bun.png")
    pastaImage = PhotoImage(file = "Pasta.png")
    riceImage = PhotoImage(file = "Rice.png")
    beansImage = PhotoImage(file = "Beans.png")
    chickenImage = PhotoImage(file = "Chicken.png")
    beefImage = PhotoImage(file = "Beef.png")
    porkImage = PhotoImage(file = "Pork.png")
    appleImage = PhotoImage(file = "Apple.png")
    bananaImage = PhotoImage(file = "Banana.png")
    spinachImage = PhotoImage(file = "Spinach.png")
    tissueImage = PhotoImage(file = "Tissue.png")
    toiletPaperImage = PhotoImage(file = "Toilet Paper.png")
    towelImage = PhotoImage(file = "Towel.png")
    soapImage = PhotoImage(file = "Soap.png")
    shampooImage = PhotoImage(file = "Shampoo.png")
    bodyWashImage = PhotoImage(file = "Body Wash.png")
    toothPasteImage = PhotoImage(file = "Tooth Paste.png")
    toothBrushImage = PhotoImage(file = "Tooth Brush.png")
    flourImage = PhotoImage(file = "Flour.png")
    sugarImage = PhotoImage(file = "Sugar.png")
    crispsImage = PhotoImage(file = "Crisps.png")
    cookingOilImage = PhotoImage(file = "Cooking Oil.png")
    saltImage = PhotoImage(file = "Salt.png")
    bbqSauceImage = PhotoImage(file = "BBQ Sauce.png")
    
    #create list of images for food 
    groceriesImages = [milkImage, eggsImage, cheeseImage, breadImage, bagelImage, bunImage, pastaImage, riceImage, beansImage, chickenImage, beefImage, porkImage, appleImage, bananaImage, spinachImage, tissueImage, toiletPaperImage, towelImage, soapImage, shampooImage, bodyWashImage, toothPasteImage, toothBrushImage, flourImage, sugarImage, crispsImage, cookingOilImage, saltImage, bbqSauceImage]

    #importing food cuisine images
    
    # Vietnamese cuisine food images
    phoImage = PhotoImage(file = "Pho.png")
    banhMiImage = PhotoImage(file = "Banh Mi.png")
    xoiImage = PhotoImage(file = "Xoi.png")
    caPheImage = PhotoImage(file = "Ca Phe.png")
    traDaImage = PhotoImage(file = "Tra Da.png")
    
    comTamImage = PhotoImage(file = "Com Tam.png")
    bunThitNuongImage = PhotoImage(file = "Bun Thit Nuong.png")
    huTieuImage = PhotoImage(file = "Hu Tieu.png")
    sinhToImage = PhotoImage(file = "Sinh To.png")
    nuocMiaImage = PhotoImage(file = "Nuoc Mia.png")
    
    banhXeoImage = PhotoImage(file = "Banh Xeo.png")
    boLucLacImage = PhotoImage(file = "Bo Luc Lac.png")
    bunBoHueImage = PhotoImage(file = "Bun Bo Hue.png")
    nuocDuaImage = PhotoImage (file = "Nuoc Dua.png")
    biaImage = PhotoImage(file = "Bia.png")
    
    banhTrangTronImage = PhotoImage(file = "Banh Trang Tron.png")
    goiCuonImage = PhotoImage(file = "Goi Cuon.png")
    chaGioImage = PhotoImage(file = "Cha Gio.png")
    cheImage = PhotoImage(file = "Che.png")
    traSuaImage = PhotoImage(file = "Tra Sua.png")
    
    # Japanese cuisine food images
    tamagoyakiImage = PhotoImage(file = "Tamagoyaki.png")
    nattoImage = PhotoImage(file = "Natto.png")
    gohanImage = PhotoImage(file = "Gohan.png")
    greenTeaImage = PhotoImage(file = "Green Tea.png")
    misoSoupImage = PhotoImage(file = "Miso Soup.png")

    sushiImage = PhotoImage(file = "Sushi.png")
    ramenImage = PhotoImage(file = "Ramen.png")
    tempuraImage = PhotoImage(file = "Tempura.png")
    matchaLatteImage = PhotoImage(file = "Matcha Latte.png")

    okonomiyakiImage = PhotoImage(file = "Okonomiyaki.png")
    yakitoriImage = PhotoImage(file = "Yakitori.png")
    shabuShabuImage = PhotoImage(file = "Shabu Shabu.png")
    sakeImage = PhotoImage(file = "Sake.png")
    umeshuImage = PhotoImage(file = "Umeshu.png")

    onigiriImage = PhotoImage(file = "Onigiri.png")
    edamameImage = PhotoImage(file = "Edamame.png")
    taiyakiImage = PhotoImage(file = "Taiyaki.png")
    milkTeaImage = PhotoImage(file = "Milk Tea.png")
    calpicoImage = PhotoImage(file = "Calpico.png")

    # Indian cuisine food images
    masalaChaiImage = PhotoImage(file = "Masala Chai.png")
    pohaImage = PhotoImage(file = "Poha.png")
    idliImage = PhotoImage(file = "Idli.png")
    mangoLassiImage = PhotoImage(file = "Mango Lassi.png")
    chaasImage = PhotoImage(file = "Chaas.png")

    biryaniImage = PhotoImage(file = "Biryani.png")
    choleBhatureImage = PhotoImage(file = "Chole Bhature.png")
    rasamImage = PhotoImage(file = "Rasam.png")
    nimbuPaniImage = PhotoImage(file = "Nimbu Pani.png")
    thandaiImage = PhotoImage(file = "Thandai.png")

    rajmaMasalaImage = PhotoImage(file = "Rajma Masala.png")
    palakSoupImage = PhotoImage(file = "Palak Soup.png")
    dalFryImage = PhotoImage(file = "Dal Fry.png")
    aamPannaImage = PhotoImage(file = "Aam Panna.png")
    roseMilkImage = PhotoImage(file = "Rose Milk.png")

    samosaImage = PhotoImage(file = "Samosa.png")
    bhelPuriImage = PhotoImage(file = "Bhel Puri.png")
    paneerTikkaImage = PhotoImage(file = "Paneer Tikka.png")
    kokumSherbetImage = PhotoImage(file = "Kokum Sherbet.png")
    badamMilkImage = PhotoImage(file = "Badam Milk.png")

    # Chinese cuisine food images
    congeeImage = PhotoImage(file = "Congee.png")
    youtiaoImage = PhotoImage(file = "Youtiao.png")
    centuryEggCongeeImage = PhotoImage(file = "Century Egg Congee.png")
    soyMilkImage = PhotoImage(file = "Soy Milk.png")
    chineseTeaImage = PhotoImage(file = "Chinese Tea.png")

    dimSumImage = PhotoImage(file = "Dim Sum.png")
    hotAndSourSoupImage = PhotoImage(file = "Hot and Sour Soup.png")
    stirFriedNoodlesImage = PhotoImage(file = "Stir Fried Noodles.png")
    chrysanthemumTeaImage = PhotoImage(file = "Chrysanthemum Tea.png")
    winterMelonTeaImage = PhotoImage(file = "Winter Melon Tea.png")

    kungPaoChickenImage = PhotoImage(file = "Kung Pao Chicken.png")
    pekingDuckImage = PhotoImage(file = "Peking Duck.png")
    eggDropSoupImage = PhotoImage(file = "Egg Drop Soup.png")
    riceWineImage = PhotoImage(file = "Rice Wine.png")
    bobaImage = PhotoImage(file = "Boba.png")

    charSiuBaoImage = PhotoImage(file = "Char Siu Bao.png")
    congYouBingImage = PhotoImage(file = "Cong You Bing.png")
    chaYeDanImage = PhotoImage(file = "Cha Ye Dan.png")

    # Thai cuisine food images
    khaoTomImage = PhotoImage(file = "Khao Tom.png")
    kaiJeowImage = PhotoImage(file = "Kai Jeow.png")
    namPrikOngImage = PhotoImage(file = "Nam Prik Ong.png")
    thaiIcedTeaImage = PhotoImage(file = "Thai Iced Tea.png")
    freshCoconutWaterImage = PhotoImage(file = "Fresh Coconut Water.png")

    padThaiImage = PhotoImage(file = "Pad Thai.png")
    gaengKeowWanImage = PhotoImage(file = "Gaeng Keow Wan.png")
    somTumImage = PhotoImage(file = "Som Tum.png")
    oliangImage = PhotoImage(file = "Oliang.png")
    chaKhiaoYenImage = PhotoImage(file = "Cha Khiao Yen.png")

    tomYumGoongImage = PhotoImage(file = "Tom Yum Goong.png")
    padKraPaoImage = PhotoImage(file = "Pad Kra Pao.png")
    massamanCurryImage = PhotoImage(file = "Massaman Curry.png")
    namDokAnchanImage = PhotoImage(file = "Nam Dok Anchan.png")
    namManaoImage = PhotoImage(file = "Nam Manao.png")

    miangKhamImage = PhotoImage(file = "Miang Kham.png")
    todMunPlaImage = PhotoImage(file = "Tod Mun Pla.png")
    khanomKrokImage = PhotoImage(file = "Khanom Krok.png")
    chaYenImage = PhotoImage(file = "Cha Yen.png")
    oliangImage = PhotoImage(file = "Oliang.png")

    # Korean cuisine food images
    kimchiBokkeumbapImage = PhotoImage(file = "Kimchi Bokkeumbap.png")
    gyeranMariImage = PhotoImage(file = "Gyeran Mari.png")
    kongnamulGukImage = PhotoImage(file = "Kongnamul Guk.png")
    sujeonggwaImage = PhotoImage(file = "Sujeonggwa.png")
    yujaChaImage = PhotoImage(file = "Yuja Cha.png")
    
    bibimbapImage = PhotoImage(file = "Bibimbap.png")
    japchaeImage = PhotoImage(file = "Japchae.png")
    samgyeopsalImage = PhotoImage(file = "Samgyeopsal.png")
    sikhyeImage = PhotoImage(file = "Sikhye.png")
    borichaImage = PhotoImage(file = "Boricha.png")

    kimchiJjigaeImage = PhotoImage(file = "Kimchi Jjigae.png")
    dakGalbiImage = PhotoImage(file = "Dak Galbi.png")
    bulgogiImage = PhotoImage(file = "Bulgogi.png")
    makgeolliImage = PhotoImage(file = "Makgeolli.png")
    sojuImage = PhotoImage(file = "Soju.png")

    twigimImage = PhotoImage(file = "Twigim.png")
    gimbapImage = PhotoImage(file = "Gimbap.png")
    tteokbokkiImage = PhotoImage(file = "Tteokbokki.png")
    yujaAdeImage = PhotoImage(file = "Yuja Ade.png")
    sikhyeImage = PhotoImage(file = "Sikhye.png")

    # Middle Eastern cuisine food images
    shakshukaImage = PhotoImage(file = "Shakshuka.png")
    fulMedamesImage = PhotoImage(file = "Ful Medames.png")
    labnehImage = PhotoImage(file = "Labneh.png")
    qahwaImage = PhotoImage(file = "Qahwa.png")
    shaiBiNanaImage = PhotoImage(file = "Shai Bi Nana.png")

    falafelWrapImage = PhotoImage(file = "Falafel Wrap.png")
    mujadaraImage = PhotoImage(file = "Mujadara.png")
    shawarmaImage = PhotoImage(file = "Shawarma.png")
    ayranImage = PhotoImage(file = "Ayran.png")
    tamrHindiImage = PhotoImage(file = "Tamr Hindi.png")

    kebabsImage = PhotoImage(file = "Kebabs.png")
    mansafImage = PhotoImage(file = "Mansaf.png")
    mezzePlatterImage = PhotoImage(file = "Mezze Platter.png")
    pomegranateJuiceImage = PhotoImage(file = "Pomegranate Juice.png")
    roseLemonadeImage = PhotoImage(file = "Rose Lemonade.png")

    pitaChipsHummusImage = PhotoImage(file = "Pita Chips Hummus.png")
    falafelImage = PhotoImage(file = "Falafel.png")
    babaGanoushImage = PhotoImage(file = "Baba Ganoush.png")
    cayImage = PhotoImage(file = "Cay.png")
    labanAyranImage = PhotoImage(file = "Laban Ayran.png")

    # American cuisine food images
    pancakesSyrupImage = PhotoImage(file = "Pancakes Syrup.png")
    eggBaconSandwichImage = PhotoImage(file = "Egg Bacon Sandwich.png")
    oatmealFruitImage = PhotoImage(file = "Oatmeal Fruit.png")
    coffeeImage = PhotoImage(file = "Coffee.png")
    orangeJuiceImage = PhotoImage(file = "Orange Juice.png")

    premiumCheeseburgerImage = PhotoImage(file = "Premium Cheeseburger.png")
    chickenCaesarSaladImage = PhotoImage(file = "Chicken Caesar Salad.png")
    grilledCheeseTomatoSoupImage = PhotoImage(file = "Grilled Cheese Tomato Soup.png")
    icedTeaImage = PhotoImage(file = "Iced Tea.png")
    lemonadeImage = PhotoImage(file = "Lemonade.png")

    barbecueRibsImage = PhotoImage(file = "Barbecue Ribs.png")
    macaroniCheeseImage = PhotoImage(file = "Macaroni Cheese.png")
    grilledSalmonVegetablesImage = PhotoImage(file = "Grilled Salmon Vegetables.png")
    redWineImage = PhotoImage(file = "Red Wine.png")
    craftBeerImage = PhotoImage(file = "Craft Beer.png")

    popcornImage = PhotoImage(file = "Popcorn.png")
    applePeanutButterImage = PhotoImage(file = "Apple Peanut Butter.png")
    trailMixImage = PhotoImage(file = "Trail Mix.png")
    smoothieImage = PhotoImage(file = "Smoothie.png")
    icedCoffeeImage = PhotoImage(file = "Iced Coffee.png")

    # Mexican cuisine food images
    huevosRancherosImage = PhotoImage(file = "Huevos Rancheros.png")
    chilaquilesImage = PhotoImage(file = "Chilaquiles.png")
    breakfastBurritoImage = PhotoImage(file = "Breakfast Burrito.png")
    horchataImage = PhotoImage(file = "Horchata.png")
    cafeDeOllaImage = PhotoImage(file = "Cafe de Olla.png")

    tacosAlPastorImage = PhotoImage(file = "Tacos Al Pastor.png")
    chickenQuesadillasImage = PhotoImage(file = "Chicken Quesadillas.png")
    enchiladasVerdesImage = PhotoImage(file = "Enchiladas Verdes.png")
    aguaFrescaImage = PhotoImage(file = "Agua Fresca.png")
    micheladaImage = PhotoImage(file = "Michelada.png")

    carneAsadaTacosImage = PhotoImage(file = "Carne Asada Tacos.png")
    chilesRellenosImage = PhotoImage(file = "Chiles Rellenos.png")
    molePoblanoImage = PhotoImage(file = "Mole Poblano.png")
    margaritaImage = PhotoImage(file = "Margarita.png")
    cervezaImage = PhotoImage(file = "Cerveza.png")

    guacamoleChipsImage = PhotoImage(file = "Guacamole Chips.png")
    eloteImage = PhotoImage(file = "Elote.png")
    tostadasImage = PhotoImage(file = "Tostadas.png")
    aguaDeJamaicaImage = PhotoImage(file = "Agua de Jamaica.png")
    pinaColadaImage = PhotoImage(file = "Piña Colada.png")

    # Soul food cuisine food images
    shrimpGritsImage = PhotoImage(file = "Shrimp Grits.png")
    chickenWafflesImage = PhotoImage(file = "Chicken Waffles.png")
    biscuitsGravyImage = PhotoImage(file = "Biscuits Gravy.png")
    sweetTeaImage = PhotoImage(file = "Sweet Tea.png")
    coffeeCreamImage = PhotoImage(file = "Coffee Cream.png")

    friedCatfishSandwichImage = PhotoImage(file = "Fried Catfish Sandwich.png")
    collardGreensSmokedTurkeyImage = PhotoImage(file = "Collard Greens Smoked Turkey.png")
    jambalayaImage = PhotoImage(file = "Jambalaya.png")
    lemonadeImage = PhotoImage(file = "Lemonade.png")
    fruitPunchImage = PhotoImage(file = "Fruit Punch.png")

    friedChickenImage = PhotoImage(file = "Fried Chicken.png")
    shrimpEtouffeeImage = PhotoImage(file = "Shrimp Étouffée.png")
    barbecueRibsImage = PhotoImage(file = "Barbecue Ribs.png")
    icedTeaLemonImage = PhotoImage(file = "Iced Tea Lemon.png")
    mintJulepImage = PhotoImage(file = "Mint Julep.png")

    deviledEggsImage = PhotoImage(file = "Deviled Eggs.png")
    pimentoCheeseDipCrackersImage = PhotoImage(file = "Pimento Cheese Dip Crackers.png")
    friedGreenTomatoesImage = PhotoImage(file = "Fried Green Tomatoes.png")
    buttermilkImage = PhotoImage(file = "Buttermilk.png")
    southernSweetTeaImage = PhotoImage(file = "Southern Sweet Tea.png")

    # Italian cuisine food images
    cornettiImage = PhotoImage(file = "Cornetti.png")
    frittataImage = PhotoImage(file = "Frittata.png")
    paneNutellaImage = PhotoImage(file = "Pane Nutella.png")
    caffeLatteImage = PhotoImage(file = "Caffe Latte.png")
    espressoImage = PhotoImage(file = "Espresso.png")

    capreseSaladImage = PhotoImage(file = "Caprese Salad.png")
    paniniImage = PhotoImage(file = "Panini.png")
    pastaPrimaveraImage = PhotoImage(file = "Pasta Primavera.png")
    aperolSpritzImage = PhotoImage(file = "Aperol Spritz.png")
    limoncelloImage = PhotoImage(file = "Limoncello.png")

    margheritaPizzaImage = PhotoImage(file = "Margherita Pizza.png")
    risottoFunghiImage = PhotoImage(file = "Risotto Funghi.png")
    chickenParmesanImage = PhotoImage(file = "Chicken Parmesan.png")
    chiantiImage = PhotoImage(file = "Chianti.png")
    proseccoImage = PhotoImage(file = "Prosecco.png")

    bruschettaImage = PhotoImage(file = "Bruschetta.png")
    aranciniImage = PhotoImage(file = "Arancini.png")
    crostiniImage = PhotoImage(file = "Crostini.png")
    limonataImage = PhotoImage(file = "Limonata.png")
    gelatoImage = PhotoImage(file = "Gelato.png")
    
    # German cuisine food images
    brotchenImage = PhotoImage(file = "Brotchen.png")
    bircherMuesliImage = PhotoImage(file = "Bircher Müsli.png")
    eierkuchenImage = PhotoImage(file = "Eierkuchen.png")
    kaffeeImage = PhotoImage(file = "Kaffee.png")
    teeImage = PhotoImage(file = "Tee.png")

    schnitzelImage = PhotoImage(file = "Schnitzel.png")
    wurstsalatImage = PhotoImage(file = "Wurstsalat.png")
    kartoffelsuppeImage = PhotoImage(file = "Kartoffelsuppe.png")
    bierImage = PhotoImage(file = "Bier.png")
    mineralwasserImage = PhotoImage(file = "Mineralwasser.png")

    bratwurstSauerkrautImage = PhotoImage(file = "Bratwurst Sauerkraut.png")
    rouladenKartoffelnImage = PhotoImage(file = "Rouladen Kartoffeln.png")
    kaesespaetzleImage = PhotoImage(file = "Kasespatzle.png")
    rotweinImage = PhotoImage(file = "Rotwein.png")
    apfelschorleImage = PhotoImage(file = "Apfelschorle.png")

    currywurstImage = PhotoImage(file = "Currywurst.png")
    leberkaeseSemmelImage = PhotoImage(file = "Leberkase Semmel.png")
    bienenstichImage = PhotoImage(file = "Bienenstich.png")
    eiskaffeeImage = PhotoImage(file = "Eiskaffee.png")

    # French cuisine food images
    croissantImage = PhotoImage(file = "Croissant.png")
    painAuChocolatImage = PhotoImage(file = "Pain au Chocolat.png")
    painPerduImage = PhotoImage(file = "Pain Perdu.png")
    cafeAuLaitImage = PhotoImage(file = "Cafe au Lait.png")
    chocolatChaudImage = PhotoImage(file = "Chocolat Chaud.png")

    saladeNicoiseImage = PhotoImage(file = "Salade Niçoise.png")
    croqueMonsieurImage = PhotoImage(file = "Croque Monsieur.png")
    quicheLorraineImage = PhotoImage(file = "Quiche Lorraine.png")
    vinRoseImage = PhotoImage(file = "Vin Rose.png")
    citronPresseImage = PhotoImage(file = "Citron Presse.png")

    coqAuVinImage = PhotoImage(file = "Coq au Vin.png")
    boeufBourguignonImage = PhotoImage(file = "Boeuf Bourguignon.png")
    ratatouilleImage = PhotoImage(file = "Ratatouille.png")
    vinRougeImage = PhotoImage(file = "Vin Rouge.png")
    kirImage = PhotoImage(file = "Kir.png")

    tarteletteAuxFruitsImage = PhotoImage(file = "Tartelette aux Fruits.png")
    gougeresImage = PhotoImage(file = "Gougeres.png")
    cafeImage = PhotoImage(file = "Cafe.png")
    theImage = PhotoImage(file = "The.png")

    # Egyptian cuisine food images
    fulMedamesImage = PhotoImage(file = "Ful Medames.png")
    taAmeyaImage = PhotoImage(file = "Ta'ameya.png")
    fiteerBaladiImage = PhotoImage(file = "Fiteer Baladi.png")
    karakadeImage = PhotoImage(file = "Karakade.png")
    sahlabImage = PhotoImage(file = "Sahlab.png")

    koshariImage = PhotoImage(file = "Koshari.png")
    mahshiImage = PhotoImage(file = "Mahshi.png")
    mulukhiyahSoupImage = PhotoImage(file = "Mulukhiyah Soup.png")
    sobiaImage = PhotoImage(file = "Sobia.png")
    sekanjabinImage = PhotoImage(file = "Sekanjabin.png")

    molokhiaImage = PhotoImage(file = "Molokhia.png")
    fattahImage = PhotoImage(file = "Fattah.png")
    koftaTagineImage = PhotoImage(file = "Kofta Tagine.png")
    qamarAlDinImage = PhotoImage(file = "Qamar Al Din.png")
    erkSousImage = PhotoImage(file = "Erk Sous.png")

    kunafaImage = PhotoImage(file = "Kunafa.png")
    basbousaImage = PhotoImage(file = "Basbousa.png")
    feteerMeshaltetImage = PhotoImage(file = "Feteer Meshaltet.png")

    # Moroccan cuisine food images
    baghrirImage = PhotoImage(file = "Baghrir.png")
    msemenImage = PhotoImage(file = "Msemen.png")
    hariraImage = PhotoImage(file = "Harira.png")
    atayefImage = PhotoImage(file = "Atayef.png")
    amlouSmoothieImage = PhotoImage(file = "Amlou Smoothie.png")
    
    tagineImage = PhotoImage(file = "Tagine.png")
    briouatImage = PhotoImage(file = "Briouat.png")
    zaaloukImage = PhotoImage(file = "Zaalouk.png")
    limonadeImage = PhotoImage(file = "Limonade.png")
    jusDAvocatImage = PhotoImage(file = "Jus D'Avocat.png")

    couscousImage = PhotoImage(file = "Couscous.png")
    pastillaImage = PhotoImage(file = "Pastilla.png")
    mechouiImage = PhotoImage(file = "Mechoui.png")
    jusDeFruitsImage = PhotoImage(file = "Jus De Fruits.png")
    lbenImage = PhotoImage(file = "Lben.png")

    chebakiaImage = PhotoImage(file = "Chebakia.png")
    sellouImage = PhotoImage(file = "Sellou.png")
    atayImage = PhotoImage(file = "Atay.png")

    # South African cuisine food images 
    boereworsRollImage = PhotoImage(file = "Boerewors Roll.png")
    milkTartImage = PhotoImage(file = "Milk Tart.png")
    vetkoekImage = PhotoImage(file = "Vetkoek.png")
    rooibosTeaImage = PhotoImage(file = "Rooibos Tea.png")
    amarulaImage = PhotoImage(file = "Amarula.png")

    bunnyChowImage = PhotoImage(file = "Bunny Chow.png")
    bobotieImage = PhotoImage(file = "Bobotie.png")
    potjiekosImage = PhotoImage(file = "Potjiekos.png")
    rooibosIcedTeaImage = PhotoImage(file = "Rooibos Iced Tea.png")
    sowetoGoldLagerImage = PhotoImage(file = "Soweto Gold Lager.png")

    braaiImage = PhotoImage(file = "Braai.png")
    papWorsImage = PhotoImage(file = "Pap Wors.png")
    chakalakaImage = PhotoImage(file = "Chakalaka.png")
    pinotageImage = PhotoImage(file = "Pinotage.png")

    biltongImage = PhotoImage(file = "Biltong.png")
    droeworsImage = PhotoImage(file = "Droewors.png")
    koeksistersImage = PhotoImage(file = "Koeksisters.png")
    umqombothiImage = PhotoImage(file = "Umqombothi.png")
    capeMalayCurryImage = PhotoImage(file = "Cape Malay Curry.png")
    
    #create list of images for food 
    vietnameseBImages = [phoImage, banhMiImage, xoiImage, caPheImage, traDaImage]
    vietnameseLImages = [comTamImage, bunThitNuongImage, huTieuImage, sinhToImage, nuocMiaImage]
    vietnameseDImages = [banhXeoImage, boLucLacImage, bunBoHueImage, nuocDuaImage, biaImage]
    vietnameseSImages = [banhTrangTronImage, goiCuonImage, chaGioImage, cheImage, traSuaImage]

    japaneseBImages = [tamagoyakiImage, nattoImage, gohanImage, greenTeaImage, misoSoupImage]
    japaneseLImages = [sushiImage, ramenImage, tempuraImage, matchaLatteImage, misoSoupImage]
    japaneseDImages = [okonomiyakiImage, yakitoriImage, shabuShabuImage, sakeImage, umeshuImage]
    japaneseSImages = [onigiriImage, edamameImage, taiyakiImage, milkTeaImage, calpicoImage]

    indianBImages = [masalaChaiImage, pohaImage, idliImage, mangoLassiImage, chaasImage]
    indianLImages = [biryaniImage, choleBhatureImage, rasamImage, nimbuPaniImage, thandaiImage]
    indianDImages = [rajmaMasalaImage, palakSoupImage, dalFryImage, aamPannaImage, roseMilkImage]
    indianSImages = [samosaImage, bhelPuriImage, paneerTikkaImage, kokumSherbetImage, badamMilkImage]

    chineseBImages = [congeeImage, youtiaoImage, centuryEggCongeeImage, soyMilkImage, chineseTeaImage]
    chineseLImages = [dimSumImage, hotAndSourSoupImage, stirFriedNoodlesImage, chrysanthemumTeaImage, winterMelonTeaImage]
    chineseDImages = [kungPaoChickenImage, pekingDuckImage, eggDropSoupImage, riceWineImage, bobaImage]
    chineseSImages = [charSiuBaoImage, congYouBingImage, chaYeDanImage, bobaImage, soyMilkImage]

    thaiBImages = [khaoTomImage, kaiJeowImage, namPrikOngImage, thaiIcedTeaImage, freshCoconutWaterImage]
    thaiLImages = [padThaiImage, gaengKeowWanImage, somTumImage, oliangImage, chaKhiaoYenImage]
    thaiDImages = [tomYumGoongImage, padKraPaoImage, massamanCurryImage, namDokAnchanImage, namManaoImage]
    thaiSImages = [miangKhamImage, todMunPlaImage, khanomKrokImage, chaYenImage, oliangImage]

    koreanBImages = [kimchiBokkeumbapImage, gyeranMariImage, kongnamulGukImage, sujeonggwaImage, yujaChaImage]
    koreanLImages = [bibimbapImage, japchaeImage, samgyeopsalImage, sikhyeImage, borichaImage]
    koreanDImages = [kimchiJjigaeImage, dakGalbiImage, bulgogiImage, makgeolliImage, sojuImage]
    koreanSImages = [twigimImage, gimbapImage, tteokbokkiImage, yujaAdeImage, sikhyeImage]

    middleEasternBImages = [shakshukaImage, fulMedamesImage, labnehImage, qahwaImage, shaiBiNanaImage]
    middleEasternLImages = [falafelWrapImage, mujadaraImage, shawarmaImage, ayranImage, tamrHindiImage]
    middleEasternDImages = [kebabsImage, mansafImage, mezzePlatterImage, pomegranateJuiceImage, roseLemonadeImage]
    middleEasternSImages = [pitaChipsHummusImage, falafelImage, babaGanoushImage, cayImage, labanAyranImage]

    americanBImages = [pancakesSyrupImage, eggBaconSandwichImage, oatmealFruitImage, coffeeImage, orangeJuiceImage]
    americanLImages = [premiumCheeseburgerImage, chickenCaesarSaladImage, grilledCheeseTomatoSoupImage, icedTeaImage, lemonadeImage]
    americanDImages = [barbecueRibsImage, macaroniCheeseImage, grilledSalmonVegetablesImage, redWineImage, craftBeerImage]
    americanSImages = [popcornImage, applePeanutButterImage, trailMixImage, smoothieImage, icedCoffeeImage]

    mexicanBImages = [huevosRancherosImage, chilaquilesImage, breakfastBurritoImage, horchataImage, cafeDeOllaImage]
    mexicanLImages = [tacosAlPastorImage, chickenQuesadillasImage, enchiladasVerdesImage, aguaFrescaImage, micheladaImage]
    mexicanDImages = [carneAsadaTacosImage, chilesRellenosImage, molePoblanoImage, margaritaImage, cervezaImage]
    mexicanSImages = [guacamoleChipsImage, eloteImage, tostadasImage, aguaDeJamaicaImage, pinaColadaImage]

    soulFoodBImages = [shrimpGritsImage, chickenWafflesImage, biscuitsGravyImage, sweetTeaImage, coffeeCreamImage]
    soulFoodLImages = [friedCatfishSandwichImage, collardGreensSmokedTurkeyImage, jambalayaImage, lemonadeImage, fruitPunchImage]
    soulFoodDImages = [friedChickenImage, shrimpEtouffeeImage, barbecueRibsImage, icedTeaLemonImage, mintJulepImage]
    soulFoodSImages = [deviledEggsImage, pimentoCheeseDipCrackersImage, friedGreenTomatoesImage, buttermilkImage, southernSweetTeaImage]

    italianBImages = [cornettiImage, frittataImage, paneNutellaImage, caffeLatteImage, espressoImage]
    italianLImages = [capreseSaladImage, paniniImage, pastaPrimaveraImage, aperolSpritzImage, limoncelloImage]
    italianDImages = [margheritaPizzaImage, risottoFunghiImage, chickenParmesanImage, chiantiImage, proseccoImage]
    italianSImages = [bruschettaImage, aranciniImage, crostiniImage, limonataImage, gelatoImage]

    germanBImages = [brotchenImage, bircherMuesliImage, eierkuchenImage, kaffeeImage, teeImage]
    germanLImages = [schnitzelImage, wurstsalatImage, kartoffelsuppeImage, bierImage, mineralwasserImage]
    germanDImages = [bratwurstSauerkrautImage, rouladenKartoffelnImage, kaesespaetzleImage, rotweinImage, apfelschorleImage]
    germanSImages = [currywurstImage, leberkaeseSemmelImage, bienenstichImage, mineralwasserImage, eiskaffeeImage]

    frenchBImages = [croissantImage, painAuChocolatImage, painPerduImage, cafeAuLaitImage, chocolatChaudImage]
    frenchLImages = [saladeNicoiseImage, croqueMonsieurImage, quicheLorraineImage, vinRoseImage, citronPresseImage]
    frenchDImages = [coqAuVinImage, boeufBourguignonImage, ratatouilleImage, vinRougeImage, kirImage]
    frenchSImages = [quicheLorraineImage, tarteletteAuxFruitsImage, gougeresImage, cafeImage, theImage]

    egyptianBImages = [fulMedamesImage, taAmeyaImage, fiteerBaladiImage, karakadeImage, sahlabImage]
    egyptianLImages = [koshariImage, mahshiImage, mulukhiyahSoupImage, sobiaImage, sekanjabinImage]
    egyptianDImages = [molokhiaImage, fattahImage, koftaTagineImage, qamarAlDinImage, erkSousImage]
    egyptianSImages = [kunafaImage, basbousaImage, feteerMeshaltetImage, sahlabImage, sobiaImage]

    moroccanBImages = [baghrirImage, msemenImage, hariraImage, atayefImage, amlouSmoothieImage]
    moroccanLImages = [tagineImage, briouatImage, zaaloukImage, limonadeImage, jusDAvocatImage]
    moroccanDImages = [couscousImage, pastillaImage, mechouiImage, jusDeFruitsImage, lbenImage]
    moroccanSImages = [briouatImage, chebakiaImage, sellouImage, atayImage, amlouSmoothieImage]

    southAfricanBImages = [boereworsRollImage, milkTartImage, vetkoekImage, rooibosTeaImage, amarulaImage]
    southAfricanLImages = [bunnyChowImage, bobotieImage, potjiekosImage, rooibosIcedTeaImage, sowetoGoldLagerImage]
    southAfricanDImages = [braaiImage, papWorsImage, chakalakaImage, pinotageImage, rooibosTeaImage]
    southAfricanSImages = [biltongImage, droeworsImage, koeksistersImage, umqombothiImage, capeMalayCurryImage]
    
    internationalCuisineImage = PhotoImage (file = "International Cuisine.png")
    generalGroceriesImage = PhotoImage (file = "General Groceries.png")
    browseGroceriesImage = PhotoImage (file = "Browse Groceries.png")

    #create app functions option buttons
    uberReturnB = Button (uberRoot, image = returnImage, borderwidth = 0, highlightthickness = 0, command = closeUberFeasts)
    uberReturnButton = uberHome.create_window (75, 660, window = uberReturnB)
    uberReturnButton = uberHome.create_window (75, 660, window = uberReturnB)
    
    
    def showHome (): #display content home page

        global menuScroll, uberFrameBox, groceriesText, storeGroceries, page, groceriesImage
        global groceriesFrame, groceriesFrameBox, groceriesCanvas, groceriesScroll, viewScroll, itemsFrame, orderButton

        page = 1 #set the page number 
        
        #create title for page
        groceriesText = uberHome.create_text (180, 100, text = "\tGeneral Store\n   Start buying your Groceries!", font = ("Helvetica", 13), fill = "#06c168")
        
        #add image
        groceriesImage = uberHome.create_image (180, 225, image = generalGroceriesImage)
        
        #create a main frame for the canvas 
        uberFrame = Frame (uberRoot, width = 275, height = 100)
        uberFrameBox = uberHome.create_window (180, 400, window = uberFrame)
    
        #create another canvas for the application area 
        uberCanvas = Canvas(uberFrame, width = 275, height = 100)
        uberCanvas.pack (side = LEFT, fill = BOTH, expand = True)
            
        #add scrollbars to the new canvas frame
        menuScroll = Scrollbar (uberFrame, orient = HORIZONTAL, command = uberCanvas.xview)
        menuScroll.place (relx = 0, rely = 1, relwidth = 1, anchor = SW)
    
        #configure the scrollbar 
        uberCanvas.configure (xscrollcommand = menuScroll.set)
        uberCanvas.bind ("<Configure>", lambda e: uberCanvas.configure (scrollregion = uberCanvas.bbox ("all")))
    
        # bind mousewheel scrolling to the scrollbar 
        uberCanvas.bind_all("<MouseWheel>", lambda event: uberCanvas.xview_scroll(-int(event.delta / 120), "units"))
    
        #create another frame inside the canvas and add to canvas 
        groceriesOptionsFrame = Frame (uberCanvas)
        groceriesOptionsFrameBox = uberCanvas.create_window (0, 0, window = groceriesOptionsFrame, anchor = NW)
        
        storeGroceries = [] #store groceries buttons
        
        for i in range (0, len(groceries)):
            
            # store the text of the food choice for each button
            groceriesOrder = StringVar()
            groceriesOrder.set (groceries)# set the initial value
            
            groceriesOptions = Button (groceriesOptionsFrame, text = groceries[i][0] + " $" + format(groceries[i][1], ".2f"),image = groceriesImages [i], compound = TOP, command = lambda foodItem = groceries[i][0], price = groceries[i][1], timeCost = groceries[i][2]: addCart(foodItem, price, timeCost))
            groceriesOptions.pack (side = LEFT, padx = 10)
            storeGroceries.append (groceriesOptions)
            
        #create a main frame for the cart canvas 
        groceriesFrame = Frame (uberRoot, width = 275, height = 100)
        groceriesFrameBox = uberHome.create_window (180, 515, window = groceriesFrame)
    
        #create another canvas for the application area 
        groceriesCanvas = Canvas (groceriesFrame, width = 275, height = 115, bg = "#06c168")
        groceriesCanvas.pack (side = LEFT, fill = BOTH, expand = True)
        
        #add scrollbars to the canvas frame
        groceriesScroll = Scrollbar (groceriesFrame, orient = VERTICAL, command = groceriesCanvas.yview)
        groceriesScroll.place (relx = 1, rely = 0, relheight = 1, anchor = NE)
        
        viewScroll = Scrollbar (groceriesFrame, orient = HORIZONTAL, command = groceriesCanvas.xview)
        viewScroll.place (relx = 1, rely = 0, relheight = 1, anchor = SW)
        
        #configure the scrollbar 
        groceriesCanvas.config (yscrollcommand = groceriesScroll.set, xscrollcommand = viewScroll.set)
        
        # bind mousewheel scrolling
        orderCanvas.bind_all("<MouseWheel>", lambda event: groceriesCanvas.yview_scroll(-int(event.delta / 120), "units"))
        orderCanvas.bind_all("<Shift-MouseWheel>", lambda event: groceriesCanvas.xview_scroll(-int(event.delta / 120), "units"))
       
        #create another frame inside the canvas to add the new canvas 
        itemsFrame = Frame (groceriesCanvas, width = 275, height = 100, bg = "#06c168")
        itemsFrameBox = groceriesCanvas.create_window (0, 0, window = itemsFrame, anchor = NW)
        
        #create confirm order button and go to checkout  
        orderB = Button (uberRoot, text = "Place Order", command = carts)
        orderButton = uberHome.create_window (180, 600, window = orderB)
        
    #buttons and text to guide user to home page
    homeB = Button (uberRoot, image = selectedHomeImage, borderwidth = 0, highlightthickness = 0, command = home)
    homeButton = uberHome.create_window (125, 654, window = homeB)
    homeText = uberHome.create_text (125, 680, text = "Home", font = ("Helvetica", 8), fill = "#605c5c")
    
    #buttons and text to guide user to foodify page
    foodifyB = Button (uberRoot, image = foodifyImage, borderwidth = 0, highlightthickness = 0, command = foodify)
    foodifyButton = uberHome.create_window (235, 654, window = foodifyB)
    foodifyText = uberHome.create_text (235, 680, text = "Foodify", font = ("Helvetica", 8), fill = "#605c5c")
    
    def showFoodify ():
        global foodifyIntroFrameBox, foodifyIntroButton, internationalImage, modifyText
        
        #introduction text
        modifyText = uberHome.create_text (180, 100, text = "Modify Your Food Today!", font = ("Helvetica", 15), fill = "#06c168")
        
        #add image
        internationalImage = uberHome.create_image (180, 220, image = internationalCuisineImage)
        
        #create a frame for the introduction text
        foodifyIntroFrame = Frame (uberRoot, width = 35, height = 50)
        foodifyIntroFrameBox = uberHome.create_window (180, 425, window = foodifyIntroFrame)
        
        #create a text box for the frame
        foodifyIntroBox = Text (foodifyIntroFrame, width = 45, height = 15, font = ("Helvetica", 8))
        foodifyIntroBox.pack ()
        
        #create introduction text and add to text box
        foodifyIntroText = "Welcome to our indecision-free zone! Tired of pondering what to eat? You're in luck! Say goodbye to indecision and hello to tasty! Welcome to Foodify, your ultimate destination for personalized dining experiences! At Foodify, we understand that everyone has their own unique preferences when it comes to food. That's why we've designed a platform where you can customize your meals based on your preferred region, cuisine, and meal type. Whether you're in the mood for a hearty Italian dinner, a spicy Mexican snack, or a light and refreshing Japanese lunch, Foodify has you covered. With just a few clicks, you can create the perfect meal tailored to your tastes and dietary needs. So why settle for ordinary when you can make every meal extraordinary with Foodify? Join us and start exploring a world of culinary possibilities today!"
        foodifyIntroBox.insert ("1.0", foodifyIntroText)
        
        #create get started button
        foodifyIntroB = Button (uberRoot, text = "Start Personalizing", font = ("Helvetica", 20), command = showRegion, fg = "#06c168")
        foodifyIntroButton = uberHome.create_window (180, 575, window = foodifyIntroB)
    
    def showRegion ():
        global regionOptionsBox, selectedRegion, regionOptions, regionPreferenceText, confirmRegionB, confirmRegionButton 
        
        #clear foodify intro screen
        uberHome.itemconfig (foodifyIntroFrameBox, state = HIDDEN)
        uberHome.itemconfig (foodifyIntroButton, state = HIDDEN)
        uberHome.itemconfig (internationalImage, state = HIDDEN)
        uberHome.itemconfig (modifyText, state = HIDDEN)
        
        #ask for region preference and a button to confirm cuisine and go next  
        regionPreferenceText = uberHome.create_text (180, 100, text = "Where's your belly's dream destination?", font = ("Helvetica", 10), fill = "#06c168")
        confirmRegionB = Button (uberRoot, text = "Confirm", command = validateRegion, fg = "#06c168")
        confirmRegionButton = uberHome.create_window (285, 135, window = confirmRegionB)
        
        #create drop down menu for region options
        selectedRegion = StringVar ()
        selectedRegion.set ("Region")
        regionOptions = OptionMenu (uberRoot, selectedRegion, *regions)
        regionOptionsBox = uberHome.create_window (180, 135, window = regionOptions)
    
    def showCuisine ():
        global cuisineOptionsBox, selectedCuisine, cuisineOptions, cuisinePreferenceText, confirmCuisineB, confirmCuisineButton
        
        #ask for cuisine preference and a button to confirm cuisine and go next 
        cuisinePreferenceText = uberHome.create_text (180, 165, text = "What cuisine has your taste-bud passport?", font = ("Helvetica", 10), fill = "#06c168")
        confirmCuisineB = Button (uberRoot, text = "Confirm", command = validateCuisine, fg = "#06c168")
        confirmCuisineButton = uberHome.create_window (285, 200, window = confirmCuisineB)
        
        #create drop down menu for cuisine options
        selectedCuisine = StringVar ()
        selectedCuisine.set ("Cuisine")
        cuisineOptions = OptionMenu (uberRoot, selectedCuisine, *cuisines)
        cuisineOptionsBox = uberHome.create_window (180, 200, window = cuisineOptions)
    
    def showMeal ():
        global mealText, confirmMealButton, mealFrameBox, mealOptions, storeMeals, selectedMeal, mealCanvas
        
        #ask for meal preference  
        mealText = uberHome.create_text (180, 235, text = "What's your hunger-time vibe today?", font = ("Helvetica", 10), fill = "#06c168")
        
        #create a main frame for the meal options 
        mealFrame = Frame (uberRoot, width = 250, height = 480)
        mealFrameBox = uberHome.create_window (180, 270, window = mealFrame)
    
        #create another canvas to place the buttons in 
        mealCanvas = Canvas (mealFrame, width = 250, height = 40)
        mealCanvas.pack (side = LEFT, fill = BOTH, expand = True)
        
        #create another frame inside the canvas and add to canvas 
        mealOptionsFrame = Frame (mealCanvas)
        mealOptionsFrameBox = mealCanvas.create_window (0, 0, window = mealOptionsFrame, anchor = NW)
        
        # store the selected food choice and their buttons
        selectedMeal = IntVar()
        storeMeals = []
        
        for i in range (len(meals)): #create the meal option buttons 
            
            mealOptions = Radiobutton (mealOptionsFrame, text = meals [i], variable = selectedMeal, value = i)
            mealOptions.pack(side = LEFT)
            storeMeals.append (mealOptions)
            
        #create confirm button to go next
        confirmMealB = Button (uberRoot, text = "Confirm", command = validateMeal, fg = "#06c168")
        confirmMealButton = uberHome.create_window (180, 290, window = confirmMealB)
        
    def showFood (): #create food options
        global optionsScroll, optionsFrameBox, foodPreferenceText, storeFood, page, foodOptions
        global orderFrame, orderFrameBox, orderCanvas, orderScroll, checkScroll, viewFrame, placeOrderText, placeOrderButton
        
        page = 4 #set page number 
        
        #intro text to their food preference 
        foodPreferenceText = uberHome.create_text (180, 300, text = "Here's your flavor forecast!", font = ("Helvetica", 10), fill = "#06c168")

        #create a main frame for the food options 
        optionsFrame = Frame (uberRoot, width = 250, height = 480)
        optionsFrameBox = uberHome.create_window (180, 340, window = optionsFrame)
    
        #create another canvas to place the buttons in 
        optionsCanvas = Canvas(optionsFrame, width = 250, height = 100)
        optionsCanvas.pack (side = LEFT, fill = BOTH, expand = True)
    
        #add scrollbars to the new canvas frame
        optionsScroll = Scrollbar (optionsFrame, orient = HORIZONTAL, command = optionsCanvas.xview)
        optionsScroll.place (relx = 0, rely = 1, relwidth = 1, anchor = SW)
    
        #configure the scrollbar 
        optionsCanvas.configure (xscrollcommand = optionsScroll.set)
        optionsCanvas.bind ("<Configure>", lambda e: optionsCanvas.configure (scrollregion = optionsCanvas.bbox ("all")))
    
        # bind mousewheel scrolling to the scrollbar 
        optionsCanvas.bind_all("<MouseWheel>", lambda event: optionsCanvas.xview_scroll(-int(event.delta / 120), "units"))
    
        #create another frame inside the canvas and add to canvas 
        foodOptionsFrame = Frame (optionsCanvas)
        foodOptionsFrameBox = optionsCanvas.create_window (0, 0, window = foodOptionsFrame, anchor = NW)
        
        storeFood = [] #store the food buttons
        
        for i in range (0, len(foodPreference)):
            
            # store the text of the food choice for each button
            foodOrder = StringVar()
            foodOrder.set (foodPreference)  # set the initial value
            
            #create food option buttons
            foodOptions = Button (foodOptionsFrame, text = foodPreference[i][0] + " $" + format(foodPreference[i][1], ".2f"), image = foodImages [i], compound = TOP, command = lambda foodItem = foodPreference[i][0], price = foodPreference[i][1], timeCost = foodPreference [i][2]: addCart(foodItem, price, timeCost))
            foodOptions.pack (side = LEFT, padx = 10)
            storeFood.append (foodOptions)
            
        #create a main frame for the cart canvas 
        orderFrame = Frame (uberRoot, width = 275, height = 135)
        orderFrameBox = uberHome.create_window (180, 515, window = orderFrame)
    
        #create another canvas for the application area 
        orderCanvas = Canvas (orderFrame, width = 275, height = 135, bg = "#06c168")
        orderCanvas.pack (side = LEFT, fill = BOTH, expand = True)
        
        #add scrollbars to the canvas frame
        orderScroll = Scrollbar (orderFrame, orient = VERTICAL, command = orderCanvas.yview)
        orderScroll.place (relx = 1, rely = 0, relheight = 1, anchor = NE)
        
        checkScroll = Scrollbar (orderFrame, orient = HORIZONTAL, command = orderCanvas.xview)
        checkScroll.place (relx = 1, rely = 0, relheight = 1, anchor = SW)
        
        #configure the scrollbar 
        orderCanvas.config (yscrollcommand = orderScroll.set, xscrollcommand = checkScroll.set)
        
        # bind mousewheel scrolling
        orderCanvas.bind_all("<MouseWheel>", lambda event: orderCanvas.yview_scroll(-int(event.delta / 120), "units"))
        orderCanvas.bind_all("<Shift-MouseWheel>", lambda event: orderCanvas.xview_scroll(-int(event.delta / 120), "units"))
       
        #create another frame inside the canvas to add the new canvas 
        viewFrame = Frame (orderCanvas, width = 275, height = 200, bg = "#06c168")
        viewFrameBox = orderCanvas.create_window (0, 0, window = viewFrame, anchor = NW)
        
        #create confirm order button and go to checkout  
        placeOrderText = uberHome.create_text (180, 420, text = "Time to seal the meal deal!", font = ("Helvetica", 10), fill = "#06c168")
        placeOrderB = Button (uberRoot, text = "Place Order", command = carts, fg = "#06c168")
        placeOrderButton = uberHome.create_window (180, 605, window = placeOrderB)
    
    #call function to define variables
    showFoodify ()
    showRegion ()
    showCuisine ()
    showMeal ()
    showFood ()
    clearFoodify ()
        
    #buttons and text to guide user to browse page
    browseB = Button (uberRoot, image = browseImage, borderwidth = 0, highlightthickness = 0, command = browse)
    browseButton = uberHome.create_window (180, 654, window = browseB)
    browseText = uberHome.create_text (180, 680, text = "Browse", font = ("Helvetica", 8), fill = "#605c5c")
    
    def showBrowse ():
        global searchFrameBox, groceriesList, searchBox, searchEntry, page, addSearchButton, addSearchB, browseIntroImage
        global browseFrame, browseFrameBox, browseCanvas, browseScroll, searchScroll, browseCartFrame, browseText
        
        page = 2 #set page number 
        
        #introduction text
        browseText = uberHome.create_text (180, 100, text = "Start Searching for your Groceries!", font = ("Helvetica", 13), fill = "#06c168")
        
        #add image
        browseIntroImage = uberHome.create_image (180, 450, image = browseGroceriesImage)
        
        #store user search entry
        searchItem = StringVar ()
        searchItem.set("")
        
        #create a search entry 
        searchEntry = Entry (uberRoot, textvariable = searchItem, width = 20, font = ("Helvetica", "10"))
        searchBox = uberHome.create_window (180, 150, window = searchEntry)
        
        #create a search frame to place the groceries list box
        searchFrame = Frame (uberRoot, width = 250, height = 280)
        searchFrameBox = uberHome.create_window (180, 250, window = searchFrame)
    
        #create a list box
        groceriesList = Listbox (searchFrame, width = 45, height = 5)
        groceriesList.pack () 
    
        #add groceries to list
        searchOptions (groceries)
    
        #create a binding to select groceries with mouse click
        groceriesList.bind ("<ButtonRelease-1>", selectedFood)
    
        #create a binding on the entry box to check groceries availiblity 
        searchEntry.bind ("<KeyRelease>", check)
        
        #create a main frame for the cart canvas 
        browseFrame = Frame (uberRoot, width = 275, height = 200)
        groceriesFrameBox = uberHome.create_window (180, 470, window = browseFrame)
    
        #create another canvas for the application area 
        browseCanvas = Canvas (browseFrame, width = 275, height = 200)
        browseCanvas.pack (side = LEFT, fill = BOTH, expand = True)
        
        #add scrollbars to the canvas frame
        browseScroll = Scrollbar (browseFrame, orient = VERTICAL, command = browseCanvas.yview)
        browseScroll.place (relx = 1, rely = 0, relheight = 1, anchor = NE)
        
        searchScroll = Scrollbar (browseFrame, orient = HORIZONTAL, command = browseCanvas.xview)
        searchScroll.place (relx = 1, rely = 0, relheight = 1, anchor = SW)
        
        #configure the scrollbar 
        browseCanvas.config (yscrollcommand = browseScroll.set, xscrollcommand = searchScroll.set)
        
        # bind mousewheel scrolling
        browseCanvas.bind_all("<MouseWheel>", lambda event: browseCanvas.yview_scroll(-int(event.delta / 120), "units"))
        browseCanvas.bind_all("<Shift-MouseWheel>", lambda event: browseCanvas.xview_scroll(-int(event.delta / 120), "units"))
       
        #create another frame inside the canvas to add the new canvas 
        browseCartFrame = Frame (browseCanvas, width = 275, height = 200)
        browseCartFrameBox = browseCanvas.create_window (0, 0, window = browseFrame, anchor = NW)
        
        #button to add item to cart
        addSearchB = Button (uberRoot, text = "Add to Cart")
        addSearchButton = uberHome.create_window (295, 150, window = addSearchB, state = HIDDEN) 
    
    #call function to define variables
    showBrowse ()
    clearBrowse ()
    
    #buttons and text to guide user to cart page
    cartsB = Button (uberRoot, image = cartsImage, borderwidth = 0, highlightthickness = 0, command = carts)
    cartButton = uberHome.create_window (285, 654, window = cartsB)
    cartsText = uberHome.create_text (285, 680, text = "Carts", font = ("Helvetica", 8), fill = "#605c5c")
    
    def showEmptyCarts ():
        
        global emptyCart
        emptyCart = uberHome.create_image (180, 360, image = emptyCartImage)
        
    def showReceipt ():
        
        global cartsFrame, cartsFrameBox, cartsCanvas, receiptScroll, receiptOrderCode, placeTime, deliverTime
        global receiptBackground, foodifyItem, receiptCostBackground, subtotalText, taxText, totalText, subtotalPayment, taxPayment, totalPayment
        
        #get values from calculations 
        subtotal, tax, total = calculateCost ()
        deliveryDuration = deliveryTime ()
        
        #store time of order
        orderTime = time.ctime (time.time())
    
        #create delivery time
        waitTime = time.ctime (time.time() + deliveryDuration + 300)
        
        #store order code
        orderCode = ""
        
        #create a main frame for the canvas 
        cartsFrame = Frame (uberRoot, width = 296, height = 350)
        cartsFrameBox = uberHome.create_window (186, 300, window = cartsFrame)
    
        #create another canvas for the application area 
        cartsCanvas = Canvas (cartsFrame, width = 296, height = 350, bg = "white")
        cartsCanvas.pack (side = LEFT, fill = BOTH, expand = True)
    
        #add scrollbars to the canvas frame
        receiptScroll = Scrollbar (cartsFrame, orient = VERTICAL, command = cartsCanvas.yview)
        receiptScroll.place (relx = 1, rely = 0, relheight = 1, anchor = NE)
    
        #configure the scrollbar 
        cartsCanvas.config (yscrollcommand = receiptScroll.set)
    
        # bind mousewheel scrolling
        cartsCanvas.bind_all("<MouseWheel>", lambda event: cartsCanvas.yview_scroll(-int(event.delta / 120), "units"))
    
        #create another frame inside the canvas to add the new canvas 
        receiptFrame = Frame (cartsCanvas)
        receiptFrameBox = cartsCanvas.create_window (0, 0, window = receiptFrame, anchor = NW)
        
        #add background images
        receiptBackground = cartsCanvas.create_image (143, 200, image = receiptFormatImage) 
        
        #display user's name on the receipt 
        receiptName = cartsCanvas.create_text (155, 30, text = userName.upper (), font = ("Helvetica", 15), fill = "white")
        
        #display the time when user place the order and the delivery time
        placeTime = cartsCanvas.create_text (115, 60, text = "Placed on" + " " + orderTime, font = ("Helvetica", 10))
        deliverTime = cartsCanvas.create_text (115, 80, text = "Delivery by" + " " + waitTime, font = ("Helvetica", 10))
    
        for i in range (0,5): #generate a random order code 
            value = random.randint (1,2)
            if value == 1:
                orderCode = orderCode + random.choice (alphabetCode)
            else:
                orderCode = orderCode + random.choice (numberCode)
        
        #create the order code text 
        receiptOrderCode = cartsCanvas.create_text (90, 30, text = orderCode, font = ("Helvetica", 15), fill = "white")
            
        #display the user's order
        if len (cart) > 0:
            
            for i in range (0, len(cart)):
                
                itemPlace = 150
                itemPlace = itemPlace + 30 * i
                
                foodifyItem = cartsCanvas.create_text (80, itemPlace, text = cart [i][0], font = ("Helvetica", 12))
                foodifyPrice = cartsCanvas.create_text (195, itemPlace, text = "$" + str(cart [i][1]), font = ("Helvetica", 12))
        
        #display the cost calculation of the order
        receiptCostBackground = uberHome.create_image (180, 550, image = receiptCostImage)
        
        subtotalText = uberHome.create_text (72, 520, text = "Subtotal", font = ("Helvetica", 12))
        taxText = uberHome.create_text (55, 545, text = "Tax", font = ("Helvetica", 12))
        totalText = uberHome.create_text (92, 580, text = "Total Payment", font = ("Helvetica", 12))
        
        subtotalPayment = uberHome.create_text (285, 520, text = "$" + format(subtotal, ".2f"), font = ("Helvetica", 12))
        taxPayment = uberHome.create_text (285, 545, text = "$" + format(tax, ".2f"), font = ("Helvetica", 12))
        totalPayment = uberHome.create_text (285, 580, text = "$" + format(total, ".2f"), font = ("Helvetica", 12))
    
    #call function to define variables
    showHome ()
    showReceipt ()
    showEmptyCarts ()
    carts ()
    clearCarts ()
    home ()
    
    timeUpdateUberFeasts () #keep the time updated
    
    uberRoot.mainloop () #close pop-up box
    
# ---------------- UberFeast ---------------- #

# ---------------- Camera ---------------- #

def openCamera ():
    
    global cameraRoot, cameraHome, cameraTime
    
    cameraRoot = Toplevel()  # create a window attached to the main root 
    
    cameraHome = Canvas(cameraRoot, width = 360, height = 710)
    cameraHome.pack()  # put the canvas onto the  window
    
    cameraRoot.title ("Camera")
    
    #importing images and buttons for apps
    cameraPhone = cameraHome.create_image (180, 360, image = phoneWallpaper)
    
    #go back button and show text
    cameraText = cameraHome.create_text (180, 360, text = "To Be Developed...", font = ("Helvetica", 20), fill = "white")
    
    cameraReturnB = Button (cameraRoot, image = returnImage, borderwidth = 0, highlightthickness = 0, command = closeCamera)
    cameraReturnButton = cameraHome.create_window (55, 130, window = cameraReturnB)
    
    #display the time 
    currentTime = time.ctime (time.time())
    cameraTime = cameraHome.create_text (120, 70, text = currentTime, font = ("Helvetica", 10), fill = "white")
        
    timeUpdateCamera () #keep the time updated
    
    cameraRoot.mainloop ()

# ---------------- Camera ---------------- #

# ---------------- Safari ---------------- #

def openSafari ():
    global safariRoot, safariHome, safariTime
    
    safariRoot = Toplevel()  # create a window attached to the main root 
    
    safariHome = Canvas(safariRoot, width = 360, height = 710)
    safariHome.pack()  # put the canvas onto the  window
    
    safariRoot.title ("Safari")
    
    #importing images and buttons for apps
    safariPhone = safariHome.create_image (180, 360, image = phoneWallpaper)
    
    #go back button and show text
    safariText = safariHome.create_text (180, 360, text = "To Be Developed...", font = ("Helvetica", 20), fill = "white")
    
    safariReturnB = Button (safariRoot, image = returnImage, borderwidth = 0, highlightthickness = 0, command = closeSafari)
    safariReturnButton = safariHome.create_window (55, 130, window = safariReturnB)
    
    #display the time 
    currentTime = time.ctime (time.time())
    safariTime = safariHome.create_text (120, 70, text = currentTime, font = ("Helvetica", 10), fill = "white")
        
    timeUpdateSafari () #keep the time updated
    
    safariRoot.mainloop ()
        
# ---------------- Safari ---------------- #

# ---------------- YouTube ---------------- #

def openYoutube ():
    global youtubeRoot, youtubeHome, youtubeTime
    
    youtubeRoot = Toplevel()  # create a window attached to the main root 
    
    youtubeHome = Canvas(youtubeRoot, width = 360, height = 710)
    youtubeHome.pack()  # put the canvas onto the  window
    
    youtubeRoot.title ("YouTube")
    
    #importing images and buttons for apps
    youtubePhone = youtubeHome.create_image (180, 360, image = phoneWallpaper)
    
    #go back button and show text
    youtubeText = youtubeHome.create_text (180, 360, text = "To Be Developed...", font = ("Helvetica", 20), fill = "white")
    
    youtubeReturnB = Button (youtubeRoot, image = returnImage, borderwidth = 0, highlightthickness = 0, command = closeYoutube)
    youtubeReturnButton = youtubeHome.create_window (55, 130, window = youtubeReturnB)
    
    #display the time 
    currentTime = time.ctime (time.time())
    youtubeTime = youtubeHome.create_text (120, 70, text = currentTime, font = ("Helvetica", 10), fill = "white")
        
    timeUpdateYoutube () #keep the time updated
    
    youtubeRoot.mainloop ()
        
# ---------------- YouTube ---------------- #

# ---------------- Messenger ---------------- #

def openMessenger ():
    
    global messengerRoot, messengerHome, messengerTime
    
    messengerRoot = Toplevel()  # create a window attached to the main root 
    
    messengerHome = Canvas(messengerRoot, width = 360, height = 710)
    messengerHome.pack()  # put the canvas onto the  window
    
    messengerRoot.title ("Messenger")
    
    #importing images and buttons for apps
    messengerPhone = messengerHome.create_image (180, 360, image = phoneWallpaper)
    
    #go back button and show text
    messengerText = messengerHome.create_text (180, 360, text = "To Be Developed...", font = ("Helvetica", 20), fill = "white")
    
    messengerReturnB = Button (messengerRoot, image = returnImage, borderwidth = 0, highlightthickness = 0, command = closeMessenger)
    messengerReturnButton = messengerHome.create_window (55, 130, window = messengerReturnB)
    
    #display the time 
    currentTime = time.ctime (time.time())
    messengerTime = messengerHome.create_text (120, 70, text = currentTime, font = ("Helvetica", 10), fill = "white")
        
    timeUpdateMessenger () #keep the time updated
    
    messengerRoot.mainloop ()
        
# ---------------- Messenger ---------------- #

# ---------------- Flappy Bird ---------------- #

def openFlappy ():
    
    global flappyRoot, flappyHome, flappyTime
    
    flappyRoot = Toplevel()  # create a window attached to the main root 
    
    flappyHome = Canvas(flappyRoot, width = 360, height = 710)
    flappyHome.pack()  # put the canvas onto the  window
    
    flappyRoot.title ("Flappy Bird")
    
    #importing images and buttons for apps
    flappyPhone = flappyHome.create_image (180, 360, image = phoneWallpaper)
    
    #go back button and show text
    flappyText = flappyHome.create_text (180, 360, text = "To Be Developed...", font = ("Helvetica", 20), fill = "white")
    
    flappyReturnB = Button (flappyRoot, image = returnImage, borderwidth = 0, highlightthickness = 0, command = closeFlappy)
    flappyReturnButton = flappyHome.create_window (55, 130, window = flappyReturnB)
    
    #display the time 
    currentTime = time.ctime (time.time())
    flappyTime = flappyHome.create_text (120, 70, text = currentTime, font = ("Helvetica", 10), fill = "white")
        
    timeUpdateFlappy () #keep the time updated
    
    flappyRoot.mainloop ()
        
# ---------------- Flappy Bird ---------------- #

# ---------------- Spotify ---------------- #

def openSpotify ():
    
    global spotifyRoot, spotifyHome, spotifyTime
    
    spotifyRoot = Toplevel()  # create a window attached to the main root 
    
    spotifyHome = Canvas(spotifyRoot, width = 360, height = 710)
    spotifyHome.pack()  # put the canvas onto the  window
    
    spotifyRoot.title ("Spotify")
    
    #importing images and buttons for apps
    spotifyPhone = spotifyHome.create_image (180, 360, image = phoneWallpaper)
    
    #go back button and show text
    spotifyText = spotifyHome.create_text (180, 360, text = "To Be Developed...", font = ("Helvetica", 20), fill = "white")
    
    spotifyReturnB = Button (spotifyRoot, image = returnImage, borderwidth = 0, highlightthickness = 0, command = closeSpotify)
    spotifyReturnButton = spotifyHome.create_window (55, 130, window = spotifyReturnB)
    
    #display the time 
    currentTime = time.ctime (time.time())
    spotifyTime = spotifyHome.create_text (120, 70, text = currentTime, font = ("Helvetica", 10), fill = "white")
        
    timeUpdateSpotify () #keep the time updated
    
    spotifyRoot.mainloop ()
        
# ---------------- Spotify ---------------- #

# ---------------- Notes ---------------- #

def openNotes ():
    
    global notesRoot, notesHome, notesTime
    
    notesRoot = Toplevel()  # create a window attached to the main root 
    
    notesHome = Canvas(notesRoot, width = 360, height = 710)
    notesHome.pack()  # put the canvas onto the  window
    
    notesRoot.title ("Notes")
    
    #importing images and buttons for apps
    notesPhone = notesHome.create_image (180, 360, image = phoneWallpaper)
    
    #go back button and show text
    notesText = notesHome.create_text (180, 360, text = "To Be Developed...", font = ("Helvetica", 20), fill = "white")
    
    notesReturnB = Button (notesRoot, image = returnImage, borderwidth = 0, highlightthickness = 0, command = closeNotes)
    notesReturnButton = notesHome.create_window (55, 130, window = notesReturnB)
    
    #display the time 
    currentTime = time.ctime (time.time())
    notesTime = notesHome.create_text (120, 70, text = currentTime, font = ("Helvetica", 10), fill = "white")
        
    timeUpdateNotes () #keep the time updated
    
    notesRoot.mainloop ()
        
# ---------------- Notes ---------------- #

# ---------------- Reminder ---------------- #

def openReminder ():
    
    global reminderRoot, reminderHome, reminderTime
    
    reminderRoot = Toplevel()  # create a window attached to the main root 
    
    reminderHome = Canvas(reminderRoot, width = 360, height = 710)
    reminderHome.pack()  # put the canvas onto the  window
    
    reminderRoot.title ("Reminder")
    
    #importing images and buttons for apps
    reminderPhone = reminderHome.create_image (180, 360, image = phoneWallpaper)
    
    #go back button and show text
    reminderText = reminderHome.create_text (180, 360, text = "To Be Developed...", font = ("Helvetica", 20), fill = "white")
    
    reminderReturnB = Button (reminderRoot, image = returnImage, borderwidth = 0, highlightthickness = 0, command = closeReminder)
    reminderReturnButton = reminderHome.create_window (55, 130, window = reminderReturnB)
    
    #display the time 
    currentTime = time.ctime (time.time())
    reminderTime = reminderHome.create_text (120, 70, text = currentTime, font = ("Helvetica", 10), fill = "white")
        
    timeUpdateReminder () #keep the time updated
    
    reminderRoot.mainloop ()
        
# ---------------- Notes ---------------- #

# ---------------- Home Canvases ---------------- #  

def homeCanvas1 ():
    
    homeRoot.title ("Home Screen")
    
    #clear introscreen
    homeScreen.itemconfig (title, state = HIDDEN)
    homeScreen.itemconfig (introduction, state = HIDDEN)
    homeScreen.itemconfig (finishButton, state = HIDDEN)
    homeScreen.itemconfig (logo, state = HIDDEN)
    homeScreen.itemconfig (nameBox, state = HIDDEN)
    homeScreen.itemconfig (backgroundInfo, state = HIDDEN)
    switchB2.config (image = switchImage)
    switchB3.config (image = switchImage)
    
    #clear the other apps
    homeScreen.itemconfig (calculatorButton, state = HIDDEN)
    homeScreen.itemconfig (toDoButton, state = HIDDEN)
    homeScreen.itemconfig (flappyButton, state = HIDDEN)
    homeScreen.itemconfig (spotifyButton, state = HIDDEN)
    homeScreen.itemconfig (notesButton, state = HIDDEN)
    homeScreen.itemconfig (reminderButton, state = HIDDEN)
    
    #clear the other application text
    homeScreen.itemconfig (calculatorText, state = HIDDEN)
    homeScreen.itemconfig (toDoText, state = HIDDEN)
    homeScreen.itemconfig (flappyText, state = HIDDEN)
    homeScreen.itemconfig (spotifyText, state = HIDDEN)
    homeScreen.itemconfig (notesText, state = HIDDEN)
    homeScreen.itemconfig (reminderText, state = HIDDEN)
    
    #show home canvas 1 
    homeScreen.itemconfig (switchButton1, state = NORMAL)
    homeScreen.itemconfig (switchButton2, state = NORMAL)
    homeScreen.itemconfig (switchButton3, state = NORMAL)
    homeScreen.itemconfig (fixBar, state = NORMAL)
    homeScreen.itemconfig (cameraButton, state = NORMAL)
    homeScreen.itemconfig (uberFeastsButton, state = NORMAL)
    homeScreen.itemconfig (uberFeastsText, state = NORMAL)
    homeScreen.itemconfig (safariButton, state = NORMAL)
    homeScreen.itemconfig (safariText, state = NORMAL)
    homeScreen.itemconfig (youtubeButton, state = NORMAL)
    homeScreen.itemconfig (youtubeText, state = NORMAL)
    homeScreen.itemconfig (messengerButton, state = NORMAL)
    homeScreen.itemconfig (messengerText, state = NORMAL)
    switchB1.config (image = selectedSwitchImage) 

def homeCanvas2 ():
    
    #clear the other apps
    homeScreen.itemconfig (uberFeastsButton, state = HIDDEN)
    homeScreen.itemconfig (notesButton, state = HIDDEN)
    homeScreen.itemconfig (reminderButton, state = HIDDEN)
    homeScreen.itemconfig (toDoButton, state = HIDDEN)
    homeScreen.itemconfig (safariButton, state = HIDDEN)
    homeScreen.itemconfig (youtubeButton, state = HIDDEN)
    homeScreen.itemconfig (messengerButton, state = HIDDEN)
    homeScreen.itemconfig (backgroundInfo, state = HIDDEN)
    switchB1.config (image = switchImage)
    switchB3.config (image = switchImage)
    
    #clear the other application text
    homeScreen.itemconfig (uberFeastsText, state = HIDDEN)
    homeScreen.itemconfig (toDoText, state = HIDDEN)
    homeScreen.itemconfig (notesText, state = HIDDEN)
    homeScreen.itemconfig (reminderText, state = HIDDEN)
    homeScreen.itemconfig (safariText, state = HIDDEN)
    homeScreen.itemconfig (youtubeText, state = HIDDEN)
    homeScreen.itemconfig (messengerText, state = HIDDEN)
    
    #show home canvas 2 
    homeScreen.itemconfig (calculatorText, state = NORMAL)
    homeScreen.itemconfig (calculatorButton, state = NORMAL)
    homeScreen.itemconfig (flappyText, state = NORMAL)
    homeScreen.itemconfig (flappyButton, state = NORMAL)
    homeScreen.itemconfig (spotifyText, state = NORMAL)
    homeScreen.itemconfig (spotifyButton, state = NORMAL)
    switchB2.config (image = selectedSwitchImage) 
    
def homeCanvas3 ():

    #clear the other apps
    homeScreen.itemconfig (calculatorButton, state = HIDDEN)
    homeScreen.itemconfig (uberFeastsButton, state = HIDDEN)
    homeScreen.itemconfig (flappyButton, state = HIDDEN)
    homeScreen.itemconfig (spotifyButton, state = HIDDEN)
    homeScreen.itemconfig (safariButton, state = HIDDEN)
    homeScreen.itemconfig (youtubeButton, state = HIDDEN)
    homeScreen.itemconfig (messengerButton, state = HIDDEN)
    switchB1.config (image = switchImage)
    switchB2.config (image = switchImage)
    
    #clear the other application text
    homeScreen.itemconfig (calculatorText, state = HIDDEN)
    homeScreen.itemconfig (uberFeastsText, state = HIDDEN)
    homeScreen.itemconfig (flappyText, state = HIDDEN)
    homeScreen.itemconfig (spotifyText, state = HIDDEN)
    homeScreen.itemconfig (safariText, state = HIDDEN)
    homeScreen.itemconfig (youtubeText, state = HIDDEN)
    homeScreen.itemconfig (messengerText, state = HIDDEN)
    
    #show home canvas 3
    homeScreen.itemconfig (toDoText, state = NORMAL)
    homeScreen.itemconfig (toDoButton, state = NORMAL)
    homeScreen.itemconfig (notesText, state = NORMAL)
    homeScreen.itemconfig (notesButton, state = NORMAL)
    homeScreen.itemconfig (reminderText, state = NORMAL)
    homeScreen.itemconfig (reminderButton, state = NORMAL)
    switchB3.config (image = selectedSwitchImage) 
     
# ---------------- Home Canvases ---------------- #
    
# ---------------- Intro Canvas ---------------- # 
def introCanvas ():
    
    homeRoot.title ("Introduction Screen")
    
    #clear the unbox home screens
    homeScreen.itemconfig (unboxPhone, state = HIDDEN)
    homeScreen.itemconfig (unboxButton, state = HIDDEN)
    
    #show introduction screen
    homeScreen.itemconfig (title, state = NORMAL)
    homeScreen.itemconfig (introduction, state = NORMAL)
    homeScreen.itemconfig (finishButton, state = NORMAL)
    homeScreen.itemconfig (wallpaper, state = NORMAL)
    homeScreen.itemconfig (logo, state = NORMAL)
    homeScreen.itemconfig (nameBox, state = NORMAL)
    homeScreen.itemconfig (shutDown, state = NORMAL)
    homeScreen.itemconfig (showTime, state = NORMAL)
    homeScreen.itemconfig (backgroundInfo, state = NORMAL)
    
# ---------------- Intro Canvas ---------------- #

# ---------------- Unbox Canvas ---------------- #

def unboxCanvas ():
    
    global homeRoot, homeScreen, title, introduction, finishButton
    global wallpaper, aPhoneImage, logo, returnImage, unboxPhone, unboxButton
    global nameEntry, nameBox, shutDown, currentTime, showTime
    global uberFeasts, camera, fixBar, selectedSwitchImage, switchImage
    global uberFeastsButton, cameraButton, calculatorButton, toDoButton
    global safariButton, youtubeButton, messengerButton, flappyButton, spotifyButton, notesButton, reminderButton
    global safariText, youtubeText, messengerText, flappyText, spotifyText, notesText, reminderText
    global uberFeastsText, calculatorText, toDoText, backgroundInfo
    global switchButton1, switchButton2, switchButton3, switchB1, switchB2, switchB3
    global waveWhispererImage, lostSpaceImage, sunsetPetalImage, cloudyHorizonImage, autumnAuraImage, codeLifeImage
    
    homeRoot = Tk () #create a pop-up box
    homeRoot.title ("Unbox APhone")
    homeRoot.iconbitmap ('APhone Logo.ico')
    
    homeScreen = Canvas (homeRoot, width = 360, height = 710)
    homeScreen.pack () #put the canvas onto the root
    
    #import current time
    currentTime = time.ctime (time.time())

    #importing images onto program 
    aPhoneImage = PhotoImage (file = "APhone.png")
    logoImage = PhotoImage (file = "Logo.png")
    cameraImage = PhotoImage (file = "Camera.png")
    uberFeastImage = PhotoImage (file = "Uber Feasts.png")
    safariImage = PhotoImage (file = "Safari.png")
    youtubeImage = PhotoImage (file = "Youtube.png")
    messengerImage = PhotoImage (file = "Messenger.png")
    calculatorImage = PhotoImage (file = "Calculator.png")
    flappyImage = PhotoImage (file = "Flappy Bird.png")
    spotifyImage = PhotoImage (file = "Spotify.png")
    toDoImage = PhotoImage (file = "To Do.png")
    notesImage = PhotoImage (file = "Notes.png")
    reminderImage = PhotoImage (file = "Reminder.png")
    fixBarImage = PhotoImage (file = "Fixed Bar.png")
    switchImage = PhotoImage (file = "Switch.png")
    selectedSwitchImage = PhotoImage (file = "Selected Switch.png")
    returnImage = PhotoImage (file = "Return.png")
    boxCaseImage = PhotoImage (file = "Box Case.png")
    
    waveWhispererImage = PhotoImage (file = "Wave Whisperer.png")
    lostSpaceImage = PhotoImage (file = "Lost in Space.png")
    sunsetPetalImage = PhotoImage (file = "Sunset Petal.png")
    cloudyHorizonImage = PhotoImage (file = "Cloudy Horizon.png")
    autumnAuraImage = PhotoImage (file = "Autumn Aura.png")
    codeLifeImage = PhotoImage (file = "Code 4 Life.png") 
    
    #display intro screen images onto canvas
    wallpaper = homeScreen.create_image (180, 360, image = aPhoneImage, state = HIDDEN)
    logo = homeScreen.create_image (180, 150, image = logoImage, state = HIDDEN)
    changeWallpaper (aPhoneImage)
    
    #add menu options to change background
    backgroundMenu = Menu(homeRoot)
    homeRoot.config (menu = backgroundMenu)
    
    backgroundOptions = Menu (backgroundMenu)
    backgroundMenu.add_cascade (label = "Background", menu = backgroundOptions)
    backgroundOptions.add_command (label = "Default", command = lambda: changeWallpaper (aPhoneImage))
    backgroundOptions.add_command (label = "Wave Whisperer", command = lambda: changeWallpaper (waveWhispererImage))
    backgroundOptions.add_command (label = "Lost in Space", command = lambda: changeWallpaper (lostSpaceImage))
    backgroundOptions.add_command (label = "Sunset Petal", command = lambda: changeWallpaper (sunsetPetalImage))
    backgroundOptions.add_command (label = "Cloudy Horizon", command = lambda: changeWallpaper (cloudyHorizonImage))
    backgroundOptions.add_command (label = "Autumn Aura", command = lambda: changeWallpaper (autumnAuraImage))
    backgroundOptions.add_command (label = "Code 4 Life", command = lambda: changeWallpaper (codeLifeImage))
    
    #diplay unbox button and images 
    unboxPhone = homeScreen.create_image (180, 360, image = boxCaseImage)
    unboxB = Button (homeRoot, text = "UNBOX", font = ("Helvitica", "20"), command = introCanvas)
    unboxButton = homeScreen.create_window (180, 675, window = unboxB) 

    #creating title, text, and features
    title = homeScreen.create_text (180, 250, text = "Welcome To APhone", font = ("Helvetica", "20"), fill = "white", state = HIDDEN)
    introduction = homeScreen.create_text (180, 350, text = '  Tell Me Your\n  FIRST Name\n  Click "Finish"\n To get Started!', font = ("Helvetica", "20"), fill = "white", state = HIDDEN)
    backgroundInfo = homeScreen.create_text (180, 575, text = "Select a Wallpaper!\n Top Left Corner!", font = ("Helvetica", "20"), state = HIDDEN)
    
    #get started button 
    finishB = Button (homeRoot, text = "FINISH", font = ("Helvitica", "20"), command = validateInput)
    finishButton = homeScreen.create_window (180, 500, window = finishB, state = HIDDEN) 

    #collecting names 
    name = StringVar () #this is the control variable that handles getting the information from the entrybox
    nameEntry = Entry (homeRoot, textvariable = name, width = 35, font = ("Helvitica", "10"))
    nameBox = homeScreen.create_window (180, 450, window = nameEntry, state = HIDDEN)

    #shut down system
    shutDownButton = Button(homeRoot, text = "Shut Down", font = ("Helvitica", "10"), command = homeRoot.destroy)
    shutDown = homeScreen.create_window (80, 100, window = shutDownButton, state = HIDDEN)
    
    #importing images and buttons for home screens
    switchB1 = Button (homeRoot, image = selectedSwitchImage, borderwidth = 0, highlightthickness = 0, command = homeCanvas1)
    switchButton1 = homeScreen.create_window (150, 560, window = switchB1, state = HIDDEN)
    
    switchB2 = Button (homeRoot, image = switchImage, borderwidth = 0, highlightthickness = 0, command = homeCanvas2)
    switchButton2 = homeScreen.create_window (180, 560, window = switchB2, state = HIDDEN)
    
    switchB3 = Button (homeRoot, image = switchImage, borderwidth = 0, highlightthickness = 0, command = homeCanvas3)
    switchButton3 = homeScreen.create_window (210, 560, window = switchB3, state = HIDDEN)
    
    fixBar = homeScreen.create_image (180, 630, image = fixBarImage, state = HIDDEN)
    
    cameraB = Button (homeRoot, image = cameraImage, borderwidth = 0, highlightthickness = 0, command = openCamera) 
    cameraButton = homeScreen.create_window (180, 630, window = cameraB, state = HIDDEN)
    cameraText = homeScreen.create_text (75, 225, text = "Camera", font = ("Helvetica", "10"), fill = "white", state = HIDDEN)
    
    uberFeastsB = Button(homeRoot, image = uberFeastImage, borderwidth = 0, highlightthickness = 0, command = openUberFeasts)
    uberFeastsButton = homeScreen.create_window (75, 175, window = uberFeastsB, state = HIDDEN)
    uberFeastsText = homeScreen.create_text (75, 225, text = "Uber Feasts", font = ("Helvetica", "10"), fill = "white", state = HIDDEN)
    
    safariB = Button(homeRoot, image = safariImage, borderwidth = 0, highlightthickness = 0, command = openSafari)
    safariButton = homeScreen.create_window (175, 175, window = safariB, state = HIDDEN)
    safariText = homeScreen.create_text (175, 225, text = "Safari", font = ("Helvetica", "10"), fill = "white", state = HIDDEN)
    
    youtubeB = Button (homeRoot, image = youtubeImage, borderwidth = 0, highlightthickness = 0, command = openYoutube)
    youtubeButton = homeScreen.create_window (275, 175, window = youtubeB, state = HIDDEN)
    youtubeText = homeScreen.create_text (275, 225, text = "Youtube", font = ("Helvetica", "10"), fill = "white", state = HIDDEN)
    
    messengerB = Button(homeRoot, image = messengerImage, borderwidth = 0, highlightthickness = 0, command = openMessenger)
    messengerButton = homeScreen.create_window (75, 275, window = messengerB, state = HIDDEN)
    messengerText = homeScreen.create_text (75, 325, text = "Messenger", font = ("Helvetica", "10"), fill = "white", state = HIDDEN)
    
    calculatorB = Button (homeRoot, image = calculatorImage, borderwidth = 0, highlightthickness = 0, command = openCalculator)
    calculatorButton = homeScreen.create_window (75, 175, window = calculatorB, state = HIDDEN)
    calculatorText = homeScreen.create_text (75, 225, text = "Calculator", font = ("Helvetica", "10"), fill = "white", state = HIDDEN)
    
    flappyB = Button (homeRoot, image = flappyImage, borderwidth = 0, highlightthickness = 0, command = openFlappy)
    flappyButton = homeScreen.create_window (175, 175, window = flappyB, state = HIDDEN)
    flappyText = homeScreen.create_text (175, 225, text = "Flappy Bird", font = ("Helvetica", "10"), fill = "white", state = HIDDEN)
    
    spotifyB = Button (homeRoot, image = spotifyImage, borderwidth = 0, highlightthickness = 0, command = openSpotify)
    spotifyButton = homeScreen.create_window (275, 175, window = spotifyB, state = HIDDEN)
    spotifyText = homeScreen.create_text (275, 225, text = "Spotify", font = ("Helvetica", "10"), fill = "white", state = HIDDEN)
    
    toDoB = Button (homeRoot, image = toDoImage, borderwidth = 0, highlightthickness = 0, command = openToDo)
    toDoButton = homeScreen.create_window (75, 175, window = toDoB, state = HIDDEN)
    toDoText = homeScreen.create_text (75, 225, text = "To Do", font = ("Helvetica", "10"), fill = "white", state = HIDDEN)
    
    notesB = Button (homeRoot, image = notesImage, borderwidth = 0, highlightthickness = 0, command = openNotes)
    notesButton = homeScreen.create_window (175, 175, window = notesB, state = HIDDEN)
    notesText = homeScreen.create_text (175, 225, text = "Notes", font = ("Helvetica", "10"), fill = "white", state = HIDDEN)
    
    reminderB = Button (homeRoot, image = reminderImage, borderwidth = 0, highlightthickness = 0, command = openReminder)
    reminderButton = homeScreen.create_window (275, 175, window = reminderB, state = HIDDEN)
    reminderText = homeScreen.create_text (275, 225, text = "Reminder", font = ("Helvetica", "10"), fill = "white", state = HIDDEN)
    
    showTime = homeScreen.create_text (120, 70, text = currentTime, font = ("Helvetica", 10), fill = "white", state = HIDDEN)
    timeUpdateHome ()  #start updating the time

    mainloop ()

unboxCanvas () #open opening screen
    
    
    





 

     