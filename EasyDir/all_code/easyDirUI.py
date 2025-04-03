# Import necessary Qt modules
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QWidget)

from easyDirCreateButtonLogic import easyDircreateButtonLogicFunc

from EasyDirHistoryFetch import fetch_xml_data, load_project_names


# Define the Ui_MainWindow class to set up the UI components
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Set the object name for the main window if not set
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        
        # Resize and set size policy for the main window
        MainWindow.resize(416, 354)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        
        # Set the minimum and maximum size for the window
        MainWindow.setMinimumSize(QSize(416, 354))
        MainWindow.setMaximumSize(QSize(416, 354))
        
        # Set the background auto-fill behavior and tab shape
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)

        # Create central widget and set it as the central widget for MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # Create and configure the 'Create' button
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 300, 91, 24))

        # Label to display subfolder list information
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 250, 301, 16))

        # LineEdit to allow user input for subfolder list
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(20, 270, 381, 21))

        # Tab widget to hold different tabs (Excel and SingleShot)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 150, 391, 91))

        # First tab for Excel-related inputs
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 131, 16))
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 111, 16))
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 30, 361, 21))
        self.tabWidget.addTab(self.tab, "Excel_Tab")

        # Second tab for SingleShot-related inputs
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.lineEdit_7 = QLineEdit(self.tab_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(10, 30, 151, 21))
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 31, 16))
        self.lineEdit_8 = QLineEdit(self.tab_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(200, 30, 161, 21))
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(200, 10, 41, 16))
        self.tabWidget.addTab(self.tab_2, "SingleShot")

        # Label for the "Easy Dir" heading with a custom font
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(120, 50, 181, 51))
        font = QFont()
        font.setFamilies([u"Modern"])
        font.setPointSize(5)
        font.setBold(True)
        font.setUnderline(False)
        self.label_8.setFont(font)

        # Label and input for directory path
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 120, 131, 16))
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(100, 120, 301, 21))

        # Label and input for project name
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(240, 10, 81, 16))
        self.lineEdit_9 = QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(320, 10, 81, 21))

        # Label for the "History" section
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 10, 81, 16))

        # ComboBox for additional user options
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(60, 10, 80, 24))

        # Button to trigger fetch action
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 10, 51, 24))

        # Set the central widget to the main window
        MainWindow.setCentralWidget(self.centralwidget)

        # Create menu bar and status bar
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 416, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Call retranslate function to set all labels and text in the UI
        self.retranslateUi(MainWindow)

        # Set the default tab to the first tab
        self.tabWidget.setCurrentIndex(0)

        # Connect the slots for the UI
        QMetaObject.connectSlotsByName(MainWindow)

         # Load project names from XML file and populate the dropdown
        project_names = load_project_names()
        self.populate_dropdown(project_names)

    def populate_dropdown(self, project_names):
        """Populates the comboBox with project names."""
        self.comboBox.addItems(project_names)

    # Function to handle translation of the UI components
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EasyDir", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.pushButton.clicked.connect(self.createButtonClick)

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"subFolder List ( ex :- \"Blender\", \"Textures\", \"Photoshop\" )", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"Blender, Textures, Photoshop , Downloads , Nuke , davinci , BlenderRender , nukeRender , otherRender, embergenFile , VDBs , Alembic, Obj, Colada, Mixamo, Temp , Hdri, Gobos , Marvolues , Refference , Others", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Excel_Path", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Excel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Seq", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Shot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"SingleShot", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Easy Dir", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Directory_Path", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Project Name", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"History", None))


        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Fetch", None))
        self.pushButton_2.clicked.connect(self.fetchButtonClick)



    #Create Button Function Connect
    def createButtonClick(self):
        excel_path = self.lineEdit.text().strip()  # Excel file path
        base_directory = self.lineEdit_6.text().strip()  # Base directory path
        subfolders = self.lineEdit_5.text().strip()  # Subfolder list
        
        SequenceSingleShot = self.lineEdit_7.text().strip()  # First SingleShot input
        shotSingleShot = self.lineEdit_8.text().strip()  # Second SingleShot input
        
        project_name = self.lineEdit_9.text().strip()  # Project name

        current_tab_index = self.tabWidget.currentIndex() # current_tab_index
        easyDircreateButtonLogicFunc(excel_path, base_directory, subfolders, SequenceSingleShot, shotSingleShot, project_name, current_tab_index)

    def fetchButtonClick(self):
        fetch_xml_data(self)  # Pass the UI object


