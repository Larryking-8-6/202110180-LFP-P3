import sys
from scanner import Scanner
from Parser import Parser
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class MainWindow(tk.Tk):
    def __init__(self):
        self.current_file = None
        super().__init__()

        # Ventana principal
        self.title('Compilador NoSQL - 202110180')
        self.geometry('1200x800')

        # Agregar widgets y configuraciones adicionales para la interfaz de usuario
        self.init_ui()

    def init_ui(self):
        # Menú principal
        self.main_menu = tk.Menu(self)
        self.config(menu=self.main_menu)

        # Menú Archivo
        self.menu_archivo = tk.Menu(self.main_menu, tearoff=0)
        self.menu_archivo.add_command(label="Nuevo", command=self.new_file)
        self.menu_archivo.add_command(label="Abrir", command=self.open_file)
        self.menu_archivo.add_command(label="Guardar", command=self.save_file)
        self.menu_archivo.add_command(label="Guardar como", command=self.save_file_as)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=self.quit)

        # Menú Análisis
        self.menu_analisis = tk.Menu(self.main_menu, tearoff=0)
        self.menu_analisis.add_command(label="Generar sentencias MongoDB", command=self.analyze_code)

        # Añadir menús a la barra de menú
        self.main_menu.add_cascade(label="Archivo", menu=self.menu_archivo)
        self.main_menu.add_cascade(label="Análisis", menu=self.menu_analisis)

        # Notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        # Pestañas
        self.code_tab = ttk.Frame(self.notebook)
        self.sentences_tab = ttk.Frame(self.notebook)
        self.tokens_tab = ttk.Frame(self.notebook)
        self.errors_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.code_tab, text="Código")
        self.notebook.add(self.sentences_tab, text="Sentencias Generadas")
        self.notebook.add(self.tokens_tab, text="Tokens")
        self.notebook.add(self.errors_tab, text="Errores")

        # Editor de código
        self.code_editor = tk.Text(self.code_tab, wrap="none")
        self.code_editor.pack(expand=True, fill="both")

        # Area de visualización de sentencias
        self.sentences_viewer = tk.Text(self.sentences_tab, wrap="none", state="disabled")
        self.sentences_viewer.pack(expand=True, fill="both")

        # Tabla de tokens
        self.tokens_table = ttk.Treeview(self.tokens_tab, columns=("No.", "Tipo", "Linea", "Lexema"), show="headings")
        self.tokens_table.pack(expand=True, fill="both")
        self.tokens_table.heading("No.", text="No.")
        self.tokens_table.heading("Tipo", text="Tipo")
        self.tokens_table.heading("Linea", text="Linea")
        self.tokens_table.heading("Lexema", text="Lexema")

        # Tabla de errores
        self.errors_table = ttk.Treeview(self.errors_tab, columns=("Tipo", "Linea", "Columna", "Mensaje"), show="headings")
        self.errors_table.pack(expand=True, fill="both")
        self.errors_table.heading("Tipo", text="Tipo")
        self.errors_table.heading("Linea", text="Linea")
        self.errors_table.heading("Columna", text="Columna")
        self.errors_table.heading("Mensaje", text="Mensaje")

    # Métodos de menú Archivo
    def new_file(self):
        self.code_editor.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                file_contents = file.read()
                self.code_editor.delete(1.0, tk.END)
                self.code_editor.insert(tk.INSERT, file_contents)
                self.current_file = file_path

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w") as file:
                file_contents = self.code_editor.get(1.0, tk.END)
                file.write(file_contents)
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as file:
                file_contents = self.code_editor.get(1.0, tk.END)
                file.write(file_contents)
                self.current_file = file_path

    def analyze_code(self):
        try:
            input_str = self.code_editor.get(1.0, tk.END)
            scanner = Scanner(input_str)
            tokens = scanner.tokenize()
            self.show_tokens(tokens)

            parser = Parser(tokens)
            statements, errors = parser.parse()

            self.show_statements(statements)
            self.show_errors(errors)

        except Exception as e:
            self.show_errors([("Error", "-", "-", f"Error inesperado: {str(e)}")])

    def show_statements(self, statements):
        self.sentences_viewer.config(state="normal")
        self.sentences_viewer.delete(1.0, tk.END)
        for statement in statements:
            formatted_statement = f"{statement}\n"
            self.sentences_viewer.insert(tk.INSERT, formatted_statement)
        self.sentences_viewer.config(state="disabled")

    def show_tokens(self, tokens):
        self.tokens_table.delete(*self.tokens_table.get_children())
        for i, token in enumerate(tokens):
            self.tokens_table.insert("", "end", values=(i + 1, token[0], token[2], token[1]))

    def show_errors(self, errors):
        self.errors_table.delete(*self.errors_table.get_children())
        for error in errors:
            self.errors_table.insert("", "end", values=(error[0], error[1], error[2], error[3]))

    def update_error_table(self, error_msg):
        self.errors_table.delete(*self.errors_table.get_children())
        self.errors_table.insert("", "end", values=("Error", "-", "-", error_msg))

if __name__ == '__main__':
    main_win = MainWindow()
    main_win.mainloop()