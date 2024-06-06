![State](https://img.shields.io/badge/State-On_Date-green)
![Status](https://img.shields.io/badge/Status-Draft-orange)
![Github Actions](https://img.shields.io/badge/Github_Actions-Unverified_%E2%9D%8C-red)

# Detección de Fraude Bancario 💳
<p align="center">
    <a href="README.md">🇬🇧</a>
    <a href="README_fr.md">🇫🇷</a>
</p>

## Visión General 
>[IMPORTANT]\
>Este repositorio contiene un proyecto de demostración que utiliza SQL, Python y Jupyter Notebooks para simular una base de datos bancaria. El objetivo principal es analizar los movimientos de las cuentas para detectar actividades fraudulentas y generar estadísticas relacionadas con los incidentes de fraude.

## Características 💎
- **Creación de base de datos**: Scripts para crear y poblar una base de datos bancaria con cuentas, transacciones y clientes.
- **Detección de fraude**: Scripts en Python y SQL para identificar transacciones potencialmente fraudulentas.
- **Análisis estadístico**: Generar estadísticas sobre las ocurrencias de fraude, como el porcentaje de transacciones fraudulentas y la cantidad total de dinero involucrado.
- **Automatización**: Flujos de trabajo de GitHub Actions para automatizar la ejecución de scripts y actualizar los resultados regularmente.

## Estructura del repositorio 📁
- `data/` Conjuntos de datos de ejemplo y scripts SQL para la creación de la base de datos.
- `notebooks/` Jupyter Notebooks para el análisis de datos y la detección de fraudes.
- `scripts/` Scripts de Python para el procesamiento y análisis de datos.
- `.github/workflows/` Flujos de trabajo de GitHub Actions para la automatización.
- `README.md` Documentación del proyecto.

## Empezando

### Prerrequisitos
- Python 3.12
- Jupyter Notebook
- SQL (por ejemplo, SQLite, PostgreSQL, MySQL)
- Git

### Instalación
1. Clona el repositorio:
    ```bash
    git clone https://github.com/yourusername/bank-fraud-detection.git
    cd bank-fraud-detection
    ```

2. Instala las dependencias de Python:
    ```bash
    pip install -r requirements.txt
    ```

3. Configura la base de datos:
    ```bash
    cd data
    # Ejecuta los scripts SQL para crear y poblar la base de datos
    ```

### Uso

1. Abre los Jupyter Notebooks en el directorio `notebooks/` para explorar los datos y ejecutar los análisis de detección de fraudes:
    ```bash
    jupyter notebook
    ```

2. Ejecuta los scripts de Python en el directorio `scripts/` para el procesamiento y análisis automatizado de datos:
    ```bash
    python scripts/analyze_fraud.py
    ```

### Automatización con GitHub Actions
El repositorio incluye flujos de trabajo de GitHub Actions que automatizan la ejecución de scripts de detección de fraudes. Estos flujos de trabajo se encuentran en el directorio `.github/workflows/`. Para activar la automatización:
1. Empuja el repositorio a GitHub.
2. Navega a la pestaña de GitHub Actions en la página de tu repositorio para monitorear las ejecuciones de los flujos de trabajo.

## Contribuciones
¡Las contribuciones son bienvenidas! Por favor, abre una issue o envía una pull request para cualquier mejora o nueva característica.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contact 
![Gmail](https://img.shields.io/badge/mathieu.audibert27@gmail.com-white?style=for-the-badge&logo=gmail&logoColor=white&logoSize=auto&color=C11E1E)
![Outlook](https://img.shields.io/badge/mathieu.audibert@efrei.net-white?style=for-the-badge&logo=microsoft-outlook&logoColor=white&logoSize=auto&color=0072C6)