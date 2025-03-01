import os
import shutil

# Carpeta donde están las migraciones
apps = ["hogares"]  # Agrega aquí el nombre de tus aplicaciones

for app in apps:
    migraciones_path = os.path.join(app, "migrations")

    if os.path.exists(migraciones_path):
        for archivo in os.listdir(migraciones_path):
            archivo_path = os.path.join(migraciones_path, archivo)
            # Borra todos los archivos excepto __init__.py
            if archivo != "__init__.py":
                os.remove(archivo_path)
        
        print(f"✅ Migraciones eliminadas en {migraciones_path}")

print("🚀 Proceso completado.")
