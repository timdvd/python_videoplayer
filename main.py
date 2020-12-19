import sys
from PyQt5.QtWidgets import QApplication
from mediaPlayer import MediaWindow

app = QApplication(sys.argv)

mediaPlayerWindow = MediaWindow()

sys.exit(app.exec_())