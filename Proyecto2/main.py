import sys
import scanner
from scanner import Scanner
from Parser import Parser
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget, QMenu, QMenuBar, QAction, QFileDialog, QVBoxLayout, QWidget, QPlainTextEdit, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ventana principal
        self.setWindowTitle('Compilador NoSQL - 202110180 - LFP')
        self.setGeometry(100, 100, 1200, 800)

        # Estilo de la interfaz de usuario
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ffb347;
            }
            QPlainTextEdit, QTextEdit, QTableWidget {
                background-color: #ffffff;
                color: #000000;
                selection-background-color: #ff6961;
                selection-color: #ffffff;
                border: 1px solid #333333;
            }
            QDockWidget::title {
                background-color: #6ba8a9;
                color: #ffffff;
                padding-left: 4px;
            }
            QDockWidget {
                font: 10pt "Courier";
            }
            QMenu::item {
                color: #000000;
            }
            QMenu::item:selected {
                color: #ffffff;
                background-color: #ff6961;
            }
            QMenuBar {
                background-color: #6ba8a9;
                color: #ffffff;
            }
            QMenuBar::item {
                color: #000000;
            }
            QMenuBar::item:selected {
                color: #ffffff;
                background-color: #ff6961;
            }
            QTableWidget::item {
                color: #000000;
            }
            QTableWidget::item:selected {
                color: #ffffff;
                background-color: #ff6961;
            }
        """)

        self.init_ui()

    def init_ui(self):

        self.code_editor = QPlainTextEdit(self)
        self.code_editor.setFont(QFont("Courier", 12))
        self.setCentralWidget(self.code_editor)

        self.sentences_viewer = QTextEdit(self)
        self.sentences_viewer.setReadOnly(True)
        self.sentences_dock = QDockWidget("Sentencias Generadas", self)
        self.sentences_dock.setWidget(self.sentences_viewer)
        self.addDockWidget(2, self.sentences_dock)

        self.tokens_table = QTableWidget(self)
        self.tokens_table.setColumnCount(4)
        self.tokens_table.setHorizontalHeaderLabels(['No.', 'Tipo', 'Linea', 'Lexema'])
        self.tokens_dock = QDockWidget("Tokens", self)
        self.tokens_dock.setWidget(self.tokens_table)
        self.addDockWidget(2, self.tokens_dock)

        self.errors_table = QTableWidget(self)
        self.errors_table.setColumnCount(5)
        self.errors_table.setHorizontalHeaderLabels(['Tipo', 'Linea', 'Columna', 'Token', 'Descripcion'])
        self.errors_dock = QDockWidget("Errores", self)
        self.errors_dock.setWidget(self.errors_table)
        self.addDockWidget(2, self.errors_dock)

        self.menu_archivo = QMenu("Archivo", self)
        self.menu_analisis = QMenu("Análisis", self)
        self.menu_ver = QMenu("Ver", self)

        self.action_nuevo = QAction("Nuevo", self)
        self.action_abrir = QAction("Abrir", self)
        self.action_guardar = QAction("Guardar", self)
        self.action_guardar_como = QAction("Guardar como", self)
        self.action_salir = QAction("Salir", self)

        self.menu_archivo.addAction(self.action_nuevo)
        self.menu_archivo.addAction(self.action_abrir)
        self.menu_archivo.addAction(self.action_guardar)
        self.menu_archivo.addAction(self.action_guardar_como)
        self.menu_archivo.addSeparator()
        self.menu_archivo.addAction(self.action_salir)

        self.action_analizar = QAction("Generar sentencias MongoDB", self)
        self.menu_analisis.addAction(self.action_analizar)

        self.action_ver_tokens = QAction("Tokens", self)
        self.menu_ver.addAction(self.action_ver_tokens)

        self.menu_bar = QMenuBar(self)
        self.menu_bar.addMenu(self.menu_archivo)
        self.menu_bar.addMenu(self.menu_analisis)
        self.menu_bar.addMenu(self.menu_ver)
        self.setMenuBar(self.menu_bar)

        self.action_abrir.triggered.connect(self.open_file)
        self.action_guardar.triggered.connect(self.save_file)
        self.action_guardar_como.triggered.connect(self.save_file_as)
        self.action_nuevo.triggered.connect(self.new_file)
        self.action_salir.triggered.connect(self.close)
        self.action_analizar.triggered.connect(self.analyze_code)
        self.action_ver_tokens.triggered.connect(self.show_tokens)

    def new_file(self):
        if self.code_editor.document().isModified():
            pass 

        self.code_editor.clear()

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                self.code_editor.setPlainText(file.read())

    def save_file(self):
        if not self.code_editor.document().isModified():
            return

        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(self.code_editor.toPlainText())

    def save_file_as(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Guardar archivo como", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.code_editor.toPlainText())

    def analyze_code(self):
        input_str = self.code_editor.toPlainText()
        scanner_instance = scanner.Scanner(input_str)
        tokens = scanner_instance.tokenize()  # Obtener los tokens
        parser = Parser(tokens)  # Crear una instancia del analizador con los tokens

        try:
            result = parser.parse()
            print(result)

            mongodb_statements = []
            for stmt in result:
                if stmt[0] == "CREATE_DB":
                    mongodb_statements.append("use " + stmt[1])
                    print("CREATE_DB:", stmt[1])
                elif stmt[0] == "DROP_DB":
                    mongodb_statements.append("db.dropDatabase()")
                    print("DROP_DB")
                elif stmt[0] == "CREATE_COLLECTION":
                    mongodb_statements.append(f"db.createCollection('{stmt[1]}')")
                    print("CREATE_COLLECTION:", stmt[1])
                    mongodb_statements.append(f"db.createCollection('{stmt[1]}')")
                elif stmt[0] == "DROP_COLLECTION":
                    mongodb_statements.append(f"db.{stmt[1]}.drop()")
                elif stmt[0] == "INSERT_ONE":
                    mongodb_statements.append(f"db.{stmt[1]}.insertOne({stmt[2]})")
                elif stmt[0] == "UPDATE_ONE":
                    mongodb_statements.append(f"db.{stmt[1]}.updateOne({stmt[2]}, {stmt[3]})")
                elif stmt[0] == "DELETE_ONE":
                    mongodb_statements.append(f"db.{stmt[1]}.deleteOne({stmt[2]})")
                elif stmt[0] == "FIND_ALL":
                    mongodb_statements.append(f"db.{stmt[1]}.find()")
                elif stmt[0] == "FIND_ONE":
                    mongodb_statements.append(f"db.{stmt[1]}.findOne({stmt[2]})")

            self.sentences_viewer.setPlainText("\n".join(mongodb_statements))
            self.show_tokens(parser.tokens)
            self.tokens_table.update()
        except Exception as e:
            self.update_error_table(f"Error inesperado: {str(e)}")
            self.errors_table.update()
        print("Result:", result)

    def update_error_table(self, error_msg):
        self.errors_table.setRowCount(1)
        self.errors_table.setItem(0, 0, QTableWidgetItem("Error"))
        self.errors_table.setItem(0, 1, QTableWidgetItem("-"))
        self.errors_table.setItem(0, 2, QTableWidgetItem("-"))
        self.errors_table.setItem(0, 3, QTableWidgetItem("-"))
        self.errors_table.setItem(0, 4, QTableWidgetItem(error_msg))

    def show_tokens(self, tokens):
        scanner = Scanner(self.code_editor.toPlainText())
        tokens = scanner.tokenize()
        print("Tokens:", tokens)  # Imprime la variable tokens aquí para ver su valor
        
        if isinstance(tokens, list):
            self.tokens_table.setRowCount(len(tokens))
            for i, token in enumerate(tokens):
                self.tokens_table.setItem(i, 0, QTableWidgetItem(str(i + 1)))
                self.tokens_table.setItem(i, 1, QTableWidgetItem(token[0]))
                self.tokens_table.setItem(i, 2, QTableWidgetItem(str(token[2])))
                self.tokens_table.setItem(i, 3, QTableWidgetItem(token[1]))
        else:
            print("Error: tokens no es una lista")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())