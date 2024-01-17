# Proyecto de Análisis de Población por País - Curso de PLatzi

Este proyecto utiliza Python para leer datos de población desde un archivo CSV, realizar análisis y generar gráficos. Los principales componentes del proyecto son `utils`, `read_csv`, y `charts`.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/anuarMoreno/Platzi-Course-World-Population.git
   cd Platzi-Course-World-Population
   ```
2. Instalación de Dependencias

    ```bash
    pip install -r requirements.txt
    ```
## Estructura del Proyecto

- **utils:** Contiene funciones de utilidad para el análisis de datos.
- **read_csv:** Maneja la lectura de datos desde archivos CSV.
- **charts:** Proporciona funciones para generar gráficos.
- **main.py:** Script principal para ejecutar el análisis y visualización.

## Uso

1. Asegúrate de descargar el archivo CSV llamado `data.csv` en la carpeta `app`.
2. Ejecuta el script principal:

    ```bash
    python main.py
    ```
## Logica del Proyecto

### `read_csv.py`

Este módulo se encarga de leer el archivo CSV y extraer información relevante para el análisis.

#### Funciones

- `read_csv(path)`: Lee el archivo CSV y devuelve una lista de diccionarios con la información de cada país.
- `read_row_csv(data)`: Toma datos específicos y devuelve etiquetas y valores para su uso en gráficos circulares.

### `charts.py`

Este módulo se encarga de generar gráficos a partir de los datos proporcionados.

#### Funciones

- `generate_bar_chart(labels, values, country)`: Genera un gráfico de barras para representar la población de un país a lo largo del tiempo.
- `generate_pie_chart(labels, values)`: Genera un gráfico circular para mostrar la distribución de la población en Sudamérica.

### `utils.py`

Este módulo proporciona funciones para obtener información específica sobre la población de un país.

#### Funciones

- `get_population(country_dict)`: Filtra y procesa los datos para obtener la población a lo largo de los años. Devuelve listas de años y poblaciones.
- `population_by_country(data, country)`: Filtra los datos para obtener información específica sobre la población de un país.

# Gracias por leerme

¡Agradezco tu tiempo y atención!

Si tienes sugerencias, estaré atento.

