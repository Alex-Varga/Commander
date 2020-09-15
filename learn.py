from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.filedialog import *
from functools import partial
import ftplib
import pymysql
from PIL import Image, ImageTk

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
    return fileformat[0]


def main_window():

    def ftp_download_dialog_window():

        def new_dialog_window():
            messagebox.showinfo("", "ГОТОВО")


        def get_name_file():
            cursor = db.cursor()
            sql = "SELECT name_file FROM save_file"
            cursor.execute(sql)
            allfile = cursor.fetchall()
            db.commit()
            return allfile

        def check_window(elem):
            if elem not in get_name_file():
                messagebox.showerror("Ошибка", "Такого названия файла нет")

        def get_all_elements():
            cursor = db.cursor()
            sql = "SELECT name_file, format_file FROM save_file"
            cursor.execute(sql)
            allfile = cursor.fetchall()
            db.commit()
            return allfile

        get_all_elements()

        def set_request():
            try:
                s = entry1.get()
                ftp_download(s)
                new_dialog_window()
            except TypeError:
                check_window(get_name_file())
            entry1.insert(0, "")
            entry1.delete(0, END)

        def set_request_on_event(event):
            try:
                s = entry1.get()
                ftp_download(s)
                new_dialog_window()
            except TypeError:
                check_window(get_name_file())
            entry1.insert(0, "")
            entry1.delete(0, END)

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
        entry1.delete(0, END)


    window = Tk()
    window.title("")

    mainmenu = Menu(window)
    window.config(menu=mainmenu)
    mainmenu.add_command(label='Файлы')
    mainmenu.add_command(label='Выделение')
    mainmenu.add_command(label='Команды')
    mainmenu.add_command(label='Сеть')
    mainmenu.add_command(label='Вид')
    mainmenu.add_command(label='Конфигурация')
    mainmenu.add_command(label='Запуск')
    mainmenu.add_command(label='Справка')
    ttk.Separator(window, orient=HORIZONTAL).pack(side=TOP)
    img0 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный.png")
    img1 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный1.png")
    img2 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный2.png")
    img3 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный3.png")
    img4 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный4.png")
    img5 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный5.png")
    img6 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный6.png")
    img7 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный7.png")
    img8 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный8.png")
    img9 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный9.png")
    img10 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный10.png")
    img11 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный11.png")
    img12 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный12.png")
    img13 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный13.png")
    img14 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный14.png")
    img15 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный15.png")
    img16 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный16.png")
    img17 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\Безымянный17.png")

    frameBTN = Frame(window)
    frameBTN.pack(side=TOP, fill=X)
    btn_img1 = Button(frameBTN, image=img0)
    btn_img1.pack(side=LEFT)
    btn_img2 = Button(frameBTN, image=img1)
    btn_img2.pack(side=LEFT)
    btn_img3 = Button(frameBTN, image=img2)
    btn_img3.pack(side=LEFT)
    btn_img4 = Button(frameBTN, image=img3)
    btn_img4.pack(side=LEFT)
    btn_img5 = Button(frameBTN, image=img4)
    btn_img5.pack(side=LEFT)
    btn_img6 = Button(frameBTN, image=img5)
    btn_img6.pack(side=LEFT)
    btn_img7 = Button(frameBTN, image=img6)
    btn_img7.pack(side=LEFT)
    btn_img8 = Button(frameBTN, image=img7)
    btn_img8.pack(side=LEFT)
    btn_img9 = Button(frameBTN, image=img8)
    btn_img9.pack(side=LEFT)
    btn_img10 = Button(frameBTN, image=img9)
    btn_img10.pack(side=LEFT)
    btn_img11 = Button(frameBTN, image=img10)
    btn_img11.pack(side=LEFT)
    btn_img12 = Button(frameBTN, image=img11)
    btn_img12.pack(side=LEFT)
    btn_img13 = Button(frameBTN, image=img12)
    btn_img13.pack(side=LEFT)
    btn_img14 = Button(frameBTN, image=img13)
    btn_img14.pack(side=LEFT)
    btn_img15 = Button(frameBTN, image=img14)
    btn_img15.pack(side=LEFT)
    btn_img16 = Button(frameBTN, image=img15)
    btn_img16.pack(side=LEFT)
    btn_img17 = Button(frameBTN, image=img16)
    btn_img17.pack(side=LEFT)
    btn_img18 = Button(frameBTN, image=img17)
    btn_img18.pack(side=LEFT)

    mainframe = Frame(window)
    mainframe.pack(side=TOP, fill=X)
    frameLIST = Frame(mainframe)
    frameLIST.pack(side=LEFT, fill=Y)
    Lb1 = Listbox(frameLIST)
    Lb1.insert(1, "Рабочий стол")
    Lb1.insert(2, "Библиотеки")
    Lb1.insert(3, "Корзина")
    Lb1.insert(4, "Панель управления")
    Lb1.insert(5, "Сеть")
    Lb1.insert(6, "Этот компютер")
    Lb1.insert(7, "One Drive")
    Lb1.insert(8, "ftp")
    Lb1.pack(side=TOP)

    frameBLOCK1 = Frame(mainframe)
    frameBLOCK1.pack(side=LEFT, fill=Y, pady=40)
    tw1 = ttk.Treeview(frameBLOCK1)
    tw1["columns"] = ("one", "two", "three")
    tw1.column("#0", width=250, minwidth=250, stretch=tk.NO)
    tw1.column("one", width=80, minwidth=70, stretch=tk.NO)
    tw1.column("two", width=80, minwidth=70, stretch=tk.NO)
    tw1.column("three", width=100, minwidth=70, stretch=tk.NO)

    tw1.heading("#0", text="Имя", anchor=tk.W)
    tw1.heading("one", text="Тип", anchor=tk.W)
    tw1.heading("two", text="Размер", anchor=tk.W)
    tw1.heading("three", text="Дата", anchor=tk.W)

    tw1.pack(side=tk.TOP)

    imgg1 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\imgg1.png")
    imgg2 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\imgg2.png")
    imgg3 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\imgg3.png")
    imgg4 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\imgg4.png")
    imgg5 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\imgg5.png")
    imgg6 = ImageTk.PhotoImage(file=r"C:\Users\Vargas\Work\untitled\Img\imgg6.png")
    frameBTN2 = Frame(mainframe)
    frameBTN2.pack(side=LEFT, fill=Y, pady=25)
    btnimg1 = Button(frameBTN2, image=imgg1)
    btnimg1.pack(side=TOP)
    btnimg2 = Button(frameBTN2, image=imgg2)
    btnimg2.pack(side=TOP)
    btnimg3 = Button(frameBTN2, image=imgg3)
    btnimg3.pack(side=TOP)
    btnimg4 = Button(frameBTN2, image=imgg4)
    btnimg4.pack(side=TOP)
    btnimg5 = Button(frameBTN2, image=imgg5)
    btnimg5.pack(side=TOP)
    btnimg6 = Button(frameBTN2, image=imgg6)
    btnimg6.pack(side=TOP)

    frameBLOCK2 = Frame(mainframe)
    frameBLOCK2.pack(side=LEFT, fill=Y, pady=40)
    tw1 = ttk.Treeview(frameBLOCK2)
    tw1["columns"] = ("one", "two", "three")
    tw1.column("#0", width=250, minwidth=250, stretch=tk.NO)
    tw1.column("one", width=80, minwidth=70, stretch=tk.NO)
    tw1.column("two", width=80, minwidth=70, stretch=tk.NO)
    tw1.column("three", width=100, minwidth=70, stretch=tk.NO)

    tw1.heading("#0", text="Имя", anchor=tk.W)
    tw1.heading("one", text="Тип", anchor=tk.W)
    tw1.heading("two", text="Размер", anchor=tk.W)
    tw1.heading("three", text="Дата", anchor=tk.W)

    tw1.pack(side=tk.TOP, fill=tk.X)

    window.mainloop()
"""
    frame = Frame(window)
    frame.pack()

    lbl = Label(frame, text="Привет. Выбери одно из действий.")
    lbl.pack(side=TOP)

    button1 = Button(frame, text="Загрузить", fg="blue", width=20, command=ftp_putter)
    button1.pack(side=LEFT, padx=10, ipadx=10, pady=20, ipady=10)

    button2 = Button(frame, text="Скачать", fg="red", width=20, command=ftp_download_dialog_window)
    button2.pack(side=RIGHT, padx=10, ipadx=10, pady=20, ipady=10)
"""

main_window()
