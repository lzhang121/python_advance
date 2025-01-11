# -*- coding: utf-8 -*-
# @Time : 2025/01/09 10:26
# @Author : zhanglei
# @Email : zhspark@gmail.com
import os
import re
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from googletrans import Translator
from PyPDF2 import PdfReader
from docx import Document

def translate_file(input_file, output_file, target_language):
    try:
        # 检测文件格式
        if input_file.endswith(".pdf"):
            reader = PdfReader(input_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
        else:
            raise ValueError("Unsupported file type. Only PDF files are supported.")

        # 翻译内容
        translator = Translator()
        text = re.sub(r"\t", " ", text)
        translated_text = translator.translate(text, dest=target_language).text

        # 保存到 Word 文件
        doc = Document()
        doc.add_paragraph(translated_text)
        doc.save(output_file)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def start_translation():
    if not file_path.get():
        messagebox.showerror("Error", "Please select a file to translate.")
        return

    target_language = language_combobox.get()
    if not target_language:
        messagebox.showerror("Error", "Please select a target language.")
        return

    # 输出文件路径
    output_file = os.path.splitext(file_path.get())[0] + f"_{target_language}.docx"

    # 执行翻译
    success = translate_file(file_path.get(), output_file, target_language)
    if success:
        messagebox.showinfo("Success", f"File translated successfully!\nSaved to: {output_file}")
    else:
        messagebox.showerror("Error", "An error occurred during translation.")

def select_file(event=None):
    file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file:
        file_path.set(file)

# 创建主窗口
root = tk.Tk()
root.title("File Translator")
root.geometry("500x300")

# 文件拖拽输入
file_path = tk.StringVar()
file_entry = tk.Entry(root, textvariable=file_path, width=50)
file_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

browse_button = tk.Button(root, text="Browse", command=select_file)
browse_button.grid(row=0, column=2, padx=10, pady=10)

# 语言选择
language_label = tk.Label(root, text="Target Language:")
language_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

languages = {
    "Chinese (Simplified)": "zh-cn",
    "Chinese (Traditional)": "zh-tw",
    "Japanese": "ja",
    "Korean": "ko",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Russian": "ru",
}
language_combobox = ttk.Combobox(root, values=list(languages.keys()), state="readonly")
language_combobox.grid(row=1, column=1, padx=10, pady=10)
language_combobox.set("Chinese (Simplified)")

# 确定按钮
translate_button = tk.Button(root, text="Translate", command=start_translation)
translate_button.grid(row=2, column=1, pady=20)

# 拖拽文件
def drop(event):
    file_path.set(event.data)

try:
    # macOS 支持拖拽文件
    import tkdnd
    dnd = tkdnd.TkinterDnD.Tk()
    root.tk.call("package", "require", "tkdnd")
    file_entry.drop_target_register(tkdnd.DND_FILES)
    file_entry.dnd_bind("<<Drop>>", drop)
except ImportError:
    pass  # 如果无法加载拖拽功能，则仅支持手动浏览

# 启动主循环
root.mainloop()