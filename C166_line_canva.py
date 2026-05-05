from tkinter import *

# Crear ventana
root = Tk()
root.title("Dibujar una línea")
root.geometry("600x600")

# Crear lienzo
canvas = Canvas(root, width=580, height=550, bg="white")
canvas.pack()

# Dibujar una línea automáticamente
canvas.create_line(50, 50, 300, 50, width=3, fill="black")

# Ejecutar ventana
root.mainloop()