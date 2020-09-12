import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from functools import partial
import ftplib
import pymysql

db = pymysql.connect('reform09.mysql.tools', 'reform09_learn', 'n5aTN&~3u2', 'reform09_learn')
ftp = ftplib.FTP('reform09.ftp.tools', 'reform09_learn', 'qwertyfun7')


def set_name():
    cursor = db.cursor()
    sql = "SELECT MAX(name_file) FROM save_file"
    cursor.execute(sql)
    name = cursor.fetchone()
    db.commit()
    if not name[0]:
        return 1
    else:
        return int(name[0]) + 1


def ftp_putter():
    local_path = askopenfilename()
    splited_local_path = local_path.split('.')
    file_name = set_name()
    sql_putter(file_name, splited_local_path[1])
    with open(local_path, 'rb') as file:
        ftp.storbinary('STOR ' + "/first_program/" + str(file_name) + "." + str(splited_local_path[1]), file, 1024)


def ftp_download(file_name):
    download_path = 'C:/Users/Vargas/Downloads/'
    full_download_path = download_path + str(file_name) + "." + str(sql_format(file_name))
    with open(full_download_path, 'wb') as file:
        ftp.retrbinary('RETR ' + "/first_program/" + str(file_name) + "." + sql_format(str(file_name)), file.write)


def sql_putter(file_name, file_format):
    cursor = db.cursor()
    sql = "INSERT INTO save_file(name_file, format_file) VALUES ('" + str(file_name) + "', '" + str(file_format) + "')"
    cursor.execute(sql)
    db.commit()


def sql_format(filename):
    cursor = db.cursor()
    sql = "SELECT format_file FROM save_file WHERE name_file = '" + str(filename) + "'"
    cursor.execute(sql)
    fileformat = cursor.fetchone()
    db.commit()
    print(fileformat)
    return fileformat[0]


def main_window():

    def ftp_download_dialog_window():

        def get_all_elements():
            cursor = db.cursor()
            sql = "SELECT name_file, format_file FROM save_file"
            cursor.execute(sql)
            allfile = cursor.fetchall()
            db.commit()
            return allfile

        get_all_elements()

        def set_request():
            s = entry1.get()
            ftp_download(s)

        def set_request_on_event(event):
            print(event)
            s = entry1.get()
            ftp_download(s)

        dialog_window = Toplevel(window)
        dialog_window.title("")

        leftframe = Frame(dialog_window)
        leftframe.pack(side=LEFT)

        tree = ttk.Treeview(leftframe, show="headings", selectmode="browse")
        tree["columns"] = ("name", "format")

        tree.column("name", width=80, minwidth=70)
        tree.column("format", width=90, minwidth=90)

        tree.heading("name", text="Им'я файла", anchor=tk.W)
        tree.heading("format", text="Формат файла", anchor=tk.W)

        for file in get_all_elements():
            tree.insert("", tk.END, values=(file[0], file[1]))

        tree.pack(side=TOP, fill=BOTH, padx=20, pady=20)
        tree.config(height=10)

        rightframe = Frame(dialog_window)
        rightframe.pack(side=LEFT)

        lbl1 = Label(rightframe, text='Введите имя файла для загрузки на ваш ПК: ')
        lbl1.pack(side=TOP)

        entry1 = Entry(rightframe, width=40)
        entry1.pack(side=TOP, padx=20, pady=20, ipady=5)

        btn = Button(rightframe, text='Загрузить', width=34, command=set_request)
        btn.pack(side=TOP, padx=20, ipady=10)

        dialog_window.bind('<Return>', set_request_on_event)

    window = Tk()
    window.title("")

    frame = Frame(window)
    frame.pack()

    lbl = Label(frame, text="Привет. Выбери одно из действий.")
    lbl.pack(side=TOP)

    button1 = Button(frame, text="Загрузить", fg="blue", width=20, command=ftp_putter)
    button1.pack(side=LEFT, padx=10, ipadx=10, pady=20, ipady=10)

    button2 = Button(frame, text="Скачать", fg="red", width=20, command=ftp_download_dialog_window)
    button2.pack(side=RIGHT, padx=10, ipadx=10, pady=20, ipady=10)


    window.mainloop()


main_window()
