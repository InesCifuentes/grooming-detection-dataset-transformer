import os
from pan12 import parse_xml_to_csv
from pj import PjDatasetProcessor

def convert_pan12(xml_folder_train, xml_folder_test, output_csv_train, output_csv_test, max_lines=200):
    # Procesa los archivos XML para el dataset de entrenamiento (train) y prueba (test)
    print("Procesando archivos XML para el dataset de PAN12...")
    parse_xml_to_csv(xml_folder_train, output_csv_train, max_lines)
    parse_xml_to_csv(xml_folder_test, output_csv_test, max_lines)

def convert_pj(folder_path, output_csv):
    # Procesa los archivos .txt para el dataset de PJ
    print("Procesando archivos .txt para el dataset de PJ...")
    processor = PjDatasetProcessor(folder_path, output_csv)
    processor.process_txt_files()

if __name__ == "__main__":
    # Define las rutas y archivos de salida
    xml_folder_train = './data/raw/Pan12/train'  # Ruta a la carpeta donde están los archivos XML
    xml_folder_test = './data/raw/Pan12/test'  # Ruta a la carpeta donde están los archivos XML
    output_csv_train = './data/processed/pan12_train_dataset.csv'  # Salida CSV para entrenamiento
    output_csv_test = './data/processed/pan12_test_dataset.csv'  # Salida CSV para prueba
    folder_path_pj = './data/raw/PJ/conversaciones'  # Ruta a la carpeta donde están los archivos .txt
    output_csv_pj = './data/processed/pj_dataset.csv'  # Salida CSV para PJ

    # Llamar a las funciones de conversión
    convert_pan12(xml_folder, output_csv_train, output_csv_test)
    convert_pj(folder_path_pj, output_csv_pj)

    print("Conversión completada para todos los datasets.")
