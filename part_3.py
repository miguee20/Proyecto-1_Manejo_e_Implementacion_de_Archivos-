def buscar_archivos_gif(directorio):
    archivos_gif = []
    for root, _, files in os.walk(directorio):
        for file in files:
            if file.lower().endswith('.gif'):
                archivos_gif.append(os.path.join(root, file))
    return archivos_gif

# Guardar datos en un archivo de texto
