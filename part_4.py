def guardar_datos_txt(datos, archivo_txt):
    with open(archivo_txt, "w") as f:
        for archivo, info in datos:
            f.write(f"Archivo: {archivo}\n")
            for k, v in info.items():
                f.write(f"{k}: {v}\n")
            f.write("\n" + "-" * 40 + "\n\n")

# Clase de la pantalla de inicio
