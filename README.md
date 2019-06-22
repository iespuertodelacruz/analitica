# Analítica

Informes hechos en Python para el análisis trimestral de rendimiento, absentismo, convivencia y otros aspectos del **IES Puerto de la Cruz - Telesforo Bravo**.

## Preparación del fichero de destino

El formato final de información con el que trabajan los Python notebooks es un fichero tipo `.xlsx` y están en la carpeta `data`:

~~~
data
├── C1516.xlsx
├── C1617.xlsx
└── C1718.xlsx
~~~

Cada fichero de estos tendrá tres *hojas* cada una con la nomenclatura `E1`, `E2` y `E3` representando las tres evaluaciones. En cada hoja habrá que cumplimentar las dos primera columnas:
- **grupo**: nombres de los grupos con los que queremos trabajar en la evaluación en cuestión.
- **etapa**: nombre de la enseñanza de cada grupo. Una forma de agrupar los datos en el análisis posterior.

Pero antes de llegar a esos ficheros, hay que **extraer la información** de varias fuentes: rendimiento, absentismo y convivencia.

### Rendimiento

Se espera que hayan **ficheros .csv** de rendimiento en la carpeta `data_tmp` con la siguiente nomenclatura:

#### Primera evaluación

~~~
data_tmp
├── C1718E1_CFGM.csv
├── C1718E1_CFGS.csv
├── C1718E1_BACH.csv
├── C1718E1_ESO.csv
└── C1718E1_FPB.csv
~~~

#### Segunda evaluación

~~~
data_tmp
├── C1718E2_1CFGM.csv
├── C1718E2_1CFGS.csv
├── C1718E2_2CFGM.csv
├── C1718E2_2CFGS.csv
├── C1718E2_3DAM.csv
├── C1718E2_BACH.csv
├── C1718E2_ESO.csv
└── C1718E2_FPB.csv
~~~

#### Tercera evaluación

~~~
data_tmp
├── C1718E3_12DAM.csv   # 1º y 2º de DAM
├── C1718E3_1CFGM.csv
├── C1718E3_1CFGS.csv
├── C1718E3_1FPB.csv
├── C1718E3_2CFGM.csv
├── C1718E3_2CFGS.csv
├── C1718E3_2FPB.csv
├── C1718E3_3DAM.csv
├── C1718E3_BACH.csv
└── C1718E3_ESO.csv
~~~

- `C1718`: indica el curso **2017/2018**
- `E1, E2, E3`: indica que es la **1ª, 2ª o 3ª evaluación**

> NOTA: Estos ficheros salen directamente de Pincel EKADE desde la opción de *"estadísticas de rendimiento"*. **OJO:** activar la opción de `.csv`

### Absentismo

El absentismo se va a estudiar de forma acumulada y será la suma de la faltas justificadas e injustificadas.

Se espera que haya un fichero de absentismo en la carpeta `data_tmp` con la siguiente nomenclatura:

~~~
data_tmp
└── C1718E1_ABSENTISMO.pdf  # E2 ó E3
~~~

- `C1718`: indica el curso **2017/2018**
- `E1, E2, E3`: indica que es la **1ª, 2ª o 3ª evaluación**

> NOTA: Este fichero sale directamente de Pincel EKADE desde la opción *"Informe de absentismo por grupos clase"*. **No olvidarse de marcar las siguientes opciones:**

- "Por grupo en páginas distintas"
- "Selección del período":
    - Desde: `01/09/<año>`
    - Hasta: `<Fecha de finalización del trimestre de estudio>`

### Convivencia

Se espera que haya un fichero de convivencia en la carpeta `data_tmp` con la siguiente nomenclatura:

~~~
data_tmp
└── C1718E1_CONVIVENCIA.ods  # E2 ó E3
~~~

- `C1718`: indica el curso **2017/2018**
- `E1, E2, E3`: indica que es la **1ª, 2ª o 3ª evaluación**

Este fichero es una hoja de cálculo de LibreOffice y debe tener la siguiente estructura:

~~~
ESO1A   3   0
ESO1B   2   1
ESO1C   4   0
ESO1D   5   0
~~~

Donde:

- La primera columna es el código del grupo.
- La segunda columna son los partes de gestión en dicha evaluación.
- La tercera columna son los partes de gestión con suspensión del derecho de asistencia al centro en dicha evaluación.

#### Observaciones

- Este fichero se debe generar "a mano" a través de un recuento de los partes físicos existentes en la jefatura de estudios.
- No poner nombres de columnas en la primera fila.
- No es necesario que aparezcan todos los grupos. Si no tienen partes de gestión ni siquiera es necesario que existan en el fichero.
- Sólo se tendrá en cuenta la primera hoja (*sheet*) del fichero.

### Lanzar la extracción de información


Activar el entorno virtual y ejecutar:

~~~console
$> python extract.py --year=1718 --eval=2  # 2ª eval. del curso 2017-2018
~~~

## Competencias básicas

Se espera que haya un fichero de estadísticas de calificaciones de competencias básicas en la carpeta `data/ccbb` con la siguiente nomenclatura:

~~~
data/ccbb
└── C1718E1_ESO_CCBB.csv  # E2 ó E3
~~~

- `C1718`: indica el curso **2017/2018**
- `E1, E2, E3`: indica que es la **1ª, 2ª o 3ª evaluación**

> NOTA: Este fichero sale directamente de Pincel EKADE desde la opción "Estadísticas de rendimiento escolar en items por evaluación".

**OJO! Este fichero va en la carpeta `data/ccbb` NO en la carpeta `data_tmp`**

## Pruebas de certificación para población escolar

Las [PCEI](http://www.gobiernodecanarias.org/educacion/web/idiomas/pruebas_certificacion/pruebas_certificacion_poblacion_escolar/) suelen ser en el mes de marzo. En el caso de que las pruebas hayan finalizado y las calificaciones estén puestas en PINCEL EKADE, se podrá obtener el fichero `.csv` de estadísticas.

Si este es el caso, se espera tener un fichero en la siguiente ruta:

~~~
data/pcei
└── C1819_PCEI.csv
~~~

- `C1819`: indica el curso **2018/2019**


## Creación del notebook

Para cada evaluación se debe crear un nuevo Jupyter Notebook. Supongamos que vamos a analizar la tercera evaluación del curso 2017-2018. Haremos lo siguiente:

~~~console
$ cd C1718
$ C1718> cp E2.ipynb E3.ipynb
$ C1718> ls
E1.ipynb E2.ipynb E3.ipynb
$ C1718> cd ..
$ jupyter notebook
...
~~~

A partir de aquí modificar las cosas necesarios en el nuevo Jupyter Notebook.

## Conversión del notebook a *html*

Ejemplo para convertir el notebook de la segunda evaluación del curso 2018-2019:

~~~console
$ ipy2html.sh C1819/E2.ipynb
~~~

> Este comando genera un fichero `C1819/E2.html` con el *"render"* y los gráficos del notebook.
