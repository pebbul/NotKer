"""
DOCUMENTATION:
------------------------
Format: 		For:

First letter 	Class
in caps			

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
		text = QTextEdit()
		self.setCentralWidget(text)

		#Status Bar
		#stat = self.statusBar()
		self.setStatusBar(QStatusBar(self))



# Menu Functions
newFile = QAction("&New")

openFile = QAction("&Open")

saveFile = QAction("&Save")

saveAsFile = QAction("&Save As")


# App Execution
win = MainWin()
win.resize(1280, 800)
win.show()
app.exec_()



