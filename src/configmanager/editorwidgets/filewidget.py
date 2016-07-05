from configmanager.editorwidgets.core import ConfigWidget
from configmanager.editorwidgets.uifiles.ui_filewidget_config import Ui_Form


class FileWidgetConfig(Ui_Form, ConfigWidget):
    description = 'Free text field'

    def __init__(self, parent=None):
        super(FileWidgetConfig, self).__init__(parent)
        self.setupUi(self)

