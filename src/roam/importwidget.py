import sqlite3
import time
import os
import struct
import shutil
import errno
import sys
import datetime

from PyQt4.QtCore import pyqtSignal, QThread, QObject
from PyQt4.QtGui import QWidget, QFileDialog, QMessageBox, QIcon
from qgis.core import QgsGPSDetector, QGis

import roam
import roam.utils as utils
import roam.config
from roam.ui.ui_import import Ui_importWidget
from roam.api.events import RoamEvents

def alert(text):
    msgBox=QMessageBox()
    msgBox.setText(text)
    msgBox.setWindowTitle("IntraMaps Roam")
    icon = QIcon(":/icons/info")
    msgBox.setWindowIcon(icon)
    msgBox.exec_()


class ImportWidget(Ui_importWidget, QWidget):
    settingsupdated = pyqtSignal(object)

    def __init__(self, parent=None):
        super(ImportWidget, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.pushButton_2.clicked.connect(self.import_)
        self.dir = os.path.expanduser("~")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setText (self.dir)
        self.projectpaths = os.path.dirname(sys.argv[0])+"/projects"

    def eventFilter(self, object, event):
        if event.type() == QEvent.FocusIn:
            RoamEvents.openkeyboard.emit()
        return False
		
    def pushButtonClicked(self):
        dir = QFileDialog.getExistingDirectory(self,"Choose directory",self.dir,QFileDialog.ShowDirsOnly)
        if dir:
            self.dir = dir
            self.lineEdit.setText (self.dir)

    
    def import_(self):
        if os.path.exists(self.dir):
            if os.path.exists(self.dir+"/project.qgs") and os.path.exists(self.dir+"/project.config"):
                t=time.strftime("%Y%m%d%H%M%S")
                new_dir="Imported_project_"+t
                self.makedirs(self.projectpaths+"/"+new_dir)
                self.copyFilesWithProgress(self.dir, self.projectpaths+"/"+new_dir)
                
                msgBox=QMessageBox()
                msgBox.setText("The project has imported.")
                msgBox.setInformativeText("Per vedere il progetto importato bisogna riavviare l'applicazione. Riavviare ora?")
                msgBox.addButton(QMessageBox.Yes)
                msgBox.addButton(QMessageBox.No)
                msgBox.setWindowTitle("IntraMaps Roam")
                icon = QIcon(":/icons/info")
                msgBox.setWindowIcon(icon)
                ret = msgBox.exec_()
                if ret==QMessageBox.Yes:
                    app1 = sys.executable
                    sys.argv[0]='"'+sys.argv[0]+'"'
                    os.execvp(app1,  sys.argv)
                else:
                    a=0
            else:
                alert("Directory is not valid")
        else:
            alert("Path doesn't exist")

    def copy(self, src, dest):
        try:
            shutil.copytree(src, dest)
        except OSError as e:
            # If the error was caused because the source wasn't a directory
            if e.errno == errno.ENOTDIR:
                shutil.copy(src, dst)
            else:
                utils.log('Directory not copied. Error: %s' % e)#print('Directory not copied. Error: %s' % e)
	
    def makedirs(self, dest):
        if not os.path.exists(dest):
                os.makedirs(dest)
  
    def countFiles(self, directory):
        files = []
        if os.path.isdir(directory):
            for path, dirs, filenames in os.walk(directory):
                files.extend(filenames)
        return len(files)			
		
    def copyFilesWithProgress(self, src, dest):
        self.pushButton.setEnabled(False)
        numFiles = self.countFiles(src)
        if numFiles > 0:
            self.makedirs(dest)
            numCopied = 0
            for path, dirs, filenames in os.walk(src):
                for directory in dirs:
                    destDir = path.replace(src,dest)
                    self.makedirs(os.path.join(destDir, directory))
                for sfile in filenames:
                    srcFile = os.path.join(path, sfile)
                    destFile = os.path.join(path.replace(src, dest), sfile)
                    shutil.copy(srcFile, destFile)
                    numCopied += 1
        self.pushButton.setEnabled(True)
