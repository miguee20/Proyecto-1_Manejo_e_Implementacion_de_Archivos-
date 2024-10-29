def guardar_datos_txt(datos, archivo_txt):
    with open(archivo_txt, "w") as f:
        for archivo, info in datos:
            f.write(f"Archivo: {archivo}\n")
            for k, v in info.items():
                f.write(f"{k}: {v}\n")
            f.write("\n" + "-" * 40 + "\n\n")

def obtener_datos_modificados(archivos_datos):
    datos_modificados = []
    for archivo, datos in archivos_datos:
        datos_modificados.append((archivo, datos))
    return datos_modificados
