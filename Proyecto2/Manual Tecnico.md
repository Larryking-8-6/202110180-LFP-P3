# Universidad San Carlos de Guatemala
## Manual Tecnico


Lenguajes Formales y de Programacion
Seccion B+
Auxiliar: Diego Obin
Estudiante: Juan Carlos Gonzalez Valdez - 
Carnet:  202110180
## Introduccion

El siguiente documento describira el codigo realizado en el Compilador NoSQL de MongoDB


## Requerimientos

- Windows 11 
- Python 3.11.0
- Visual Studio Code 64 Bits
- 4Gb de RAM

## Codigo 

#### Main,py 

El primer archivo perteneciente al perfil seria main.py el cual contiene los imports necesarios para crear el ambiente grafico asi como la correcta ejecucion de los comandos necesarios para generar la sentencias y los tokens, para este proyecto se utilizo la libreria PyQt5 para el ambiente grafico y el import sys para poder abrir los documentos

 
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


import sys
import scanner
from scanner import Scanner
from Parser import Parser
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget, QMenu, QMenuBar, QAction, QFileDialog, QVBoxLayout, QWidget, QPlainTextEdit, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont





## Funciones Auxiliares


    
### Scanner,py
El scanner.py es un analizador léxico que se encarga de convertir el código fuente (texto) en una secuencia de tokens que representan los elementos básicos del lenguaje.

El archivo scanner.py contiene la clase Scanner, que tiene varios métodos para procesar y analizar el código fuente. Algunos de los métodos clave en la clase Scanner incluyen:

_init_(self, input_str): Este es el constructor de la clase Scanner. Recibe el código fuente como una cadena de caracteres y realiza la inicialización de las variables de instancia, como la lista de tokens, las palabras clave y los delimitadores.

is_identifier(self, s): Este método verifica si una cadena de caracteres dada es un identificador válido en el lenguaje. Los identificadores son nombres de variables, funciones, clases, etc.

tokenize(self): Este es el método principal que se llama para iniciar el proceso de análisis léxico. Este método implementa un autómata finito determinista (AFD) utilizando una tabla de transiciones (TRANSITION_TABLE) y un conjunto de funciones auxiliares (como is_alpha, is_alnum_or_underscore, is_delimiter, etc.) para procesar el código fuente y generar tokens.

El proceso de análisis léxico comienza con el método tokenize, que itera a través del código fuente y utiliza la tabla de transiciones y las funciones auxiliares para identificar y generar tokens. A medida que se procesa el código fuente, se generan tokens que representan palabras clave, identificadores, delimitadores, números, cadenas y otros elementos básicos del lenguaje.

def is_alpha(c):
    return c.isalpha()

def is_alnum_or_underscore(c):
    return c.isalnum() or c == '_'

def is_delimiter(c):
    return c in r'{}()=,.;"\'\':}-$“”-* /'

def is_digit(c):
    return c.isdigit()

def is_quote(c):
    return c in "\"'"


TRANSITION_TABLE = {
    'S0': {
        'is_alpha': 'S1',
        'is_delimiter': 'S2',
        'is_quote': 'S3',
    },
    'S1': {
        'is_alnum_or_underscore': 'S1',
        'not_is_alnum_or_underscore': 'S0'
    },
    'S2': {
        'not_is_delimiter': 'S0'
    },
    'S3': {
        'is_quote': 'S3_end',
    },
    'S3_end': {
        'not_is_quote': 'S0'
    },
}

def is_comment_start(input_str, i):
    return input_str[i:i+3] == '---'

class Scanner:
    def __init__(self, input_str):
        self.input_str = input_str
        self.tokens = []
        self.keywords = {
            "CrearBD": "CREATE_DB",
            "nueva": "NEW",
            "EliminarBD": "DROP_DB",
            "CrearColeccion": "CREATE_COLLECTION",
            "EliminarColeccion": "DROP_COLLECTION",
            "InsertarUnico": "INSERT_ONE",
            "ActualizarUnico": "UPDATE_ONE",
            "EliminarUnico": "DELETE_ONE",
            "BuscarTodo": "FIND_ALL",
            "BuscarUnico": "FIND_ONE"
        }

        self.delimiters = {
            '{': 'LBRACE',
            '}': 'RBRACE',
            '(': 'LPAREN',
            ')': 'RPAREN',
            '=': 'EQUALS',
            ',': 'COMMA',
            '.': 'DOT',
            ';': 'SEMICOLON',
            '"': 'DQUOTE',
            "'": 'SQUOTE',
            ':': 'COLON',
            '$': 'DOLLAR',
            '“': 'OPEN_QUOTE',
            '”': 'CLOSE_QUOTE',
            '-': 'SPACE',
            '*': 'ASTERISK',
            '/': 'BAR'
        }

    def is_identifier(self, s):
        if s[0].isalpha() or s[0] == '_':
            return all(c.isalnum() or c == '_' for c in s[1:])
        return False

    def tokenize(self):
        self.tokens = []
        state = 'S0'
        line_num = 1
        line_start = 0
        i = 0
        n = len(self.input_str)

        while i < n:
            c = self.input_str[i]

            if is_comment_start(self.input_str, i):
                while i < n and self.input_str[i] != '\n':
                    i += 1
                continue

            if state == 'S0':
                if is_alpha(c):
                    start = i
                    state = TRANSITION_TABLE[state]['is_alpha']
                elif c.isspace():
                    if c == '\n':
                        line_num += 1
                        line_start = i + 1
                    i += 1
                    continue
                elif is_delimiter(c):
                    state = TRANSITION_TABLE[state]['is_delimiter']
                    self.tokens.append((self.delimiters[c], c, line_num, i, i+1))
                elif is_quote(c):
                    start = i
                    state = TRANSITION_TABLE[state]['is_quote']
                elif is_digit(c):
                    state = TRANSITION_TABLE[state]['is_digit']
                    start = i
                else:
                    raise RuntimeError(f'{c!r} inesperado en la línea {line_num}')

            elif state == 'S1':
                if is_alnum_or_underscore(c):
                    state = TRANSITION_TABLE[state]['is_alnum_or_underscore']
                else:
                    token = self.input_str[start:i]
                    if token in self.keywords:
                        self.tokens.append((self.keywords[token], token, line_num, start, i))
                        if token == "nueva":
                            while self.input_str[i].isspace():
                                i += 1
                            if self.input_str[i:i+1] == "=":
                                i += 1
                                self.tokens.append(('EQUALS', '=', line_num, i-1, i))
                            else:
                                i -= 1  # Revert the index back to handle the next token properly
                    elif self.is_identifier(token):
                        self.tokens.append(('ID', token, line_num, start, i))
                    else:
                        raise RuntimeError(f'{token!r} no es una palabra clave ni un identificador válido en la línea {line_num}')
                    state = 'S0'
                    continue

            elif state == 'S2':
                state = 'S0'
                continue

            elif state == 'S3':
                if is_quote(c):
                    state = TRANSITION_TABLE[state]['is_quote']
                i += 1

            elif state == 'S3_end':
                token = self.input_str[start + 1:i - 1]
                self.tokens.append(('STRING', token, line_num, start, i))
                state = 'S0'
                i += 1

            elif state == 'S4':
                if not is_digit(c) and c != '.':
                    token = self.input_str[start:i]
                    self.tokens.append(('NUMBER', token, line_num, start, i))
                    state = 'S0'
                    continue

            i += 1

        return self.tokens + [None]

Esto sigue una sentencia Lexica y Sintactica de la siguiente estructura
LEXICO:
    CrearDB
    EliminarDB
    CrearColeccion
    EliminarColeccion
    InsertarUnico
    ActualizarUnico
    EliminarUnico
    BuscarTodo
    BuscarUnico
    nueva
    (
    )
    ;
    =
    ID -> [a-z_A-Z_][a-z_A-Z_0-9]*
    NUMERO -> [0-9]+
    STRING -> "[^"]*"
    IGNORE -> \t\r
    COMENTARIOS -> //.*
                | /\([^]|\+[^/])\+/
    "

SINTACTICO:
    init : instrucciones

    instrucciones : instruccion instrucciones
                | instruccion

    instruccion : crearDB ;
                | eliminarDB ; 
                | crearColeccion ;
                | eliminarColeccion ;
                | insertarUnico ;
                | actualizarUnico ;
                | eliminarUnico ;
                | buscarTodo ;
                | buscarUnico ;

    crearDB : CrearDB ID = nueva CrearDB ( )

    eliminarDB : EliminarDB ID = nueva EliminarDB ( )

    crearColeccion : CrearColeccion ID = nueva CrearColeccion ( STRING )

    eliminarColeccion : EliminarColeccion ID = nueva EliminarColeccion ( STRING )

    insertarUnico : InsertarUnico ID = nueva InsertarUnico ( STRING , STRING )

    actualizarUnico : ActualizarUnico ID = nueva ActualizarUnico ( STRING , STRING )

    eliminarUnico : EliminarUnico ID = nueva EliminarUnico ( STRING )

    buscarTodo : BuscarTodo ID = nueva BuscarTodo ( STRING )

    buscarUnico : BuscarUnico ID = nueva BuscarUnico ( STRING )
## Parser,py
El archivo Parser.py alberga la clase Parser, que cuenta con diversos métodos para examinar y tratar los tokens creados por el Scanner. Dichos métodos se ejecutan según las normas gramaticales del lenguaje y la organización del código fuente. Algunos métodos importantes en la clase Parser son:

init(self, tokens): Es el constructor de la clase Parser. Acepta la lista de tokens creada por el Scanner e inicializa las variables de instancia, como el índice del token actual y el token en sí.

parse(self): Es el método principal que se invoca para comenzar el análisis. Inicia la creación del AST llamando a otros métodos de la clase Parser.

Métodos para analizar reglas gramaticales: Estos métodos tienen nombres como parse_statement, parse_expression, etc., y se encargan de examinar las distintas reglas gramaticales del lenguaje. Cada método evalúa una sección específica de la gramática y crea nodos del AST correspondientes a esa sección.

Métodos para procesar tokens: Estos métodos tienen nombres como consume, match, etc., y se emplean para procesar tokens de la lista y comprobar que cumplen con las expectativas del Parser según las normas gramaticales. Si se encuentra un token inesperado, estos métodos generarán un error.

El análisis se inicia con el método parse, que a su vez invoca otros métodos de la clase Parser en función de las normas gramaticales del lenguaje y la organización del código fuente. A medida que se examinan los tokens, se van creando nodos del AST. Al finalizar el análisis, se obtiene un AST completo que representa la estructura y el significado del código fuente.

En resumen, Parser.py contiene una clase Parser que implementa un analizador sintáctico para el lenguaje en cuestión. El Parser emplea una serie de métodos para evaluar las normas gramaticales del lenguaje y construir un AST a partir de la lista de tokens generada por el Scanner.
