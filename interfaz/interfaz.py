import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from interfaz import *

buscar_raza = []

#region Interfaz
class Interfaz:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.pantalla.title("Veterinaria")
        self.pantalla.geometry("1280x720")
        self.pantalla.protocol("WM_DELETE_WINDOW", self.pantalla.quit)
        
        # Cargar la imagen de fondo
        imagen = Image.open("TrabajoFinal/Trabajo_final_TPI/interfaz/imagenes/veterinaria fondo.jpg")
        imagen = imagen.resize((1280, 720), Image.LANCZOS)
        imagen_fondo = ImageTk.PhotoImage(imagen)
        
        # Crear un Label para mostrar la imagen de fondo
        label_imagen = tk.Label(self.pantalla, image=imagen_fondo)
        label_imagen.place(x=0, y=0, relwidth=1, relheight=1)
        label_imagen.image = imagen_fondo
    
        # Etiqueta del título
        labelpantalla_principal = tk.Label(self.pantalla, text="Veterinaria -nombre-", font=("Helvetica", 28), bg="white", fg="Black")
        labelpantalla_principal.place(relx=0.37, rely=0.15)
        # Etiqueta del usuario
        label_usuario = tk.Label(self.pantalla, text="Usuario", font=("Helvetica", 12), bg="white", fg="Black")
        label_usuario.place(relx=0.43, rely=0.35)
        # Etiqueta del contraseña
        label_contrasena = tk.Label(self.pantalla, text="Contraseña", font=("Helvetica", 12), bg="white", fg="Black")
        label_contrasena.place(relx=0.43, rely=0.45)
        
        # Crear un estilo personalizado para los botones y los entry
        estilo = ttk.Style()
        estilo.configure('TButton', background='orange', foreground='black', font=('Helvetica', 12, 'bold'))
        estilo.map('TButton', background=[('active', 'darkorange')], foreground=[('active', 'black')])
        
        # Estilo para Entry
        estilo.configure('TEntry', fieldbackground='lightgray', foreground='black', font=('Helvetica', 12))
        
        # Entry ingresos de usuario y contraseña
        entry_usuario = ttk.Entry(pantalla, style='TEntry', width=40)
        entry_usuario.place(relx=0.5, rely=0.40, anchor="center")  # Posición del Entry
        
        entry_contrasena = ttk.Entry(pantalla, show="*", style='TEntry', width=40)
        entry_contrasena.place(relx=0.5, rely=0.50, anchor="center")  # Posición del Entry
    
        # Botón de inicio
        boton_inicio = ttk.Button(self.pantalla, text="INEGRESAR", style='TButton', command=lambda: Menu(self.pantalla))
        boton_inicio.place(relx=0.5, rely=0.65, anchor="center")
        boton_inicio.config(padding=(10, 10))
    
        # Botón de salida
        boton_salir = ttk.Button(self.pantalla, text="SALIR", style='TButton', command=self.pantalla.quit)
        boton_salir.place(relx=0.5, rely=0.75, anchor="center")
        boton_salir.config(padding=(10, 10))
#endregion

#region menu
class Menu:
    def __init__(self, pantalla):
        pantalla.withdraw()
        
        self.menu = tk.Toplevel(pantalla)
        self.menu.title("Menu")
        self.menu.geometry("1280x720")
        self.menu.config(bg="white")
        self.menu.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_todo(pantalla))

        # Cargar la imagen de fondo
        self.imagen = Image.open("TrabajoFinal/Trabajo_final_TPI/interfaz/imagenes/fondo menu.png")
        self.imagen = self.imagen.resize((1280, 720), Image.LANCZOS)
        self.imagen_fondo = ImageTk.PhotoImage(self.imagen)
        
        # Crear un Label para mostrar la imagen de fondo
        self.label_imagen = tk.Label(self.menu, image=self.imagen_fondo)
        self.label_imagen.place(x=0, y=0, relwidth=1, relheight=1)
        self.label_imagen.image = self.imagen_fondo
        
        # Boton volver
        self.botonVolver = ttk.Button(self.menu, text="Volver", command=lambda: self.cerrar_pantalla(pantalla, self.menu))
        self.botonVolver.place(relx=0.5, rely=0.7, anchor="center")
        self.botonVolver.config(padding=(10, 10))
        
        # Boton consulta
        self.botonConsulta = ttk.Button(self.menu, text="CONSULTA", command=self.abrir_consulta)
        self.botonConsulta.place(relx=0.3, rely=0.5, anchor="center")
        self.botonConsulta.config(padding=(10, 10))
        
        # Boton Mascota
        self.botonMascota = ttk.Button(self.menu, text="MASCOTAS", command=self.abrir_mascotas)
        self.botonMascota.place(relx=0.5, rely=0.5, anchor="center")
        self.botonMascota.config(padding=(10, 10))
        
        # Boton cliente 
        self.botonCliente = ttk.Button(self.menu, text="CLIENTE", command=self.abrir_cliente)
        self.botonCliente.place(relx=0.7, rely=0.5, anchor="center")
        self.botonCliente.config(padding=(10, 10))
        
    def cerrar_todo(self, pantalla):
        self.menu.destroy()
        pantalla.destroy()

    def cerrar_pantalla(self, pantalla, ventana):
        ventana.destroy()
        pantalla.deiconify()
    
    def abrir_consulta(self):
        self.menu.withdraw()
        Consulta(self.menu)
    
    def abrir_mascotas(self):
        self.menu.withdraw()
        Mascotas(self.menu)
    
    def abrir_cliente(self):
        self.menu.withdraw()
        Cliente(self.menu)
#endregion

#region Consulta
class Consulta:
    def __init__(self, pantalla):
        
        self.consulta = tk.Toplevel(pantalla)
        self.consulta.title("Consulta")
        self.consulta.geometry("1280x720")
        self.consulta.config(bg="white")
        self.consulta.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_pantalla(pantalla, self.consulta))
        
        self.label = tk.Label(self.consulta, text="prueba", font=("Helvetica", 12), bg="white", fg="Black")
        self.label.place(relx=0.10, rely=0.10)
        
        entry = ttk.Entry(self.consulta, style='TEntry', width=40)
        entry.place(relx=0.5, rely=0.40, anchor="center")  # Posición del Entry
        
        listacomboBox = ttk.Combobox(self.consulta, values=buscar_raza, state="readonly")
        try:
            listacomboBox.set(buscar_raza[0])
        except:
            listacomboBox.set("No encontrado")
            listacomboBox.bind("<<ComboboxSelected>>")
            listacomboBox.place(relx=0.5, rely=0.40)
        
        # boton volver
        self.botonVolver = ttk.Button(self.consulta, text="Volver", command=lambda: self.cerrar_pantalla(pantalla, self.consulta))
        self.botonVolver.place(relx=0.5, rely=0.7, anchor="center")
        self.botonVolver.config(padding=(10, 10))
        
    def cerrar_pantalla(self, pantalla, ventana):
        ventana.destroy()
        pantalla.deiconify()
        
#endregion

#region Mascotas
class Mascotas:
    def __init__(self, pantalla):
        self.mascotas = tk.Toplevel(pantalla)
        self.mascotas.title("Mascotas")
        self.mascotas.geometry("1280x720")
        self.mascotas.config(bg="white")
        self.mascotas.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_pantalla(pantalla, self.mascotas))
        
        # Añadir widgets para la pantalla de mascotas aquí
        
        self.botonVolver = ttk.Button(self.mascotas, text="Volver", command=lambda: self.cerrar_pantalla(pantalla, self.mascotas))
        self.botonVolver.place(relx=0.5, rely=0.7, anchor="center")
        self.botonVolver.config(padding=(10, 10))
        
    def cerrar_pantalla(self, pantalla, ventana):
        ventana.destroy()
        pantalla.deiconify()
#endregion
        
#region CCliente
class Cliente:
    def __init__(self, pantalla):
        self.cliente = tk.Toplevel(pantalla)
        self.cliente.title("Cliente")
        self.cliente.geometry("1280x720")
        self.cliente.config(bg="white")
        self.cliente.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_pantalla(pantalla, self.cliente))
        
        # Añadir widgets para la pantalla de cliente aquí
        
        self.botonVolver = ttk.Button(self.cliente, text="Volver", command=lambda: self.cerrar_pantalla(pantalla, self.cliente))
        self.botonVolver.place(relx=0.5, rely=0.7, anchor="center")
        self.botonVolver.config(padding=(10, 10))
        
    def cerrar_pantalla(self, pantalla, ventana):
        ventana.destroy()
        pantalla.deiconify()
#endregion

#region main
if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()
#endregion

