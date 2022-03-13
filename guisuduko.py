from tkinter import *
from suduko23 import solver23
root = Tk()
root.title("Sudoku Solver")
root.geometry("549x490")

label = Label(root, text="Fill in the numbers and click solve the Sudoku",fg="blue").grid(
    row=0, column=1, columnspan=10)

errLabel = Label(root, text="")

errLabel.grid(row=15, column=1, columnspan=10, pady=5)

solvedLabel = Label(root, text="")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)
cells = {}


def ValidateNumber(P):
    out = (P.isdigit() or P == "") and len(P) < 2  # =
    return out


reg = root.register(ValidateNumber)


def draw3x3Grid(row, column, bgcolor):
    for i in range(1):
        for j in range(1):
            e = Entry(root, width=5, bg=bgcolor, justify="center",
                      validate="key", validatecommand=(reg, "%P"),fg="orange",font="bold")
            e.grid(row=row+i+1, column=column+j+1,
                   sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(row+i+1, column+j+1)] = e


def draw9x9Grid():
    color = "black"
    for rowNo in range(1, 10, 1):
        for colNo in range(0, 9, 1):
            draw3x3Grid(rowNo, colNo, color)
            if color == "black":
                color = "white"
            else:
                color = "black"


def clearValues():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2, 11):
        for col in range(1, 10):
            cell = cells[(row, col)]
            cell.delete(0, "end")


def getValues():
    board = []
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2, 11):
        rows = []
        for col in range(1, 10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateValues(board)


btn = Button(root, command=getValues, text="Solve", width=10,bg="purple" ,foreground="yellow",font="bold")
btn.grid(row=20, column=1, columnspan=5, pady=20)

btn = Button(root, command=clearValues, text="Clear", width=10,bg="purple",foreground="yellow",font="bold")
btn.grid(row=20, column=5, columnspan=5, pady=20)


def updateValues(s):
    sol=solver23(s)
    if(sol !="no"):
        for rows in range(2,11):
            for col in range(1,10):
                cells[(rows,col)].delete(0,"end")
                cells[(rows,col)].insert(0,sol[rows-2][col-1])
        solvedLabel.configure(text="Suduko solved")
    else:
        errLabel.configure(text="No solution exists for this suduko")
        
draw9x9Grid()

root.mainloop()
