import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class MenuCliente:
    def __init__(self, pantalla):
        self.cliente = tk.Toplevel(pantalla)
        self.cliente.title("Cliente")
        self.cliente.geometry("800x500")
        self.cliente.config(bg="white")
        self.cliente.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_pantalla(pantalla, self.cliente))
        
        self.botonVolver = ttk.Button(self.cliente, text="Volver", command=lambda: self.cerrar_pantalla(pantalla, self.cliente))
        self.botonVolver.place(relx=0.5, rely=0.7, anchor="center")
        self.botonVolver.config(padding=(10, 10))
        
    def cerrar_pantalla(self, pantalla, ventana):
        ventana.destroy()
        pantalla.deiconify()
