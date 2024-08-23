import json
import sys
from paddleocr import PaddleOCR
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene, QGraphicsPixmapItem, QGraphicsView, QGraphicsItem, QComboBox
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

    def parse_ocr_text(self, data):
        formatted_data = {}
        items = []

        for entry in data:
            if not entry:
                continue

            line = entry[0]

            if "Invoice" in line:
                 formatted_data['invoice_number'] = line.split(":")[1].strip()
            elif "Date" in line:
                formatted_data['date'] = line.split(":")[1].strip() + ":" + line.split(":")[2].strip()
            elif "Table" in line:
                formatted_data['table'] = line.split(":")[1].strip()
            elif "Order No" in line:
                formatted_data['order_number'] = line.split(":")[1].strip()
            elif "Host" in line:
                formatted_data['host'] = line.split(":")[1].strip()
            elif "Order Type" in line:
                formatted_data['order_type'] = line.split(":")[1].strip()
            elif "VAT#" in line:
                formatted_data['vat_number'] = line.split("#")[1].strip()
            elif "Total Before Discount" in line:
                formatted_data['total_before_discount'] = entry[1]
            elif "Round Off" in line:
                formatted_data['round_off'] = entry[1]
            elif "Total Before VAT" in line:
                formatted_data['total_before_vat'] = entry[1]
            elif "VAT Amount" in line:
                formatted_data['vat_amount'] = entry[1]
            elif "Service Charge" in line:
                formatted_data['service_charge'] = entry[1]
            elif "Total" in line and "Before" not in line:
                formatted_data['total'] = line.strip()
            elif "Change Due" in line:
                formatted_data['change_due'] = entry[1]
            elif "Qty" in line:  # Start of items
                continue  # Skip header line
            else:
                continue
                if len(entry) == 3:
                    item = {
                        "quantity": int(entry[0].strip()),
                        "name": entry[1].strip(),
                        "amount": float(entry[2].strip())
                    }
                    items.append(item)

        formatted_data['items'] = items

        return json.dumps(formatted_data, indent=4)


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

        res = []
        first_y = 0
        temp = []

        for line in result[0]:
            print(line)
            if line[1][1] < 0.8:
                continue
            flag = False
            for i in range(1):
                if abs(line[0][i][1] - first_y) > 8:
                    flag = True
                    break
                elif line[0][i][1] < first_y:
                    first_y = line[0][i][1]
            if flag:
                res.append(temp)
                temp = [line[1][0]]
                first_y = line[0][0][1]
            else:
                temp.append(line[1][0])

        data = self.parse_ocr_text(res)
        self.update_ui_with_data(data)

    def update_ui_with_data(self, formatted_data):
        data = json.loads(formatted_data)

        self.doc_number.setText(data.get('invoice_number', ''))
        self.bp_name.setText(data.get('host', ''))
        self.date.setText(data.get('date', ''))
        self.terms.setText(data.get('order_type', ''))
        self.round_off.setText(data.get('round_off', ''))
        self.total.setText(data.get('total', ''))
        self.discount.setText(data.get('service_charge', ''))
        self.gst.setText(data.get('vat_amount', ''))
        self.vat.setText(data.get('vat_number', ''))
        self.net_amount.setText(data.get('total_before_vat', ''))
        self.description.setText('')

        # self.items_table.clear()  # Clear existing items
        # self.items_table.setRowCount(0)  # Reset row count
        # for item in data.get('items', []):
        #     row_position = self.items_table.rowCount()
        #     self.items_table.insertRow(row_position)
        #     self.items_table.setItem(row_position, 0, QTableWidgetItem(str(item['quantity'])))
        #     self.items_table.setItem(row_position, 1, QTableWidgetItem(item['name']))
        #     self.items_table.setItem(row_position, 2, QTableWidgetItem(f"{item['amount']:.2f}"))

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
