from roam.api import RoamEvents
from PyQt4.QtGui import QLineEdit, QPlainTextEdit, QAction, QIcon, QWidget, QFileDialog
from PyQt4.QtCore import QEvent, pyqtSignal, QFile

from roam.editorwidgets.core import EditorWidget, registerwidgets
from roam.editorwidgets.uifiles import ui_filewidget
from roam.popupdialogs import PickActionDialog
from shutil import copy2
from os.path import basename, splitext
import time
import os
class FileUiWidget(ui_filewidget.Ui_Form, QWidget):
    fileSelected = pyqtSignal()
    def __init__(self, parent=None):
        super(FileUiWidget, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.selectFile)
        self.cancButton.clicked.connect(self.deleteFile)        
        self.filename = ''
        self.lineEdit.setText (self.filename)
        self.lineEdit.setEnabled(False)
    
    def selectFile(self, event):
        file = QFileDialog.getOpenFileName(self, "Select File")
        self.fileSelected.emit()            
        if file is None or not file:
            return
        #self.filename = file
        #self.lineEdit.setText (self.filename)
        self.loadFile(file)
    
    def deleteFile(self, event):
        dir = '_files/'
        if self.filename and self.filename != '':
            if os.path.exists(dir+"/"+self.filename):
                os.remove(dir+"/"+self.filename)
            self.filename = ''
            self.lineEdit.setText ('')
            self.fileSelected.emit()
    
    def loadFile(self, file):
        nomeFile = basename(file)
        extension = splitext(nomeFile)[1]
        t=time.strftime("file_%Y-%m-%d-%H-%M-%S"+extension)
        dir = '_files/'
        if os.path.exists(dir) == False:
            os.mkdir(dir)
        filepath = dir + "/" + t
        copy2(file, filepath)
        if self.filename and self.filename != '':
            if os.path.exists(dir+"/"+self.filename):
                os.remove(dir+"/"+self.filename)
        self.filename = t
        self.lineEdit.setText (file)


class FileWidget(EditorWidget):
    widgettype = 'File'

    def __init__(self, *args):
        super(FileWidget, self).__init__(*args)
        self.defaultlocation = ''

    def createWidget(self, parent):
        return FileUiWidget(parent)

    def initWidget(self, widget):
        widget.fileSelected.connect(self.emitvaluechanged)
        widget.installEventFilter(self)

    def eventFilter(self, object, event):
        # Hack I really don't like this but there doesn't seem to be a better way at the
        # moment
        if event.type() in [QEvent.FocusIn, QEvent.MouseButtonPress]:
            RoamEvents.openkeyboard.emit()
        return False

    def validate(self, *args):
        if not self.value():
            return False
        else:
            return True

    def setvalue(self, value):
        self.widget.lineEdit.setText (value)
        self.widget.filename = value

    def value(self):
        return self.widget.filename
        
    def save(self):
        setvalue('000000000')
            