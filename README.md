# Grooming Detection Dataset Transformer

Este repositorio contiene scripts en Python para transformar datasets públicos sobre grooming online en archivos `.csv` limpios y listos para análisis.

## 📁 Estructura del Proyecto

```
grooming-detection-dataset-transformer/
├── scripts/
│   └── pan12.py            ← contiene ambos scripts XML (train y test)
│   └── pj.py               ← contiene el script de los .txt
│   └── convert_all.py      ← ejecuta todo desde un solo punto
├── data/
│   └── processed/
│       ├── pan12_train_dataset.csv
│       ├── pan12_test_dataset.csv
│       └── pj_dataset.csv
├── README.md
└── requirements.txt
```

## Descripción de los Archivos

- **scripts/pan12.py**: Contiene los scripts que procesan los archivos XML para los datasets de `train` y `test`.
- **scripts/pj.py**: Contiene el script para procesar los archivos `.txt` del dataset PJ.
- **scripts/convert_all.py**: Script principal que ejecuta todos los procesos de conversión de datos.
- **data/processed**: Carpeta que contiene los datasets procesados en formato CSV.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar el proyecto.

## Uso

```bash
python scripts/convert_all.py
