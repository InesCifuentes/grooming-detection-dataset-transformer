# Grooming Detection Dataset Transformer

Este repositorio contiene scripts en Python para transformar datasets públicos sobre grooming online en archivos `.csv` limpios y listos para análisis.

## 📁 Estructura del Proyecto

grooming-detection-dataset-transformer/
├── scripts/
│   └── pan12.py            ← contiene ambos scripts XML (train y test)
│   └── pj.py               ← contiene el script de los .txt
│   └── convert_all.py      ← ejecuta todo desde un solo punto
├── data/
│   ├── raw/
│   │   ├── Pan12/
│   │   │   ├── train/
│   │   │   │   └── pan12-sexual-predator-identification-train.xml
│   │   │   └── test/
│   │   │       └── pan12-sexual-predator-identification-test.xml
│   │   └── PJ/
│   │       └── conversaciones/
│   │           └── [archivos .txt]
│   └── processed/
│       ├── pan12_train_dataset.csv
│       ├── pan12_test_dataset.csv
│       └── pj_dataset.csv
├── README.md
├── .gitignore
└── requirements.txt

## Uso

```bash
python scripts/convert_all.py
