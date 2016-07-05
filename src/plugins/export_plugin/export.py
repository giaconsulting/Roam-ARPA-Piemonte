import sqlite3
import time
import os
import struct
import shutil
import errno
from PyQt4.QtCore import Qt, QObject, pyqtSignal, QThread, QEvent
from PyQt4.QtGui import QWidget, QGridLayout, QLabel, QListWidgetItem, QStyledItemDelegate, QFontMetricsF, QTextOption, QFileDialog, QMessageBox, QIcon, QPixmap
from PyQt4.uic import loadUiType

from roam import utils
import roam.utils

import roam.api.utils
from roam.flickwidget import FlickCharm
from roam.api.events import RoamEvents
from roam.api.plugins import Page


_fromUtf8 = lambda s: s

def resolve(name):
    f = os.path.join(os.path.dirname(__file__), name)
    return f


widget, base = loadUiType(resolve("ui_export.ui"))


def alert(text):
    msgBox=QMessageBox()
    msgBox.setText(text)
    msgBox.setWindowTitle("IntraMaps Roam")
    icon = QIcon(":/icons/info")
    msgBox.setWindowIcon(icon)
    msgBox.exec_()


class ExportPlugin(widget, base, Page):
    title = "Export"
    icon = resolve("export.svg")

    def __init__(self, api, parent=None):
        super(ExportPlugin, self).__init__(parent)
        self.setupUi(self)
        self.api = api
        self.project = None
        self.pushButton_2.clicked.connect(self.pushButtonClicked)
        self.pushButton.clicked.connect(self.export)
        self.dir = os.path.expanduser("~")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setText (self.dir)

    def eventFilter(self, object, event):
        if event.type() == QEvent.FocusIn:
            RoamEvents.openkeyboard.emit()
        return False
		
    def pushButtonClicked(self):
        dir = QFileDialog.getExistingDirectory(self,"Choose directory",self.dir,QFileDialog.ShowDirsOnly)
        if dir:
            self.dir = dir
            self.lineEdit.setText (self.dir)

    def project_loaded(self, project):
        self.project = project

    
    def export(self):
        if os.path.exists(self.dir):
            self.copyFilesWithProgress(self.project.folder,self.dir+"/"+self.project.settings['title'])
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
                    #p.calculateAndUpdate(numCopied, numFiles)
            alert("Project been exported.");
        self.pushButton.setEnabled(True)

