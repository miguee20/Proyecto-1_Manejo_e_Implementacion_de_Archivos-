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
