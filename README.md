# Analítica

Informes hechos en Python para el análisis trimestral de rendimiento, absentismo, convivencia y otros aspectos del **IES Puerto de la Cruz - Telesforo Bravo**.

## Extracción de información

El formato final de información con el que trabajan los Python notebooks es un fichero tipo `.xlsx` y están en la carpeta `data`:

~~~
data
├── C1516.xlsx
├── C1617.xlsx
└── C1718.xlsx
~~~

Cada fichero de estos tendrá tres *hojas* cada una con la nomenclatura `E1`, `E2` y `E3` representando las tres evaluaciones. Pero antes de llegar a esos ficheros, hay que extraer la información de varias fuentes: rendimiento, absentismo y convivencia.

### Rendimiento

Se espera que hayan ficheros de rendimiento en la carpeta `data_tmp` con la siguiente nomenclatura:

#### Primera evaluación

~~~
data_tmp
├── C1718E1_1CFGM.xls
├── C1718E1_1CFGS.xls
├── C1718E1_2CFGM.xls
├── C1718E1_2CFGS.xls
├── C1718E1_3DAM.xls
├── C1718E1_BACH.xls
├── C1718E1_ESO.xls
└── C1718E1_FPB.xls
~~~

#### Segunda evaluación

~~~
data_tmp
├── C1718E2_1CFGM.xls
├── C1718E2_1CFGS.xls
├── C1718E2_2CFGM.xls
├── C1718E2_2CFGS.xls
├── C1718E2_3DAM.xls
├── C1718E2_BACH.xls
├── C1718E2_ESO.xls
└── C1718E2_FPB.xls
~~~

#### Tercera evaluación

~~~
data_tmp
├── C1718E3_12DAM.xls   # 1º y 2º de DAM
├── C1718E3_1CFGM.xls
├── C1718E3_1CFGS.xls
├── C1718E3_1FPB.xls
├── C1718E3_2CFGM.xls
├── C1718E3_2CFGS.xls
├── C1718E3_2FPB.xls
├── C1718E3_3DAM.xls
├── C1718E3_BACH.xls
└── C1718E3_ESO.xls
~~~

- `C1718`: indica el curso **2017/2018**
- `E1, E2, E3`: indica que es la **1ª, 2ª o 3ª evaluación**

> NOTA: Estos ficheros salen directamente de Pincel EKADE desde la opción de *"estadísticas de rendimiento"*.

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

- "Por grupo en distintas páginas"
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

> NOTA: Este fichero se debe generar "a mano" a través de un recuento de los partes físicos existentes en la jefatura de estudios.

> No es necesario que aparezcan todos los grupos. Si no tienen partes de gestión ni siquiera es necesario que existan en el fichero.

### Lanzar la extracción de información

1. Limpiar la hoja de la evaluación correspondiente del fichero `data/CXXYY.xlsx` **dejando intactas las dos primeras columnas de `grupo` y `etapa`**.
2. Activar el entorno virtual y ejecutar:

~~~console
$> python extract.py --year=1718 --eval=2
~~~

> NOTA: En este caso lanzaríamos la extracción de información de la segunda evaluación del curso 2017-2018, e incluirá los valores correspondientes en el fichero `data/C1718.xlsx`.

## Competencias básicas

Se espera que haya un fichero de estadísticas de calificaciones de competencias básicas en la carpeta `data` con la siguiente nomenclatura:

~~~
data
└── C1718E1_ESO_CCBB.csv  # E2 ó E3
~~~

- `C1718`: indica el curso **2017/2018**
- `E1, E2, E3`: indica que es la **1ª, 2ª o 3ª evaluación**

> NOTA: Este fichero sale directamente de Pincel EKADE desde la opción "Estadísticas de rendimiento escolar en items por evaluación".

**OJO! Este fichero va en la carpeta `data` NO en la carpeta `data_tmp`**

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
