from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QWidget
from PySide6.QtCore import QSize

from methods import scrape, convert_XML_to_XLSX

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.specimen_data = []
        
        self.setWindowTitle("Hello User! I convert files!")
        
        # this button prompts the user to select a file to load
        self.button1 = QPushButton("Select File")
        self.button1.clicked.connect(self.select_file)
        self.label1 = QLabel("Once a file is loaded, the input path will be displayed here.")
    
        # this button prompts the user to select a save location for the transformed file
        self.button2 = QPushButton("Save File"); self.button2.setEnabled(False)
        self.button2.clicked.connect(self.save_file)
        self.label2 = QLabel("I am deactivated, no file is ready for saving.")
        
        # generating application layout pattern
        layout = QVBoxLayout(); layout1 = QHBoxLayout(); layout2 = QHBoxLayout()
        layout1.addWidget(self.button1); layout1.addWidget(self.label1)
        layout2.addWidget(self.button2); layout2.addWidget(self.label2)
        layout.addLayout(layout1); layout.addLayout(layout2)
        
        container = QWidget()
        container.setLayout(layout)
        self.setFixedSize(QSize(600, 450))
        self.setCentralWidget(container)
    
    # this method retrieves the xml filepath from a file dialog, saves specimen data as a 2D array, and updates widget states
    def select_file(self):
        
        # reading in xml filepath and loading data as 2D array
        infile_path, active_filter = QFileDialog.getOpenFileName(self, filter="Extensible Markup Language (*.xml)", dir="")
        self.specimen_data = scrape(infile_path)
        
        # updating application state
        self.button1.setEnabled(False); self.label1.setText(f"I am deactivated. The path of the loaded file is: \n {infile_path}")
        self.button2.setEnabled(True); self.label2.setText("Once a file is saved, the output path will be displayed here.")
        
    # this method retrives the save location from a file dialog, exports specimen data as a .xlsx, and updates widget states
    def save_file(self):
        
        # reading in intended save location and exporting .xlsx
        outfile_path, active_filter = QFileDialog.getSaveFileName(self, filter="Microsoft Excel Spreadsheet (*.xlsx)", dir="")
        convert_XML_to_XLSX(outfile_path, self.specimen_data); self.specimen_data = []
        
        #updating application state
        self.button1.setEnabled(True); self.label1.setText("Once another file is loaded, the input path will be displayed here.")
        self.button2.setEnabled(False); self.label2.setText(f"I am deactivated. The path of the last saved file is: \n {outfile_path}")
        
app = QApplication([])

window = MainWindow()
window.show()

app.exec()