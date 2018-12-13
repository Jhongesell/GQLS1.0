# -*- coding: utf-8 -*-
# ----------------
# Nombre: gclsVO1.py
# Autor: Jhon Gesell
# Creado: 09 de diciembre 2018
# Modificado 12 de diciembre 2018
# License: GNU V3

# --------------

__version__ = "1.0"

"""
La aplicación GCLS (Gestor de caudales líquidos y sólidos) fue diseñada y desarrollada
por JHON GESELL (Python developer). Sientase libre de usarla.
"""

# Version Python: 3.5.2
# Versión PyQt5: 5.11.3

import sqlite3

from PyQt5.QtGui import QFont, QIcon, QPalette, QBrush, QColor, QPixmap, QRegion, QClipboard
from PyQt5.QtCore import (Qt, QFile, QDate, QTime, QSize, QTimer, QRect, QTranslator, QLocale,
                          QLibraryInfo)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog, QPushButton, QAction,
                             QTableWidget, QTableWidgetItem, QAbstractItemView, QMenu, QStyle,
                             QLineEdit, QActionGroup, QMessageBox, QToolButton, QFrame,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QLabel)


# ======== CLASE Ayuda ===================

class Ayuda(QDialog):
    def __init__(self, parent=None):
        super(Ayuda, self).__init__()

        self.setWindowTitle("Ayuda")
        self.setWindowFlags(Qt.WindowTitleHint | Qt.CustomizeWindowHint |
                        Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(450, 500)

        self.initUI()

    def initUI(self):
        label = QLabel(self)
        label.setPixmap(QPixmap("Imagenes/imagenreferencialN00.png").scaled(450, 450, Qt.KeepAspectRatio,
                                                                Qt.SmoothTransformation))
        label.move(0, 0)

        botonCerrar = QPushButton("Cerrar", self)
        botonCerrar.setFixedSize(430, 32)
        botonCerrar.move(10, 457)

        # ================= EVENTO ==================0000

        botonCerrar.clicked.connect(self.close)


# =================== CLASE Acerca ==========================

class Acerca(QDialog):
    def __init__(self, parent=None):
        super(Acerca, self).__init__()

        self.setWindowTitle("Acerca del Gcls")
        self.setWindowFlags(Qt.WindowTitleHint | Qt.CustomizeWindowHint |
                            Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(450, 500)

        self.initUI()

    def initUI(self):
        label = QLabel(self)
        label.setPixmap(QPixmap("Imagenes/imagenreferencialN01.png").scaled(450, 450, Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation))
        label.move(0, 0)

        labelAcerca = QLabel("GCLS: Gestor de caudales líquidos y sólidos\n"
                             "Licencia GNU V03.", self)
        labelAcerca.move(10,460)

        botonCerrar =QPushButton("Cerrar", self)
        botonCerrar.setFixedSize(80, 32)
        botonCerrar.move(360, 457)

        # ================== EVENTO =========================0

        botonCerrar.clicked.connect(self.close)


# ========================= CLASE Configuracion =================

class Configuracion(QDialog):
    def __init__(self, parent=None):
        super(Configuracion, self).__init__(parent)

        self.setWindowFlags(Qt.Popup)
        self.setFixedSize(450, 500)

        paleta = self.palette()
        paleta.setColor(QPalette.Background, QColor("white"))
        self.setPalette(paleta)

        self.initUI()

    def initUI(self):
        frame = QFrame(self)
        frame.setFrameShape(QFrame.Box)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setFixedSize(450, 500)
        frame.move(0, 0)

        label = QLabel(frame)
        label.setPixmap(QPixmap("Imagenes/config_N01.png").scaled(447, 447, Qt.KeepAspectRatio,
                                                              Qt.SmoothTransformation))
        label.move(1, 1)

        botonConfigurar = QPushButton("Configuración", frame)
        botonConfigurar.setFixedSize(430, 32)
        botonConfigurar.move(10, 457)

      # ========================= EVENTO =========================

        botonConfigurar.clicked.connect(self.Configuracion)

  # ========================= FUNCIONES ==========================

    def Configuracion(self):
        QMessageBox.information(self, "Configuración", "Este es un mensaje de ejemplo.\n\n26 "
                                "de Enero de 2019: revelación de enigmas y misterios   \na "
                                "toda la humanidad.", QMessageBox.Ok)


# =============== CLASE Boton ===================================

class Boton(QToolButton):
    def __init__(self, parent=None):
        super(Boton, self).__init__(parent)

        self.setMask(QRegion(QRect(2, 2, 220, 36), QRegion.Rectangle))
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.setIconSize(QSize(26, 26))
        self.setIcon(QIcon("Imagenes/Check.png"))
        self.setFixedSize(224, 40)


# ========================== CLASE Widgets ===============================

class Widgets(QWidget):
    def __init__(self, parent=None):
        super(Widgets, self).__init__(parent)

        self.initUI()

    def initUI(self):

        fuenteGcls = self.font()
        fuenteGcls.setBold(True)
        fuenteGcls.setPointSize(12)

      # ===================== FRAME PANEL DE CONTROL ===================

        paletaBotones = self.palette()
        paletaBotones.setColor(QPalette.Background, QColor("#5F04B4"))          ##2EFEC8

        frameBotones = QFrame()
        frameBotones.setFrameStyle(QFrame.NoFrame)
        frameBotones.setAutoFillBackground(True)
        frameBotones.setPalette(paletaBotones)
        frameBotones.setFixedWidth(220)

      # ================================================================

        paletaPanel = self.palette()
        paletaPanel.setBrush(QPalette.Background, QBrush(QColor(255, 90, 0), Qt.SolidPattern))
        paletaPanel.setColor(QPalette.Foreground, Qt.white)

        labelGcls = QLabel("PANEL DE CONTROL", frameBotones)
        labelGcls.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        labelGcls.setFont(fuenteGcls)
        labelGcls.setAutoFillBackground(True)
        labelGcls.setPalette(paletaPanel)
        labelGcls.setFixedSize(220, 46)
        labelGcls.move(0, 0)

      # ===================================================================

        tamanioIcono = QSize(30, 30)

        botonNuevo = Boton(frameBotones)
        botonNuevo.setText(" Nuevo")
        botonNuevo.setToolTip("Nueva muestra")
        botonNuevo.setCursor(Qt.PointingHandCursor)
        botonNuevo.move(-2, 45)

        botonActualizar = Boton(frameBotones)
        botonActualizar.setText(" Actualizar")
        botonActualizar.setToolTip("Actualizar muestra")
        botonActualizar.setCursor(Qt.PointingHandCursor)
        botonActualizar.move(-2, 82)

        botonEliminar = Boton(frameBotones)
        botonEliminar.setText(" Eliminar")
        botonEliminar.setToolTip("Eliminar registro de muestra")
        botonEliminar.setCursor(Qt.PointingHandCursor)
        botonEliminar.move(-2, 119)

        botonLimpiar = Boton(frameBotones)
        botonLimpiar.setText(" Limpiar tabla")
        botonLimpiar.setToolTip("Limpiar tabla")
        botonLimpiar.setCursor(Qt.PointingHandCursor)
        botonLimpiar.move(-2, 156)

      # ==========================================================0

        paletaSuscribete = self.palette()
        paletaSuscribete.setBrush(QPalette.Background, QBrush(QColor(135, 206, 250),
                                                            Qt.SolidPattern))

        fuenteSuscribete = self.font()
        fuenteSuscribete.setBold(True)
        fuenteSuscribete.setFamily("Arial")
        fuenteSuscribete.setPointSize(11)

        labelSuscribete = QLabel("<a href='https://www.facebook.com/Gestor-de-Caudales-Líquidos-y-Sólidos-2291721417728833/'>SUSCRIBETE.</a>", frameBotones)

        labelSuscribete.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        labelSuscribete.setOpenExternalLinks(True)
        labelSuscribete.setFont(fuenteSuscribete)
        labelSuscribete.setAutoFillBackground(True)
        labelSuscribete.setPalette(paletaSuscribete)
        labelSuscribete.setFixedSize(220, 46)
        labelSuscribete.move(0, 210)

      # ========================== FRAME BIENVENIDO - CONFIGURACIÓN ===========

        paletaFrame = self.palette()
        paletaFrame.setColor(QPalette.Background, QColor("#424242"))       # blue

        frameBienvenido = QFrame()
        frameBienvenido.setFrameStyle(QFrame.NoFrame)
        frameBienvenido.setAutoFillBackground(True)
        frameBienvenido.setPalette(paletaFrame)
        frameBienvenido.setFixedHeight(46)

      # ===============================================================0

        paletaTitulo = self.palette()
        paletaTitulo.setColor(QPalette.Foreground, Qt.yellow)

        labelBienvenido = QLabel("BIENVENIDO AL MODULO SE LABORATORIO DEL GQLS")
        labelBienvenido.setAlignment(Qt.AlignCenter)
        labelBienvenido.setFont(fuenteGcls)
        labelBienvenido.setPalette(paletaTitulo)

        botonConfiguracion = QPushButton()
        botonConfiguracion.setIcon(QIcon("Imagenes/configuracion_V01.png"))
        botonConfiguracion.setIconSize(QSize(24, 24))
        botonConfiguracion.setToolTip("Configurar Gcls")
        botonConfiguracion.setCursor(Qt.PointingHandCursor)
        botonConfiguracion.setFixedWidth(36)

        disenioFrame = QHBoxLayout()
        disenioFrame.addWidget(labelBienvenido, Qt.AlignCenter)
        disenioFrame.addStretch()
        disenioFrame.addWidget(botonConfiguracion)
        disenioFrame.setContentsMargins(0, 0, 5, 0)
        frameBienvenido.setLayout(disenioFrame)

      # ===================================================================

        self.buscarLineEdit = QLineEdit()
        self.buscarLineEdit.setObjectName("Enter")
        self.buscarLineEdit.setPlaceholderText("Nombre de la muestra")
        self.buscarLineEdit.setMinimumSize(200, 26)

        botonBuscar = QPushButton("Buscar")
        botonBuscar.setObjectName("Buscar")
        botonBuscar.setCursor(Qt.PointingHandCursor)
        botonBuscar.setMinimumSize(60, 26)

        separadorTodos = QFrame()
        separadorTodos.setFrameShape(QFrame.VLine)
        separadorTodos.setFrameShadow(QFrame.Raised)
        separadorTodos.setFixedSize(1, 26)

        botonTodos = QPushButton("Todos")
        botonTodos.setObjectName("Todos")
        botonTodos.setCursor(Qt.PointingHandCursor)
        botonTodos.setMinimumSize(60, 26)

        nombreColumnas = ("ID", "Código de botella", "N° de repeticiones", "Fecha y hora", "Nivel de cota", "Código de chapa",
                          "Peso de botella con líquido", "Peso de botella vacía", "Peso del agua", "Peso inicial de filtro fino",
                          "Peso final de filtro fino", "Peso inicial de filtro grueso", "Peso final de filtro grueso", "Nombre de la estación")

        menuMostrarOcultar = QMenu()
        for indice, columna in enumerate(nombreColumnas, start=0):
            accion = QAction(columna, menuMostrarOcultar)
            accion.setCheckable(True)
            accion.setChecked(True)
            accion.setData(indice)

            menuMostrarOcultar.addAction(accion)

        botonMostrarOcultar = QPushButton("Mostrar/ocultar columnas")
        botonMostrarOcultar.setCursor(Qt.PointingHandCursor)
        botonMostrarOcultar.setMenu(menuMostrarOcultar)
        botonMostrarOcultar.setMinimumSize(180, 26)

        disenioBuscar = QHBoxLayout()
        disenioBuscar.setSpacing(10)
        disenioBuscar.addWidget(self.buscarLineEdit)
        disenioBuscar.addWidget(botonBuscar)
        disenioBuscar.addWidget(separadorTodos)
        disenioBuscar.addWidget(botonTodos)
        disenioBuscar.addWidget(botonMostrarOcultar)

      # ======================== WIDGET QTableWidget ====================

        self.tabla = QTableWidget()

        # Deshabilitar edición
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Deshabilitar el comportamiento de arrastrar y soltar
        self.tabla.setDragDropOverwriteMode(False)

        # Seleccionar toda la fila
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Seleccionar una fila a la vez
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)

        # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
        # textos que no encajan
        self.tabla.setTextElideMode(Qt.ElideRight)# Qt.ElideNone

        # Establecer el ajuste de palabras del texto
        self.tabla.setWordWrap(False)

        # Deshabilitar clasificación
        self.tabla.setSortingEnabled(False)

        # Establecer el número de nombreColumnas
        self.tabla.setColumnCount(14)

        # Establecer el número de filas
        self.tabla.setRowCount(0)

        # Alineación del texto del encabezado
        self.tabla.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
                                                          Qt.AlignCenter)

        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.tabla.horizontalHeader().setHighlightSections(False)

        # Hacer que la última sección visible del encabezado ocupa todo el espacio disponible
        self.tabla.horizontalHeader().setStretchLastSection(True)

        # Ocultar encabezado vertical
        self.tabla.verticalHeader().setVisible(False)

        # Dibujar el fondo usando colores alternados
        self.tabla.setAlternatingRowColors(True)

        # Establecer altura de las filas
        self.tabla.verticalHeader().setDefaultSectionSize(20)

        # self.tabla.verticalHeader().setHighlightSections(True)

        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tabla.setHorizontalHeaderLabels(nombreColumnas)

        # Menú contextual
        self.tabla.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabla.customContextMenuRequested.connect(self.menuContextual)

        # Establecer ancho de las nombreColumnas
        for indice, ancho in enumerate((40, 120, 130, 140, 100, 130, 190, 160, 140, 200, 200, 200, 200, 160), start=0):
            self.tabla.setColumnWidth(indice, ancho)

        # =============================================================

        disenioBuscarTabla = QVBoxLayout()
        disenioBuscarTabla.addLayout(disenioBuscar)
        disenioBuscarTabla.addWidget(self.tabla)
        disenioBuscarTabla.setSpacing(8)
        disenioBuscarTabla.setContentsMargins(10, 10, 10, 0)

        # ================ LAYOUT DERECHO ==========================

        disenioDerecho = QVBoxLayout()
        disenioDerecho.addWidget(frameBienvenido)
        disenioDerecho.addLayout(disenioBuscarTabla)
        disenioDerecho.setContentsMargins(0, 0, 0, 0)

        # ================= LAYOUT FINAL =================================

        disenioFinal = QGridLayout()
        disenioFinal.addWidget(frameBotones, 0, 0)
        disenioFinal.addLayout(disenioDerecho, 0, 1)
        disenioFinal.setSpacing(0)
        disenioFinal.setContentsMargins(0, 0, 0, 0)

        self.setLayout(disenioFinal)

        # ========================= GUARDAR INFORMACION EN EL PORTAPAPELES =====

        self.copiarInformacion = QApplication.clipboard()

      # ======================== EVENTOS =========================

        botonNuevo.clicked.connect(self.Nuevo)
        botonActualizar.clicked.connect(self.Actualizar)
        botonEliminar.clicked.connect(self.Eliminar)
        botonLimpiar.clicked.connect(self.limpiarTabla)

        self.buscarLineEdit.returnPressed.connect(self.Buscar)
        botonBuscar.clicked.connect(self.Buscar)
        botonTodos.clicked.connect(self.Buscar)

        botonConfiguracion.clicked.connect(lambda: Configuracion(self).exec_())

        self.tabla.itemDoubleClicked.connect(self.Suscribete)

        menuMostrarOcultar.triggered.connect(self.mostrarOcultar)

    # ============================ FUNCIONES ===========================

    def Nuevo(self):
        # nuevoCliente(self).exec_()

        QMessageBox.information(self, "Nueva muestra", "En desarrollo.   ", QMessageBox.Ok)

    def Actualizar(self):
        fila = self.tabla.selectedItems()

        if fila:
            indice = fila[0].row()
            datos = [self.tabla.item(indice, i).text() for i in range(14)]

            QMessageBox.information(self, "Actualizar muestra", "En desarrollo.   ",
                                    QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Actualizar muestra", "Seleccione una muestra.   ",
                                 QMessageBox.Ok)

    def Eliminar(self):
        fila = self.tabla.selectedItems()

        if fila:
            eliminar = QMessageBox(self)

            eliminar.setWindowTitle("Eliminar muestra")
            eliminar.setIcon(QMessageBox.Question)
            eliminar.setText("¿Esta seguro que desea eliminar la muestra?   ")
            botonSi = eliminar.addButton("Si", QMessageBox.YesRole)
            botonCancelar = eliminar.addButton("Cancelar", QMessageBox.NoRole)

            eliminar.exec_()

            if eliminar.clickedButton() == botonSi:
                indiceFila = fila[0].row()
                idMuestra = self.tabla.item(indiceFila, 0).text()

                if QFile.exists("DB_GCLS/DB_GCLS.db"):
                    conexion = sqlite3.connect("DB_GCLS/DB_GCLS.db")
                    cursor = conexion.cursor()

                    try:
                        cursor.execute("DELETE FROM MUESTRAS WHERE ID = ?", (idMuestra,))
                        conexion.commit()

                        conexion.close()

                        self.tabla.removeRow(indiceFila)
                        self.tabla.clearSelection()

                        QMessageBox.information(self, "Eliminar muestra", "Muestra eliminada."
                                                "   ", QMessageBox.Ok)
                    except:
                        conexion.close()
                        QMessageBox.critical(self, "Eliminar muestra", "Error desconocido.   ",
                                             QMessageBox.Ok)
                else:
                    QMessageBox.critical(self, "Buscar muestras", "No se encontro la base de "
                                         "datos.   ", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Eliminar muestra", "Seleccione una muestra.   ",
                                 QMessageBox.Ok)

    def Suscribete(self, celda):
        QMessageBox.warning(self, "Suscribirse", "Hola, l@ invito a que se suscriba al "
                            "canal.\nPor cierto hiciste doble clic sobre esta "
                            "celda: {}.   ".format(celda.text()), QMessageBox.Ok)

    def Buscar(self):
        widget = self.sender().objectName()

        if widget in ("Enter", "Buscar"):
            cliente = " ".join(self.buscarLineEdit.text().split()).lower()

            if cliente:
                sql = "SELECT * FROM MUESTRAS WHERE CODIGO LIKE ?", ("%"+cliente+"%",)
            else:
                self.buscarLineEdit.setFocus()
                return
        else:
            self.buscarLineEdit.clear()
            sql = "SELECT * FROM MUESTRAS"

        if QFile.exists("DB_GCLS/DB_GCLS.db"):
            conexion = sqlite3.connect("DB_GCLS/DB_GCLS.db")
            cursor = conexion.cursor()

            try:
                if widget in ("Enter", "Buscar"):
                    cursor.execute(sql[0], sql[1])
                else:
                    cursor.execute(sql)

                datosDevueltos = cursor.fetchall()
                conexion.close()

                self.tabla.clearContents()
                self.tabla.setRowCount(0)

                if datosDevueltos:
                    fila = 0
                    for datos in datosDevueltos:
                        self.tabla.setRowCount(fila + 1)

                        idDato = QTableWidgetItem(str(datos[0]))
                        idDato.setTextAlignment(Qt.AlignCenter)

                        self.tabla.setItem(fila,  0, idDato)
                        self.tabla.setItem(fila,  1, QTableWidgetItem(datos[1]))
                        self.tabla.setItem(fila,  2, QTableWidgetItem(datos[2]))
                        self.tabla.setItem(fila,  3, QTableWidgetItem(datos[3]))
                        self.tabla.setItem(fila,  4, QTableWidgetItem(datos[4]))
                        self.tabla.setItem(fila,  5, QTableWidgetItem(datos[5]))
                        self.tabla.setItem(fila,  6, QTableWidgetItem(datos[6]))
                        self.tabla.setItem(fila,  7, QTableWidgetItem(datos[7]))
                        self.tabla.setItem(fila,  8, QTableWidgetItem(datos[8]))
                        self.tabla.setItem(fila,  9, QTableWidgetItem(datos[9]))
                        self.tabla.setItem(fila, 10, QTableWidgetItem(datos[10]))
                        self.tabla.setItem(fila, 11, QTableWidgetItem(datos[11]))
                        self.tabla.setItem(fila, 12, QTableWidgetItem(datos[12]))
                        self.tabla.setItem(fila, 13, QTableWidgetItem(datos[13]))
                        self.tabla.setItem(fila, 14, QTableWidgetItem(datos[14]))

                        fila += 1
                else:
                    QMessageBox.information(self, "Buscar muestras", "No se encontro "
                                            "información.   ", QMessageBox.Ok)
            except:
                conexion.close()
                QMessageBox.critical(self, "Buscar muestras", "Error desconocido.   ",
                                     QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Buscar muestras", "No se encontro la base de datos.   ",
                                 QMessageBox.Ok)

        self.buscarLineEdit.setFocus()

    def mostrarOcultar(self, accion):
        columna = accion.data()

        if accion.isChecked():
            self.tabla.setColumnHidden(columna, False)
        else:
            self.tabla.setColumnHidden(columna, True)

    def limpiarTabla(self):
        self.tabla.clearContents()
        self.tabla.setRowCount(0)

    def menuContextual(self, posicion):
        indices = self.tabla.selectedItems()

        if indices:
            menu = QMenu()

            itemsGrupo = QActionGroup(self)
            itemGrupo.setExclusive(True)

            menu.addAction(QAction("Copiar todo", itemsGrupo))

            columnas = [self.tabla.horizontalHeaderItem(columna).text()
                        for columna in range(self.tabla.columnCount())
                        if not self.tabla.isColumnHidden(columna)]

            copiarIndividual = menu.addMenu("Copiar individual")
            for indice, item in enumerate(columnas, start=0):
                accion = QAction(item, itemsGrupo)
                accion = setData(indice)

                copiarIndividual.addAction(accion)

            itemsGrupo.triggered.connect(self.copiarTableWidgetItem)

            menu.exec(self.tabla.viewport().mapToGlobal(posicion))

        def copiarTableWidgetItem(self, accion):
            filaSeleccionada = [dato.text() for dato in self.tabla.selectedItems()]

            if accion.text() == "Copiar todo":
                filaSeleccionada = tuple(filaSelecionada)
            else:
                filaSelecionada = filaSelecionada[accion.data()]

            self.copiarInformacion.clear(mode = QClipboard.Clipboard)
            self.copiarIndividual.setText(str(filaSeleccionada), QClipboard.Clipboard)


# ======================= CLASE Gcls =================================0

class Gcls(QMainWindow):  # class Siacle(QMainWindow):
    def __init__(self, parent=None):
        super(Gcls, self).__init__(parent)

        self.setWindowIcon(QIcon("Imagenes/logoGCLS_N04.png"))
        self.setWindowTitle("Gcls (Gestor de caudales líquidos y solidos - IGP)")
        self.setMinimumSize(820, 302)

        self.initUI()

    def initUI(self):

        # ====================== ITEMS MENÚ ======================

        salir = QAction(self.style().standardIcon(QStyle.SP_MessageBoxCritical), " Salir",
                        self)
        salir.setShortcut("ESC")
        salir.triggered.connect(self.close)

        ayuda = QAction(self.style().standardIcon(QStyle.SP_MessageBoxQuestion),
                        " Ver la Ayuda", self)
        ayuda.setShortcut("Ctrl+A")
        ayuda.triggered.connect(lambda: Ayuda(self).exec_())

        acercaDe = QAction(self.style().standardIcon(QStyle.SP_MessageBoxInformation),
                           " Acerca de", self)
        acercaDe.setShortcut("Ctrl+D")
        acercaDe.triggered.connect(lambda: Acerca(self).exec_())

        # ============== MENÚ ====================================

        menu = self.menuBar()

        gclsMenu = menu.addMenu("&Gcls")    # siacleMenu = menu.addMenu("&Siacle")
        gclsMenu.addAction(salir)             # siacleMenu.addAction(salir)

        ayudaMenu = menu.addMenu("&Ayuda")
        ayudaMenu.addAction(ayuda)
        ayudaMenu.addSeparator()
        ayudaMenu.addAction(acercaDe)

        # ==================== LLAMAR WIDGETS ===============================

        self.widgets = Widgets(self)
        self.setCentralWidget(self.widgets)

        # =============== BARRA DE ESTADO (STATUSBAR) ========================

        labelVersion = QLabel(self)
        labelVersion.setText("GCLS versión beta: 1.0 ")

        hora = QTime.currentTime().toString("hh:mm:ss A ")

        self.labelHora = QLabel(self)
        self.labelHora.setText("Hora: {}".format(hora))

        statusBar = self.statusBar()
        statusBar.addPermanentWidget(self.labelHora, 1)
        statusBar.addPermanentWidget(labelVersion, 0)

        # Actualizar la hora cada segundo (1000 milisegundos)
        self.hora = QTimer(self)
        self.hora.setInterval(1000)
        self.hora.timeout.connect(self.Hora)
        self.hora.start()

    # ===================== FUNCIONES ==============================

    def Hora(self):
        hora = QTime.currentTime().toString("hh:mm:ss A ")
        self.labelHora.setText("Hora: {}".format(hora))

    def closeEvent(self, event):
        cerrar = QMessageBox(self)

        cerrar.setWindowTitle("¿Salir del Gcls?")
        cerrar.setIcon(QMessageBox.Question)
        cerrar.setText("¿Estás seguro que desea cerrar el gestor de caudales líquidos y sólidos?   ")
        botonSalir = cerrar.addButton("Salir", QMessageBox.YesRole)
        botonCancelar = cerrar.addButton("Cancelar", QMessageBox.NoRole)

        cerrar.exec_()

        if cerrar.clickedButton() == botonSalir:
            event.accept()
        else:
            event.ignore()



# ===========================================================

if __name__ == "__main__":

    import sys

    aplicacion = QApplication(sys.argv)

    traductor = QTranslator(aplicacion)
    lugar = QLocale.system().name()
    path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    traductor.load("qtbase_%s" % lugar, path)
    aplicacion.installTranslator(traductor)

    fuente = QFont()
    fuente.setPointSize(10)
    aplicacion.setFont(fuente)

    ventana = Gcls()
    ventana.showMaximized()

    sys.exit(aplicacion.exec_())
