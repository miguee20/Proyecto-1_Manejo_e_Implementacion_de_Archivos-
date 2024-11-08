import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from PIL import Image, ImageTk
import time

# Función para extraer información de un archivo GIF
def obtener_datos_gif(ruta_archivo):
    try:
        with Image.open(ruta_archivo) as img:
            datos = {
                "Versión": img.info.get("version", "Desconocida"),
                "Tamaño": img.size,
                "Colores": len(img.getpalette()) // 3 if img.getpalette() else 0,
                "Compresión": img.info.get("compression", "No especificado"),
                "Formato Numérico": img.mode,
                "Color de Fondo": img.info.get("background", "No especificado"),
                "Imágenes": img.n_frames if hasattr(img, "n_frames") else 1,
                "Fecha Creación": time.ctime(os.path.getctime(ruta_archivo)),
                "Fecha Modificación": time.ctime(os.path.getmtime(ruta_archivo)),
                "Comentarios": img.info.get("comment", b"").decode("utf-8") if "comment" in img.info else ""
            }
            return datos
    except Exception as e:
        print(f"Error al procesar {ruta_archivo}: {e}")
        return None

# Función para buscar archivos GIF en una carpeta y subcarpetas
def buscar_archivos_gif(directorio):
    archivos_gif = []
    for root, _, files in os.walk(directorio):
        for file in files:
            if file.lower().endswith('.gif'):
                archivos_gif.append(os.path.join(root, file))
    return archivos_gif

# Guardar datos en un archivo de texto
def guardar_datos_txt(datos, archivo_txt):
    with open(archivo_txt, "w") as f:
        for archivo, info in datos:
            f.write(f"Archivo: {archivo}\n")
            for k, v in info.items():
                f.write(f"{k}: {v}\n")
            f.write("\n" + "-" * 40 + "\n\n")

# Clase de la pantalla de inicio
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
class AplicacionGIFExtractor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()  # Ocultar la ventana principal al inicio

        # Crear la pantalla de inicio
        self.pantalla_inicio = PantallaInicio(self)

        # Configuración de la ventana principal
        self.title("Extractor de Datos GIF")
        self.geometry("800x600")
        self.configure(bg="#2e2e2e")
        self.resizable(True, True)
        self.archivos_datos = []
        self.gif_frames = None
        self.frame_index = 0
        self.current_gif = None

        # Título de la interfaz
        self.label_titulo = tk.Label(self, text="Extractor de Datos GIF", font=("Arial", 16, "bold"), fg="#ffffff", bg="#2e2e2e")
        self.label_titulo.pack(pady=(20, 10))

        # Frame izquierdo para botones y lista de archivos
        self.frame_izquierdo = tk.Frame(self, bg="#2e2e2e")
        self.frame_izquierdo.pack(side=tk.LEFT, padx=(20, 10), pady=(10, 10), fill=tk.Y)

        # Frame para botones (centrar)
        self.frame_botones = tk.Frame(self.frame_izquierdo, bg="#2e2e2e")
        self.frame_botones.pack(pady=5)

        # Botones para cargar archivos o carpetas
        self.boton_cargar_carpeta = tk.Button(self.frame_botones, text="Cargar Carpeta", command=self.cargar_carpeta, width=20, height=2, bg="#8BC34A", fg="#ffffff", font=("Arial", 10, "bold"))
        self.boton_cargar_archivo = tk.Button(self.frame_botones, text="Cargar Archivo", command=self.cargar_archivo, width=20, height=2, bg="#FFC107", fg="#ffffff", font=("Arial", 10, "bold"))
        self.boton_mostrar_datos = tk.Button(self.frame_botones, text="Mostrar Datos", command=self.mostrar_datos, width=20, height=2, bg="#03A9F4", fg="#ffffff", font=("Arial", 10, "bold"))
        self.boton_guardar_txt = tk.Button(self.frame_botones, text="Guardar en TXT", command=self.guardar_txt, width=20, height=2, bg="#E91E63", fg="#ffffff", font=("Arial", 10, "bold"))
        self.boton_salir = tk.Button(self.frame_botones, text="Salir", command=self.destroy, width=20, height=2, bg="#F44336", fg="#ffffff", font=("Arial", 10, "bold"))

        self.boton_cargar_carpeta.pack(pady=5)
        self.boton_cargar_archivo.pack(pady=5)
        self.boton_mostrar_datos.pack(pady=5)
        self.boton_guardar_txt.pack(pady=5)
        self.boton_salir.pack(pady=5)

        # Lista de archivos cargados
        self.lista_archivos = tk.Listbox(self.frame_izquierdo, width=50, height=15, bg="#333333", fg="#ffffff", selectbackground="#555555")
        self.lista_archivos.pack(pady=10, fill=tk.BOTH, expand=True)

        # Frame derecho para vista previa y datos
        self.frame_derecho = tk.Frame(self, bg="#2e2e2e")
        self.frame_derecho.pack(side=tk.RIGHT, padx=(10, 20), pady=(10, 10), fill=tk.BOTH, expand=True)

        # Vista previa del GIF
        self.label_imagen = tk.Label(self.frame_derecho, text="Vista Previa del GIF", font=("Arial", 12), fg="#ffffff", bg="#2e2e2e")
        self.label_imagen.pack(pady=10)
        self.canvas_imagen = tk.Label(self.frame_derecho, bg="#2e2e2e")
        self.canvas_imagen.pack(pady=10)

        # Caja de texto para mostrar datos
        self.texto_datos = scrolledtext.ScrolledText(self.frame_derecho, wrap=tk.WORD, bg="#333333", fg="#ffffff", insertbackground='white')
        self.texto_datos.pack(pady=(10, 20), fill=tk.BOTH, expand=True)

    def cargar_carpeta(self):
        directorio = filedialog.askdirectory()
        if directorio:
            archivos_gif = buscar_archivos_gif(directorio)
            self.lista_archivos.delete(0, tk.END)
            self.archivos_datos = []

            for archivo in archivos_gif:
                datos = obtener_datos_gif(archivo)
                if datos:
                    self.archivos_datos.append((archivo, datos))
                    self.lista_archivos.insert(tk.END, archivo)

    def cargar_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos GIF", "*.gif")])
        if archivo:
            datos = obtener_datos_gif(archivo)
            if datos:
                self.archivos_datos.append((archivo, datos))
                self.lista_archivos.insert(tk.END, archivo)

    def mostrar_datos(self):
        seleccion = self.lista_archivos.curselection()
        if seleccion:
            indice = seleccion[0]
            archivo, datos = self.archivos_datos[indice]
            self.texto_datos.delete(1.0, tk.END)
            self.texto_datos.insert(tk.END, f"Archivo: {archivo}\n")
            for clave, valor in datos.items():
                self.texto_datos.insert(tk.END, f"{clave}: {valor}\n")

            # Mostrar el GIF en la vista previa
            self.mostrar_gif(archivo)

    def mostrar_gif(self, ruta_archivo):
        self.gif_frames = []
        self.frame_index = 0

        with Image.open(ruta_archivo) as img:
            for i in range(img.n_frames):
                img.seek(i)
                frame = ImageTk.PhotoImage(img.resize((150, 150), Image.LANCZOS).convert("RGBA"))
                self.gif_frames.append(frame)

        self.actualizar_gif()

    def actualizar_gif(self):
        if self.gif_frames:
            self.canvas_imagen.config(image=self.gif_frames[self.frame_index])
            self.frame_index = (self.frame_index + 1) % len(self.gif_frames)
            self.after(100, self.actualizar_gif)
            
    def guardar_datos_actualizados(self):
        seleccion = self.lista_archivos.curselection()
        if seleccion:
            indice = seleccion[0]
            archivo, datos = self.archivos_datos[indice]

            contenido = self.texto_datos.get("1.0", tk.END)
            for linea in contenido.splitlines():
                if linea.startswith("Comentarios:"):
                    comentario_actualizado = linea.replace("Comentarios: ", "").strip()
                    datos["Comentarios"] = comentario_actualizado

        self.archivos_datos[indice] = (archivo, datos)

    def guardar_txt(self):
        self.guardar_datos_actualizados()

        archivo_txt = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivo de Texto", "*.txt")])
        if archivo_txt:
            guardar_datos_txt(self.archivos_datos, archivo_txt)
            messagebox.showinfo("Guardado", f"Datos guardados en {archivo_txt}")

    # Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = AplicacionGIFExtractor()
    app.mainloop()
