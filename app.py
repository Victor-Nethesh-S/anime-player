from PySide6.QtWidgets import QApplication, QWidget

import sys

app = QApplication(sys.argv)
window = QWidget()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.
app.exec()