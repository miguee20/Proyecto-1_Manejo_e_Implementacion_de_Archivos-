class PantallaInicio(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Pantalla de Inicio")
        self.geometry("600x400")
        self.configure(bg="#2e2e2e")
        self.resizable(True, True)

        # Frame central para organizar elementos
        self.frame_central = tk.Frame(self, bg="#2e2e2e", padx=20, pady=20)
        self.frame_central.pack(expand=True)

        # Título del programa
        self.label_titulo = tk.Label(self.frame_central, text="Extractor de Datos GIF", font=("Arial", 18, "bold"), fg="#ffffff", bg="#2e2e2e")
        self.label_titulo.pack(pady=(0, 10))

        # Texto "Manejo de Archivos"
        self.label_manejo_archivos = tk.Label(self.frame_central, text="Manejo de Archivos", font=("Arial", 14), fg="#ffffff", bg="#2e2e2e")
        self.label_manejo_archivos.pack()

        # Nombres
        self.label_nombres = tk.Label(self.frame_central, text="Miguel Antonio Salguero Sandoval\nIván Alexander Ordoñez López", font=("Arial", 12), fg="#b0bec5", bg="#2e2e2e")
        self.label_nombres.pack(pady=(10, 20))

        # Mensaje de bienvenida
        self.label_bienvenida = tk.Label(self.frame_central, text="¡Bienvenido!\nExplora y extrae datos de tus archivos GIF.", font=("Arial", 12), fg="#ffffff", bg="#2e2e2e")
        self.label_bienvenida.pack(pady=(0, 20))

        # Botón de Iniciar
        self.boton_iniciar = tk.Button(self.frame_central, text="Iniciar", font=("Arial", 12, "bold"), bg="#8BC34A", fg="#ffffff", width=20, height=2, command=self.iniciar_aplicacion)
        self.boton_iniciar.pack(pady=(0, 10))

    def iniciar_aplicacion(self):
        self.destroy()
        self.master.deiconify()

# Clase principal de la aplicación
