import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class MenuConsulta:
    def __init__(self, pantalla):
        self.consulta = tk.Toplevel(pantalla)
        self.consulta.title("Consulta")
        self.consulta.geometry("1280x720")
        self.consulta.config(bg="white")
        self.consulta.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_pantalla(pantalla, self.consulta))
        self.cargarFondo()
        
        # Titulo
        self.label = tk.Label(self.consulta, text="CONSULTAS", font=("Helvetica", 24), bg="white", fg="Black")
        self.label.place(relx=0.5, rely=0.15, anchor="center")
        
        # Indicacion de entradas
        self.label = tk.Label(self.consulta, text="Escriba nombre de la mascota para acceder al historial.", font=("Helvetica", 14), bg="white", fg="Black")
        self.label.place(relx=0.30, rely=0.25)
        
        # Entrada de nombre de mascota
        self.entry = ttk.Entry(self.consulta, style='TEntry', width=40)
        self.entry.place(relx=0.4, rely=0.35, anchor="center")
        
        # Botón buscar (no tocar)
        self.botonBuscar = ttk.Button(self.consulta, text="Buscar", command=self.buscar_mascota)
        self.botonBuscar.place(relx=0.7, rely=0.35, anchor="center")
        self.botonBuscar.config(padding=(10, 10))

        # Cuadro de texto para mostrar la información de la mascota
        self.textoInfo = tk.Text(self.consulta, width=75, height=15, bg="white")
        self.textoInfo.place(relx=0.53, rely=0.6, anchor="center")
        
        # Botón volver
        self.botonVolver = ttk.Button(self.consulta, text="Volver", command=lambda: self.cerrar_pantalla(pantalla, self.consulta))
        self.botonVolver.place(relx=0.95, rely=0.90, anchor="center")
        self.botonVolver.config(padding=(10, 10))
        
    def cargarFondo(self):
        imagen = Image.open("TrabajoFinal/Trabajo_final_TPI/interfaz/imagenes/fondo menu.png")
        imagen = imagen.resize((1280, 720), Image.LANCZOS)
        imagen_fondo = ImageTk.PhotoImage(imagen)
        label_imagen = tk.Label(self.consulta, image=imagen_fondo)
        label_imagen.place(x=0, y=0, relwidth=1, relheight=1)
        label_imagen.image = imagen_fondo

    def cerrar_pantalla(self, pantalla, ventana):
        ventana.destroy()
        pantalla.deiconify()

    def buscar_mascota(self):
        nombre_mascota = self.entry.get()
        informacion = self.obtener_informacion_mascota(nombre_mascota)
        self.textoInfo.delete("1.0", tk.END)
        self.textoInfo.insert(tk.END, informacion)
    
    def obtener_informacion_mascota(self, nombre):
        # Aquí deberías buscar la información de la mascota en tu base de datos o estructura de datos.
        # Este es un ejemplo sencillo que devuelve información ficticia.
        datos_mascotas = {
            "Fido": "Nombre: Fido\nTipo: Perro\nEdad: 5 años\nDueño: Juan Perez",
            "Whiskers": "Nombre: Whiskers\nTipo: Gato\nEdad: 3 años\nDueño: Ana Garcia"
        }
        return datos_mascotas.get(nombre, "Mascota no encontrada")
