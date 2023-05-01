#Las pruebas del proyecto
# import tkinter as tk

# # ventana principal
# root = tk.Tk()
# root.title("Proyecto 2 - 202110180")

# # marco para la entrada de texto
# input_frame = tk.Frame(root)
# input_frame.pack(side="top", padx=10, pady=10)

# # campo de entrada de texto
# input_text = tk.Text(input_frame, height=10, width=50)
# input_text.pack()

# # marco salida de texto
# output_frame = tk.Frame(root)
# output_frame.pack(side="bottom", padx=10, pady=10)

# # salida de texto
# output_text = tk.Text(output_frame, height=10, width=50)
# output_text.pack()

# # Crea botones
# action_button = tk.Button(root, text="Nuevo")
# action_button.pack(side="left", padx=10, pady=10)

# empty_button1 = tk.Button(root, text="Abrir")
# empty_button1.pack(side="left", padx=10, pady=10)

# empty_button2 = tk.Button(root, text="Guardar")
# empty_button2.pack(side="left", padx=10, pady=10)

# empty_button3 = tk.Button(root, text="Guardar como")
# empty_button3.pack(side="left", padx=10, pady=10)

# exit_button = tk.Button(root, text="Salir", command=root.quit)
# exit_button.pack(side="right", padx=10, pady=10)

# root.mainloop()

##main.py
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Configurar la ventana principal
#         self.setWindowTitle('Compilador NoSQL')
#         self.setGeometry(100, 100, 800, 600)

#         # Aquí puedes agregar widgets y configuraciones adicionales para la interfaz de usuario


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     main()

# import re

# TOKENS = [
#     ("ID", r'[a-zA-Z_][a-zA-Z_0-9]*'),
#     ("NUM", r'\d+'),
#     ("PLUS", r'\+'),
#     ("MINUS", r'-'),
#     ("MUL", r'\*'),
#     ("DIV", r'/'),
#     ("WS", r'\s+'),  # Espacios en blanco (ignorar)
# ]

# def lex(input_str):
#     pos = 0
#     tokens = []
#     while pos < len(input_str):
#         match = None
#         for token_type, regex in TOKENS:
#             pattern = re.compile(regex)
#             match = pattern.match(input_str, pos)
#             if match:
#                 text = match.group(0)
#                 if token_type != "WS":  # No agregar espacios en blanco a la lista de tokens
#                     tokens.append((token_type, text))
#                 pos = match.end()
#                 break
#         if not match:
#             raise Exception(f"Error léxico en la posición {pos}")
#     return tokens

# input_str = "variable1 = 5 * 3"
# tokens = lex(input_str)
# print(tokens)

# import tkinter as tk
# from tkinter import filedialog

# def nuevo():
#     global current_file
#     if input_text.edit_modified():
#         save_changes = tk.messagebox.askyesnocancel("Guardar cambios", "¿Desea guardar los cambios?")
#         if save_changes:
#             guardar_archivo()
#             input_text.edit_modified(False)
#         elif save_changes is None:
#             return
#     input_text.delete("1.0", "end")
#     output_text.delete("1.0", "end")
#     current_file = ""

# def abrir_archivo():
#     global current_file
#     if input_text.edit_modified():
#         save_changes = tk.messagebox.askyesnocancel("Guardar cambios", "¿Desea guardar los cambios?")
#         if save_changes:
#             guardar_archivo()
#             input_text.edit_modified(False)
#         elif save_changes is None:
#             return
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         with open(file_path, "r") as file:
#             input_text.delete("1.0", "end")
#             input_text.insert("1.0", file.read())
#             current_file = file_path

# def guardar_archivo():
#     global current_file
#     if current_file:
#         with open(current_file, "w") as file:
#             file.write(input_text.get("1.0", "end"))
#             input_text.edit_modified(False)
#     else:
#         file_path = filedialog.asksaveasfilename(defaultextension=".txt")
#         if file_path:
#             with open(file_path, "w") as file:
#                 file.write(input_text.get("1.0", "end"))
#                 current_file = file_path
#                 input_text.edit_modified(False)

# def guardar_como():
#     file_path = filedialog.asksaveasfilename(defaultextension=".txt")
#     if file_path:
#         with open(file_path, "w") as file:
#             file.write(input_text.get("1.0", "end"))

# # Crear la ventana principal
# root = tk.Tk()
# root.title("Proyecto 2 - 202110180")

# # Crear el marco para la entrada de texto
# input_frame = tk.Frame(root)
# input_frame.pack(side="top", padx=10, pady=5)

# # Crear el campo de entrada de texto
# input_text = tk.Text(input_frame, height=9, width=80)
# input_text.pack()

# # Crear el marco para la salida de texto
# output_frame = tk.Frame(root)
# output_frame.pack(side="bottom", padx=10, pady=10)

# # Crear el campo de salida de texto
# output_text = tk.Text(output_frame, height=12, width=70)
# output_text.pack()

# # Crear los botones
# new_button = tk.Button(root, text="Nuevo", command=nuevo)
# new_button.pack(side="left", padx=10, pady=10)

# open_button = tk.Button(root, text="Abrir", command=abrir_archivo)
# open_button.pack(side="left", padx=10, pady=10)

# save_button = tk.Button(root, text="Guardar", command=guardar_archivo)
# save_button.pack(side="left", padx=10, pady=10)

# save_as_button = tk.Button(root, text="Guardar como", command=guardar_como)
# save_as_button.pack(side="left", padx=10, pady=10)

# exit_button = tk.Button(root, text="Salir", command=root.quit)
# exit_button.pack(side="right", padx=10, pady=10)


# root.mainloop()


#Version funcional 0.2

# import sys
# import os
# from scanner import lex
# from Parser import Parser
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget, QMenu, QMenuBar, QAction, QFileDialog, QVBoxLayout, QWidget, QPlainTextEdit, QLabel, QTableWidget, QTableWidgetItem
# from PyQt5.QtGui import QFont

# def generate_select_mongodb(statement):
#     select_fields = ', '.join(statement['fields'])
#     where_clause = generate_where_mongodb(statement['where'])

#     return f"db.{statement['table']}.find({where_clause}, '{select_fields}')"

# def generate_insert_mongodb(statement):
#     fields_and_values = dict(zip(statement['fields'], statement['values']))
#     return f"db.{statement['table']}.insertOne({fields_and_values})"

# def generate_delete_mongodb(statement):
#     where_clause = generate_where_mongodb(statement['where'])
#     return f"db.{statement['table']}.deleteMany({where_clause})"

# def generate_where_mongodb(conditions):
#     if not conditions:
#         return '{}'

#     condition_strs = []
#     for condition in conditions:
#         if isinstance(condition, tuple):
#             operator, cond = condition
#             condition_strs.append(f'${operator.lower()}')
#             condition = cond

#         field, op, value = condition
#         if op == '=':
#             op = 'eq'
#         elif op == '>':
#             op = 'gt'
#         elif op == '<':
#             op = 'lt'
#         elif op == '>=':
#             op = 'gte'
#         elif op == '<=':
#             op = 'lte'

#         value_str = value if isinstance(value, (int, float)) else f"'{value}'"
#         condition_strs.append(f"{{'{field}': {{${op}: {value_str}}}}}")

#     return '{' + ', '.join(condition_strs) + '}'

# def parse_sql_file(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()
#     parser = Parser(content)
#     return parser.parse()

# def generate_mongodb(statements):
#     mongodb_statements = []
#     for statement in statements:
#         if statement["type"] == "select":
#             mongodb_statement = generate_select_mongodb(statement)
#         elif statement["type"] == "insert":
#             mongodb_statement = generate_insert_mongodb(statement)
#         elif statement["type"] == "delete":
#             mongodb_statement = generate_delete_mongodb(statement)
#         mongodb_statements.append(mongodb_statement)
#     return mongodb_statements

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         #Ventana principal
#         self.setWindowTitle('Compilador NoSQL')
#         self.setGeometry(100, 100, 1200, 800)

#         # Agregar widgets y configuraciones adicionales para la interfaz de usuario
#         self.init_ui()

#     def init_ui(self):
#         # Editor de código
#         self.code_editor = QPlainTextEdit(self)
#         self.code_editor.setFont(QFont("Courier", 12))
#         self.setCentralWidget(self.code_editor)

#         # Area de visualización de sentencias
#         self.sentences_viewer = QTextEdit(self)
#         self.sentences_viewer.setReadOnly(True)
#         self.sentences_dock = QDockWidget("Sentencias Generadas", self)
#         self.sentences_dock.setWidget(self.sentences_viewer)
#         self.addDockWidget(2, self.sentences_dock)

#         # Agregar tabla de tokens
#         self.tokens_table = QTableWidget(self)
#         self.tokens_table.setColumnCount(4)
#         self.tokens_table.setHorizontalHeaderLabels(['No.', 'Tipo', 'Linea', 'Lexema'])
#         self.tokens_dock = QDockWidget("Tokens", self)
#         self.tokens_dock.setWidget(self.tokens_table)
#         self.addDockWidget(2, self.tokens_dock)

#         # Area de errores
#         self.errors_table = QTableWidget(self)
#         self.errors_table.setColumnCount(5)
#         self.errors_table.setHorizontalHeaderLabels(['Tipo', 'Linea', 'Columna', 'Token', 'Descripcion'])
#         self.errors_dock = QDockWidget("Errores", self)
#         self.errors_dock.setWidget(self.errors_table)
#         self.addDockWidget(2, self.errors_dock)

#         # Menú Archivo
#         self.menu_archivo = QMenu("Archivo", self)
#         self.menu_analisis = QMenu("Análisis", self)
#         self.menu_ver = QMenu("Ver", self)

#         # Menú Archivo acciones
#         self.action_nuevo = QAction("Nuevo", self)
#         self.action_abrir = QAction("Abrir", self)
#         self.action_guardar = QAction("Guardar", self)
#         self.action_guardar_como = QAction("Guardar como", self)
#         self.action_salir = QAction("Salir", self)

#         self.menu_archivo.addAction(self.action_nuevo)
#         self.menu_archivo.addAction(self.action_abrir)
#         self.menu_archivo.addAction(self.action_guardar)
#         self.menu_archivo.addAction(self.action_guardar_como)
#         self.menu_archivo.addSeparator()
#         self.menu_archivo.addAction(self.action_salir)

#         # Menú Análisis acciones
#         self.action_analizar = QAction("Generar sentencias MongoDB", self)
#         self.menu_analisis.addAction(self.action_analizar)

#         # Menú Ver acciones
#         self.action_ver_tokens = QAction("Tokens", self)
#         self.menu_ver.addAction(self.action_ver_tokens)

#         # Añadir menús a la barra de menú
#         self.menu_bar = QMenuBar(self)
#         self.menu_bar.addMenu(self.menu_archivo)
#         self.menu_bar.addMenu(self.menu_analisis)
#         self.menu_bar.addMenu(self.menu_ver)
#         self.setMenuBar(self.menu_bar)

#         # Conectar acciones a funciones
#         self.action_abrir.triggered.connect(self.open_file)
#         self.action_guardar.triggered.connect(self.save_file)
#         self.action_guardar_como.triggered.connect(self.save_file_as)
#         self.action_nuevo.triggered.connect(self.new_file)
#         self.action_salir.triggered.connect(self.close)
#         self.action_analizar.triggered.connect(self.analyze_code)
#         self.action_ver_tokens.triggered.connect(self.show_tokens)

#     def new_file(self):
#         if self.code_editor.document().isModified():
#             pass 

#         self.code_editor.clear()

#     def open_file(self):
#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Text Files (*.txt);;All Files (*)", options=options)

#         if file_name:
#             with open(file_name, 'r') as file:
#                 self.code_editor.setPlainText(file.read())

#     def save_file(self):
#         if not self.code_editor.document().isModified():
#             return

#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Text Files (*.txt);;All Files (*)", options=options)

#         if file_name:
#             with open(file_name, 'w') as file:
#                 file.write(self.code_editor.toPlainText())

#     def save_file_as(self):
#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getSaveFileName(self, "Guardar archivo como", "", "Text Files (*.txt);;All Files (*)", options=options)

#         if file_name:
#             with open(file_name, 'w') as file:
#                 file.write(self.code_editor.toPlainText())

#     def analyze_code(self):
#         input_str = self.code_editor.toPlainText()

#         # Crear una instancia del analizador y analizar la entrada
#         parser = Parser(input_str)

#         try:
#             result = parser.parse()
#             # Verificar la estructura del objeto 'result'
#             print(result)

#             # Procesar y mostrar el resultado según sea necesario (por ejemplo, generar sentencias MongoDB)
#             if 'statements' in result:
#                 self.sentences_viewer.setPlainText("\n".join(result['statements']))
#             else:
#                 self.sentences_viewer.setPlainText('')

#             # Llamar a show_tokens para actualizar la tabla de tokens
#             self.show_tokens(parser.tokens)
#         except Exception as e:
#             # Manejar errores en el análisis y mostrarlos en la tabla de errores
#             self.update_error_table(f"Error inesperado: {str(e)}")

#     def update_error_table(self, error_msg):
#         self.errors_table.setRowCount(1)
#         self.errors_table.setItem(0, 0, QTableWidgetItem("Error"))
#         self.errors_table.setItem(0, 1, QTableWidgetItem("-"))
#         self.errors_table.setItem(0, 2, QTableWidgetItem("-"))
#         self.errors_table.setItem(0, 3, QTableWidgetItem("-"))
#         self.errors_table.setItem(0, 4, QTableWidgetItem(error_msg))

#     def show_tokens(self, tokens):
#         self.tokens_table.setRowCount(len(tokens))
#         for i, token in enumerate(tokens):
#             if len(token) == 3:
#                 token_type, token_text, line_number = token
#             else:
#                 token_type, token_text = token
#                 line_number = '-'

#             self.tokens_table.setItem(i, 0, QTableWidgetItem(str(i + 1)))
#             self.tokens_table.setItem(i, 1, QTableWidgetItem(token_type))
#             self.tokens_table.setItem(i, 2, QTableWidgetItem(str(line_number)))
#             self.tokens_table.setItem(i, 3, QTableWidgetItem(token_text))


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     main_window.show()
#     sys.exit(app.exec_())



# if __name__ == "__main__":
# #     sql_statements = parse_sql_file("input.txt")
# #     mongodb_statements = generate_mongodb(sql_statements)
# #     for mongodb_statement in mongodb_statements:
# #         print(mongodb_statement)




# #La que no se arregloimport sys
# from scanner import lex
# from Parser import Parser
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget, QMenu, QMenuBar, QAction, QFileDialog, QVBoxLayout, QWidget, QPlainTextEdit, QLabel, QTableWidget, QTableWidgetItem
# from PyQt5.QtGui import QFont

# def generate_select_mongodb(statement):
#     select_fields = ', '.join(statement['fields'])
#     where_clause = generate_where_mongodb(statement['where'])

#     return f"db.{statement['table']}.find({where_clause}, '{select_fields}')"

# def generate_insert_mongodb(statement):
#     fields_and_values = dict(zip(statement['fields'], statement['values']))
#     return f"db.{statement['table']}.insertOne({fields_and_values})"

# def generate_delete_mongodb(statement):
#     where_clause = generate_where_mongodb(statement['where'])
#     return f"db.{statement['table']}.deleteMany({where_clause})"

# def generate_where_mongodb(conditions):
#     if not conditions:
#         return '{}'

#     condition_strs = []
#     for condition in conditions:
#         if isinstance(condition, tuple):
#             operator, cond = condition
#             condition_strs.append(f'${operator.lower()}')
#             condition = cond

#         field, op, value = condition
#         if op == '=':
#             op = 'eq'
#         elif op == '>':
#             op = 'gt'
#         elif op == '<':
#             op = 'lt'
#         elif op == '>=':
#             op = 'gte'
#         elif op == '<=':
#             op = 'lte'

#         value_str = value if isinstance(value, (int, float)) else f"'{value}'"
#         condition_strs.append(f"{{'{field}': {{${op}: {value_str}}}}}")

#     return '{' + ', '.join(condition_strs) + '}'

# def parse_sql_content(content):
#     parser = Parser(content)
#     return parser.parse()


# def generate_mongodb(parsed_statements):
#     mongodb_statements = []

#     for statement_type, statement in parsed_statements:
#         if statement_type == "INSERT":
#             mongodb_statement = generate_insert_mongodb(statement)
#         elif statement_type == "DELETE":
#             mongodb_statement = generate_delete_mongodb(statement)
#         elif statement_type == "SELECT":
#             mongodb_statement = generate_select_mongodb(statement)
#         else:
#             raise ValueError(f"Tipo de declaración desconocida: {statement_type}")

#         mongodb_statements.append(mongodb_statement)

#     return mongodb_statements

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         #Ventana principal
#         self.setWindowTitle('Compilador NoSQL')
#         self.setGeometry(100, 100, 1200, 800)

#         # Agregar widgets y configuraciones adicionales para la interfaz de usuario
#         self.init_ui()

#     def init_ui(self):
#         # Editor de código
#         self.code_editor = QPlainTextEdit(self)
#         self.code_editor.setFont(QFont("Courier", 12))
#         self.setCentralWidget(self.code_editor)

#         # Area de visualización de sentencias
#         self.sentences_viewer = QTextEdit(self)
#         self.sentences_viewer.setReadOnly(True)
#         self.sentences_dock = QDockWidget("Sentencias Generadas", self)
#         self.sentences_dock.setWidget(self.sentences_viewer)
#         self.addDockWidget(2, self.sentences_dock)

#         # Agregar tabla de tokens
#         self.tokens_table = QTableWidget(self)
#         self.tokens_table.setColumnCount(4)
#         self.tokens_table.setHorizontalHeaderLabels(['No.', 'Tipo', 'Linea', 'Lexema'])
#         self.tokens_dock = QDockWidget("Tokens", self)
#         self.tokens_dock.setWidget(self.tokens_table)
#         self.addDockWidget(2, self.tokens_dock)

#         # Area de errores
#         self.errors_table = QTableWidget(self)
#         self.errors_table.setColumnCount(5)
#         self.errors_table.setHorizontalHeaderLabels(['Tipo', 'Linea', 'Columna', 'Token', 'Descripcion'])
#         self.errors_dock = QDockWidget("Errores", self)
#         self.errors_dock.setWidget(self.errors_table)
#         self.addDockWidget(2, self.errors_dock)

#         # Menú Archivo
#         self.menu_archivo = QMenu("Archivo", self)
#         self.menu_analisis = QMenu("Análisis", self)
#         self.menu_ver = QMenu("Ver", self)

#         # Menú Archivo acciones
#         self.action_nuevo = QAction("Nuevo", self)
#         self.action_abrir = QAction("Abrir", self)
#         self.action_guardar = QAction("Guardar", self)
#         self.action_guardar_como = QAction("Guardar como", self)
#         self.action_salir = QAction("Salir", self)

#         self.menu_archivo.addAction(self.action_nuevo)
#         self.menu_archivo.addAction(self.action_abrir)
#         self.menu_archivo.addAction(self.action_guardar)
#         self.menu_archivo.addAction(self.action_guardar_como)
#         self.menu_archivo.addSeparator()
#         self.menu_archivo.addAction(self.action_salir)

#         # Menú Análisis acciones
#         self.action_analizar = QAction("Generar sentencias MongoDB", self)
#         self.menu_analisis.addAction(self.action_analizar)

#         # Menú Ver acciones
#         self.action_ver_tokens = QAction("Tokens", self)
#         self.menu_ver.addAction(self.action_ver_tokens)

#         # Añadir menús a la barra de menú
#         self.menu_bar = QMenuBar(self)
#         self.menu_bar.addMenu(self.menu_archivo)
#         self.menu_bar.addMenu(self.menu_analisis)
#         self.menu_bar.addMenu(self.menu_ver)
#         self.setMenuBar(self.menu_bar)

#         # Conectar acciones a funciones
#         self.action_abrir.triggered.connect(self.open_file)
#         self.action_guardar.triggered.connect(self.save_file)
#         self.action_guardar_como.triggered.connect(self.save_file_as)
#         self.action_nuevo.triggered.connect(self.new_file)
#         self.action_salir.triggered.connect(self.close)
#         self.action_analizar.triggered.connect(self.analyze_code)
#         self.action_ver_tokens.triggered.connect(self.show_tokens)

#     def new_file(self):
#         if self.code_editor.document().isModified():
#             pass 

#         self.code_editor.clear()

#     def open_file(self):
#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Text Files (*.txt);;All Files (*)", options=options)

#         if file_name:
#             with open(file_name, 'r') as file:
#                 self.code_editor.setPlainText(file.read())

#     def save_file(self):
#         if not self.code_editor.document().isModified():
#             return

#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Text Files (*.txt);;All Files (*)", options=options)

#         if file_name:
#             with open(file_name, 'w') as file:
#                 file.write(self.code_editor.toPlainText())

#     def save_file_as(self):
#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getSaveFileName(self, "Guardar archivo como", "", "Text Files (*.txt);;All Files (*)", options=options)

#         if file_name:
#             with open(file_name, 'w') as file:
#                 file.write(self.code_editor.toPlainText())

#     def analyze_code(self):
#         input_str = self.code_editor.toPlainText()

#         # Crear una instancia del analizador y analizar la entrada
#         parsed_statements = parse_sql_content(input_str)
#         mongodb_statements = generate_mongodb(parsed_statements)

#         # Mostrar las sentencias de MongoDB en el visor de sentencias
#         self.sentences_viewer.setPlainText("\n".join(mongodb_statements))

#         # Llamar a show_tokens para actualizar la tabla de tokens
#         self.show_tokens(parsed_statements[0].tokens)  # Asumimos que solo hay una declaración en la entrada

#     def update_error_table(self, error_msg):
#         self.errors_table.setRowCount(1)
#         self.errors_table.setItem(0, 0, QTableWidgetItem("Error"))
#         self.errors_table.setItem(0, 1, QTableWidgetItem("-"))
#         self.errors_table.setItem(0, 2, QTableWidgetItem("-"))
#         self.errors_table.setItem(0, 3, QTableWidgetItem("-"))
#         self.errors_table.setItem(0, 4, QTableWidgetItem(error_msg))

#     def show_tokens(self, tokens):
#         self.tokens_table.setRowCount(len(tokens))
#         for i, token in enumerate(tokens):
#             if len(token) == 3:
#                 token_type, token_text, line_number = token
#             else:
#                 token_type, token_text = token
#                 line_number = '-'

#             self.tokens_table.setItem(i, 0, QTableWidgetItem(str(i + 1)))
#             self.tokens_table.setItem(i, 1, QTableWidgetItem(token_type))
#             self.tokens_table.setItem(i, 2, QTableWidgetItem(str(line_number)))
#             self.tokens_table.setItem(i, 3, QTableWidgetItem(token_text))


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     main_window.show()
#     sys.exit(app.exec_())

# def lex(input_str):
#     token_iter = REGEX.finditer(input_str)
#     tokens = []
#     for token_match in token_iter:
#         token_type = token_match.lastgroup
#         token_text = token_match.group(token_type)
#         if token_type == "ID" and token_text.upper() in KEYWORDS:
#             token_type = token_text.upper()
#         if token_type != "WS" and token_type != "COMMENT":
#             tokens.append((token_type, token_text))
#     return tokens


##Sacener.py 
#import re

# TOKENS = [
#     ("ID", r"[a-zA-Z_][a-zA-Z_0-9]*"),
#     ("NUM", r"\d+(\.\d*)?"),
#     ("STRING", r"'((?:''|[^'])*)'"),
#     ("LPAREN", r"\("),
#     ("RPAREN", r"\)"),
#     ("COMMA", r","),
#     ("OPERATOR", r"[=<>!]+"),
#     ("SEMICOLON", r";"),
#     ("COMMENT", r"--.*"),
#     ("WS", r"\s+"),
#     ("UNRECOGNIZED", r"."),
# ]

# KEYWORDS = {'SELECT', 'FROM', 'INSERT', 'INTO', 'VALUES', 'DELETE', 'WHERE', 'AND', 'OR'}
# REGEX = re.compile("|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKENS))

# def lex(input_str):
#     token_iter = REGEX.finditer(input_str)
#     tokens = []
#     for token_match in token_iter:
#         token_type = token_match.lastgroup
#         token_text = token_match.group(token_type)
#         if token_type == "ID" and token_text.upper() in KEYWORDS:
#             token_type = token_text.upper()
#         if token_type != "WS" and token_type != "COMMENT":
#             tokens.append((token_type, token_text))
#     return tokens


##Parser.py
# from scanner import lex, TOKENS

# class Parser:
#     def __init__(self, input_str):
#         self.tokens = lex(input_str)
#         self.pos = 0

#     def parse(self):
#         statements = []
#         while self.pos < len(self.tokens):
#             self.skip_comments()
#             self.skip_whitespace()
#             if self.match("ID"):
#                 current_token = self.current_token().upper()
#                 if current_token in ["SELECT", "INSERT", "DELETE"]:
#                     statement = self.query()
#                     if statement:
#                         statements.append(statement)
#                     self.skip_semicolon_or_newline()
#                 elif current_token == "WHERE":
#                     self.error("SELECT, INSERT o DELETE antes de WHERE")
#                 else:
#                     self.error("SELECT, INSERT o DELETE")
#             elif self.match("COMMENT"):
#                 self.consume_token()
#             elif self.match("WHITESPACE"):
#                 self.consume_token()
#             else:
#                 break
#         return statements

#     def skip_semicolon_or_newline(self):
#         while self.match("SEMICOLON") or self.match("NEWLINE"):
#             self.consume_token()

#     def skip_whitespace(self):
#         while self.pos < len(self.tokens) and self.tokens[self.pos][0] == "WHITESPACE":
#             self.consume_token()

#     def skip_comments(self):
#         while self.match("COMMENT"):
#             self.consume_token()
#             self.skip_whitespace()

#     def query(self):
#         self.skip_comments()

#         if self.match("ID"):
#             current_token = self.current_token().upper()
#             if current_token == "SELECT":
#                 return self.select()
#             elif current_token == "INSERT":
#                 return self.insert()
#             elif current_token == "DELETE":
#                 return self.delete()
#             else:
#                 self.error("SELECT, INSERT o DELETE")
#         else:
#             self.error("SELECT, INSERT o DELETE")

#     def semicolon(self):
#         self.skip_comments()
#         if self.match("SEMICOLON") or self.match("NEWLINE"):
#             self.consume_token()
#         else:
#             self.error("SEMICOLON or NEWLINE")

#     def select(self):
#         self.consume_token()

#         field_list = self.field_list()

#         if not self.match("FROM"):
#             self.error("FROM")
#         self.consume_token()

#         table = self.table()

#         where_clause = self.where_clause()

#         return {
#             "type": "select",
#             "fields": field_list,
#             "table": table,
#             "where": where_clause
#         }

#     def insert(self):
#         self.consume_token()  # Consume INSERT
#         if self.match("ID") and self.tokens[self.pos][1].upper() == "INTO":
#             self.consume_token()
#             table = self.table()
#             if self.match("LPAREN"):
#                 self.consume_token()
#                 field_list = self.field_list()
#                 if self.match("RPAREN"):
#                     self.consume_token()
#                     if self.match("ID") and self.tokens[self.pos][1].upper() == "VALUES":
#                         self.consume_token()
#                         if self.match("LPAREN"):
#                             self.consume_token()
#                             value_list = self.value_list()
#                             if self.match("RPAREN"):
#                                 self.consume_token()
#                                 return {"type": "insert", "table": table, "fields": field_list, "values": value_list}
#                             else:
#                                 self.error("RPAREN")
#                         else:
#                             self.error("LPAREN")
#                     else:
#                         self.error("VALUES")
#                 else:
#                     self.error("RPAREN")
#             else:
#                 self.error("LPAREN")
#         else:
#             self.error("INTO")

#     def delete(self):
#         if not (self.match("ID") and self.tokens[self.pos][1].upper() == "DELETE"):
#             self.error("DELETE")
#         self.consume_token()
#         if self.match("ID") and self.tokens[self.pos][1].upper() == "FROM":
#             self.consume_token()
#             table = self.table()
#             where_clause = self.where_clause()
#             return {"type": "delete", "table": table, "where": where_clause}
#         else:
#             self.error("FROM")

#     def field_list(self):
#         fields = []

#         if not self.match("ID"):
#             self.error("field name")
#         fields.append(self.current_token())
#         self.consume_token()

#         while self.match("COMMA"):
#             self.consume_token()
#             if not self.match("ID"):
#                 self.error("field name")
#             fields.append(self.current_token())
#             self.consume_token()

#         return fields

#     def table(self):
#         if not self.match("ID"):
#             self.error("table name")
#         table_name = self.current_token()
#         self.consume_token()
#         return table_name

#     def where_clause(self):
#         if not self.match("WHERE"):
#             return None
#         self.consume_token()

#         conditions = []
#         condition = self.condition()
#         conditions.append(condition)

#         while self.match("AND") or self.match("OR"):
#             operator = self.current_token()
#             self.consume_token()
#             condition = self.condition()
#             conditions.append((operator, condition))

#         return conditions

#     def condition(self):
#             if not self.match("ID"):
#                 self.error("field name")
#             field = self.current_token()
#             self.consume_token()

#             if not self.match("OPERATOR"):
#                 self.error("comparison operator")
#             operator = self.current_token()
#             self.consume_token()

#             if not (self.match("ID") or self.match("NUM")):
#                 self.error("value or field name")
#             value = self.current_token()
#             self.consume_token()

#             return (field, operator, value)
    
#     def value_list(self):
#         values = []
#         if self.match("NUM") or self.match("STRING"):
#             values.append(self.current_token())
#             self.consume_token()
#             while self.match("COMMA"):
#                 self.consume_token()
#                 if self.match("NUM") or self.match("STRING"):
#                     values.append(self.current_token())
#                     self.consume_token()
#                 else:
#                     self.error("NUM o STRING")
#         else:
#             self.error("NUM o STRING")
#         return values

#     def match(self, token_type):
#         if self.pos < len(self.tokens) and self.tokens[self.pos][0] == token_type:
#             return True
#         return False

#     def current_token(self):
#         return self.tokens[self.pos][1]
    
#     def consume_token(self):
#         if self.pos < len(self.tokens):
#             self.pos += 1
#         else:
#             self.error("Fin de la entrada")

#     def string_literal(self):
#         if not self.match("STRING"):
#             self.error("STRING")
#         string_value = self.current_token()
#         self.consume_token()
#         return string_value

#     def error(self, expected):
#         if self.pos < len(self.tokens):
#             token_type, token_value = self.tokens[self.pos]
#             raise Exception(f"Se esperaba {expected}, pero se encontró {token_type} ('{token_value}') en la posición {self.pos}.")
#         else:
#             raise Exception(f"Se esperaba {expected}, pero se encontró el final de la entrada.")



##Namas pa borrar luego 
import sys
# import os
# from scanner import Scanner
# from Parser import Parser
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget, QMenu, QMenuBar, QAction, QFileDialog, QVBoxLayout, QWidget, QPlainTextEdit, QLabel, QTableWidget, QTableWidgetItem
# from PyQt5.QtGui import QFont

# def generate_select_mongodb(statement):
#     select_fields = ', '.join(statement['fields'])
#     where_clause = generate_where_mongodb(statement['where'])

#     return f"db.{statement['table']}.find({where_clause}, '{select_fields}')"

# def generate_insert_mongodb(statement):
#     fields_and_values = dict(zip(statement['fields'], statement['values']))
#     return f"db.{statement['table']}.insertOne({fields_and_values})"

# def generate_delete_mongodb(statement):
#     where_clause = generate_where_mongodb(statement['where'])
#     return f"db.{statement['table']}.deleteMany({where_clause})"

# def generate_where_mongodb(conditions):
#     if not conditions:
#         return '{}'

#     condition_strs = []
#     for condition in conditions:
#         if isinstance(condition, tuple):
#             operator, cond = condition
#             condition_strs.append(f'${operator.lower()}')
#             condition = cond

#         field, op, value = condition
#         if op == '=':
#             op = 'eq'
#         elif op == '>':
#             op = 'gt'
#         elif op == '<':
#             op = 'lt'
#         elif op == '>=':
#             op = 'gte'
#         elif op == '<=':
#             op = 'lte'

#         value_str = value if isinstance(value, (int, float)) else f"'{value}'"
#         condition_strs.append(f"{{'{field}': {{${op}: {value_str}}}}}")

#     return '{' + ', '.join(condition_strs) + '}'

# def parse_sql_file(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()
#     parser = Parser(content)
#     return parser.parse()

# def generate_mongodb(statements):
#         mongodb_statements = []
#         for statement in statements:
#             if statement["type"] == "select":
#                 mongodb_statement = generate_select_mongodb(statement)
#             elif statement["type"] == "insert":
#                 mongodb_statement = generate_insert_mongodb(statement)
#             elif statement["type"] == "delete":
#                 mongodb_statement = generate_delete_mongodb(statement)
#             mongodb_statements.append(mongodb_statement)
#         return mongodb_statements

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         #Ventana principal
#         self.setWindowTitle('Compilador NoSQL')
#         self.setGeometry(100, 100, 1200, 800)

#         # Agregar widgets y configuraciones adicionales para la interfaz de usuario
#         self.init_ui()

#     def init_ui(self):
#         # Editor de código
#         self.code_editor = QPlainTextEdit(self)
#         self.code_editor.setFont(QFont("Courier", 12))
#         self.setCentralWidget(self.code_editor)

#         # Area de visualización de sentencias
#         self.sentences_viewer = QTextEdit(self)
#         self.sentences_viewer.setReadOnly(True)
#         self.sentences_dock = QDockWidget("Sentencias Generadas", self)
#         self.sentences_dock.setWidget(self.sentences_viewer)
#         self.addDockWidget(2, self.sentences_dock)

#         # Agregar tabla de tokens
#         self.tokens_table = QTableWidget(self)
#         self.tokens_table.setColumnCount(4)
#         self.tokens_table.setHorizontalHeaderLabels(['No.', 'Tipo', 'Linea', 'Lexema'])
#         self.tokens_dock = QDockWidget("Tokens", self)
#         self.tokens_dock.setWidget(self.tokens_table)
#         self.addDockWidget(2, self.tokens_dock)

#         # Area de errores
#         self.errors_table = QTableWidget(self)
#         self.errors_table.setColumnCount(5)
#         self.errors_table.setHorizontalHeaderLabels(['Tipo', 'Linea', 'Columna', 'Token', 'Descripcion'])
#         self.errors_dock = QDockWidget("Errores", self)
#         self.errors_dock.setWidget(self.errors_table)
#         self.addDockWidget(2, self.errors_dock)

#         # Menú Archivo
#         self.menu_archivo = QMenu("Archivo", self)
#         self.menu_analisis = QMenu("Análisis", self)
#         self.menu_ver = QMenu("Ver", self)

#         # Menú Archivo acciones
#         self.action_nuevo = QAction("Nuevo", self)
#         self.action_abrir = QAction("Abrir", self)
#         self.action_guardar = QAction("Guardar", self)
#         self.action_guardar_como = QAction("Guardar como", self)
#         self.action_salir = QAction("Salir", self)

#         self.menu_archivo.addAction(self.action_nuevo)
#         self.menu_archivo.addAction(self.action_abrir)
#         self.menu_archivo.addAction(self.action_guardar)
#         self.menu_archivo.addAction(self.action_guardar_como)
#         self.menu_archivo.addSeparator()
#         self.menu_archivo.addAction(self.action_salir)

#         # Menú Análisis acciones
#         self.action_analizar = QAction("Generar sentencias MongoDB", self)
#         self.menu_analisis.addAction(self.action_analizar)

#         # Menú Ver acciones
#         self.action_ver_tokens = QAction("Tokens", self)
#         self.menu_ver.addAction(self.action_ver_tokens)

#         # Añadir menús a la barra de menú
#         self.menu_bar = QMenuBar(self)
#         self.menu_bar.addMenu(self.menu_archivo)
#         self.menu_bar.addMenu(self.menu_analisis)
#         self.menu_bar.addMenu(self.menu_ver)
#         self.setMenuBar(self.menu_bar)

#         # Conectar acciones a funciones
#         self.action_abrir.triggered.connect(self.open_file)
#         self.action_guardar.triggered.connect(self.save_file)
#         self.action_guardar_como.triggered.connect(self.save_file_as)
#         self.action_nuevo.triggered.connect(self.new_file)
#         self.action_salir.triggered.connect(self.close)
#         self.action_analizar.triggered.connect(self.analyze_code)
#         self.action_ver_tokens.triggered.connect(self.show_tokens)

#     def new_file(self):
#         if self.code_editor.document().isModified():
#             pass 

#         self.code_editor.clear()

#     def open_file(self):
#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Text Files (*.txt);;All Files (*)", options=options)

#         if file_name:
#             with open(file_name, 'r', encoding='utf-8') as file:
#                 self.code_editor.setPlainText(file.read())

#     def save_file(self):
#         if not self.code_editor.document().isModified():
#             return

#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Text Files (*.txt);;All Files (*)", options=options)

#         if file_name:
#             with open(file_name, 'w', encoding='utf-8') as file:
#                 file.write(self.code_editor.toPlainText())

#     def save_file_as(self):
#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getSaveFileName(self, "Guardar archivo como", "", "Text Files (*.txt);;All Files (*)", options=options)

#         if file_name:
#             with open(file_name, 'w') as file:
#                 file.write(self.code_editor.toPlainText())

#     def analyze_code(self):
#         input_str = self.code_editor.toPlainText()
#         scanner = Scanner(input_str)  # Crear una instancia de Scanner
#         tokens = scanner.tokenize()  # Obtener los tokens
#         parser = Parser(tokens) 

#         # Crear una instancia del analizador y analizar la entrada
#         parser = Parser(input_str)

#         try:
#             result = parser.parse()
#             # Verificar la estructura del objeto 'result'
#             print(result)

#             # Procesar y mostrar el resultado según sea necesario (por ejemplo, generar sentencias MongoDB)
#             if 'statements' in result:
#                 self.sentences_viewer.setPlainText("\n".join(result['statements']))
#             else:
#                 self.sentences_viewer.setPlainText('')

#             # Llamar a show_tokens para actualizar la tabla de tokens
#             self.show_tokens(parser.tokens)
#         except Exception as e:
#             # Manejar errores en el análisis y mostrarlos en la tabla de errores
#             self.update_error_table(f"Error inesperado: {str(e)}")

#     def update_error_table(self, error_msg):
#         self.errors_table.setRowCount(1)
#         self.errors_table.setItem(0, 0, QTableWidgetItem("Error"))
#         self.errors_table.setItem(0, 1, QTableWidgetItem("-"))
#         self.errors_table.setItem(0, 2, QTableWidgetItem("-"))
#         self.errors_table.setItem(0, 3, QTableWidgetItem("-"))
#         self.errors_table.setItem(0, 4, QTableWidgetItem(error_msg))

#     def show_tokens(self, tokens):
#         self.tokens_table.setRowCount(len(tokens))
#         for i, token in enumerate(tokens):
#             if len(token) == 3:
#                 token_type, token_text, line_number = token
#             else:
#                 token_type, token_text = token
#                 line_number = '-'

#             self.tokens_table.setItem(i, 0, QTableWidgetItem(str(i + 1)))
#             self.tokens_table.setItem(i, 1, QTableWidgetItem(token_type))
#             self.tokens_table.setItem(i, 2, QTableWidgetItem(str(line_number)))
#             self.tokens_table.setItem(i, 3, QTableWidgetItem(token_text))


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     main_window.show()
#     sys.exit(app.exec_())
# 


        # # Añadir menús a la barra de menú
        # self.menu_bar = QMenuBar(self)
        # self.menu_bar.addMenu(self.menu_archivo)
        # self.menu_bar.addMenu(self.menu_analisis)
        # self.menu_bar.addMenu(self.menu_ver)



##Parser.py 

# from scanner import Scanner

# class Parser:
#     def __init__(self, tokens):
#         self.tokens = tokens
#         self.pos = 0

#     def accept(self, kind):
#         if self.pos < len(self.tokens) and self.tokens[self.pos][0] == kind:
#             self.pos += 1
#             return True
#         return False

#     def expect(self, kind):
#         if not self.accept(kind):
#             raise SyntaxError(f"Se esperaba {kind} en la línea {self.tokens[self.pos][2]}")

#     def parse(self):
#         statements = []

#         while self.pos < len(self.tokens):
#             try:
#                 if self.accept("CREATE_DB"):
#                     self.expect("EQUALS")
#                     self.expect("NEW")
#                     self.expect("CREATE_DB")
#                     self.expect("LPAREN")
#                     self.expect("RPAREN")
#                     self.expect("SEMICOLON")
#                     statements.append(("CREATE_DB",))

#                 elif self.accept("DROP_DB"):
#                     self.expect("EQUALS")
#                     self.expect("NEW")
#                     self.expect("DROP_DB")
#                     self.expect("LPAREN")
#                     self.expect("RPAREN")
#                     self.expect("SEMICOLON")
#                     statements.append(("DROP_DB",))

#                 elif self.accept("CREATE_COLLECTION"):
#                     self.expect("EQUALS")
#                     self.expect("NEW")
#                     self.expect("CREATE_COLLECTION")
#                     self.expect("LPAREN")
#                     self.expect("DQUOTE")
#                     collection_name = self.tokens[self.pos][1]
#                     self.expect("ID")
#                     self.expect("DQUOTE")
#                     self.expect("RPAREN")
#                     self.expect("SEMICOLON")
#                     statements.append(("CREATE_COLLECTION", collection_name))

#                 elif self.accept("DROP_COLLECTION"):
#                     self.expect("EQUALS")
#                     self.expect("NEW")
#                     self.expect("DROP_COLLECTION")
#                     self.expect("LPAREN")
#                     self.expect("DQUOTE")
#                     collection_name = self.tokens[self.pos][1]
#                     self.expect("ID")
#                     self.expect("DQUOTE")
#                     self.expect("RPAREN")
#                     self.expect("SEMICOLON")
#                     statements.append(("DROP_COLLECTION", collection_name))

#                 elif self.accept("INSERT_ONE"):
#                     self.expect("EQUALS")
#                     self.expect("NEW")
#                     self.expect("INSERT_ONE")
#                     self.expect("LPAREN")
#                     self.expect("DQUOTE")
#                     collection_name = self.tokens[self.pos][1]
#                     self.expect("ID")
#                     self.expect("DQUOTE")
#                     self.expect("COMMA")
#                     json_content = self.tokens[self.pos][1]
#                     self.expect("ID")
#                     self.expect("RPAREN")
#                     self.expect("SEMICOLON")
#                     statements.append(("INSERT_ONE", collection_name, json_content))

#                 elif self.accept("UPDATE_ONE"):
#                     self.expect("EQUALS")
#                     self.expect("NEW")
#                     self.expect("UPDATE_ONE")
#                     self.expect("LPAREN")
#                     self.expect("DQUOTE")
#                     collection_name = self.tokens[self.pos][1]
#                     self.expect("ID")
#                     self.expect("DQUOTE")
#                     self.expect("COMMA")
#                     json_query = self.tokens[self.pos][1]
#                     self.expect("ID")
#                     self.expect("RPAREN")
#                     self.expect("SEMICOLON")
#                     statements.append(("UPDATE_ONE", collection_name, json_query))

#                 elif self.accept("DELETE_ONE"):
#                     self.expect("EQUALS")
#                     self.expect("NEW")
#                     self.expect("DELETE_ONE")
#                     self.expect("LPAREN")
#                     self.expect("DQUOTE")
#                     collection_name = self.tokens[self.pos][1]
#                     self.expect("ID")
#                     self.expect("DQUOTE")
#                     self.expect("COMMA")
#                     json_query = self.tokens[self.pos][1]
#                     self.expect("ID")
#                     self.expect("RPAREN")
#                     self.expect("SEMICOLON")
#                     statements.append(("DELETE_ONE", collection_name, json_query))

#                 elif self.accept("FIND_ALL"):
#                     self.expect("EQUALS")
#                     self.expect("NEW")
#                     self.expect("FIND_ALL")
#                     self.expect("LPAREN")
#                     self.expect("DQUOTE")
#                     collection_name = self.tokens[self.pos][1]
#                     self.expect("ID")
#                     self.expect("DQUOTE")
#                     self.expect("RPAREN")
#                     self.expect("SEMICOLON")
#                     statements.append(("FIND_ALL", collection_name))

#                 elif self.accept("FIND_ONE"):
#                     self.expect("EQUALS")
#                     self.expect("NEW")
#                     self.expect("FIND_ONE")
#                     self.expect("LPAREN")
#                     self.expect("DQUOTE")
#                     collection_name = self.tokens[self.pos][1]
#                     self.expect("ID")
#                     self.expect("DQUOTE")
#                     self.expect("RPAREN")
#                     self.expect("SEMICOLON")
#                     statements.append(("FIND_ONE", collection_name))

#                 else:
#                     raise SyntaxError(f"Una sentencia válida esperada en la línea {self.tokens[self.pos][2]}", self.tokens[self.pos])

#             except IndexError as ie:
#                 raise SyntaxError(f"Fin inesperado del archivo en la línea {self.tokens[self.pos - 1][2]}")

#         return {"statements": statements}

# if __name__ == "__main__":
#     with open("input.txt", "r") as file:
#         input_str = file.read()

#     scanner = Scanner(input_str)
#     tokens = scanner.tokenize()

#     parser = Parser(tokens)
#     parse_tree = parser.parse()

#     print(parse_tree)




###Por si quires arreglarloimport sys
# from scanner import Scanner
# from Parser import Parser
# from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget, QMenu, QMenuBar, QAction, QFileDialog, QVBoxLayout, QWidget, QPlainTextEdit, QLabel, QTableWidget, QTableWidgetItem
# from PyQt5.QtGui import QFont

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Ventana principal
#         self.setWindowTitle('Compilador NoSQL')
#         self.setGeometry(100, 100, 1200, 800)

#         # Agregar widgets y configuraciones adicionales para la interfaz de usuario
#         self.init_ui()

#     def init_ui(self):
#         # Editor de código
#         self.code_editor = QPlainTextEdit(self)
#         self.code_editor.setFont(QFont("Courier", 12))
#         self.setCentralWidget(self.code_editor)

#         # Area de visualización de sentencias
#         self.sentences_viewer = QTextEdit(self)
#         self.sentences_viewer.setReadOnly(True)
#         self.sentences_dock = QDockWidget("Sentencias Generadas", self)
#         self.sentences_dock.setWidget(self.sentences_viewer)
#         self.addDockWidget(2, self.sentences_dock)

#         # Agregar tabla de tokens
#         self.tokens_table = QTableWidget(self)
#         self.tokens_table.setColumnCount(4)
#         self.tokens_table.setHorizontalHeaderLabels(['No.', 'Tipo', 'Linea', 'Lexema'])
#         self.tokens_dock = QDockWidget("Tokens", self)
#         self.tokens_dock.setWidget(self.tokens_table)
#         self.addDockWidget(2, self.tokens_dock)

#         # Area de errores
#         self.errors_table = QTableWidget(self)
#         self.errors_table.setColumnCount(5)
#         self.errors_table.setHorizontalHeaderLabels(['Tipo', 'Linea', 'Columna', 'Token', 'Descripcion'])
#         self.errors_dock = QDockWidget("Errores", self)
#         self.errors_dock.setWidget(self.errors_table)
#         self.addDockWidget(2, self.errors_dock)

#         # Menú Archivo
#         self.menu_archivo = QMenu("Archivo", self)
#         self.menu_analisis = QMenu("Análisis", self)
#         self.menu_ver = QMenu("Ver", self)

#         # Menú Archivo acciones
#         self.action_nuevo = QAction("Nuevo", self)
#         self.action_abrir = QAction("Abrir", self)
#         self.action_guardar = QAction("Guardar", self)
#         self.action_guardar_como = QAction("Guardar como", self)
#         self.action_salir = QAction("Salir", self)

#         self.menu_archivo.addAction(self.action_nuevo)
#         self.menu_archivo.addAction(self.action_abrir)
#         self.menu_archivo.addAction(self.action_guardar)
#         self.menu_archivo.addAction(self.action_guardar_como)
#         self.menu_archivo.addSeparator()
#         self.menu_archivo.addAction(self.action_salir)

#         # Menú Análisis acciones
#         self.action_analizar = QAction("Generar sentencias MongoDB", self)
#         self.menu_analisis.addAction(self.action_analizar)

#         # Menú Ver acciones
#         self.action_ver_tokens = QAction("Tokens", self)
#         self.menu_ver.addAction(self.action_ver_tokens)

#         # Añadir menús a la barra de menú
#         self.menu_bar = QMenuBar(self)
#         self.menu_bar.addMenu(self.menu_archivo)
#         self.menu_bar.addMenu(self.menu_analisis)
#         self.menu_bar.addMenu(self.menu_ver)
#         self.setMenuBar(self.menu_bar)

#         # Conectar acciones a funciones
#         self.action_abrir.triggered.connect(self.open_file)
#         self.action_guardar.triggered.connect(self.save_file)
#         self.action_guardar_como.triggered.connect(self.save_file_as)
#         self.action_nuevo.triggered.connect(self.new_file)
#         self.action_salir.triggered.connect(self.close)
#         self.action_analizar.triggered.connect(self.analyze_code)
#         self.action_ver_tokens.triggered.connect(self.show_tokens)

#     def new_file(self):
#         if self.code_editor.document().isModified():
#             pass 

#         self.code_editor.clear()

#     def open_file(self):
#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Text Files (*.txt);;All Files (*)", options=options)

#         if file_name:
#             with open(file_name, 'r', encoding='utf-8') as file:
#                 self.code_editor.setPlainText(file.read())

#     def save_file(self):
#         if not self.code_editor.document().isModified():
#             return

#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Text Files (*.txt);;All Files (*)", options=options)

#         if file_name:
#             with open(file_name, 'w', encoding='utf-8') as file:
#                 file.write(self.code_editor.toPlainText())

#     def save_file_as(self):
#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getSaveFileName(self, "Guardar archivo como", "", "Text Files (*.txt);;All Files (*)", options=options)

#         if file_name:
#             with open(file_name, 'w', encoding='utf-8') as file:
#                 file.write(self.code_editor.toPlainText())

#     def analyze_code(self):
#         input_str = self.code_editor.toPlainText()
#         scanner = Scanner(input_str)  # Crear una instancia de Scanner
#         tokens = scanner.tokenize()  # Obtener los tokens
#         parser = Parser(tokens)  # Crear una instancia del analizador con los tokens

#         try:
#             result = parser.parse()

#             mongodb_statements = []
#             for stmt in result:
#                 if stmt[0] == "CREATE_DB":
#                     mongodb_statements.append("use " + stmt[1])
#                     print("CREATE_DB:", stmt[1])
#                 elif stmt[0] == "DROP_DB":
#                     mongodb_statements.append("db.dropDatabase()")
#                     print("DROP_DB")
#                 elif stmt[0] == "CREATE_COLLECTION":
#                     mongodb_statements.append(f"db.createCollection('{stmt[1]}')")
#                     print("CREATE_COLLECTION:", stmt[1])
#                 elif stmt[0] == "DROP_COLLECTION":
#                     mongodb_statements.append(f"db.{stmt[1]}.drop()")
#                     print("DROP_COLLECTION:", stmt[1])
#                 elif stmt[0] == "INSERT_ONE":
#                     mongodb_statements.append(f"db.{stmt[1]}.insertOne({stmt[2]})")
#                 elif stmt[0] == "UPDATE_ONE":
#                     mongodb_statements.append(f"db.{stmt[1]}.updateOne({stmt[2]}, {stmt[3]})")
#                 elif stmt[0] == "DELETE_ONE":
#                     mongodb_statements.append(f"db.{stmt[1]}.deleteOne({stmt[2]})")
#                 elif stmt[0] == "FIND_ALL":
#                     mongodb_statements.append(f"db.{stmt[1]}.find()")
#                 elif stmt[0] == "FIND_ONE":
#                     mongodb_statements.append(f"db.{stmt[1]}.findOne({stmt[2]})")

#             self.sentences_viewer.setPlainText("\n".join(mongodb_statements))
#             self.show_tokens(parser.tokens)
#         except SyntaxError as e:
#             self.display_parser_errors(parser.errors)
#             print("Error: " + str(e))

#     def update_error_table(self, error_msg):
#         self.errors_table.setRowCount(1)
#         self.errors_table.setItem(0, 0, QTableWidgetItem("Error"))
#         self.errors_table.setItem(0, 1, QTableWidgetItem("-"))
#         self.errors_table.setItem(0, 2, QTableWidgetItem("-"))
#         self.errors_table.setItem(0, 3, QTableWidgetItem("-"))
#         self.errors_table.setItem(0, 4, QTableWidgetItem(error_msg))

#     def display_parser_errors(self, errors):
#         self.errors_table.setRowCount(len(errors))
#         for i, error in enumerate(errors):
#             self.errors_table.setItem(i, 0, QTableWidgetItem(error[0]))
#             self.errors_table.setItem(i, 1, QTableWidgetItem(str(error[1])))
#             self.errors_table.setItem(i, 2, QTableWidgetItem(str(error[2])))
#             self.errors_table.setItem(i, 3, QTableWidgetItem(error[3]))
#             self.errors_table.setItem(i, 4, QTableWidgetItem(error[4]))

#     def show_tokens(self, tokens):
#         scanner = Scanner(self.code_editor.toPlainText())
#         tokens = scanner.tokenize()
#         print("Tokens:", tokens)  # Imprime la variable tokens aquí para ver su valor
        
#         if isinstance(tokens, list):
#             self.tokens_table.setRowCount(len(tokens))
#             for i, token in enumerate(tokens):
#                 self.tokens_table.setItem(i, 0, QTableWidgetItem(str(i + 1)))
#                 self.tokens_table.setItem(i, 1, QTableWidgetItem(token[0]))
#                 self.tokens_table.setItem(i, 2, QTableWidgetItem(str(token[2])))
#                 self.tokens_table.setItem(i, 3, QTableWidgetItem(token[1]))
#         else:
#             print("Error: tokens no es una lista")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main_win = MainWindow()
#     main_win.show()
#     sys.exit(app.exec_())


# def is_alpha(c):
#     return c.isalpha()

# def is_alnum_or_underscore(c):
#     return c.isalnum() or c == '_'

# def is_delimiter(c):
#     return c in r'{}()=,.;"\'\':}-$“”-* /'

# def is_digit(c):
#     return c.isdigit()

# def is_quote(c):
#     return c in "\"'"


# TRANSITION_TABLE = {
#     'S0': {
#         'is_alpha': 'S1',
#         'is_delimiter': 'S2',
#         'is_quote': 'S3',
#     },
#     'S1': {
#         'is_alnum_or_underscore': 'S1',
#         'not_is_alnum_or_underscore': 'S0'
#     },
#     'S2': {
#         'not_is_delimiter': 'S0'
#     },
#     'S3': {
#         'is_quote': 'S3_end',
#     },
#     'S3_end': {
#         'not_is_quote': 'S0'
#     },
# }

# def is_comment_start(input_str, i):
#     return input_str[i:i+3] == '---'

# class Scanner:
#     def __init__(self, input_str):
#         self.input_str = input_str
#         self.tokens = []
#         self.keywords = {
#             "CrearBD": "CREATE_DB",
#             "nueva": "NEW",
#             "EliminarBD": "DROP_DB",
#             "CrearColeccion": "CREATE_COLLECTION",
#             "EliminarColeccion": "DROP_COLLECTION",
#             "InsertarUnico": "INSERT_ONE",
#             "ActualizarUnico": "UPDATE_ONE",
#             "EliminarUnico": "DELETE_ONE",
#             "BuscarTodo": "FIND_ALL",
#             "BuscarUnico": "FIND_ONE"
#         }

#         self.delimiters = {
#             '{': 'LBRACE',
#             '}': 'RBRACE',
#             '(': 'LPAREN',
#             ')': 'RPAREN',
#             '=': 'EQUALS',
#             ',': 'COMMA',
#             '.': 'DOT',
#             ';': 'SEMICOLON',
#             '"': 'DQUOTE',
#             "'": 'SQUOTE',
#             ':': 'COLON',
#             '$': 'DOLLAR',
#             '“': 'OPEN_QUOTE',
#             '”': 'CLOSE_QUOTE',
#             '-': 'SPACE',
#             '*': 'ASTERISK',
#             '/': 'BAR'
#         }

#     def is_identifier(self, s):
#         if s[0].isalpha() or s[0] == '_':
#             return all(c.isalnum() or c == '_' for c in s[1:])
#         return False

#     def tokenize(self):
#         self.tokens = []
#         state = 'S0'
#         line_num = 1
#         line_start = 0
#         i = 0
#         n = len(self.input_str)

#         while i < n:
#             c = self.input_str[i]

#             if is_comment_start(self.input_str, i):
#                 while i < n and self.input_str[i] != '\n':
#                     i += 1
#                 continue

#             if state == 'S0':
#                 if is_alpha(c):
#                     start = i
#                     state = TRANSITION_TABLE[state]['is_alpha']
#                 elif c.isspace():
#                     if c == '\n':
#                         line_num += 1
#                         line_start = i + 1
#                     i += 1
#                     continue
#                 elif is_delimiter(c):
#                     state = TRANSITION_TABLE[state]['is_delimiter']
#                     self.tokens.append((self.delimiters[c], c, line_num, i, i+1))
#                 elif is_quote(c):
#                     start = i
#                     state = TRANSITION_TABLE[state]['is_quote']
#                 elif is_digit(c):
#                     state = TRANSITION_TABLE[state]['is_digit']
#                     start = i
#                 else:
#                     raise RuntimeError(f'{c!r} inesperado en la línea {line_num}')

#             elif state == 'S1':
#                 if is_alnum_or_underscore(c):
#                     state = TRANSITION_TABLE[state]['is_alnum_or_underscore']
#                 else:
#                     token = self.input_str[start:i]
#                     if token in self.keywords:
#                         self.tokens.append((self.keywords[token], token, line_num, start, i))
#                         if token == "nueva":
#                             while self.input_str[i].isspace():
#                                 i += 1
#                             if self.input_str[i:i+1] == "=":
#                                 i += 1
#                                 self.tokens.append(('EQUALS', '=', line_num, i-1, i))
#                             else:
#                                 i -= 1  # Revert the index back to handle the next token properly
#                     elif self.is_identifier(token):
#                         self.tokens.append(('ID', token, line_num, start, i))
#                     else:
#                         raise RuntimeError(f'{token!r} no es una palabra clave ni un identificador válido en la línea {line_num}')
#                     state = 'S0'
#                     continue

#             elif state == 'S2':
#                 state = 'S0'
#                 continue

#             elif state == 'S3':
#                 if is_quote(c):
#                     state = TRANSITION_TABLE[state]['is_quote']
#                 i += 1

#             elif state == 'S3_end':
#                 token = self.input_str[start + 1:i - 1]
#                 self.tokens.append(('STRING', token, line_num, start, i))
#                 state = 'S0'
#                 i += 1

#             elif state == 'S4':
#                 if not is_digit(c) and c != '.':
#                     token = self.input_str[start:i]
#                     self.tokens.append(('NUMBER', token, line_num, start, i))
#                     state = 'S0'
#                     continue

#             i += 1

#         return self.tokens + [None]


# def is_alpha(c):
#     return c.isalpha()

# def is_alnum_or_underscore(c):
#     return c.isalnum() or c == '_'

# def is_delimiter(c):
#     return c in r'{}()=,.;"\'\':}-$“”-* /'

# def is_quote(c):
#     return c in "\"'"


# TRANSITION_TABLE = {
#     'S0': {
#         'is_alpha': 'S1',
#         'is_delimiter': 'S2',
#         'is_quote': 'S3',
#     },
#     'S1': {
#         'is_alnum_or_underscore': 'S1',
#         'not_is_alnum_or_underscore': 'S0'
#     },
#     'S2': {
#         'not_is_delimiter': 'S0'
#     },
#     'S3': {
#         'is_quote': 'S3_end',
#     },
#     'S3_end': {
#         'not_is_quote': 'S0'
#     },
# }

# def is_comment_start(input_str, i):
#     return input_str[i:i+3] == '---'

# class Scanner:
#     def __init__(self, input_str):
#         self.input_str = input_str
#         self.tokens = []
#         self.keywords = {
#             "CrearBD": "CREATE_DB",
#             "nueva": "NEW",
#             "EliminarBD": "DROP_DB",
#             "CrearColeccion": "CREATE_COLLECTION",
#             "EliminarColeccion": "DROP_COLLECTION",
#             "InsertarUnico": "INSERT_ONE",
#             "ActualizarUnico": "UPDATE_ONE",
#             "EliminarUnico": "DELETE_ONE",
#             "BuscarTodo": "FIND_ALL",
#             "BuscarUnico": "FIND_ONE"
#         }

#         self.delimiters = {
#             '{': 'LBRACE',
#             '}': 'RBRACE',
#             '(': 'LPAREN',
#             ')': 'RPAREN',
#             '=': 'EQUALS',
#             ',': 'COMMA',
#             '.': 'DOT',
#             ';': 'SEMICOLON',
#             '"': 'DQUOTE',
#             "'": 'SQUOTE',
#             ':': 'COLON',
#             '$': 'DOLLAR',
#             '“': 'OPEN_QUOTE',
#             '”': 'CLOSE_QUOTE',
#             '-': 'SPACE',
#             '*': 'ASTERISK',
#             '/': 'BAR'
#         }

#     def is_identifier(self, s):
#         if s[0].isalpha() or s[0] == '_':
#             return all(c.isalnum() or c == '_' for c in s[1:])
#         return False

#     def tokenize(self):
#         self.tokens = []
#         state = 'S0'
#         line_num = 1
#         line_start = 0
#         i = 0
#         n = len(self.input_str)

#         while i < n:
#             c = self.input_str[i]

#             if is_comment_start(self.input_str, i):
#                 while i < n and self.input_str[i] != '\n':
#                     i += 1
#                 continue

#             if state == 'S0':
#                 if is_alpha(c):
#                     start = i
#                     state = TRANSITION_TABLE[state]['is_alpha']
#                 elif c.isspace():
#                     if c == '\n':
#                         line_num += 1
#                         line_start = i + 1
#                     i += 1
#                     continue
#                 elif is_delimiter(c):
#                     state = TRANSITION_TABLE[state]['is_delimiter']
#                     self.tokens.append((self.delimiters[c], c, line_num, i, i+1))
#                 elif is_quote(c):
#                     start = i
#                     state = TRANSITION_TABLE[state]['is_quote']
#                 else:
#                     raise RuntimeError(f'{c!r} inesperado en la línea {line_num}')

#             elif state == 'S1':
#                 if is_alnum_or_underscore(c):
#                     state = TRANSITION_TABLE[state]['is_alnum_or_underscore']
#                 else:
#                     token = self.input_str[start:i]
#                     if token in self.keywords:
#                         self.tokens.append((self.keywords[token], token, line_num, start, i))
#                         if token == "nueva":
#                             while self.input_str[i].isspace():
#                                 i += 1
#                             if self.input_str[i:i+1] == "=":
#                                 i += 1
#                                 self.tokens.append(('EQUALS', '=', line_num, i-1, i))
#                             else:
#                                 i -= 1  # Revert the index back to handle the next token properly
#                     elif self.is_identifier(token):
#                         self.tokens.append(('ID', token, line_num, start, i))
#                     else:
#                         raise RuntimeError(f'{token!r} no es una palabra clave ni un identificador válido en la línea {line_num}')
#                     state = 'S0'
#                     continue

#             elif state == 'S2':
#                 state = 'S0'
#                 continue

#             elif state == 'S3':
#                 if is_quote(c):
#                     state = TRANSITION_TABLE[state]['is_quote']
#                 i += 1

#             if state == 'S3_end':
#                 token = self.input_str[start + 1:i - 1]
#                 self.tokens.append(('STRING', token, line_num, start, i))
#                 state = 'S0'
#                 i += 1
#             else:
#                 i += 1

#         return self.tokens + [None]
