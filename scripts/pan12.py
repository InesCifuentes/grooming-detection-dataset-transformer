import os
import xml.etree.ElementTree as ET
import pandas as pd

def parse_xml_to_csv(xml_folder, output_csv, max_lines=200):
    data = []
    line_count = 0  # Contador de líneas procesadas
    
    # Iterar sobre todos los archivos en la carpeta especificada
    for filename in os.listdir(xml_folder):
        if filename.endswith('.xml'):
            print(f"Processing file: {filename}")
            file_path = os.path.join(xml_folder, filename)
            try:
                tree = ET.parse(file_path)
                root = tree.getroot()
                
                # Extraer mensajes del XML
                for conversation in root.findall('conversation'):
                    conversation_id = conversation.get('id', 'Unknown')
                    for message in conversation.findall('message'):
                        if line_count >= max_lines:
                            break  # Detener si se alcanzan las líneas máximas
                        
                        # Validar y extraer datos de las etiquetas
                        author = message.find('author').text if message.find('author') is not None else 'Unknown'
                        text = message.find('text').text if message.find('text') is not None else ''
                        timestamp = message.find('time').text if message.find('time') is not None else 'Unknown'
                        
                        # Verificar que el texto ocupe solo una línea
                        if '\n' not in text:
                            # Agregar datos a la lista
                            data.append([conversation_id, author, text, timestamp])
                            line_count += 1  # Incrementar el contador de líneas
                    
                    if line_count >= max_lines:
                        break  # Detener si se alcanzan las líneas máximas
            except ET.ParseError as e:
                print(f"Error parsing file {filename}: {e}")
        
        if line_count >= max_lines:
            break  # Detener si se alcanzan las líneas máximas
    
    # Crear DataFrame y guardar como CSV
    df = pd.DataFrame(data, columns=['conversation_id', 'author', 'text', 'timestamp'])
    df.to_csv(output_csv, index=False, encoding='utf-8')

# Uso de la función para el dataset de test
xml_folder_test = './data/raw/Pan12/test'  # Ruta pasada por parámetro para los archivos XML de test
output_csv_test = './data/processed/pan12_test_dataset.csv'  # Salida CSV para el test
parse_xml_to_csv(xml_folder_test, output_csv_test, max_lines=200)

# Uso de la función para el dataset de train
xml_folder_train = './data/raw/Pan12/train'  # Ruta pasada por parámetro para los archivos XML de train
output_csv_train = './data/processed/pan12_train_dataset.csv'  # Salida CSV para el train
parse_xml_to_csv(xml_folder_train, output_csv_train, max_lines=200)
