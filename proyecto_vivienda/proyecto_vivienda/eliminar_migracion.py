import os

migrations_path = "proyecto_vivienda/hogares/migrations"

# Verificar si la carpeta de migraciones existe
if os.path.exists(migrations_path):
    for file in os.listdir(migrations_path):
        if file != "__init__.py":  # No borrar __init__.py
            file_path = os.path.join(migrations_path, file)
            os.remove(file_path)
            print(f"Eliminado: {file_path}")
    print("✅ Migraciones eliminadas correctamente.")
else:
    print("⚠️ La carpeta de migraciones no existe.")
