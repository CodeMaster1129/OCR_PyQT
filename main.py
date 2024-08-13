import sys
from paddleocr import PaddleOCR
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene, QGraphicsPixmapItem, QGraphicsView, QGraphicsItem
from PyQt5.QtGui import QPixmap, QImage, QPainter
from PyQt5.QtCore import Qt
import fitz  
from dashboard import Ui_dashboard  
import numpy as np

class MyApp(QMainWindow, Ui_dashboard):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.upload_btn.clicked.connect(self.upload_pdf)
        self.rotate_left_btn.clicked.connect(self.rotate_left)
        self.rotate_right_btn.clicked.connect(self.rotate_right)
        self.zoom_in_btn.clicked.connect(self.zoom_in)
        self.zoom_out_btn.clicked.connect(self.zoom_out)
        self.load_flag = False
        self.pdf_document = None
        self.current_page = 0
        self.rotation_angle = 0
        self.zoom_factor = 1.0
        self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ocr = PaddleOCR(use_angle_cls=True, lang="en")

    def upload_pdf(self):
        self.load_flag = False
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf)", options=options)
        if file_name:
            self.load_pdf(file_name)
        self.file_name.setText("FILE(Uploaded) - "+file_name.split("/")[-1])

    def load_pdf(self, file_name):
        self.pdf_document = fitz.open(file_name)
        self.current_page = 0
        self.rotation_angle = 0
        self.zoom_factor = 1.0
        self.display_page()

    def processing_ocr(self, image):
        init_size = image.byteCount()
        ptr = image.bits()
        ptr.setsize(init_size)
        arr = np.array(ptr).reshape(image.height(), image.width(), 3)
        result = self.ocr.ocr(arr, cls=True)
        for line in result:
            for elements in line:
                print("dddddd", elements[1][0])

    def display_page(self):
        if self.pdf_document:
            page = self.pdf_document.load_page(self.current_page)
            matrix = fitz.Matrix(self.zoom_factor, self.zoom_factor).prerotate(self.rotation_angle)
            pix = page.get_pixmap(matrix=matrix, alpha=False)
            image = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
            if self.load_flag == False:
                self.processing_ocr(image)
                self.load_flag = True
            pixmap = QPixmap.fromImage(image)
            scene = QGraphicsScene(self)
            item = QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            self.graphicsView.setScene(scene)
            self.graphicsView.setRenderHint(QPainter.SmoothPixmapTransform)  # Improve scaling quality
            self.graphicsView.setRenderHint(QPainter.Antialiasing)  # Smooth rendering

    def rotate_left(self):
        self.rotation_angle -= 90
        self.display_page()

    def rotate_right(self):
        self.rotation_angle += 90
        self.display_page()

    def zoom_in(self):
        self.zoom_factor *= 1.2  
        self.display_page()

    def zoom_out(self):
        self.zoom_factor /= 1.2  
        self.display_page()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
