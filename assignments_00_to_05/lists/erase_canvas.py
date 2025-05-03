import tkinter as tk


cell_width = 40
cell_height = 40
Rows = 8
Cols = 8

def create_grid(canvas):
    cell = []
    for i in range(Rows):
        row = []
        for j in range(Cols):
            x1 = j * cell_width
            y1 = i * cell_height
            x2 = x1 + cell_width 
            y2 = y1 + cell_height
            cell_id = canvas.create_rectangle(x1,y1,x2,y2, fill="blue", outline="black")
            row.append(cell_id)
        cell.append(row)
    return cell


def canvas_click(event, canvas, cell):
    col = event.x // cell_width
    row = event.y // cell_height

    if 0 <= row < Rows and 0 <= col < Cols:
        canvas.itemconfig(cell[row][col], fill="white", outline="white")

def main():
    root = tk.Tk()
    root.title("Erase Canvas Grid")

    canvas_width = cell_width * Cols
    canvas_height = cell_height * Rows

    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    cell = create_grid(canvas)

    canvas.bind("<Button-1>", lambda event: canvas_click(event, canvas, cell))

    root.mainloop()




if __name__ == "__main__":
    main()


        



