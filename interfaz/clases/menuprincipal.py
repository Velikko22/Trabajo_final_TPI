import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from menucliente import MenuCliente
from menuconsulta import MenuConsulta
from menumascotas import MenuMascotas

class Menuprincipal:
    def __init__(self, pantalla):
        
        pantalla.withdraw()
        self.menu = tk.Toplevel(pantalla)
        self.menu.title("Menu")
        self.menu.geometry("1280x720")
        self.menu.config(bg="white")
        self.menu.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_todo(pantalla))
        self.cargarFondo()

        labelpantalla_principal = tk.Label(self.menu, text="REGIMASCOTAS", font=("Helvetica", 28), bg="white", fg="Black")
        labelpantalla_principal.place(relx=0.37, rely=0.25)
        
        self.botonVolver = ttk.Button(self.menu, text="Volver", command=lambda: self.cerrar_pantalla(pantalla, self.menu))
        self.botonVolver.place(relx=0.5, rely=0.7, anchor="center")
        self.botonVolver.config(padding=(10, 10))
        
        self.botonConsulta = ttk.Button(self.menu, text="CONSULTA", command=self.abrir_consulta)
        self.botonConsulta.place(relx=0.35, rely=0.5, anchor="center")
        self.botonConsulta.config(padding=(10, 10))
        
        self.botonMascota = ttk.Button(self.menu, text="MASCOTAS", command=self.abrir_mascotas)
        self.botonMascota.place(relx=0.5, rely=0.5, anchor="center")
        self.botonMascota.config(padding=(10, 10))
        
        self.botonCliente = ttk.Button(self.menu, text="CLIENTE", command=self.abrir_cliente)
        self.botonCliente.place(relx=0.65, rely=0.5, anchor="center")
        self.botonCliente.config(padding=(10, 10))
        
    def cargarFondo(self):
        imagen = Image.open("TrabajoFinal/Trabajo_final_TPI/interfaz/imagenes/fondo menu.png")
        imagen = imagen.resize((1280, 720), Image.LANCZOS)
        imagen_fondo = ImageTk.PhotoImage(imagen)
        label_imagen = tk.Label(self.menu, image=imagen_fondo)
        label_imagen.place(x=0, y=0, relwidth=1, relheight=1)
        label_imagen.image = imagen_fondo

    def cerrar_todo(self, pantalla):
        self.menu.destroy()
        pantalla.destroy()

    def cerrar_pantalla(self, pantalla, ventana):
        ventana.destroy()
        pantalla.deiconify()
    
    def abrir_consulta(self):
        self.menu.withdraw()
        MenuConsulta(self.menu)
    
    def abrir_mascotas(self):
        self.menu.withdraw()
        MenuMascotas(self.menu)
    
    def abrir_cliente(self):
        self.menu.withdraw()
        MenuCliente(self.menu)
