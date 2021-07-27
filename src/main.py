"""
DOCUMENTATION:
------------------------
Format: 		For:

First letter 	Class
in caps	

First two 		Element
letters in
caps		

all lower		Var

camelCase		Function
------------------------
Issues:
------------------------
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence, QPalette, QColor

# Initialises app via creating an instance
app = QApplication(sys.argv)

# App Contents
class MainWin(QMainWindow):
	def __init__(self):
		# Utilises QMainWindow lib functions for the app
		super().__init__()
		self.setWindowTitle("NotKer")

		# Menu Functions
		newFile = QAction("&New", self)

		openFile = QAction("&Open", self)
		openFile.setShortcut("Ctrl+O")
		openFile.triggered.connect(self.file_open)

		saveFile = QAction("&Save", self)
		saveFile.setShortcut("Ctrl+S")
		saveFile.triggered.connect(self.file_save)

		saveAsFile = QAction("&Save As", self)

		# Menu Bar
		menu = self.menuBar()
		menu_file = menu.addMenu("&File")
		menu_file.addAction(newFile)
		menu_file.addSeparator()
		menu_file.addAction(openFile)
		menu_file.addSeparator()
		menu_file.addAction(saveFile)
		menu_file.addAction(saveAsFile)

		#Tool Bar
	
		# Main Text
		editor = QTextEdit()
		self.setCentralWidget(editor)

		#Status Bar
		#stat = self.statusBar()
		self.setStatusBar(QStatusBar(self))

	#Supporting Functions for Menu Bar (Doesnt work atm)

	def file_open(self):
		name = QFileDialog.getOpenFileName(self, "Open File")
		file = open(name,"r")
		with  file:
			text = file.read()
			editor.textEdit.setText(text)

	def file_save(self):
		name = QFileDialog.getSaveFileName(self, "Save File")
		file = open(name,"w")
		text = self.textEdit.toPlainText()
		file.write(text)
		file.close()

# App Execution
win = MainWin()
win.resize(1280, 800)
win.show()
app.exec_()



