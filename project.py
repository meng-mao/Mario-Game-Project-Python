import tkinter as tk
import winsound
root = tk.Tk()
# ===============Adjust size--------------------------
root.geometry("1820x750")
frame = tk.Frame()
canvas = tk.Canvas(frame)
# ==================background interface-----------------------
bg = tk.PhotoImage(file="images/My_bg.png")
startMusic=winsound .PlaySound("Sound\StartGame.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
# ======================title of frame-----------------------
frame.master.title("Friends Help")
Mario = tk.PhotoImage(file="images\mario.png")
Diamond = tk.PhotoImage(file="images\purpleDiamond.png")
myEnemy = tk.PhotoImage(file="images\enemy.png")
# ======================banner slide show -----------------
banner = tk.PhotoImage(file="Images\Game.png")
canvas.create_image(0, 0, image=banner, anchor="nw")
grid = [
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 1, 3, 2, 0, 3, 0, 0, 0, 4],
    [4, 0, 0, 3, 0, 0, 0, 3, 0, 4],
    [4, 3, 0, 0, 3, 0, 0, 3, 0, 4],
    [4, 2, 3, 0, 0, 0, 0, 3, 0, 4],
    [4, 0, 3, 0, 3, 3, 0, 3, 0, 4],
    [4, 0, 0, 0, 3, 0, 0, 3, 0, 4],
    [4, 0, 3, 3, 0, 0, 3, 3, 0, 4],
    [4, 2, 3, 2, 0, 3, 2, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
]
isGameOver = False
isGameWin=False
# ==================Function draw grid=======================================
def drawGrid():
        global isGameOver,isGameWin
        if isGameOver == False and isGameWin==False:
            canvas.delete("all")
            canvas.create_image(0, 0, image=bg,anchor="nw")
            y1 = 15
            y2 = 75
            x1 = 10
            x2 = 110
            for elements in range(len(grid)):
                for values in range(len(grid[elements])):
                    x1 = x2
                    x2 += 100
                    if grid[elements][values] == 1:
                        canvas.create_image(x2-55, y2-32, image=Mario, tags="play")
                    elif grid[elements][values] == 2:
                        canvas.create_image(x2-50, y2-30, image=Diamond)
                    else:
                        canvas.create_rectangle(x1, y1, x2, y2,outline="orange")
                    if grid[elements][values] == 0:
                        canvas.create_rectangle(x1, y1, x2, y2,outline="orange")
                    elif grid[elements][values] == 1:
                        canvas.create_image(x2-55, y2-32, image=Mario)
                    elif grid[elements][values] == 2:
                        canvas.create_image(x2-50, y2-30, image=Diamond)
                    elif grid[elements][values] == 3:
                        canvas.create_image(x2-55, y2-32, image=myEnemy)
                    elif grid[elements][values] == 4:
                        canvas.create_rectangle(x1, y1, x2, y2,outline="orange",fill="brown")
                y1 = y2
                y2 += 65
                x1 = 10
                x2 = 110
            displayScore()
    # ============Count down timer========================
def button_countdown(i, label):
    if i > 0:
        i -= 1
        label.set(i)
        root.after(1000, lambda: button_countdown(i, label))
    else:
        close()
def close():
    if Score<5 or counter==0:
        LostGame()
    elif Score==5 or counter>=0:
        WinGame()
counter = 30
button_label = tk.StringVar()
button_label.set(counter)
myTimer=tk.Button( textvariable=button_label, command=close).pack()
canvas.itemconfig(myTimer,text=button_label)
def deplay():
    button_countdown(counter, button_label)
    drawGrid()
def displayButton():
    # button start to play
    myButton = tk.Button(root, text="Play", command=deplay)
    myButton.config(width=7, height=1, bg="#007EE9",fg="yellow",border="5", font=("Arial", 20, "bold"))
    myButton_canvas = canvas.create_window(630, 450, anchor="nw", window=myButton, tags="button")
#=====================================button exit ---------------------
    myButton = tk.Button(root, text="Exit", command=root.destroy)
    myButton.config(width=7, height=1, bg="#007EE9",fg="yellow",border="5",font=("Arial", 20, "bold"))
    myButton_canvas = canvas.create_window(630, 520, anchor="nw", window=myButton)
displayButton()
# ===================================find row of marion------------------
def findRow(array):
    for row in range(len(array)):
        if 1 in array[row]:
            return row
# =========================Find column of mario===========================
def findCol(array):
    for row in range(len(array)):
        if 1 in array[row]:
            for col in range(len(array[row])):
                if array[row][col] == 1:
                    return col
# ========================Find row of diamond=============================
def findRowDiamond(array):
    for row in range(len(array)):
        if 2 in array[row]:
            return row
# =========================Find column of diamond===========================
def findColDiamond(array):
    for row in range(len(array)):
        if 2 in array[row]:
            for col in range(len(array[row])):
                if array[row][col] == 2:
                    return col
# ======================Fine row of enemy============================
def findRowOfEnemy(array):
    for row in range(len(array)):
        if 3 in array[row]:
            return row
# ====================Find column of enemy===========================
def findColOfEnemy(array):
    for row in range(len(array)):
        if 3 in array[row]:
            for col in range(len(array[row])):
                if array[row][col] == 3:
                    return col
# ==============Game Over==========================================
def LostGame():
    global isGameOver
    isGameOver = True
    canvas.create_text(660,300,text="Game Over!!",font=("",60),fill="red")
    LostGame()
Score = 0
# ================Game Vactory======================================
def WinGame():
    global isGameWin,Score,startMusic
    isGameWin = True
    canvas.create_text(660,300,text="You Win!!",font=("",60),fill="red")
    WinGame()
# ========================Display Scores=================================
def displayScore():
    global Score
    canvas.create_text(1200,200,text="Score",font=("",20),fill="black")
    myText=canvas.create_text(1300,200,text=Score,font=("",20),fill="red")
    if grid==2:
        Score+=1
        canvas.itemconfig(myText,text=Score)
    displayScore()
# ====================Move Right-===========================================
def moveRight(event):
    global isGameOver, isGameWin,Score,startMusic
    if isGameOver == False and isGameWin==False:
        Row1 = findRow(grid)
        Col1 = findCol(grid)
        canvas.delete("all")
        if Col1+1 < len(grid[Col1]) :
            if grid[Row1][Col1+1] ==0 and Score<5:
                startMusic=winsound .PlaySound("Sound\walk.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                grid[Row1][Col1] = 0
                grid[Row1][Col1+1] = 1
            elif grid[Row1][Col1+1] == 2 :
                startMusic=winsound .PlaySound("Sound\CatchDiamond.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                grid[Row1][Col1] = 0
                grid[Row1][Col1+1] = 1
                Score += 1
            elif grid[Row1][Col1+1] == 3 :
                startMusic=winsound .PlaySound("Sound\lost1.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                grid[Row1][Col1] = 0
                LostGame()
            elif grid[Row1][Col1+1] ==0 and Score==5:
                startMusic=winsound .PlaySound("Sound\winhoo.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                grid[Row1][Col1] = 0
                WinGame()             
        drawGrid()
# =================================move left-----------------------
def moveLeft(event):
    global Score,startMusic,isGameOver,isGameWin
    if isGameOver == False and isGameWin==False:
        Row1 = findRow(grid)
        Col1 = findCol(grid)
        canvas.delete("all")
        if Col1-1 > -1  :
            if grid[Row1][Col1-1] == 0 and Score<5:
                startMusic=winsound .PlaySound("Sound\walk.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                grid[Row1][Col1] = 0
                grid[Row1][Col1-1] = 1
            elif grid[Row1][Col1-1] == 2 :
                startMusic=winsound .PlaySound("Sound\CatchDiamond.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                grid[Row1][Col1] = 0
                grid[Row1][Col1-1] = 1
                Score += 1
            elif grid[Row1][Col1-1] == 3 :
                startMusic=winsound .PlaySound("Sound\lost1.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                grid[Row1][Col1] = 0
                grid[Row1][Col1-1] = 1
                LostGame()
            elif grid[Row1][Col1-1] == 0 and Score==5:
                startMusic=winsound .PlaySound("Sound\winhoo.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                grid[Row1][Col1] = 0
                WinGame()
        drawGrid()
# ===============================Move up------------------------------
def moveUp(event):
    global Score,startMusic,isGameOver
    if isGameOver == False and isGameWin==False:
        Row1 = findRow(grid)
        Col1 = findCol(grid)
        canvas.delete("all")
        if Row1-1 > -1 :
            if grid[Row1-1][Col1] == 0 and Score<5:
                startMusic=winsound .PlaySound("Sound\walk.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                grid[Row1][Col1] = 0
                grid[Row1-1][Col1] = 1
            elif grid[Row1-1][Col1] == 2 :
                startMusic=winsound .PlaySound("Sound\CatchDiamond.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                grid[Row1][Col1] = 0
                grid[Row1-1][Col1] = 1
                Score += 1
            elif grid[Row1-1][Col1] == 3:
                startMusic=winsound .PlaySound("Sound\lost1.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                grid[Row1][Col1] = 0
                grid[Row1-1][Col1] = 1
                LostGame()
            elif grid[Row1-1][Col1] == 0 and Score==5:
                startMusic=winsound .PlaySound("Sound\winhoo.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                grid[Row1][Col1] = 0
                WinGame()
        drawGrid()
# ==========================move Down----------------------------
def moveDown(event):
    global Score,startMusic,isGameOver,Row1
    if isGameOver == False and isGameWin==False:
        Row1 = findRow(grid)
        Col1 = findCol(grid)
        canvas.delete("all")
        if Row1+1 < len(grid[Row1]):
            if grid[Row1+1][Col1] == 0 and Score<5:
                startMusic=winsound .PlaySound("Sound\walk.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                grid[Row1][Col1] = 0
                grid[Row1+1][Col1] = 1
            elif grid[Row1+1][Col1] == 2 :
                startMusic=winsound .PlaySound("Sound\CatchDiamond.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                grid[Row1][Col1] = 0
                grid[Row1+1][Col1] = 1
                Score += 1
            elif grid[Row1+1][Col1] == 3 :
                startMusic=winsound .PlaySound("Sound\lost1.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                grid[Row1][Col1] = 0
                grid[Row1+1][Col1]=1
                LostGame()
            elif grid[Row1+1][Col1] == 0 and Score==5:
                startMusic=winsound .PlaySound("Sound\winhoo.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                grid[Row1][Col1] = 0
                WinGame()
        drawGrid()
# ==================Display=========================================
root.bind("<Down>", moveDown)
root.bind("<Up>", moveUp)
root.bind("<Left>", moveLeft)
root.bind('<Right>', moveRight)
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()