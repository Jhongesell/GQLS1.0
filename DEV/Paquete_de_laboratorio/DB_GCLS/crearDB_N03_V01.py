# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Nombre:       crearDB.py
# Autor:        Jhon Gesell Vilanueva Portella
# Creado:       22 de Octubre de 2018
# Modificado:   24 de Octubre de 2018

# Licencia:     GNU V3
# ------------------------------------------------------------------------

__version__ = "1.0"

"""
El módulo *crearDB* permite crear la Base de Datos para el programa de computadora GCLS.
"""

# Versión Python:

import sqlite3

# Crear base de datos física (reside en el disco)

"""Crear objeto de conexión, si la base de datos no existe se creara
automáticamente y estará alojada en la misma ubicación de este script"""
conexion = sqlite3.connect("DB_GCLS.db")

# Crear setCursor
cursor = conexion.cursor()

try:
    # Crear tabla si no existe
    cursor.execute("CREATE TABLE IF NOT EXISTS MUESTRAS (ID INTEGER PRIMARY KEY, CODIGO TEXT NOT NULL, "
    "REPETICIONES TEXT NOT NULL, FECHA TEXT NOT NULL, COTA_NIVEL REAL NOT NULL, "
    "COD_CHAPA TEXT NOT NULL, PESO_BOTELLA_CON_LIQUIDO REAL NOT NULL, PESO_BOTELLA REAL NOT NULL, "
    "VOLUMEN REAL NOT NULL, FINOS_PESO_INICIAL_FILTRO REAL NOT NULL, FINOS_PESO_FINAL_FILTRO REAL NOT NULL, "
    "GRUESOS_PESO_INICIAL_FILTRO REAL NOT NULL, GRUESOS_PESO_FINAL_FILTRO REAL NOT NULL, "
    "ESTACION TEXT NOT NULL)")

    datos_insertar = [("A2", "2", "03/03/2003 03:03h", "4.0", "E5", "0.6", "0.07", "0.8", "0.9", "1.0", "1.1", "1.2", "CATORCE"),
    ("A2", "2", "03/03/2003 03:03h", "4.0", "E5", "0.6", "0.07", "0.8", "0.9", "1.0", "1.1", "1.2", "CATORCE"),
    ("A2", "2", "03/03/2003 03:03h", "4.0", "E5", "0.6", "0.07", "0.8", "0.9", "1.0", "1.1", "1.2", "CATORCE"),
    ("A2", "2", "03/03/2003 03:03h", "4.0", "E5", "0.6", "0.07", "0.8", "0.9", "1.0", "1.1", "1.2", "CATORCE"),
    ("A2", "2", "03/03/2003 03:03h", "4.0", "E5", "0.6", "0.07", "0.8", "0.9", "1.0", "1.1", "1.2", "CATORCE"),
    ("A2", "2", "03/03/2003 03:03h", "4.0", "E5", "0.6", "0.07", "0.8", "0.9", "1.0", "1.1", "1.2", "CATORCE"),
    ("A2", "2", "03/03/2003 03:03h", "4.0", "E5", "0.6", "0.07", "0.8", "0.9", "1.0", "1.1", "1.2", "CATORCE"),
    ("A2", "2", "03/03/2003 03:03h", "4.0", "E5", "0.6", "0.07", "0.8", "0.9", "1.0", "1.1", "1.2", "CATORCE"),
    ("A2", "2", "03/03/2003 03:03h", "4.0", "E5", "0.6", "0.07", "0.8", "0.9", "1.0", "1.1", "1.2", "CATORCE"),
    ("A2", "2", "03/03/2003 03:03h", "4.0", "E5", "0.6", "0.07", "0.8", "0.9", "1.0", "1.1", "1.2", "CATORCE"),
    ("A2", "2", "03/03/2003 03:03h", "4.0", "E5", "0.6", "0.07", "0.8", "0.9", "1.0", "1.1", "1.2", "CATORCE"),
    ("A2", "2", "03/03/2003 03:03h", "4.0", "E5", "0.6", "0.07", "0.8", "0.9", "1.0", "1.1", "1.2", "CATORCE"),
    ("A2", "2", "03/03/2003 03:03h", "4.0", "E5", "0.6", "0.07", "0.8", "0.9", "1.0", "1.1", "1.2", "CATORCE")]

    # Insertar multiples filas o datos
    cursor.executemany("INSERT INTO MUESTRAS VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)", datos_insertar)

    # Guardar los cambios en la base de datos
    conexion.commit()

    print("Base de datos creada con éxito.")

# Capturar cualquier error que genere sqlite3
except sqlite3.Error as error:
    print("Error inesperado: {}".format(error))

# Cerrar conexión
conexion.close()
