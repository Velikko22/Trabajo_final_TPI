import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os

class MenuMascotas:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.mascotas = tk.Toplevel(pantalla)
        self.mascotas.title("Mascotas")
        self.mascotas.geometry("800x500")
        self.mascotas.config(bg="white")
        self.mascotas.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_pantalla(pantalla, self.mascotas))

        self.mascotas_file = "TrabajoFinal/Trabajo_final_TPI/interfaz/archivos/mascotas.txt"
        self.lista_mascotas = self.cargar_mascotas()
        
        self.lista_de_mascotas()

        self.botonVolver = ttk.Button(self.mascotas, text="Volver", command=lambda: self.cerrar_pantalla(pantalla, self.mascotas))
        self.botonVolver.place(relx=0.5, rely=0.9, anchor="center")
        self.botonVolver.config(padding=(10, 10))

    def cargar_mascotas(self):
        if os.path.exists(self.mascotas_file):
            with open(self.mascotas_file, "r") as file:
                return [line.strip() for line in file.readlines()]
        return []

    def guardar_mascotas(self):
        with open(self.mascotas_file, "w") as file:
            for mascota in self.lista_mascotas:
                file.write(f"{mascota}\n")

    def lista_de_mascotas(self):
        label_lista = tk.Label(self.mascotas, text="Lista de Mascotas:", font=("Helvetica", 12), bg="white", fg="Black")
        label_lista.place(relx=0.5, rely=0.1, anchor="center")
        
        self.listbox_mascotas = tk.Listbox(self.mascotas)
        self.listbox_mascotas.place(relx=0.5, rely=0.3, anchor="center")
        for mascota in self.lista_mascotas:
            self.listbox_mascotas.insert(tk.END, mascota)
        
        label_nueva_mascota = tk.Label(self.mascotas, text="Agregar nueva mascota:", font=("Helvetica", 12), bg="white", fg="Black")
        label_nueva_mascota.place(relx=0.5, rely=0.6, anchor="center")
        
        self.entry_nueva_mascota = ttk.Entry(self.mascotas, style='TEntry', width=40)
        self.entry_nueva_mascota.place(relx=0.5, rely=0.65, anchor="center")
        
        self.boton_agregar_mascota = ttk.Button(self.mascotas, text="Agregar", command=self.agregar_mascota)
        self.boton_agregar_mascota.place(relx=0.4, rely=0.75, anchor="center")
        self.boton_agregar_mascota.config(padding=(10, 10))

        self.boton_eliminar_mascota = ttk.Button(self.mascotas, text="Eliminar", command=self.eliminar_mascota)
        self.boton_eliminar_mascota.place(relx=0.6, rely=0.75, anchor="center")
        self.boton_eliminar_mascota.config(padding=(10, 10))

    def agregar_mascota(self):
        nueva_mascota = self.entry_nueva_mascota.get()
        if nueva_mascota and nueva_mascota not in self.lista_mascotas:
            self.lista_mascotas.append(nueva_mascota)
            self.listbox_mascotas.insert(tk.END, nueva_mascota)
            self.entry_nueva_mascota.delete(0, tk.END)
            self.guardar_mascotas()
        else:
            messagebox.showinfo("Error", "La mascota ya existe o el nombre está vacío")
    
    def eliminar_mascota(self):
        seleccion = self.listbox_mascotas.curselection()
        if seleccion:
            mascota = self.listbox_mascotas.get(seleccion)
            self.lista_mascotas.remove(mascota)
            self.listbox_mascotas.delete(seleccion)
            self.guardar_mascotas()
        else:
            messagebox.showinfo("Error", "Seleccione una mascota para eliminar")

    def cerrar_pantalla(self, pantalla, ventana):
        ventana.destroy()
        pantalla.deiconify()
