import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from highlighter import SyntaxHighlighter
from lexer import tokenize
from parser import Parser

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/main.ui", self)

        self.highlighter = SyntaxHighlighter(self.codeEditor.document())
        self.codeEditor.textChanged.connect(self.parse_code)  
         

    def parse_code(self):  
        code = self.codeEditor.toPlainText()
        try:
            tokens = tokenize(code)
            parser = Parser(tokens)
            parser.parse()
            self.statusLabel.setText("✅ Geçerli sözdizimi.")
        except SyntaxError as e:
            self.statusLabel.setText(f"❌ Hata: {e}")
        except Exception as ex:
            import traceback
            self.statusLabel.setText(str(ex))
            traceback.print_exc()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
