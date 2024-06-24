#region Import
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk
#endregion

#region Login
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1280x720")
        self.root.config(bg="white")
        self.cargarFondo()
        
        buttunFont = ("Helvetica", 14)
        
        # Titulo veterinaria
        self.label_Title = tk.Label(root, text="REGISMASCOTAS", font=("helvetica", 20), bg="white")
        self.label_Title.place(relx=0.5 ,rely=0.2, anchor="center")
        
        # Usuario
        self.label_user = tk.Label(root, text="Usuario:", font=("Helvetica", 14), bg="white")
        self.label_user.place(relx=0.44, rely=0.4, anchor="center")
        
        self.entry_user = ttk.Entry(root, font=("Helvetica", 14))
        self.entry_user.place(relx=0.5, rely=0.45, anchor="center")

        # Contraseña
        self.label_pass = tk.Label(root, text="Contraseña:", font=("Helvetica", 14), bg="white")
        self.label_pass.place(relx=0.455, rely=0.55, anchor="center")
        
        self.entry_pass = ttk.Entry(root, font=("Helvetica", 14), show="*")
        self.entry_pass.place(relx=0.5, rely=0.6, anchor="center")

        # boton ingresar
        self.button_login = ttk.Button(root, text="Ingresar", command=self.verificar_login)
        self.button_login.place(relx=0.5, rely=0.7, anchor="center")
        self.button_login.config(padding=(10, 10), width=35)

    def cargarFondo(self):
        imagen = Image.open("TrabajoFinal/Trabajo_final_TPI/interfaz/imagenes/fondoLoing.jpg")
        imagen = imagen.resize((1280, 720), Image.LANCZOS)
        imagen_fondo = ImageTk.PhotoImage(imagen)
        label_imagen = tk.Label(self.root, image=imagen_fondo)
        label_imagen.place(x=0, y=0, relwidth=1, relheight=1)
        label_imagen.image = imagen_fondo
    
    def verificar_login(self):
        usuario = self.entry_user.get()
        contrasena = self.entry_pass.get()
        if usuario == "admin" and contrasena == "admin":
            self.root.withdraw()
            Menuprincipal(self.root)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
#endregion

#region Menú principal
class Menuprincipal:
    
    def __init__(self, pantalla):
        pantalla.withdraw()
        self.menu = tk.Toplevel(pantalla)
        self.menu.title("Menu")
        self.menu.geometry("1280x720")
        self.menu.config(bg="white")
        self.menu.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_todo(pantalla))
        self.cargarFondo()

        # Titulo
        labelpantalla_principal = tk.Label(self.menu, text="REGIMASCOTAS", font=("helvetica",24), bg="white", fg="Black")
        labelpantalla_principal.place(relx=0.39, rely=0.30)

        # Boton Salir / Volver
        self.botonVolver = ttk.Button(self.menu, text="SALIR", command=self.cerrar_pantalla)
        self.botonVolver.place(relx=0.5, rely=0.7, anchor="center")
        self.botonVolver.config(padding=(10, 10), width=25)

        # Boton Consulta
        self.botonConsulta = ttk.Button(self.menu, text="CONSULTA", command=self.abrir_consulta)
        self.botonConsulta.place(relx=0.35, rely=0.5, anchor="center")
        self.botonConsulta.config(padding=(10, 10), width=25)

        # Boton Mascotas
        self.botonMascota = ttk.Button(self.menu, text="MASCOTAS",command=self.abrir_mascotas)
        self.botonMascota.place(relx=0.5, rely=0.5, anchor="center")
        self.botonMascota.config(padding=(10, 10), width=25)

        # Boton Clientes
        self.botonCliente = ttk.Button(self.menu, text="CLIENTE",command=self.abrir_cliente)
        self.botonCliente.place(relx=0.65, rely=0.5, anchor="center")
        self.botonCliente.config(padding=(10, 10), width=25)


    def cargarFondo(self):
        imagen = Image.open("TrabajoFinal/Trabajo_final_TPI/interfaz/imagenes/fondoLoing.jpg")
        imagen = imagen.resize((1280, 720), Image.LANCZOS)
        imagen_fondo = ImageTk.PhotoImage(imagen)
        label_imagen = tk.Label(self.menu, image=imagen_fondo)
        label_imagen.place(x=0, y=0, relwidth=1, relheight=1)
        label_imagen.image = imagen_fondo

    def cerrar_todo(self, pantalla):
        self.menu.destroy()
        pantalla.destroy()

    def cerrar_pantalla(self):
        self.menu.destroy()

    def abrir_consulta(self):
        self.menu.withdraw()
        MenuConsulta(self.menu)

    def abrir_mascotas(self):
        self.menu.withdraw()
        MenuMascotas(self.menu)

    def abrir_cliente(self):
        self.menu.withdraw()
        MenuCliente(self.menu)
#endregion

#region Menú Consulta
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
        
        # Titulo "Ingreso nombre de propietario + entry correspondiente"
        self.label = tk.Label(self.consulta, text="Escriba nombre de propietario/a.", font=("Helvetica", 14), bg="white", fg="Black")
        self.label.place(relx=0.225, rely=0.30)

        self.entry = ttk.Entry(self.consulta, style='TEntry', width=40, font=("Helvetica", 14))
        self.entry.place(relx=0.4, rely=0.37, anchor="center")
        
        # Titulo "Ingreso nombre de mascota + entry correspondiente"
        self.label = tk.Label(self.consulta, text="Escriba nombre de la mascota.", font=("Helvetica", 14), bg="white", fg="Black")
        self.label.place(relx=0.225, rely=0.42)

        self.entry = ttk.Entry(self.consulta, style='TEntry', width=40, font=("Helvetica", 14))
        self.entry.place(relx=0.4, rely=0.49, anchor="center")
        
        # Boton buscar
        self.botonBuscar = ttk.Button(self.consulta, text="Buscar", command=self.buscar_mascota)
        self.botonBuscar.place(relx=0.68, rely=0.43, anchor="center")
        self.botonBuscar.config(padding=(10, 10),width=25)

        # Boton Volver al menu principal
        self.botonVolver = ttk.Button(self.consulta, text="Volver", command=lambda: self.cerrar_pantalla(pantalla, self.consulta))
        self.botonVolver.place(relx=0.9, rely=0.9, anchor="center")
        self.botonVolver.config(padding=(10, 10),width=25)

        # Cuadro resultado de busqueda
        self.textoInfo = tk.Text(self.consulta, width=85, height=15, bg="white")
        self.textoInfo.place(relx=0.493, rely=0.7, anchor="center")

        
    def cargarFondo(self):
        imagen = Image.open("TrabajoFinal/Trabajo_final_TPI/interfaz/imagenes/fondoLoing.jpg")
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
        datos_mascotas = {
        }
        return datos_mascotas.get(nombre, "Mascota no encontrada")
#endregion

#region Menú Mascotas
class MenuMascotas:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        pantalla.withdraw()
        self.mascotas = tk.Toplevel(pantalla)
        self.mascotas.title("Gestor de Mascotas")
        self.mascotas.geometry("1280x720")
        self.mascotas.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_pantalla(pantalla))
        self.cargarFondo()
        
        label_font = ("Helvetica", 14)
        entry_font = ("Helvetica", 14)
        button_font = ("Helvetica", 14)

        # Frame para los datos de la mascota
        datos_frame = tk.Frame(self.mascotas, pady=20)
        datos_frame.pack(padx=10, pady=(50, 20))

        # Titulo para el cuadro de datos
        tk.Label(datos_frame, text="Ingreso de Datos de la Mascota", font=("Helvetica", 18)).grid(row=0, columnspan=2, pady=10)

        # Ingreso del nombre del animal
        tk.Label(datos_frame, text="Nombre:", font=label_font).grid(row=1, column=0)
        self.name_entry = tk.Entry(datos_frame, font=entry_font, width=30)
        self.name_entry.grid(row=1, column=1, pady=5)

        # Ingreso de edad del animal
        tk.Label(datos_frame, text="Edad:", font=label_font).grid(row=2, column=0)
        self.age_entry = tk.Entry(datos_frame, font=entry_font, width=30)
        self.age_entry.grid(row=2, column=1, pady=5)

        # Ingreso del peso del animal
        tk.Label(datos_frame, text="Peso:", font=label_font).grid(row=3, column=0)
        self.weight_entry = tk.Entry(datos_frame, font=entry_font, width=30)
        self.weight_entry.grid(row=3, column=1, pady=5)

        # Ingreso de altura del animal
        tk.Label(datos_frame, text="Altura:", font=label_font).grid(row=4, column=0)
        self.height_entry = tk.Entry(datos_frame, font=entry_font, width=30)
        self.height_entry.grid(row=4, column=1, pady=5)

        # Ventana de selección del tipo de animal
        tk.Label(datos_frame, text="Tipo:", font=label_font).grid(row=1, column=2)
        self.pet_type_var = tk.StringVar()
        self.pet_type_combo = ttk.Combobox(datos_frame, textvariable=self.pet_type_var, font=entry_font, width=27)
        self.pet_type_combo['values'] = ("Perro", "Gato")
        self.pet_type_combo.grid(row=1, column=3)
        self.pet_type_combo.bind("<<ComboboxSelected>>", self.eleccion_de_razas)

        # Ventana de selección de raza del animal
        tk.Label(datos_frame, text="Raza:", font=label_font).grid(row=2, column=2)
        self.breed_var = tk.StringVar()
        self.breed_combo = ttk.Combobox(datos_frame, textvariable=self.breed_var, font=entry_font, width=27)
        self.breed_combo.grid(row=2, column=3)

        # Ventana de las opciones para vacunación
        tk.Label(datos_frame, text="Vacunación:", font=label_font).grid(row=3, column=2)
        self.vaccination_status_var = tk.StringVar()
        self.vaccination_status_combo = ttk.Combobox(datos_frame, textvariable=self.vaccination_status_var, font=entry_font, width=27)
        self.vaccination_status_combo['values'] = ["Al Día", "Vencida", "Falta vacunar", "Sin vacunaciones"]
        self.vaccination_status_combo.grid(row=3, column=3)

        # Boton agregar mascota
        self.button_agregar_mascotas = tk.Button(self.mascotas, text="Agregar Mascota", font=button_font, command=self.agregarMascota)
        self.button_agregar_mascotas.place(relx=0.5, rely=0.45, anchor="center")
        self.button_agregar_mascotas.config(width=25)

        # Frame para la lista de mascotas agregadas
        self.pet_list_frame = tk.Frame(self.mascotas)
        self.pet_list_frame.pack(padx=10, pady=55, fill=tk.BOTH)

        # Cuadro de previsualización de la información que se agregó al sistema
        self.pet_list = tk.Listbox(self.pet_list_frame, font=entry_font, width=113, height=11)
        self.pet_list.pack(side=tk.LEFT, fill=tk.BOTH)
        
        # Scrollbar para la lista de mascotas
        scrollbar = tk.Scrollbar(self.pet_list_frame, orient=tk.VERTICAL, command=self.pet_list.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.pet_list.config(yscrollcommand=scrollbar.set)

        # Boton volver
        self.button_Volver = tk.Button(self.mascotas, text="Volver", font=button_font, command=lambda: self.cerrar_pantalla(pantalla))
        self.button_Volver.place(relx=0.8, rely=0.9, anchor="center")
        self.button_Volver.config(width=25)

    def cargarFondo(self):
        imagen = Image.open("TrabajoFinal/Trabajo_final_TPI/interfaz/imagenes/fondoLoing.jpg")
        imagen = imagen.resize((1280, 720), Image.LANCZOS)
        imagen_fondo = ImageTk.PhotoImage(imagen)
        label_imagen = tk.Label(self.mascotas, image=imagen_fondo)
        label_imagen.place(x=0, y=0, relwidth=1, relheight=1)
        label_imagen.image = imagen_fondo

    def eleccion_de_razas(self, event):
        pet_type = self.pet_type_var.get()
        breeds = {"Perro": ["Labrador", "Bulldog", "Beagle"], "Gato": ["Persa", "Siamés", "Bengalí"]}
        self.breed_combo['values'] = breeds.get(pet_type, [])

    def agregarMascota(self):
        pet_name = self.name_entry.get()
        pet_age = self.age_entry.get()
        pet_weight = self.weight_entry.get()
        pet_height = self.height_entry.get()
        pet_type = self.pet_type_var.get()
        pet_breed = self.breed_var.get()
        vaccination_status = self.vaccination_status_var.get()

        if pet_name and pet_age and pet_weight and pet_height and pet_type and pet_breed and vaccination_status:
            datos_animal = f"Nombre: {pet_name} | Edad: {pet_age} | Peso: {pet_weight} | Altura: {pet_height} | Tipo: {pet_type} | Raza: {pet_breed} | Vacunación: {vaccination_status}"
            self.pet_list.insert(tk.END,datos_animal)

            self.name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
            self.weight_entry.delete(0, tk.END)
            self.height_entry.delete(0, tk.END)
            self.pet_type_combo.set('')
            self.breed_combo.set('')
            self.vaccination_status_combo.set('')
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
        
        return datos_animal

    def getagregarAnimal(self,datos_animal):
        return self.pet_list(datos_animal)

    def cerrar_pantalla(self, pantalla):
        self.mascotas.destroy()
        pantalla.deiconify()
        
#endregion

#region Menú Cliente
class MenuCliente:
    def __init__(self, pantalla):
        pantalla.withdraw()
        self.cliente = tk.Toplevel(pantalla)
        self.cliente.title("Gestor de Clientes")
        self.cliente.geometry("1280x720")
        self.cliente.protocol("WM_DELETE_WINDOW", lambda: self.cerrar_pantalla(pantalla))
        self.cargarFondo()
        
        label_font = ("Helvetica", 14)
        entry_font = ("Helvetica", 14)
        button_font = ("Helvetica", 14)

        self.client_data_frame = tk.Frame(self.cliente)
        self.client_data_frame.pack(padx=10, pady=10)

        tk.Label(self.client_data_frame, text="Nombre:", font=label_font).grid(row=0, column=0)
        self.name_entry = tk.Entry(self.client_data_frame, font=entry_font, width=30)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.client_data_frame, text="Apellido:", font=label_font).grid(row=1, column=0)
        self.surname_entry = tk.Entry(self.client_data_frame, font=entry_font, width=30)
        self.surname_entry.grid(row=1, column=1)

        tk.Label(self.client_data_frame, text="Teléfono:", font=label_font).grid(row=2, column=0)
        self.phone_entry = tk.Entry(self.client_data_frame, font=entry_font, width=30)
        self.phone_entry.grid(row=2, column=1)

        tk.Label(self.client_data_frame, text="Dirección:", font=label_font).grid(row=3, column=0)
        self.address_entry = tk.Entry(self.client_data_frame, font=entry_font, width=30)
        self.address_entry.grid(row=3, column=1)

        self.add_client_button = tk.Button(self.cliente, text="Agregar Cliente", font=button_font, command=self.agregarCliente)
        self.add_client_button.pack(padx=10, pady=10)

        self.client_list_frame = tk.Frame(self.cliente)
        self.client_list_frame.pack(padx=10, pady=10)

        self.client_list = tk.Listbox(self.client_list_frame, font=entry_font, width=100, height=10)
        self.client_list.pack(padx=10, pady=10)

        self.cargaListaClientes()

        self.back_button = tk.Button(self.cliente, text="Volver", font=button_font, command=lambda: self.cerrar_pantalla(pantalla))
        self.back_button.pack(pady=10)

    def cargarFondo(self):
        imagen = Image.open("TrabajoFinal/Trabajo_final_TPI/interfaz/imagenes/fondoLoing.jpg")
        imagen = imagen.resize((1280, 720), Image.LANCZOS)
        imagen_fondo = ImageTk.PhotoImage(imagen)
        label_imagen = tk.Label(self.cliente, image=imagen_fondo)
        label_imagen.place(x=0, y=0, relwidth=1, relheight=1)
        label_imagen.image = imagen_fondo
    
    def agregarCliente(self):
        client_name = self.name_entry.get()
        client_surname = self.surname_entry.get()
        client_phone = self.phone_entry.get()
        client_address = self.address_entry.get()

        client_data = f"{client_name} {client_surname} | Teléfono: {client_phone} | Dirección: {client_address}"
        self.client_list.insert(tk.END, client_data)

        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def cargaListaClientes(self):
        self.client_list.delete(0, tk.END)
        clients = []
        for client in clients:
            self.client_list.insert(tk.END, client)

    def cerrar_pantalla(self, pantalla):
        self.cliente.destroy()
        pantalla.deiconify()
#endregion

#region Arranque
if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
#endregion

