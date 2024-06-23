import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from menuprincipal import Menuprincipal

class Interfaz:
    
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.pantalla.title("Veterinaria")
        self.pantalla.geometry("1280x720")
        self.pantalla.protocol("WM_DELETE_WINDOW", self.pantalla.quit)

    def cargarFondo(self):
        imagen = Image.open("TrabajoFinal/Trabajo_final_TPI/interfaz/imagenes/veterinaria fondo.jpg")
        imagen = imagen.resize((1280, 720), Image.LANCZOS)
        imagen_fondo = ImageTk.PhotoImage(imagen)
        label_imagen = tk.Label(self.pantalla, image=imagen_fondo)
        label_imagen.place(x=0, y=0, relwidth=1, relheight=1)
        label_imagen.image = imagen_fondo

    def labelTitulos(self):
        labelpantalla_principal = tk.Label(self.pantalla, text="REGIMASCOTAS", font=("Helvetica", 28), bg="white", fg="Black")
        labelpantalla_principal.place(relx=0.37, rely=0.10)
        label_usuario = tk.Label(self.pantalla, text="Usuario", font=("Helvetica", 14), bg="white", fg="Black")
        label_usuario.place(relx=0.40, rely=0.33)
        label_contrasena = tk.Label(self.pantalla, text="Contraseña", font=("Helvetica", 14), bg="white", fg="Black")
        label_contrasena.place(relx=0.40, rely=0.43)
        
    def estilo(self):
        estilo = ttk.Style()
        estilo.configure('TButton', background='orange', foreground='black', font=('Helvetica', 12, 'bold'))
        estilo.map('TButton', background=[('active', 'darkorange')], foreground=[('active', 'black')])
        estilo.configure('TEntry', fieldbackground='lightgray', foreground='black', font=('Helvetica', 12))
        
    def entryMenu(self):
        entry_usuario = ttk.Entry(self.pantalla, style='TEntry', width=40)
        entry_usuario.place(relx=0.5, rely=0.40, anchor="center")
        entry_contrasena = ttk.Entry(self.pantalla, show="*", style='TEntry', width=40)
        entry_contrasena.place(relx=0.5, rely=0.50, anchor="center")
    
    def botonesPrincipales(self):
        boton_inicio = ttk.Button(self.pantalla, text="INGRESAR", style='TButton', command=lambda: Menuprincipal(self.pantalla))
        boton_inicio.place(relx=0.5, rely=0.65, anchor="center")
        boton_inicio.config(padding=(10, 10))
        boton_salir = ttk.Button(self.pantalla, text="SALIR", style='TButton', command=self.pantalla.quit)
        boton_salir.place(relx=0.5, rely=0.75, anchor="center")
        boton_salir.config(padding=(10, 10))

if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    app.cargarFondo()
    app.labelTitulos()
    app.entryMenu()
    app.botonesPrincipales()
    root.mainloop()
