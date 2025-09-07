import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Visualization App")
        
        # Создаем все элементы интерфейса
        self.create_for_label()
        self.create_for_table()
        self.create_while_label()
        self.create_while_table()
        self.create_plot()
        self.create_variables_section()
        self.create_image()
        self.create_radiobuttons()
        
    def create_for_label(self):
        """Создает label с надписью 'for' слева"""
        self.for_label = tk.Label(self.root, text="for", font=("Arial", 12, "bold"))
        self.for_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    
    def create_for_table(self):
        """Создает таблицу Treeview со скроллбаром для 'for'"""
        # Фрейм для таблицы и скроллбара
        table_frame = tk.Frame(self.root)
        table_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        
        # Создаем Treeview
        self.for_tree = ttk.Treeview(table_frame, columns=("x", "y"), show="headings", height=10)
        self.for_tree.heading("x", text="x")
        self.for_tree.heading("y", text="y")
        self.for_tree.column("x", width=50)
        self.for_tree.column("y", width=50)
        
        # Скроллбар
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.for_tree.yview)
        self.for_tree.configure(yscrollcommand=scrollbar.set)
        
        # Размещаем элементы
        self.for_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Заполняем данными
        x_data = [1, 2, 3, 4, 5]
        y_data = [2, 4, 1, 5, 3]
        
        for x, y in zip(x_data, y_data):
            self.for_tree.insert("", "end", values=(x, y))
    
    def create_while_label(self):
        """Создает label с надписью 'while' правее"""
        self.while_label = tk.Label(self.root, text="while", font=("Arial", 12, "bold"))
        self.while_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")
    
    def create_while_table(self):
        """Создает таблицу Treeview со скроллбаром для 'while'"""
        # Фрейм для таблицы и скроллбара
        table_frame = tk.Frame(self.root)
        table_frame.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")
        
        # Создаем Treeview
        self.while_tree = ttk.Treeview(table_frame, columns=("x", "y"), show="headings", height=10)
        self.while_tree.heading("x", text="x")
        self.while_tree.heading("y", text="y")
        self.while_tree.column("x", width=50)
        self.while_tree.column("y", width=50)
        
        # Скроллбар
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.while_tree.yview)
        self.while_tree.configure(yscrollcommand=scrollbar.set)
        
        # Размещаем элементы
        self.while_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def create_plot(self):
        """Создает поле для matplotlib графика"""
        # Фрейм для графика
        plot_frame = tk.Frame(self.root)
        plot_frame.grid(row=1, column=2, rowspan=2, padx=10, pady=5, sticky="nsew")
        
        # Создаем график
        fig, ax = plt.subplots(figsize=(5, 4))
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 1, 5, 3]
        ax.plot(x, y, 'o-')
        ax.set_title("Data Plot")
        
        # Встраиваем график в Tkinter
        self.canvas = FigureCanvasTkAgg(fig, plot_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def create_variables_section(self):
        """Создает секцию с переменными для построения графика"""
        variables_frame = tk.Frame(self.root)
        variables_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        
        # Переменные a, b, h
        labels = ["a:", "b:", "h:"]
        self.entries = {}
        
        for i, label_text in enumerate(labels):
            label = tk.Label(variables_frame, text=label_text)
            label.grid(row=0, column=i*2, padx=5)
            
            entry = tk.Entry(variables_frame, width=10)
            entry.grid(row=0, column=i*2+1, padx=5)
            self.entries[label_text[:-1]] = entry
    
    def create_image(self):
        """Создает поле для картинки"""
        image_frame = tk.Frame(self.root)
        image_frame.grid(row=1, column=3, padx=10, pady=5, sticky="nsew")
        
        try:
            # Пытаемся загрузить картинку (замените путь на свой)
            image = Image.open("example_image.png")  # Укажите путь к вашей картинке
            image = image.resize((150, 150), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
            
            image_label = tk.Label(image_frame, image=self.photo)
            image_label.pack()
            
        except FileNotFoundError:
            # Если картинка не найдена, показываем заглушку
            error_label = tk.Label(image_frame, text="Image not found", bg="lightgray", width=20, height=10)
            error_label.pack()
    
    def create_radiobuttons(self):
        """Создает 3 radiobutton с подписями"""
        rb_frame = tk.Frame(self.root)
        rb_frame.grid(row=2, column=3, padx=10, pady=5, sticky="nw")
        
        self.radio_var = tk.StringVar(value="Option 1")
        
        options = ["Option 1", "Option 2", "Option 3"]
        
        for i, option in enumerate(options):
            rb = tk.Radiobutton(rb_frame, text=option, variable=self.radio_var, value=option)
            rb.pack(anchor="w", pady=2)

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()