import os
import pandas as pd

class PjDatasetProcessor:
    def __init__(self, folder_path, output_csv):
        self.folder_path = folder_path
        self.output_csv = output_csv

    def process_txt_files(self):
        # Listas para almacenar datos
        data = []

        # Recorre todos los archivos .txt
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(self.folder_path, filename)

                # Determina el tipo de archivo: 'officer' o 'predator'
                if filename.lower().startswith("officer"):
                    sender = "officer"
                elif filename.lower().startswith("predator"):
                    sender = "predator"
                else:
                    continue  # Saltar si no cumple formato

                # Extrae ID de la conversación
                base_id = filename.split("_")[1].split(".")[0]
                conversation_id = f"conv{base_id.zfill(3)}"

                # Lee cada línea como un mensaje
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        line = line.strip()
                        if line:  # Evitar líneas vacías
                            data.append({
                                "conversation_id": conversation_id,
                                "sender": sender,
                                "text": line
                            })

        # Crear DataFrame y guardar como CSV
        df = pd.DataFrame(data)
        df.to_csv(self.output_csv, index=False)

        print(f"Conversión completada. Archivo guardado como {self.output_csv}")
