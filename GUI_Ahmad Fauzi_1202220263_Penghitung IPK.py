import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
import numpy as np

class PilihMode:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Penghitung IPK Telkom University")
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.exit_gui)
        style = ThemedStyle(self.root)
        style.set_theme("arc")
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.background_img = Image.open('Telkom.jpg')
        self.background_img = ImageTk.PhotoImage(self.background_img.resize((800, 600)))
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_img)
        self.frame_all = ttk.Frame(self.root)
        self.frame_all.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.6)
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_title = ttk.Label(self.frame_title, text="APLIKASI PENGHITUNG IPK", font=("Helvetica", 17, "bold"), foreground="white", background="#1AA7EC")
        self.label_title.pack(pady=25)
        self.frame_buttons = ttk.Frame(self.frame_all)
        self.frame_buttons.pack(pady=(50, 20))
        self.button_mahasiswa = tk.Button(self.frame_buttons, text="Portal Mahasiswa", command=self.open_login_mahasiswa, font=("Helvetica", 12, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=25)
        self.button_mahasiswa.grid(row=0, column=0, pady=10, sticky="ew")
        self.button_admin = tk.Button(self.frame_buttons, text="Portal Admin", command=self.open_login_admin, font=("Helvetica", 12, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove",  width=25)
        self.button_admin.grid(row=1, column=0, pady=10, sticky="ew")
        self.label_contact = ttk.Label(self.frame_all, text="Call Center (022) 7566456\nWebsite www.telkomuniversity.ac.id\nJl. Telekomunikasi. 1, Bojongsoang,\nKabupaten Bandung, Jawa Barat 40257", font=("Helvetica", 10), foreground="grey")
        self.label_contact.pack(pady=(20, 20))
        self.label_contact.configure(justify="center", anchor="center")
        
    def exit_gui(self):
        result = messagebox.askyesno('Exit', 'Apakah Anda yakin ingin keluar dari aplikasi?')
        if result:
            self.root.destroy()

    def open_login_mahasiswa(self):
        self.root.withdraw()
        login_mahasiswa_window = tk.Toplevel(self.root)
        login_mahasiswa_form = LoginMahasiswaForm(login_mahasiswa_window)

    def open_login_admin(self):
        self.root.withdraw()
        login_admin_window = tk.Toplevel(self.root)
        login_admin_form = LoginAdminForm(login_admin_window)

class LoginAdminForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Admin")
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.exit_gui)
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.background_img = Image.open('Telkom.jpg')
        self.background_img = ImageTk.PhotoImage(self.background_img.resize((800, 600)))
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_img)
        self.frame_all = ttk.Frame(self.root)
        self.frame_all.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5)
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_login = ttk.Label(self.frame_title, text="LOGIN ADMIN", font=("Helvetica", 18, "bold"), foreground="white", background="#1AA7EC")
        self.label_login.pack(pady=(15,10))
        self.label_app = ttk.Label(self.frame_title, text="Aplikasi Penghitung IPK", foreground="white", background="#1AA7EC", font=("Helvetica", 13))
        self.label_app.pack(pady=(5,15))
        self.frame_input = ttk.Frame(self.frame_all)
        self.frame_input.pack(pady=(30,20))
        self.label_nim = ttk.Label(self.frame_input, text="Kode Admin", foreground="#555", font=("Helvetica", 10))
        self.label_nim.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_kode_admin = ttk.Entry(self.frame_input, foreground="#555", font=("Helvetica", 10), width=25)
        self.entry_kode_admin.grid(row=0, column=1, padx=5, pady=5)
        self.label_password = ttk.Label(self.frame_input, text="Password", foreground="#555", font=("Helvetica", 10))
        self.label_password.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_password = ttk.Entry(self.frame_input, show="*", foreground="#555", font=("Helvetica", 10), width=25)
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)
        self.frame_create_account = ttk.Frame(self.frame_all)
        self.frame_create_account.pack(pady=(10,20))
        self.label_create_account = ttk.Label(self.frame_create_account, text="Kalau kamu belum memiliki akun", foreground="#555", font=("Helvetica", 10))
        self.label_create_account.grid(row=0, column=0, padx=5)
        self.label_signup = ttk.Label(self.frame_create_account, text="Sign Up", font=("Helvetica", 10, "underline"), foreground="blue", cursor="hand2")
        self.label_signup.grid(row=0, column=1, padx=5)
        self.label_signup.bind("<Button-1>", self.open_signup_form)
        self.button_login = tk.Button(self.frame_all, text="Login", command=self.login, font=("Helvetica", 12, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove",  width=25)
        self.button_login.pack(pady=(5, 30))
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="alpro_penghitungipk",
            port="3308")

    def exit_gui(self):
        result = messagebox.askyesno('Exit', 'Apakah Anda yakin ingin keluar dari aplikasi?')
        if result:
            self.root.destroy()
    
    def login(self):
        kode_admin = self.entry_kode_admin.get()
        password = self.entry_password.get()
        try:
            kode_admin = int(kode_admin)
        except ValueError:
            messagebox.showerror("Login", "Kode Admin harus berupa angka!")
            return
        cursor = self.db.cursor()
        if password == "Admin":
            query = "SELECT nama FROM admin WHERE id_admin = %s"
            cursor.execute(query, (kode_admin,))
            result = cursor.fetchone()
            if result:
                nama = result[0]
                messagebox.showinfo("Login", f"Login Berhasil!\nSelamat Datang, {nama}!")
                self.root.withdraw()
                self.open_menu_admin_utama(nama, kode_admin)
            else:
                messagebox.showerror("Login", "Login gagal! Kode Admin atau Password salah!")
        else:
            messagebox.showerror("Login", "Login gagal! Kode Admin atau Password salah!")
        cursor.close()

    def open_menu_admin_utama(self, nama, kode_admin):
        menu_admin_utama_window = tk.Toplevel(self.root)
        menu_admin_utama_form = MainMenuAdminForm(menu_admin_utama_window, nama, kode_admin, self.db)

    def open_signup_form(self, event):
        self.root.withdraw()
        signup_admin_form = tk.Toplevel(self.root)
        signup_admin_form = SignupAdminForm(signup_admin_form, self.db)
    
class SignupAdminForm:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Sign Up Admin")
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.exit_gui)
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.background_img = Image.open('Telkom.jpg')
        self.background_img = ImageTk.PhotoImage(self.background_img.resize((800, 600)))
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_img)
        self.frame_all = ttk.Frame(self.root)
        self.frame_all.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5)
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_signup = ttk.Label(self.frame_title, text="SIGN UP ADMIN", font=("Helvetica", 24, "bold"), foreground="white", background="#1AA7EC")
        self.label_signup.pack(pady=(15,10))
        self.label_app = ttk.Label(self.frame_title, text="Aplikasi Penghitung IPK", foreground="white", background="#1AA7EC", font=("Helvetica", 13))
        self.label_app.pack(pady=(5,15))
        self.frame_input = ttk.Frame(self.frame_all)
        self.frame_input.pack(pady=(30,20))
        self.label_kode_admin = ttk.Label(self.frame_input, text="Kode Admin", foreground="#555", font=("Helvetica", 10))
        self.label_kode_admin.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_kode_admin = ttk.Entry(self.frame_input, foreground="#555", font=("Helvetica", 10), width=25)
        self.entry_kode_admin.grid(row=0, column=1, padx=5, pady=5)
        self.label_nama = ttk.Label(self.frame_input, text="Nama Admin", foreground="#555", font=("Helvetica", 10))
        self.label_nama.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_nama = ttk.Entry(self.frame_input, foreground="#555", font=("Helvetica", 10), width=25)
        self.entry_nama.grid(row=1, column=1, padx=5, pady=5)
        self.label_status_admin = ttk.Label(self.frame_input, text="Status", foreground="#555", font=("Helvetica", 10))
        self.label_status_admin.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.combobox_status_admin = ttk.Combobox(self.frame_input, values=["LAA", "Tim IT"], font=("Helvetica", 10), width=23)
        self.combobox_status_admin.grid(row=2, column=1, padx=5, pady=5)
        self.combobox_status_admin.set("")
        self.frame_login_account = ttk.Frame(self.frame_all)
        self.frame_login_account.pack(pady=(10,20))
        self.label_login_account = ttk.Label(self.frame_login_account, text="Kembali Ke Menu", foreground="#555", font=("Helvetica", 10))
        self.label_login_account.grid(row=0, column=0, padx=5)
        self.label_login = ttk.Label(self.frame_login_account, text="Login", font=("Helvetica", 10, "underline"), foreground="blue", cursor="hand2")
        self.label_login.grid(row=0, column=1, padx=5)
        self.label_login.bind("<Button-1>", self.open_login_form)
        self.button_daftar = tk.Button(self.frame_all, text="Daftar", command=self.daftar, font=("Helvetica", 12, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove",  width=25)
        self.button_daftar.pack(pady=(5, 30))
        self.db = db

    def exit_gui(self):
        self.open_login_form(None)

    def daftar(self):
        kode_admin = self.entry_kode_admin.get()
        nama = self.entry_nama.get()
        status = self.combobox_status_admin.get()
        if not kode_admin or not nama or not status:
            messagebox.showwarning("Sign Up", "Harap isi semua kolom!")
            return
        try:
            int(kode_admin)
        except ValueError:
            messagebox.showerror("Error", "Kode Admin harus berupa angka!")
            return
        cursor = self.db.cursor()
        try:
            query = "INSERT INTO admin (id_admin, nama, status) VALUES (%s, %s, %s)"
            data = (kode_admin, nama, status)
            cursor.execute(query, data)
            self.db.commit()
            cursor.close()
            messagebox.showinfo("Sign Up", f"Nama {nama} dengan status {status} berhasil terdaftar!")
            self.entry_kode_admin.delete(0, tk.END)
            self.entry_nama.delete(0, tk.END)
            self.combobox_status_admin.set("") 
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", f"Kode Admin {kode_admin} sudah terdaftar!")
        
    def open_login_form(self, event):
        self.root.withdraw()
        login_admin_form = tk.Toplevel(self.root)
        login_admin_form = LoginAdminForm(login_admin_form)

class LoginMahasiswaForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Mahasiswa")
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.exit_gui)
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.background_img = Image.open('Telkom.jpg')
        self.background_img = ImageTk.PhotoImage(self.background_img.resize((800, 600)))
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_img)
        self.frame_all = ttk.Frame(self.root)
        self.frame_all.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5)
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_login = ttk.Label(self.frame_title, text="LOGIN MAHASISWA", font=("Helvetica", 18, "bold"), foreground="white", background="#1AA7EC")
        self.label_login.pack(pady=(15,10))
        self.label_app = ttk.Label(self.frame_title, text="Aplikasi Penghitung IPK", foreground="white", background="#1AA7EC", font=("Helvetica", 13))
        self.label_app.pack(pady=(5,15))
        self.frame_input = ttk.Frame(self.frame_all)
        self.frame_input.pack(pady=(30,20))
        self.label_nim = ttk.Label(self.frame_input, text="NIM", foreground="#555", font=("Helvetica", 10))
        self.label_nim.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_nim = ttk.Entry(self.frame_input, foreground="#555", font=("Helvetica", 10), width=25)
        self.entry_nim.grid(row=0, column=1, padx=5, pady=5)
        self.label_password = ttk.Label(self.frame_input, text="Password", foreground="#555", font=("Helvetica", 10))
        self.label_password.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_password = ttk.Entry(self.frame_input, show="*", foreground="#555", font=("Helvetica", 10), width=25)
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)
        self.frame_create_account = ttk.Frame(self.frame_all)
        self.frame_create_account.pack(pady=(10,20))
        self.label_create_account = ttk.Label(self.frame_create_account, text="Kalau kamu belum memiliki akun", foreground="#555", font=("Helvetica", 10))
        self.label_create_account.grid(row=0, column=0, padx=5)
        self.label_signup = ttk.Label(self.frame_create_account, text="Sign Up", font=("Helvetica", 10, "underline"), foreground="blue", cursor="hand2")
        self.label_signup.grid(row=0, column=1, padx=5)
        self.label_signup.bind("<Button-1>", self.open_signup_form)
        self.button_login = tk.Button(self.frame_all, text="Login", command=self.login, font=("Helvetica", 12, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove",  width=25)
        self.button_login.pack(pady=(5, 30))
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="alpro_penghitungipk",
            port="3308")

    def exit_gui(self):
        result = messagebox.askyesno('Exit', 'Apakah Anda yakin ingin keluar dari aplikasi?')
        if result:
            self.root.destroy()

    def login(self):
        nim = self.entry_nim.get()
        password = self.entry_password.get()
        try:
            nim = int(nim)
        except ValueError:
            messagebox.showerror("Login", "NIM harus berupa angka!")
            return
        cursor = self.db.cursor()
        if password == "Mahasiswa":
            query = "SELECT * FROM mahasiswa WHERE nim = %s"
            cursor.execute(query, (nim,))
            result = cursor.fetchone()
            if result:
                nama = result[1]
                messagebox.showinfo("Login", f"Login Berhasil!\nSelamat Datang, {nama}!")
                self.root.withdraw()
                self.open_menu_mahasiswa_utama(nama, nim)
            else:
                messagebox.showerror("Login", "Login gagal! NIM atau Password salah!")
        else:
            messagebox.showerror("Login", "Login gagal! NIM atau Password salah!")
        cursor.close()

    def open_signup_form(self, event):
        self.root.withdraw()
        signup_mahasiswa_form = tk.Toplevel(self.root)
        signup_mahasiswa_form = SignupMahasiswaForm(signup_mahasiswa_form, self.db)

    def open_menu_mahasiswa_utama(self, nama_mahasiswa, nim):
        menu_mahasiswa_utama_form = tk.Toplevel()
        menu_mahasiswa_utama_form = MainMenuMahasiswaForm(menu_mahasiswa_utama_form, nama_mahasiswa, nim, self.db)

class SignupMahasiswaForm:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Sign Up Admin")
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.exit_gui)
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.background_img = Image.open('Telkom.jpg')
        self.background_img = ImageTk.PhotoImage(self.background_img.resize((800, 600)))
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_img)
        self.frame_all = ttk.Frame(self.root)
        self.frame_all.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5)
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_signup = ttk.Label(self.frame_title, text="SIGN UP MAHASISWA", font=("Helvetica", 24, "bold"), foreground="white", background="#1AA7EC")
        self.label_signup.pack(pady=(15,10))
        self.label_app = ttk.Label(self.frame_title, text="Aplikasi Penghitung IPK", foreground="white", background="#1AA7EC", font=("Helvetica", 13))
        self.label_app.pack(pady=(5,15))
        self.frame_input = ttk.Frame(self.frame_all)
        self.frame_input.pack(pady=(30,20))
        self.label_nim = ttk.Label(self.frame_input, text="NIM", foreground="#555", font=("Helvetica", 10))
        self.label_nim.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_nim = ttk.Entry(self.frame_input, foreground="#555", font=("Helvetica", 10), width=25)
        self.entry_nim.grid(row=0, column=1, padx=5, pady=5)
        self.label_nama = ttk.Label(self.frame_input, text="Nama Mahasiswa", foreground="#555", font=("Helvetica", 10))
        self.label_nama.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_nama = ttk.Entry(self.frame_input, foreground="#555", font=("Helvetica", 10), width=25)
        self.entry_nama.grid(row=1, column=1, padx=5, pady=5)
        self.label_program_studi = ttk.Label(self.frame_input, text="Program Studi", foreground="#555", font=("Helvetica", 10))
        self.label_program_studi.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_program_studi = ttk.Entry(self.frame_input, foreground="#555", font=("Helvetica", 10), width=25)
        self.entry_program_studi.grid(row=2, column=1, padx=5, pady=5)
        self.label_fakultas = ttk.Label(self.frame_input, text="Fakultas", foreground="#555", font=("Helvetica", 10))
        self.label_fakultas.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_fakultas = ttk.Entry(self.frame_input, foreground="#555", font=("Helvetica", 10), width=25)
        self.entry_fakultas.grid(row=3, column=1, padx=5, pady=5)
        self.frame_login_account = ttk.Frame(self.frame_all)
        self.frame_login_account.pack(pady=(10,20))
        self.label_login_account = ttk.Label(self.frame_login_account, text="Kembali Ke Menu", foreground="#555", font=("Helvetica", 10))
        self.label_login_account.grid(row=0, column=0, padx=5)
        self.label_login = ttk.Label(self.frame_login_account, text="Login", font=("Helvetica", 10, "underline"), foreground="blue", cursor="hand2")
        self.label_login.grid(row=0, column=1, padx=5)
        self.label_login.bind("<Button-1>", self.open_login_form)
        self.button_daftar = tk.Button(self.frame_all, text="Daftar", command=self.daftar, font=("Helvetica", 12, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove",  width=25)
        self.button_daftar.pack(pady=(5, 30))
        self.db = db

    def exit_gui(self):
        self.open_login_form(None)

    def daftar(self):
        nim = self.entry_nim.get()
        nama = self.entry_nama.get()
        program_studi = self.entry_program_studi.get()
        fakultas = self.entry_fakultas.get()
        if not nim or not nama or not program_studi:
            messagebox.showwarning("Sign Up", "Harap isi semua kolom!")
            return
        try:
            int(nim)
        except ValueError:
            messagebox.showerror("Error", "NIM harus berupa angka!")
            return
        cursor = self.db.cursor()
        try:
            query = "INSERT INTO mahasiswa (nim, nama, prodi, fakultas) VALUES (%s, %s, %s, %s)"
            data = (nim, nama, program_studi, fakultas)
            cursor.execute(query, data)
            self.db.commit()
            cursor.close()
            messagebox.showinfo("Sign Up", f"Mahasiswa dengan nama {nama} dari Program Studi {program_studi} dan {fakultas} berhasil terdaftar!")
            self.entry_nim.delete(0, tk.END)
            self.entry_nama.delete(0, tk.END) 
            self.entry_program_studi.delete(0, tk.END)
            self.entry_fakultas.delete(0, tk.END)
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", f"NIM {nim} sudah terdaftar!")
        
    def open_login_form(self, event):
        self.root.withdraw()
        login_mahasiswa_form = tk.Toplevel(self.root)
        login_mahasiswa_form = LoginMahasiswaForm(login_mahasiswa_form)

class MainMenuMahasiswaForm:
    def __init__(self, root, nama_mahasiswa, nim, db):
        self.root = root
        self.root.title("Menu Utama Mahasiswa")
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.exit_gui)
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.background_img = Image.open('Telkom.jpg')
        self.background_img = ImageTk.PhotoImage(self.background_img.resize((800, 600)))
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_img)
        self.frame_all = ttk.Frame(self.root)
        self.frame_all.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.6)
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_app = ttk.Label(self.frame_title, text="APLIKASI PENGHITUNG IPK", font=("Helvetica", 17, "bold"), foreground="white", background="#1AA7EC")
        self.label_app.pack(pady=(15,10))
        self.label_welcome = ttk.Label(self.frame_title, text=f"Selamat Datang, {nama_mahasiswa}!", foreground="white", background="#1AA7EC", font=("Helvetica", 13))
        self.label_welcome.pack(pady=(5,15))
        self.input_frame = ttk.LabelFrame(self.frame_all, text=" Pilihan Menu ")
        self.input_frame.pack(pady=(30,30))
        self.button_input = tk.Button(self.input_frame, text="Input Nilai", command=self.open_input_nilai_form, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=30)
        self.button_input.grid(row=0, pady=5, padx=15, sticky="ew")
        self.button_edit = tk.Button(self.input_frame, text="Edit Nilai", command=self.open_edit_nilai_form, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=30)
        self.button_edit.grid(row=1, pady=5, padx=15, sticky="ew")
        self.button_delete_nilai = tk.Button(self.input_frame, text="Delete Nilai", command=self.open_delete_nilai_form, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=30)
        self.button_delete_nilai.grid(row=2, pady=5, padx=15, sticky="ew")
        self.button_tampilkan_tabel_ipk = tk.Button(self.input_frame, text="Tampilkan Tabel IPK Per Semester", command=self.tampilkan_tabel_ipk, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=30)
        self.button_tampilkan_tabel_ipk.grid(row=3, pady=5, padx=15, sticky="ew")
        self.button_tampilkan_grafik_ipk = tk.Button(self.input_frame, text="Tampilkan Grafik IPK Per Semester", command=self.tampilkan_grafik_ipk, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=30)
        self.button_tampilkan_grafik_ipk.grid(row=4, pady=5, padx=15, sticky="ew")
        self.button_logout = tk.Button(self.input_frame, text="Logout", command=self.logout, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=30)
        self.button_logout.grid(row=5, pady=(5,10), padx=15, sticky="ew")
        self.nama_mahasiswa = nama_mahasiswa
        self.nim = nim
        self.db = db

    def exit_gui(self):
        result = messagebox.askyesno('Exit', 'Apakah Anda yakin ingin keluar dari aplikasi?')
        if result:
            self.root.destroy()

    def open_input_nilai_form(self):
        input_nilai_window = tk.Toplevel(self.root)
        input_nilai_form = Input_Nilai_Form(input_nilai_window, self.nim, self.db)
    
    def open_edit_nilai_form(self):
        edit_nilai_window = tk.Toplevel(self.root)
        edit_nilai_form = Edit_Nilai_Form(edit_nilai_window, self.nim, self.db)
    
    def open_delete_nilai_form(self):
        delete_nilai_window = tk.Toplevel(self.root)
        delete_nilai_form = Delete_Nilai_Form(delete_nilai_window, self.nim, self.db)

    def tampilkan_tabel_ipk(self):
        tabel_ipk_window = tk.Toplevel(self.root)
        tabel_ipk_form = TabelIPKForm(tabel_ipk_window, self.nim, self.db)

    def tampilkan_grafik_ipk(self):
        grafik_ipk_window = tk.Toplevel(self.root)
        grafik_ipk_form = GrafikIPKForm(grafik_ipk_window, self.nim, self.nama_mahasiswa, self.db)
    
    def logout(self):
        result = messagebox.askyesno('Exit', 'Apakah Anda yakin ingin Logout?')
        if result:
            self.root.destroy()
            pilih_mode_window = tk.Toplevel()
            pilih_mode_form = PilihMode(pilih_mode_window)

class Input_Nilai_Form:
    def __init__(self, root, nim, db):
        self.root = root
        self.root.title("Input Nilai")
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.exit_gui)
        self.frame_all = tk.Frame(self.root, background="white")
        self.frame_all.pack()
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_judul = ttk.Label(self.frame_title, text="INPUT NILAI", font=("Helvetica", 17, "bold"), foreground="white", background="#1AA7EC")
        self.label_judul.pack(pady=10)
        self.input_button_frame = tk.Frame(self.frame_all, background="white")
        self.input_button_frame.pack(padx=20, pady=(25,10))
        self.input_frame = tk.LabelFrame(self.input_button_frame, text=" Input Data Nilai Mahasiswa ", background="white")
        self.input_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.label_semester = tk.Label(self.input_frame, text="Semester: ", background="white")
        self.label_semester.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_semester = ttk.Combobox(self.input_frame, values=["1", "2", "3", "4", "5", "6", "7", "8"], font=("Helvetica", 10))
        self.combo_semester.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.combo_semester.bind("<<ComboboxSelected>>", self.load_semester_data)
        self.label_mata_kuliah = tk.Label(self.input_frame, text="Mata Kuliah: ", background="white")
        self.label_mata_kuliah.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_mata_kuliah = ttk.Combobox(self.input_frame)
        self.combo_mata_kuliah.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.label_indeks_nilai = tk.Label(self.input_frame, text="Indeks Nilai: ", font=("Helvetica", 10), background="white")
        self.label_indeks_nilai.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_indeks_nilai = ttk.Combobox(self.input_frame, values=["A", "AB", "B", "BC", "C", "D", "E"], font=("Helvetica", 10))
        self.combo_indeks_nilai.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.button_frame = tk.Frame(self.input_button_frame, background="white")
        self.button_frame.grid(row=0, column=2, padx=15, pady=5)
        self.button_input_nilai = tk.Button(self.button_frame, text="Input Nilai", command=self.simpan_nilai, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove")
        self.button_input_nilai.pack(fill=tk.X, padx=5, pady=5)
        self.table_frame = tk.Frame(self.frame_all)
        self.table_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        self.treeview = ttk.Treeview(self.table_frame, columns=("Mata Kuliah", "Indeks Nilai"), show="headings")
        self.treeview.heading("Mata Kuliah", text="Mata Kuliah")
        self.treeview.heading("Indeks Nilai", text="Indeks Nilai")
        self.treeview.pack(fill=tk.BOTH, expand=True)
        self.nim = nim
        self.db = db
        self.load_data()

    def exit_gui(self):
        self.root.destroy()
    
    def load_semester_data(self, event):
        self.load_mata_kuliah(event)
        self.combo_mata_kuliah.set("")
        self.combo_indeks_nilai.set("")
        self.load_data(event)
        
    def load_data(self, event=None):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        semester = self.combo_semester.get()
        cursor = self.db.cursor()
        query = "SELECT mata_kuliah, nilai FROM nilai WHERE nim = %s AND semester = %s"
        cursor.execute(query, (self.nim, semester))
        rows = cursor.fetchall()
        for row in rows:
            self.treeview.insert("", "end", values=row)
        cursor.close()
    
    def load_mata_kuliah(self, event):
        semester = self.combo_semester.get()
        if self.combo_mata_kuliah.winfo_exists():
            self.combo_mata_kuliah.set("")
        else:
            self.combo_mata_kuliah = ttk.Combobox(self.input_frame)
        cursor = self.db.cursor()
        table_name = f"semester{semester}"
        query = f"SELECT mata_kuliah FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchall()
        mata_kuliah_list = [row[0] for row in result]
        self.combo_mata_kuliah['values'] = mata_kuliah_list
        cursor.close()
    
    def simpan_nilai(self):
        semester = self.combo_semester.get()
        mata_kuliah = self.combo_mata_kuliah.get()
        indeks_nilai = self.combo_indeks_nilai.get()
        if not semester or not mata_kuliah or not indeks_nilai:
            messagebox.showwarning("Input Nilai", "Harap isi semua kolom sebelum menekan button!")
            return
        # Memeriksa apakah mata kuliah sudah memiliki nilai pada semester yang sama
        cursor = self.db.cursor()
        query = f"SELECT COUNT(*) FROM nilai WHERE nim = {self.nim} AND mata_kuliah = '{mata_kuliah}' AND semester = {semester}"
        cursor.execute(query)
        result = cursor.fetchone()
        if result[0] > 0:
            messagebox.showwarning("Input Nilai", f"Mata kuliah '{mata_kuliah}' sudah memiliki nilai pada semester {semester}!")
            cursor.close()
            return
        cursor.close()
        # Mengambil SKS dari tabel semester
        cursor = self.db.cursor()
        table_name = f"semester{semester}"
        query = f"SELECT sks FROM {table_name} WHERE mata_kuliah = '{mata_kuliah}'"
        cursor.execute(query)
        sks_result = cursor.fetchone()
        sks = sks_result[0]
        cursor.close()
        # Simpan data nilai ke tabel 'nilai'
        cursor = self.db.cursor()
        query = "INSERT INTO nilai (nim, semester, mata_kuliah, nilai, sks) VALUES (%s, %s, %s, %s, %s)"
        data = (self.nim, semester, mata_kuliah, indeks_nilai, sks)
        cursor.execute(query, data)
        self.db.commit()
        cursor.close()
        self.update_ipk()
        messagebox.showinfo("Input Nilai", f"Nilai Mata Kuliah {mata_kuliah} Pada Semester {semester} Berhasil Disimpan!")
        self.load_data()
    
    def update_ipk(self):
        semester = self.combo_semester.get()
        total_ipk = self.HitungNilai(semester)
        cursor = self.db.cursor()
        query = f"UPDATE mahasiswa SET semester{semester} = {total_ipk} WHERE nim = {self.nim}"
        cursor.execute(query)
        self.db.commit()
        cursor.close()
    
    def KonversiNilai(self, nilai):
        if nilai.upper() == "A":
            nilai_konversi = 4
        elif nilai.upper() == "AB":
            nilai_konversi = 3.5
        elif nilai.upper() == "B":
            nilai_konversi = 3
        elif nilai.upper() == "BC":
            nilai_konversi = 2.5
        elif nilai.upper() == "C":
            nilai_konversi = 2
        elif nilai.upper() == "D":
            nilai_konversi = 1
        elif nilai.upper() == "E":
            nilai_konversi = 0
        return nilai_konversi

    def HitungNilai(self, semester):
        cur = self.db.cursor()
        cur.execute(f"SELECT nilai, sks FROM nilai WHERE semester = {semester}")
        hasil = cur.fetchall()
        total_sks = 0
        total_nilai = 0
        for nilai, sks in hasil:
            total_sks += sks
            nilai_konversi = self.KonversiNilai(nilai) * sks
            total_nilai += nilai_konversi
        if total_sks > 0:
            ipk = total_nilai / total_sks
        else:
            ipk = 0
        return ipk

class Edit_Nilai_Form(Input_Nilai_Form):
    def __init__(self, root, nim, db):
        super().__init__(root, nim, db)
        self.root.title("Edit Nilai")
        self.frame_all.destroy()
        self.frame_all = tk.Frame(self.root, background="white")
        self.frame_all.pack()
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_judul = ttk.Label(self.frame_title, text="EDIT NILAI", font=("Helvetica", 17, "bold"), foreground="white", background="#1AA7EC")
        self.label_judul.pack(pady=10)
        self.input_button_frame = tk.Frame(self.frame_all, background="white")
        self.input_button_frame.pack(padx=20, pady=(25,10))
        self.input_frame = tk.LabelFrame(self.input_button_frame, text=" Input Data Nilai Mahasiswa ", background="white")
        self.input_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.label_semester = tk.Label(self.input_frame, text="Semester: ", background="white")
        self.label_semester.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_semester = ttk.Combobox(self.input_frame, values=["1", "2", "3", "4", "5", "6", "7", "8"], font=("Helvetica", 10))
        self.combo_semester.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.combo_semester.bind("<<ComboboxSelected>>", self.load_semester_data)
        self.label_indeks_nilai = tk.Label(self.input_frame, text="Indeks Nilai: ", font=("Helvetica", 10), background="white")
        self.label_indeks_nilai.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_indeks_nilai = ttk.Combobox(self.input_frame, values=["A", "AB", "B", "BC", "C", "D", "E"], font=("Helvetica", 10))
        self.combo_indeks_nilai.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.button_frame = tk.Frame(self.input_button_frame, background="white")
        self.button_frame.grid(row=0, column=2, padx=15, pady=5)
        self.button_edit_nilai = tk.Button(self.button_frame, text="Edit Nilai", command=self.edit_nilai, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove")
        self.button_edit_nilai.pack(fill=tk.X, padx=5, pady=5)
        self.table_frame = tk.Frame(self.frame_all)
        self.table_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        self.treeview = ttk.Treeview(self.table_frame, columns=("Mata Kuliah", "Indeks Nilai"), show="headings")
        self.treeview.heading("Mata Kuliah", text="Mata Kuliah")
        self.treeview.heading("Indeks Nilai", text="Indeks Nilai")
        self.treeview.pack(fill=tk.BOTH, expand=True)

    def edit_nilai(self):
        if not self.treeview.focus():
            tk.messagebox.showwarning("Warning", "Silahkan pilih data pada tabel nilai yang ingin diedit!")
            return
        semester = self.combo_semester.get()
        indeks_nilai = self.combo_indeks_nilai.get()
        selected_item = self.treeview.focus()
        values = self.treeview.item(selected_item, "values")
        mata_kuliah = values[0]
        if not semester or not indeks_nilai:
            messagebox.showwarning("Edit Nilai", "Harap isi semua kolom sebelum menekan button Edit Nilai!")
            return
        cursor = self.db.cursor()
        query = "UPDATE nilai SET nilai=%s WHERE nim=%s AND semester=%s AND mata_kuliah=%s"
        data = (indeks_nilai, self.nim, semester, mata_kuliah)
        cursor.execute(query, data)
        self.db.commit()
        self.update_ipk()
        cursor.close()
        self.treeview.set(selected_item, "Indeks Nilai", indeks_nilai)
        messagebox.showinfo("Edit Berhasil!", f"Data Mata Kuliah {mata_kuliah} Pada Semester {semester} Berhasil Diedit!")

class Delete_Nilai_Form(Edit_Nilai_Form):
    def __init__(self, root, nim, db):
        super().__init__(root, nim, db)
        self.root.title("Delete Nilai")
        self.frame_all.destroy()
        self.frame_all = tk.Frame(self.root, background="white")
        self.frame_all.pack()
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_judul = ttk.Label(self.frame_title, text="DELETE NILAI", font=("Helvetica", 17, "bold"), foreground="white", background="#1AA7EC")
        self.label_judul.pack(pady=10)
        self.input_button_frame = tk.Frame(self.frame_all, background="white")
        self.input_button_frame.pack(padx=20, pady=(25,10))
        self.input_frame = tk.LabelFrame(self.input_button_frame, text=" Input Data Nilai Mahasiswa ", background="white")
        self.input_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.label_semester = tk.Label(self.input_frame, text="Semester: ", background="white")
        self.label_semester.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_semester = ttk.Combobox(self.input_frame, values=["1", "2", "3", "4", "5", "6", "7", "8"], font=("Helvetica", 10))
        self.combo_semester.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.combo_semester.bind("<<ComboboxSelected>>", self.load_data)
        self.button_frame = tk.Frame(self.input_button_frame, background="white")
        self.button_frame.grid(row=0, column=2, padx=15, pady=5)
        self.button_delete_nilai = tk.Button(self.button_frame, text="Delete Nilai", command=self.delete_nilai, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove")
        self.button_delete_nilai.pack(fill=tk.X, padx=5, pady=5)
        self.table_frame = tk.Frame(self.frame_all)
        self.table_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        self.treeview = ttk.Treeview(self.table_frame, columns=("Mata Kuliah", "Indeks Nilai"), show="headings")
        self.treeview.heading("Mata Kuliah", text="Mata Kuliah")
        self.treeview.heading("Indeks Nilai", text="Indeks Nilai")
        self.treeview.pack(fill=tk.BOTH, expand=True)

    def delete_nilai(self):
        if not self.treeview.focus():
            tk.messagebox.showwarning("Warning", "Silahkan pilih data pada tabel nilai yang ingin dihapus!")
            return
        semester = self.combo_semester.get()
        selected_item = self.treeview.focus()
        values = self.treeview.item(selected_item, "values")
        mata_kuliah = values[0]
        cursor = self.db.cursor()
        query = "DELETE FROM nilai WHERE nim=%s AND mata_kuliah=%s AND semester=%s"
        data = ( self.nim, mata_kuliah, semester)
        cursor.execute(query, data)
        self.db.commit()
        self.update_ipk()
        cursor.close()
        self.treeview.delete(selected_item)
        messagebox.showinfo("Delete Berhasil!", f"Data Mata Kuliah {mata_kuliah} Pada Semester {semester} Telah Dihapus!")

class TabelIPKForm(Delete_Nilai_Form):
    def __init__(self, root, nim, db):
        super().__init__(root, nim, db)
        self.root.title("Tabel IPK")
        self.frame_all.destroy()
        self.frame_all = tk.Frame(self.root, background="white")
        self.frame_all.pack()
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_judul = ttk.Label(self.frame_title, text="TABEL IPK MAHASISWA", font=("Helvetica", 17, "bold"), foreground="white", background="#1AA7EC")
        self.label_judul.pack(pady=10)
        self.input_button_frame = tk.Frame(self.frame_all, background="white")
        self.input_button_frame.pack(padx=20, pady=(25,10))
        self.input_frame = tk.LabelFrame(self.input_button_frame, text=" Pilihan Menu ", background="white")
        self.input_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.label_semester = tk.Label(self.input_frame, text="Semester: ", background="white")
        self.label_semester.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_semester = ttk.Combobox(self.input_frame, values=["1", "2", "3", "4", "5", "6", "7", "8"], font=("Helvetica", 10))
        self.combo_semester.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.button_frame = tk.Frame(self.input_button_frame, background="white")
        self.button_frame.grid(row=0, column=2, padx=15, pady=5)
        self.button_delete_ipk = tk.Button(self.button_frame, text="Delete IPK", command=self.delete_ipk, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove")
        self.button_delete_ipk.pack(fill=tk.X, padx=5, pady=5)
        self.table_frame = tk.Frame(self.frame_all)
        self.table_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        self.treeview = ttk.Treeview(self.table_frame, columns=["Semester", "IPK"], show="headings")
        self.treeview.column("Semester",anchor="center")
        self.treeview.column("IPK", anchor="center")
        self.treeview.heading("Semester", text="Semester")
        self.treeview.heading("IPK", text="IPK")
        self.treeview.pack(fill=tk.BOTH, expand=True)
        self.frame_stat = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_stat.pack(fill=tk.X)
        self.label_rata_rata_ipk = tk.Label(self.frame_stat, text="Rata-rata IPK: ", foreground="white", background="#1AA7EC")
        self.label_rata_rata_ipk.pack(padx=5, pady=5)
        self.label_max_ipk = tk.Label(self.frame_stat, text="Max IPK: ", foreground="white", background="#1AA7EC")
        self.label_max_ipk.pack(padx=5, pady=5)
        self.label_min_ipk = tk.Label(self.frame_stat, text="Min IPK: ", foreground="white", background="#1AA7EC")
        self.label_min_ipk.pack(padx=5, pady=5)
        self.loads_data()

    def delete_ipk(self):
        semester = self.combo_semester.get()
        if not semester:
            messagebox.showwarning("Delete IPK", "Harap pilih semester sebelum menekan tombol Delete IPK!")
            return
        cursor = self.db.cursor()
        # Menghapus data IPK pada tabel mahasiswa
        query = f"UPDATE mahasiswa SET semester{semester} = NULL WHERE nim = {self.nim}"
        cursor.execute(query)
        self.db.commit()
        # Menghapus data nilai pada tabel nilai
        query = f"DELETE FROM nilai WHERE semester = {semester} AND nim = {self.nim}"
        cursor.execute(query)
        self.db.commit()
        cursor.close()
        messagebox.showinfo("Delete IPK", f"Data IPK pada Semester {semester} berhasil dihapus!")
        self.combo_semester.set("")
        self.loads_data()

    def loads_data(self):
        self.treeview.delete(*self.treeview.get_children())  # Menghapus semua item pada Treeview
        cursor = self.db.cursor()
        query = "SELECT semester1, semester2, semester3, semester4, semester5, semester6, semester7, semester8 FROM mahasiswa WHERE nim = %s"
        cursor.execute(query, (self.nim,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            sem1, sem2, sem3, sem4, sem5, sem6, sem7, sem8 = row
            ipk_list = [sem1, sem2, sem3, sem4, sem5, sem6, sem7, sem8]
            for i in range(len(ipk_list)):
                if ipk_list[i] is None:
                    ipk_list[i] = "Nilai Tidak Ditemukan"
                else:
                    ipk_list[i] = float(ipk_list[i])
            for semester, ipk in enumerate(ipk_list, start=1):
                self.treeview.insert("", "end", values=(semester, ipk if isinstance(ipk, float) else ipk))
            filtered_ipk_list = [ipk for ipk in ipk_list if isinstance(ipk, float)]
            if filtered_ipk_list:
                rata_rata = sum(filtered_ipk_list) / len(filtered_ipk_list)
                max_ipk = max(filtered_ipk_list)
                min_ipk = min(filtered_ipk_list)
                self.label_rata_rata_ipk.config(text=f"Rata-rata IPK: {rata_rata:.2f}", font=("Helvetica", 10, "bold"))
                self.label_max_ipk.config(text=f"Max IPK: {max_ipk:.2f}", font=("Helvetica", 10, "bold"))
                self.label_min_ipk.config(text=f"Min IPK: {min_ipk:.2f}", font=("Helvetica", 10, "bold"))
            else:
                self.label_rata_rata_ipk.config(text="Rata-rata IPK: Nilai Tidak Ditemukan")
                self.label_max_ipk.config(text="Max IPK: Nilai Tidak Ditemukan")
                self.label_min_ipk.config(text="Min IPK: Nilai Tidak Ditemukan")
        else:
            messagebox.showwarning("Data Mahasiswa", "Data mahasiswa tidak ditemukan!")

class GrafikIPKForm:
    def __init__(self, root, nim, nama_mahasiswa, db):
        self.root = root
        self.root.title("Grafik IPK")
        self.nim = nim
        self.nama_mahasiswa = nama_mahasiswa
        self.db = db
        cursor = self.db.cursor()
        query = f"SELECT semester1, semester2, semester3, semester4, semester5, semester6, semester7, semester8 FROM mahasiswa WHERE nim = {self.nim}"
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()
        if not row:
            messagebox.showwarning("Data Mahasiswa", "Data mahasiswa tidak ditemukan!")
            return
        nilai = list(row)
        if all(value is None or value == 0 for value in nilai):
            messagebox.showwarning("Data Mahasiswa", "Data nilai mahasiswa kosong!")
            return
        self.figure = None
        self.show_graph()

    def show_graph(self):
        if self.figure is not None:
            self.figure.clear()
        cursor = self.db.cursor()
        query = f"SELECT semester1, semester2, semester3, semester4, semester5, semester6, semester7, semester8 FROM mahasiswa WHERE nim = {self.nim}"
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()
        nilai = list(row)
        val = list(range(8))
        data = []
        for i in range(8):
            if nilai[i] is not None:
                data.append(nilai[i])
            else:
                data.append(0)
        self.figure = plt.figure(figsize=(8, 6), dpi=80)
        ax = self.figure.add_subplot(111)
        ax.bar(val, data, color="lightblue")
        ax.set_title(f"IPK Mahasiswa {self.nama_mahasiswa} - {self.nim}", fontsize=12)
        ax.set_xlabel("Semester", fontsize=10)
        ax.set_ylabel("Nilai", fontsize=10)
        ax.set_xticks(val)
        ax.set_xticklabels(["Sem. 1", "Sem. 2", "Sem. 3", "Sem. 4", "Sem. 5", "Sem. 6", "Sem. 7", "Sem. 8"], fontsize=10)
        ax.tick_params(axis="y", labelsize=10)
        ax.set_ylim(bottom=0, top=4.5)  # Mengatur batas sumbu y
        ax.grid(True)
        canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()

class MainMenuAdminForm:
    def __init__(self, root, nama, kode_admin, db):
        self.root = root
        self.root.title("Menu Utama Mahasiswa")
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.exit_gui)
        self.canvas = tk.Canvas(self.root, width=900, height=700)
        self.canvas.pack()
        self.background_img = Image.open('Telkom.jpg')
        self.background_img = ImageTk.PhotoImage(self.background_img.resize((900, 700)))
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_img)
        self.frame_all = ttk.Frame(self.root)
        self.frame_all.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.6)
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_app = ttk.Label(self.frame_title, text="APLIKASI PENGHITUNG IPK", font=("Helvetica", 17, "bold"), foreground="white", background="#1AA7EC")
        self.label_app.pack(pady=(15,10))
        self.label_welcome = ttk.Label(self.frame_title, text=f"Selamat Datang, {nama}!", foreground="white", background="#1AA7EC", font=("Helvetica", 13))
        self.label_welcome.pack(pady=(5,15))
        self.input_frame = ttk.LabelFrame(self.frame_all, text=" Pilihan Menu ")
        self.input_frame.pack(pady=(30,30))
        self.button_input = tk.Button(self.input_frame, text="Input Nilai", command=self.open_input_nilai_form, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=45)
        self.button_input.grid(row=0, pady=5, padx=15, sticky="ew")
        self.button_edit = tk.Button(self.input_frame, text="Edit Nilai", command=self.open_edit_nilai_form, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=45)
        self.button_edit.grid(row=1, pady=5, padx=15, sticky="ew")
        self.button_delete_nilai = tk.Button(self.input_frame, text="Delete Nilai", command=self.open_delete_nilai_form, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=45)
        self.button_delete_nilai.grid(row=2, pady=5, padx=15, sticky="ew")
        self.button_tampilkan_delete_ipk = tk.Button(self.input_frame, text="Delete IPK", command=self.tampilkan_delete_ipk, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=45)
        self.button_tampilkan_delete_ipk.grid(row=3, pady=5, padx=15, sticky="ew")
        self.button_tampilkan_nilai = tk.Button(self.input_frame, text="Tampilkan Nilai Seluruh Mahasiswa", command=self.tampilkan_nilai, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=45)
        self.button_tampilkan_nilai.grid(row=4, pady=5, padx=15, sticky="ew")
        self.button_tampilkan_grafik_ipk = tk.Button(self.input_frame, text="Tampilkan Grafik IPK Per Semester", command=self.tampilkan_grafik_ipk, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=45)
        self.button_tampilkan_grafik_ipk.grid(row=5, pady=5, padx=15, sticky="ew")
        self.button_grafik_ipk_avg = tk.Button(self.input_frame, text="Tampilkan Grafik Rata-Rata IPK Seluruh Mahasiswa", command=self.grafik_ipk_avg, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=45)
        self.button_grafik_ipk_avg.grid(row=6, pady=5, padx=15, sticky="ew")
        self.button_input_mk = tk.Button(self.input_frame, text="Input Mata Kuliah", command=self.open_input_mk_form, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=45)
        self.button_input_mk.grid(row=7, pady=5, padx=15, sticky="ew")
        self.button_edit_mk = tk.Button(self.input_frame, text="Edit Mata Kuliah", command=self.open_edit_mk_form, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=45)
        self.button_edit_mk.grid(row=8, pady=5, padx=15, sticky="ew")
        self.button_delete_mk = tk.Button(self.input_frame, text="Delete Mata Kuliah", command=self.open_delete_mk_form, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=45)
        self.button_delete_mk.grid(row=9, pady=5, padx=15, sticky="ew")
        self.button_logout = tk.Button(self.input_frame, text="Logout", command=self.logout, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove", width=45)
        self.button_logout.grid(row=10, pady=(5,10), padx=15, sticky="ew")
        self.nama = nama
        self.kode_admin = kode_admin
        self.db = db

    def exit_gui(self):
        result = messagebox.askyesno('Exit', 'Apakah Anda yakin ingin keluar dari aplikasi?')
        if result:
            self.root.destroy()

    def open_input_mk_form(self):
        input_mk_window = tk.Toplevel(self.root)
        input_mk_form = InputMataKuliahForm(input_mk_window, self.db)

    def open_edit_mk_form(self):
        edit_mk_window = tk.Toplevel(self.root)
        edit_mk_form = EditMataKuliahForm(edit_mk_window, self.db)

    def open_delete_mk_form(self):
        delete_mk_window = tk.Toplevel(self.root)
        delete_mk_form = DeleteMataKuliahForm(delete_mk_window, self.db)

    def open_input_nilai_form(self):
        input_nilai_window = tk.Toplevel(self.root)
        input_nilai_form = InputNilaiFormAdmin(input_nilai_window, self.nama, self.db)

    def open_edit_nilai_form(self):
        edit_nilai_window = tk.Toplevel(self.root)
        edit_nilai_form = EditNilaiFormAdmin(edit_nilai_window, self.nama, self.db)

    def open_delete_nilai_form(self):
        delete_nilai_window = tk.Toplevel(self.root)
        delete_nilai_form = DeleteNilaiFormAdmin(delete_nilai_window, self.nama, self.db)
    
    def tampilkan_delete_ipk(self):
        grafik_window = tk.Toplevel(self.root)
        grafik_form = DeleteIPKFormAdmin(grafik_window, self.nama, self.db)
    
    def tampilkan_nilai(self):
        nilai_window = tk.Toplevel(self.root)
        nilai_form = NilaiMahasiswa(nilai_window, self.nama, self.db)

    def tampilkan_grafik_ipk(self):
        grafik_window = tk.Toplevel(self.root)
        grafik_form = GrafikIPKFormAdmin(grafik_window, self.nama, self.db)
    
    def grafik_ipk_avg(self):
        grafikavg_window = tk.Toplevel(self.root)
        grafikavg_form = GrafikRataIPKPerSemester(grafikavg_window, self.db)
    
    def logout(self):
        result = messagebox.askyesno('Exit', 'Apakah Anda yakin ingin Logout?')
        if result:
            self.root.destroy()
            pilih_mode_window = tk.Toplevel()
            pilih_mode_form = PilihMode(pilih_mode_window)

class InputNilaiFormAdmin:
    def __init__(self, root, nim, db):
        self.root = root
        self.root.title("Input Nilai")
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.exit_gui)
        self.frame_all = tk.Frame(self.root, background="white")
        self.frame_all.pack()
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_judul = tk.Label(self.frame_title, text="INPUT NILAI ADMIN", font=("Helvetica", 17, "bold"), foreground="white", background="#1AA7EC")
        self.label_judul.pack(pady=10)
        self.input_button_frame = tk.Frame(self.frame_all, background="white")
        self.input_button_frame.pack(padx=20, pady=(25,10))
        self.input_frame = tk.LabelFrame(self.input_button_frame, text=" Input Data Nilai Mahasiswa ", background="white")
        self.input_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.label_nim = tk.Label(self.input_frame, text="NIM: ", font=("Helvetica", 10), background="white")
        self.label_nim.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.db = db
        cur = db.cursor()
        cur.execute("SELECT nim FROM mahasiswa")
        nim_list = [str(row[0]) for row in cur.fetchall()]
        cur.close()
        self.combo_nim = ttk.Combobox(self.input_frame, values=nim_list, font=("Helvetica", 10))
        self.combo_nim.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.combo_nim.bind("<<ComboboxSelected>>", self.load_semester_options)
        self.label_semester = tk.Label(self.input_frame, text="Semester: ", font=("Helvetica", 10), background="white")
        self.label_semester.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_semester = ttk.Combobox(self.input_frame, values=["1", "2", "3", "4", "5", "6", "7", "8"], font=("Helvetica", 10))
        self.combo_semester.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.combo_semester.bind("<<ComboboxSelected>>", self.load_semester_data)
        self.label_mata_kuliah = tk.Label(self.input_frame, text="Mata Kuliah: ", background="white")
        self.label_mata_kuliah.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_mata_kuliah = ttk.Combobox(self.input_frame)
        self.combo_mata_kuliah.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        self.label_indeks_nilai = tk.Label(self.input_frame, text="Indeks Nilai: ", font=("Helvetica", 10), background="white")
        self.label_indeks_nilai.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_indeks_nilai = ttk.Combobox(self.input_frame, values=["A", "AB", "B", "BC", "C", "D", "E"], font=("Helvetica", 10))
        self.combo_indeks_nilai.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
        self.button_frame = tk.Frame(self.input_button_frame, background="white")
        self.button_frame.grid(row=0, column=2, padx=15, pady=5)
        self.button_input_nilai = tk.Button(self.button_frame, text="Input Nilai", command=self.simpan_nilai, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove")
        self.button_input_nilai.pack(fill=tk.X, padx=5, pady=5)
        self.table_frame = tk.Frame(self.frame_all)
        self.table_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        self.treeview = ttk.Treeview(self.table_frame, columns=("Mata Kuliah", "Indeks Nilai"), show="headings")
        self.treeview.heading("Mata Kuliah", text="Mata Kuliah")
        self.treeview.heading("Indeks Nilai", text="Indeks Nilai")
        self.treeview.pack(fill=tk.BOTH, expand=True)
        self.load_data()

    def exit_gui(self):
        self.root.destroy()

    def load_semester_options(self, event):
        selected_nim = self.combo_nim.get()
        if selected_nim:
            self.treeview.delete(*self.treeview.get_children())
            if self.combo_mata_kuliah.winfo_exists():
                self.combo_mata_kuliah['values'] = []
                self.combo_mata_kuliah.set("")
            self.combo_semester.set("")
            self.combo_indeks_nilai.set("")

    def load_semester_data(self, event):
        self.load_mata_kuliah(event)
        self.combo_mata_kuliah.set("")
        self.combo_indeks_nilai.set("")
        self.load_data(event)

    def load_mata_kuliah(self, event):
        semester = self.combo_semester.get()
        if self.combo_mata_kuliah.winfo_exists():
            self.combo_mata_kuliah.set("")
        else:
            self.combo_mata_kuliah = ttk.Combobox(self.input_frame)
        # Mengambil daftar mata kuliah dari tabel semester
        cursor = self.db.cursor()
        table_name = f"semester{semester}"
        query = f"SELECT mata_kuliah FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchall()
        mata_kuliah_list = [row[0] for row in result]
        self.combo_mata_kuliah['values'] = mata_kuliah_list
        cursor.close()

    def load_data(self, event=None):
        self.treeview.delete(*self.treeview.get_children())
        selected_nim = self.combo_nim.get()
        selected_semester = self.combo_semester.get()
        cursor = self.db.cursor()
        query = "SELECT mata_kuliah, nilai, semester FROM nilai WHERE nim = %s AND semester = %s"
        cursor.execute(query, (selected_nim, selected_semester))
        rows = cursor.fetchall()
        for row in rows:
            self.treeview.insert("", "end", values=row)
        cursor.close()

    def simpan_nilai(self):
        nim = self.combo_nim.get()
        semester = self.combo_semester.get()
        mata_kuliah = self.combo_mata_kuliah.get()
        indeks_nilai = self.combo_indeks_nilai.get()
        if not semester or not mata_kuliah or not indeks_nilai:
            messagebox.showwarning("Input Nilai", "Harap isi semua kolom sebelum menekan tombol!")
            return
        # Memeriksa apakah mata kuliah sudah memiliki nilai pada semester yang sama
        cursor = self.db.cursor()
        query = f"SELECT COUNT(*) FROM nilai WHERE nim = '{nim}' AND mata_kuliah = '{mata_kuliah}' AND semester = {semester}"
        cursor.execute(query)
        result = cursor.fetchone()
        if result[0] > 0:
            messagebox.showwarning("Input Nilai", f"Mata kuliah '{mata_kuliah}' sudah memiliki nilai pada semester {semester}!")
            cursor.close()
            return
        cursor.close()
        # Mengambil SKS dari tabel semester
        cursor = self.db.cursor()
        table_name = f"semester{semester}"
        query = f"SELECT sks FROM {table_name} WHERE mata_kuliah = '{mata_kuliah}'"
        cursor.execute(query)
        sks_result = cursor.fetchone()
        sks = sks_result[0]
        cursor.close()
        # Simpan data nilai ke tabel 'nilai'
        cursor = self.db.cursor()
        query = "INSERT INTO nilai (nim, semester, mata_kuliah, nilai, sks) VALUES (%s, %s, %s, %s, %s)"
        data = (nim, semester, mata_kuliah, indeks_nilai, sks)
        cursor.execute(query, data)
        self.db.commit()
        cursor.close()
        self.update_ipk(nim, semester)
        messagebox.showinfo("Input Nilai", f"Nilai Mata Kuliah {mata_kuliah} Pada Semester {semester} Berhasil Disimpan!")
        self.load_data()

    def update_ipk(self, nim, semester):
        total_ipk = self.HitungNilai(semester)
        cursor = self.db.cursor()
        query = f"UPDATE mahasiswa SET semester{semester} = %s WHERE nim = %s"
        data = (total_ipk, nim)
        cursor.execute(query, data)
        self.db.commit()
        cursor.close()
    
    def KonversiNilai(self, nilai):
        if nilai.upper() == "A":
            nilai_konversi = 4
        elif nilai.upper() == "AB":
            nilai_konversi = 3.5
        elif nilai.upper() == "B":
            nilai_konversi = 3
        elif nilai.upper() == "BC":
            nilai_konversi = 2.5
        elif nilai.upper() == "C":
            nilai_konversi = 2
        elif nilai.upper() == "D":
            nilai_konversi = 1
        elif nilai.upper() == "E":
            nilai_konversi = 0
        return nilai_konversi

    def HitungNilai(self, semester):
        cur = self.db.cursor()
        cur.execute(f"SELECT nilai, sks FROM nilai WHERE semester = {semester}")
        hasil = cur.fetchall()
        total_sks = 0
        total_nilai = 0
        for nilai, sks in hasil:
            total_sks += sks
            nilai_konversi = self.KonversiNilai(nilai) * sks
            total_nilai += nilai_konversi
        if total_sks > 0:
            ipk = total_nilai / total_sks
        else:
            ipk = 0
        return ipk

class EditNilaiFormAdmin(InputNilaiFormAdmin):
    def __init__(self, root, nim, db):
        super().__init__(root, nim, db)
        self.root.title("Edit Nilai")
        self.frame_all.destroy()
        self.frame_all = tk.Frame(self.root, background="white")
        self.frame_all.pack()
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_judul = ttk.Label(self.frame_title, text="EDIT NILAI ADMIN", font=("Helvetica", 17, "bold"), foreground="white", background="#1AA7EC")
        self.label_judul.pack(pady=10)
        self.input_button_frame = tk.Frame(self.frame_all, background="white")
        self.input_button_frame.pack(padx=20, pady=(25,10))
        self.input_frame = tk.LabelFrame(self.input_button_frame, text=" Input Data Nilai Mahasiswa ", background="white")
        self.input_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.label_nim = tk.Label(self.input_frame, text="NIM: ", font=("Helvetica", 10), background="white")
        self.label_nim.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        cur = db.cursor()
        cur.execute("SELECT nim FROM mahasiswa")
        nim_list = [str(row[0]) for row in cur.fetchall()]
        cur.close()
        self.combo_nim = ttk.Combobox(self.input_frame, values=nim_list, font=("Helvetica", 10))
        self.combo_nim.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.combo_nim.bind("<<ComboboxSelected>>", self.load_semester_options)
        self.label_semester = tk.Label(self.input_frame, text="Semester: ", font=("Helvetica", 10))
        self.label_semester.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_semester = ttk.Combobox(self.input_frame, values=["1", "2", "3", "4", "5", "6", "7", "8"], font=("Helvetica", 10))
        self.combo_semester.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.combo_semester.bind("<<ComboboxSelected>>", self.load_semester_data)
        self.label_indeks_nilai = tk.Label(self.input_frame, text="Indeks Nilai: ", font=("Helvetica", 10), background="white")
        self.label_indeks_nilai.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_indeks_nilai = ttk.Combobox(self.input_frame, values=["A", "AB", "B", "BC", "C", "D", "E"], font=("Helvetica", 10))
        self.combo_indeks_nilai.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.button_frame = tk.Frame(self.input_button_frame, background="white")
        self.button_frame.grid(row=0, column=2, padx=5, pady=5)
        self.button_edit_nilai = tk.Button(self.button_frame, text="Edit Nilai", command=self.edit_nilai, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove")
        self.button_edit_nilai.pack(fill=tk.X, padx=5, pady=5)
        self.table_frame = tk.Frame(self.frame_all)
        self.table_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        self.treeview = ttk.Treeview(self.table_frame, columns=("Mata Kuliah", "Indeks Nilai"), show="headings")
        self.treeview.heading("Mata Kuliah", text="Mata Kuliah")
        self.treeview.heading("Indeks Nilai", text="Indeks Nilai")
        self.treeview.pack(fill=tk.BOTH, expand=True)

    def edit_nilai(self):
        if not self.treeview.focus():
            tk.messagebox.showwarning("Warning", "Silahkan pilih data pada tabel nilai yang ingin diedit!")
            return
        nim = self.combo_nim.get()
        semester = self.combo_semester.get()
        indeks_nilai = self.combo_indeks_nilai.get()
        selected_item = self.treeview.focus()
        values = self.treeview.item(selected_item, "values")
        mata_kuliah = values[0]
        if not semester or not indeks_nilai:
            messagebox.showwarning("Edit Nilai", "Harap isi semua kolom sebelum menekan tombol Edit Nilai!")
            return
        cursor = self.db.cursor()
        query = "UPDATE nilai SET nilai=%s WHERE nim=%s AND semester=%s AND mata_kuliah=%s"
        data = (indeks_nilai, nim, semester, mata_kuliah)
        cursor.execute(query, data)
        self.db.commit()
        self.update_ipk(nim, semester)
        cursor.close()
        self.treeview.set(selected_item, "Indeks Nilai", indeks_nilai)
        messagebox.showinfo("Edit Berhasil!", f"Data Mata Kuliah {mata_kuliah} Pada Semester {semester} Berhasil Diedit!")

class DeleteNilaiFormAdmin(EditNilaiFormAdmin):
    def __init__(self, root, nim, db):
        super().__init__(root, nim, db)
        self.root.title("Delete Nilai")
        self.frame_all.destroy()
        self.frame_all = tk.Frame(self.root, background="white")
        self.frame_all.pack()
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_judul = tk.Label(self.frame_title, text="DELETE NILAI ADMIN", font=("Helvetica", 17, "bold"), foreground="white", background="#1AA7EC")
        self.label_judul.pack(pady=10)
        self.input_button_frame = tk.Frame(self.frame_all, background="white")
        self.input_button_frame.pack(padx=20, pady=(25,10))
        self.input_frame = tk.LabelFrame(self.input_button_frame, text=" Input Data Nilai Mahasiswa ", background="white")
        self.input_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.label_nim = tk.Label(self.input_frame, text="NIM: ", font=("Helvetica", 10), background="white")
        self.label_nim.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        cur = db.cursor()
        cur.execute("SELECT nim FROM mahasiswa")
        nim_list = [str(row[0]) for row in cur.fetchall()]
        cur.close()
        self.combo_nim = ttk.Combobox(self.input_frame, values=nim_list, font=("Helvetica", 10))
        self.combo_nim.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.combo_nim.bind("<<ComboboxSelected>>", self.load_semester_options)
        self.label_semester = tk.Label(self.input_frame, text="Semester: ", font=("Helvetica", 10))
        self.label_semester.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_semester = ttk.Combobox(self.input_frame, values=["1", "2", "3", "4", "5", "6", "7", "8"], font=("Helvetica", 10))
        self.combo_semester.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.combo_semester.bind("<<ComboboxSelected>>", self.load_data)
        self.button_frame = tk.Frame(self.input_button_frame, background="white")
        self.button_frame.grid(row=0, column=2, padx=5, pady=5)
        self.button_delete_nilai = tk.Button(self.button_frame, text="Delete Nilai", command=self.delete_nilai, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove")
        self.button_delete_nilai.pack(fill=tk.X, padx=5, pady=5)
        self.table_frame = tk.Frame(self.frame_all)
        self.table_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        self.treeview = ttk.Treeview(self.table_frame, columns=("Mata Kuliah", "Indeks Nilai"), show="headings")
        self.treeview.heading("Mata Kuliah", text="Mata Kuliah")
        self.treeview.heading("Indeks Nilai", text="Indeks Nilai")
        self.treeview.pack(fill=tk.BOTH, expand=True)

    def load_semester_options(self, event):
        selected_nim = self.combo_nim.get()
        if selected_nim:
            self.treeview.delete(*self.treeview.get_children())
            self.combo_semester.set("")

    def delete_nilai(self):
        if not self.treeview.focus():
            tk.messagebox.showwarning("Warning", "Silahkan pilih data pada tabel nilai yang ingin dihapus!")
            return
        nim = self.combo_nim.get()
        semester = self.combo_semester.get()
        selected_item = self.treeview.focus()
        values = self.treeview.item(selected_item, "values")
        mata_kuliah = values[0]
        cursor = self.db.cursor()
        query = "DELETE FROM nilai WHERE nim=%s AND mata_kuliah=%s AND semester=%s"
        data = (nim, mata_kuliah, semester)
        cursor.execute(query, data)
        self.db.commit()
        self.update_ipk(nim, semester)
        cursor.close()
        self.treeview.delete(selected_item)
        messagebox.showinfo("Delete Berhasil!", f"Data Mata Kuliah {mata_kuliah} Pada Semester {semester} Telah Dihapus!")

class DeleteIPKFormAdmin(DeleteNilaiFormAdmin):
    def __init__(self, root, nim, db):
        super().__init__(root, nim, db)
        self.root.title("Tabel IPK")
        self.frame_all.destroy()
        self.frame_all = tk.Frame(self.root, background="white")
        self.frame_all.pack()
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_judul = tk.Label(self.frame_title, text="TABEL IPK ADMIN", font=("Helvetica", 17, "bold"), foreground="white", background="#1AA7EC")
        self.label_judul.pack(pady=10)
        self.input_button_frame = tk.Frame(self.frame_all, background="white")
        self.input_button_frame.pack(padx=20, pady=(25,10))
        self.input_frame = tk.LabelFrame(self.input_button_frame, text=" Pilihan Menu ", background="white")
        self.input_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.label_nim = tk.Label(self.input_frame, text="NIM: ", font=("Helvetica", 10), background="white")
        self.label_nim.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        cur = db.cursor()
        cur.execute("SELECT nim FROM mahasiswa")
        nim_list = [str(row[0]) for row in cur.fetchall()]
        cur.close()
        self.combo_nim = ttk.Combobox(self.input_frame, values=nim_list, font=("Helvetica", 10))
        self.combo_nim.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.combo_nim.bind("<<ComboboxSelected>>", self.load_data)
        self.label_semester = tk.Label(self.input_frame, text="Semester: ", font=("Helvetica", 10), background="white")
        self.label_semester.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_semester = ttk.Combobox(self.input_frame, values=["1", "2", "3", "4", "5", "6", "7", "8"], font=("Helvetica", 10))
        self.combo_semester.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.button_frame = tk.Frame(self.input_button_frame, background="white")
        self.button_frame.grid(row=0, column=2, padx=5, pady=5)
        self.button_delete_ipk = tk.Button(self.button_frame, text="Delete IPK", command=self.delete_ipk, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove")
        self.button_delete_ipk.pack(fill=tk.X, padx=5, pady=5)
        self.table_frame = tk.Frame(self.frame_all)
        self.table_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        self.treeview = ttk.Treeview(self.table_frame, columns=["Semester", "IPK"], show="headings")
        self.treeview.heading("Semester", text="Semester")
        self.treeview.heading("IPK", text="IPK")
        self.treeview.pack(fill=tk.BOTH, expand=True)
        self.load_data()

    def delete_ipk(self):
        nim = self.combo_nim.get()
        semester = self.combo_semester.get()
        if not semester:
            messagebox.showwarning("Delete IPK", "Harap pilih semester sebelum menekan tombol Delete IPK!")
            return
        cursor = self.db.cursor()
        query = f"UPDATE mahasiswa SET semester{semester} = NULL WHERE nim = {nim}"
        cursor.execute(query)
        self.db.commit()
        query = f"DELETE FROM nilai WHERE semester = {semester} AND nim = {nim}"
        cursor.execute(query)
        self.db.commit()
        cursor.close()
        messagebox.showinfo("Delete IPK", f"Data IPK pada Semester {semester} berhasil dihapus!")
        self.combo_semester.set("")
        self.load_data()

    def load_data(self, event=None):
        self.treeview.delete(*self.treeview.get_children())  # Menghapus semua item pada Treeview
        nim = self.combo_nim.get()
        cursor = self.db.cursor()
        query = "SELECT semester1, semester2, semester3, semester4, semester5, semester6, semester7, semester8 FROM mahasiswa WHERE nim = %s"
        cursor.execute(query, (nim,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            sem1, sem2, sem3, sem4, sem5, sem6, sem7, sem8 = row
            ipk_list = [sem1, sem2, sem3, sem4, sem5, sem6, sem7, sem8]
            for i in range(len(ipk_list)):
                if ipk_list[i] is None:
                    ipk_list[i] = "Nilai Tidak Ditemukan"
            for semester, ipk in enumerate(ipk_list, start=1):
                self.treeview.insert("", "end", values=(semester, ipk))

class NilaiMahasiswa(DeleteIPKFormAdmin):
    def __init__(self, root, nim, db):
        super().__init__(root, nim, db)
        self.root.title("Statistik IPK Seluruh Mahasiswa")
        self.frame_all.destroy()
        self.frame_all = tk.Frame(self.root, background="white")
        self.frame_all.grid(row=0, column=0)
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.grid(row=0, column=0, columnspan=2, sticky=tk.EW)
        self.label_judul = tk.Label(self.frame_title, text="STATISTIK NILAI SELURUH MAHASISWA", font=("Helvetica", 16, "bold"), foreground="white", background="#1AA7EC")
        self.label_judul.pack(pady=10)
        self.input_button_frame = tk.Frame(self.frame_all, background="white")
        self.input_button_frame.grid(row=1, column=0, padx=20, pady=10, sticky=tk.W)
        self.input_frame = tk.LabelFrame(self.input_button_frame, text=" Input Data NIM Mahasiswa ", background="white")
        self.input_frame.grid(row=0, column=0, columnspan=1, padx=5, pady=5, sticky=tk.W)
        self.label_nim = tk.Label(self.input_frame, text="NIM: ", font=("Helvetica", 10), background="white")
        self.label_nim.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        cur = db.cursor()
        cur.execute("SELECT nim FROM mahasiswa")
        nim_list = [str(row[0]) for row in cur.fetchall()]
        cur.close()
        self.combo_nim = ttk.Combobox(self.input_frame, values=nim_list, font=("Helvetica", 10))
        self.combo_nim.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.combo_nim.bind("<<ComboboxSelected>>", self.loaddata)
        self.table_frame1 = tk.Frame(self.frame_all)
        self.table_frame1.grid(row=2, column=0, padx=10, pady=10, sticky=tk.NSEW)
        self.treeview1 = ttk.Treeview(self.table_frame1, columns=("Semester", "IPK"), show="headings")
        self.treeview1.heading("Semester", text="Semester")
        self.treeview1.heading("IPK", text="IPK")
        self.treeview1.pack(fill=tk.BOTH, expand=True)
        self.table_frame2 = tk.Frame(self.frame_all)
        self.table_frame2.grid(row=2, column=1, padx=10, pady=10, sticky=tk.NSEW)
        self.treeview2 = ttk.Treeview(self.table_frame2, columns=("Semester", "Avg", "Max", "Min"), show="headings")
        self.treeview2.heading("Semester", text="Semester")
        self.treeview2.heading("Avg", text="Avg")
        self.treeview2.heading("Max", text="Max")
        self.treeview2.heading("Min", text="Min")
        self.treeview2.pack(fill=tk.BOTH, expand=True)
        self.display_summary()

    def display_summary(self):
        cursor = self.db.cursor()
        avg_ipk_list = []
        max_ipk_list = []
        min_ipk_list = []
        for i in range(1, 9):
            query = f"SELECT AVG(semester{i}) FROM mahasiswa"
            cursor.execute(query)
            avg_ipk = cursor.fetchone()[0]
            avg_ipk = "{:.2f}".format(avg_ipk) if avg_ipk is not None else None
            avg_ipk_list.append(avg_ipk)
            query = f"SELECT MAX(semester{i}) FROM mahasiswa"
            cursor.execute(query)
            max_ipk = cursor.fetchone()[0]
            max_ipk = "{:.2f}".format(max_ipk) if max_ipk is not None else None
            max_ipk_list.append(max_ipk)
            query = f"SELECT MIN(semester{i}) FROM mahasiswa"
            cursor.execute(query)
            min_ipk = cursor.fetchone()[0]
            min_ipk = "{:.2f}".format(min_ipk) if min_ipk is not None else None
            min_ipk_list.append(min_ipk)
        cursor.close()
        for semester, avg, maxi, mini in zip(range(1, 9), avg_ipk_list, max_ipk_list, min_ipk_list):
            if all(ipk is None for ipk in [avg, maxi, mini]):
                self.treeview2.insert("", tk.END, values=(semester, "Nilai Tidak Ditemukan", "Nilai Tidak Ditemukan", "Nilai Tidak Ditemukan"))
            else:
                self.treeview2.insert("", tk.END, values=(semester, avg, maxi, mini))

    def loaddata(self, event=None):
        self.treeview1.delete(*self.treeview1.get_children())  # Menghapus semua item pada Treeview
        nim = self.combo_nim.get()
        cursor = self.db.cursor()
        query = "SELECT semester1, semester2, semester3, semester4, semester5, semester6, semester7, semester8 FROM mahasiswa WHERE nim = %s"
        cursor.execute(query, (nim,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            sem1, sem2, sem3, sem4, sem5, sem6, sem7, sem8 = row
            ipk_list = [sem1, sem2, sem3, sem4, sem5, sem6, sem7, sem8]
            for i in range(len(ipk_list)):
                if ipk_list[i] is None:
                    ipk_list[i] = "Nilai Tidak Ditemukan"
            for semester, ipk in enumerate(ipk_list, start=1):
                self.treeview1.insert("", "end", values=(semester, ipk))

class GrafikIPKFormAdmin:
    def __init__(self, root, nim, db):
        self.root = root
        self.root.title("Grafik IPK")
        self.root.geometry("800x600")
        self.root.configure(bg="white")
        self.root.resizable(False, False)
        self.canvas = None
        self.nim = nim
        self.db = db
        self.previous_nim = None
        self.frame_all = tk.Frame(self.root, background="white")
        self.frame_all.pack()
        self.input_frame = tk.LabelFrame(self.frame_all, text=" Input Data ", background="white")
        self.input_frame.pack(padx=20, pady=10)
        self.label_nim = tk.Label(self.input_frame, text="NIM: ", background="white")
        self.label_nim.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        cur = db.cursor()
        cur.execute("SELECT nim FROM mahasiswa")
        nim_list = [str(row[0]) for row in cur.fetchall()]
        cur.close()
        self.combo_nim = ttk.Combobox(self.input_frame, values=nim_list, font=("Helvetica", 10))
        self.combo_nim.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.combo_nim.bind("<<ComboboxSelected>>", self.show_graph)
        self.fig = None
        self.ax = None

    def show_graph(self, event=None):
        nim = self.combo_nim.get()
        cursor = self.db.cursor()
        query = f"SELECT semester1, semester2, semester3, semester4, semester5, semester6, semester7, semester8, nama FROM mahasiswa WHERE nim = '{nim}'"
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()
        if nim != self.previous_nim:
            if self.canvas:
                self.canvas.get_tk_widget().destroy() 
            if self.ax:
                self.ax.clear()
            self.fig = plt.figure(figsize=(6, 4), dpi=80) 
            self.ax = self.fig.add_subplot(111)
            self.ax.set_xlabel("Semester", fontsize=10)
            self.ax.set_ylabel("Nilai", fontsize=10)
            self.ax.set_xticks(list(range(1, 9)))
            self.ax.set_xticklabels(["Sem. 1", "Sem. 2", "Sem. 3", "Sem. 4", "Sem. 5", "Sem. 6", "Sem. 7", "Sem. 8"], fontsize=10)
            self.ax.tick_params(axis="y", labelsize=10)
            self.ax.set_ylim(0, 4.5)
            self.previous_nim = nim
        if row:
            nilai = list(row[:-1])
            nama_mahasiswa = row[-1]
            if all(value is None or value == 0 for value in nilai):
                messagebox.showwarning("Data Mahasiswa", "Data nilai mahasiswa kosong!")
                return
            val = list(range(1, 9))
            data = [0 if value is None else value for value in nilai]
            self.ax.bar(val, data, color="lightblue")
            self.ax.set_title(f"IPK Mahasiswa {nama_mahasiswa} - {nim}", fontsize=12)
            self.ax.set_xlabel("Semester", fontsize=10)
            self.ax.set_ylabel("Nilai", fontsize=10)
            self.ax.set_xticks(val)
            self.ax.set_xticklabels(["Sem. 1", "Sem. 2", "Sem. 3", "Sem. 4", "Sem. 5", "Sem. 6", "Sem. 7", "Sem. 8"], fontsize=10)
            self.ax.tick_params(axis="y", labelsize=10)
            self.ax.set_ylim(0, 4.5)
            self.ax.grid(True)
            plt.tight_layout()
            if self.canvas:
                self.canvas.get_tk_widget().destroy()
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        else:
            messagebox.showwarning("Data Mahasiswa", "Data mahasiswa tidak ditemukan!")

class GrafikRataIPKPerSemester:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Grafik Rata-rata IPK per Semester")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.db = db
        self.fig, self.ax = plt.subplots(figsize=(8,6), dpi=80)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.plot_graph()

    def plot_graph(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT AVG(semester1), AVG(semester2), AVG(semester3), AVG(semester4), AVG(semester5), AVG(semester6), AVG(semester7), AVG(semester8) FROM mahasiswa")
        avg_ipk = cursor.fetchone()
        cursor.execute("SELECT MAX(semester1), MAX(semester2), MAX(semester3), MAX(semester4), MAX(semester5), MAX(semester6), MAX(semester7), MAX(semester8) FROM mahasiswa")
        max_ipk = cursor.fetchone()
        cursor.execute("SELECT MIN(semester1), MIN(semester2), MIN(semester3), MIN(semester4), MIN(semester5), MIN(semester6), MIN(semester7), MIN(semester8) FROM mahasiswa")
        min_ipk = cursor.fetchone()
        cursor.close()
        semesters = ['Sem. 1', 'Sem. 2', 'Sem. 3', 'Sem. 4', 'Sem. 5', 'Sem. 6', 'Sem. 7', 'Sem. 8']
        avg_values = list(avg_ipk)
        max_values = list(max_ipk)
        min_values = list(min_ipk)
        self.ax.clear()
        bar_width = 0.25
        index = np.arange(len(semesters))
        if any(value is not None for value in avg_values):
            self.ax.bar(index, avg_values, bar_width, color="lightblue", label="Avg")
        else:
            self.ax.bar(index, [0] * len(semesters), bar_width, color="lightblue", label="Avg")
        if any(value is not None for value in max_values):
            self.ax.bar(index + bar_width, max_values, bar_width, color="lightgreen", label="Max")
        if any(value is not None for value in min_values):
            self.ax.bar(index + (2 * bar_width), min_values, bar_width, color="pink", label="Min")
        self.ax.set_xlabel("Semester", fontsize=10)
        self.ax.set_ylabel("IPK", fontsize=10)
        self.ax.set_title("Grafik Rata-rata, Maksimum, dan Minimum IPK per Semester", fontsize=12)
        self.ax.set_xticks(index + bar_width)
        self.ax.set_xticklabels(semesters)
        self.ax.tick_params(axis="y", labelsize=10)
        self.ax.set_xlim(index[0] - 3 * bar_width, index[-1] + 5 * bar_width)
        self.ax.set_ylim(0, 4.5)
        self.ax.grid(alpha=0.5)
        self.ax.legend(loc='upper right')
        plt.tight_layout()
        self.canvas.draw()

class InputMataKuliahForm:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Input Mata Kuliah")
        self.db = db
        self.frame_all = tk.Frame(self.root, background="white")
        self.frame_all.pack()
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_judul = tk.Label(self.frame_title, text="INPUT MATA KULIAH", font=("Helvetica", 17, "bold"), foreground="white", background="#1AA7EC")
        self.label_judul.pack(pady=10)
        self.input_button_frame = tk.Frame(self.frame_all, background="white")
        self.input_button_frame.pack(padx=20, pady=(25,10))
        self.input_frame = tk.LabelFrame(self.input_button_frame, text=" Input Data Mata Kuliah ", background="white")
        self.input_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.label_mata_kuliah = tk.Label(self.input_frame, text="Mata Kuliah:", font=("Helvetica", 10), background="white")
        self.label_mata_kuliah.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_mata_kuliah = tk.Entry(self.input_frame, width=30, font=("Helvetica", 10), background="white")
        self.entry_mata_kuliah.grid(row=0, column=1, padx=5, pady=5)
        self.label_semester = tk.Label(self.input_frame, text="Semester:", font=("Helvetica", 10), background="white")
        self.label_semester.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_semester = ttk.Combobox(self.input_frame, values=["1", "2", "3", "4", "5", "6", "7", "8"], font=("Helvetica", 10))
        self.combo_semester.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.label_sks = tk.Label(self.input_frame, text="SKS:", font=("Helvetica", 10), background="white")
        self.label_sks.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_sks = ttk.Combobox(self.input_frame, values=["1", "2", "3", "4"], font=("Helvetica", 10))
        self.combo_sks.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.button_input_matkul = tk.Button(self.input_frame, text="Execute", command=self.input_matkul, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove")
        self.button_input_matkul.grid(row=0, column=2, rowspan=3, padx=5, pady=5)
        self.table_frame = tk.LabelFrame(self.frame_all, text=" Tabel ", background="white")
        self.table_frame.pack(padx=10, pady=10)
        self.treeview = ttk.Treeview(self.table_frame, columns=("Mata Kuliah", "SKS"), show="headings")
        self.treeview.column("Mata Kuliah", width=200)
        self.treeview.column("SKS", width=50)
        self.treeview.heading("Mata Kuliah", text="Mata Kuliah")
        self.treeview.heading("SKS", text="SKS")
        self.treeview.pack(padx=10, pady=10)
        self.combo_semester.bind("<<ComboboxSelected>>", self.load_table_data)

    def input_matkul(self):
        mata_kuliah = self.entry_mata_kuliah.get()
        semester = self.combo_semester.get()
        sks = self.combo_sks.get()
        if not mata_kuliah or not semester or not sks:
            messagebox.showerror("Error", "Harap lengkapi semua field")
            return
        try:
            semester = int(semester)
            sks = int(sks)
        except ValueError:
            messagebox.showerror("Error", "Semester dan SKS harus berupa angka")
            return
        cursor = self.db.cursor()
        query = f"SELECT mata_kuliah FROM semester{semester} WHERE mata_kuliah = %s"
        cursor.execute(query, (mata_kuliah,))
        result = cursor.fetchall()
        if result:
            messagebox.showerror("Error", "Mata kuliah sudah terdaftar pada semester tersebut")
        else:
            query = f"INSERT INTO semester{semester} (mata_kuliah, sks) VALUES (%s, %s)"
            cursor.execute(query, (mata_kuliah, sks))
            self.db.commit()
            messagebox.showinfo("Success", f"Mata Kuliah {mata_kuliah} dengan SKS {sks} berhasil diinput pada semester {semester}!")
            self.entry_mata_kuliah.delete(0, tk.END)
        cursor.close()
        self.load_table_data()

    def load_table_data(self, event=None):
        semester = self.combo_semester.get()
        self.treeview.delete(*self.treeview.get_children())
        if semester:
            cursor = self.db.cursor()
            query = f"SELECT mata_kuliah, sks FROM semester{semester}"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            for row in result:
                self.treeview.insert("", "end", values=row)

class EditMataKuliahForm(InputMataKuliahForm):
    def __init__(self, root, db):
        super().__init__(root, db)
        self.root.title("Edit Mata Kuliah")
        self.label_judul.configure(text="EDIT MATA KULIAH", font=("Helvetica", 17, "bold"), foreground="white", background="#1AA7EC")
        self.treeview.bind("<ButtonRelease-1>", self.select_matkul)
        self.button_input_matkul.configure(text="Edit Nilai", command=self.edit_matkul)

    def select_matkul(self, event):
        selected_item = self.treeview.focus()
        values = self.treeview.item(selected_item, "values")
        if values:
            mata_kuliah = values[0]
            sks = values[1]
            self.entry_mata_kuliah.delete(0, tk.END)
            self.entry_mata_kuliah.insert(0, mata_kuliah)
            self.combo_sks.set(sks)

    def edit_matkul(self):
        mata_kuliah = self.entry_mata_kuliah.get()
        semester = self.combo_semester.get()
        sks = self.combo_sks.get()
        if not mata_kuliah or not semester or not sks:
            messagebox.showerror("Error", "Harap lengkapi semua field")
            return
        try:
            semester = int(semester)
            sks = int(sks)
        except ValueError:
            messagebox.showerror("Error", "Semester dan SKS harus berupa angka")
            return
        cursor = self.db.cursor()
        selected_item = self.treeview.focus()
        values = self.treeview.item(selected_item, "values")
        if values:
            old_mata_kuliah = values[0]
            query = f"UPDATE semester{semester} SET mata_kuliah = %s, sks = %s WHERE mata_kuliah = %s"
            cursor.execute(query, (mata_kuliah, sks, old_mata_kuliah))
            self.db.commit()
            messagebox.showinfo("Success", f"Mata Kuliah {old_mata_kuliah} berhasil diupdate menjadi {mata_kuliah} dengan SKS {sks} pada semester {semester}!")
        else:
            messagebox.showerror("Error", "Pilih mata kuliah yang ingin diedit dari tabel!")
        cursor.close()
        self.load_table_data()

class DeleteMataKuliahForm(EditMataKuliahForm):
    def __init__(self, root, db):
        super().__init__(root, db)
        self.root.title("Delete Mata Kuliah")
        self.frame_all.destroy()
        self.frame_all = tk.Frame(self.root, background="white")
        self.frame_all.pack()
        self.frame_title = tk.Frame(self.frame_all, background="#1AA7EC")
        self.frame_title.pack(fill=tk.X)
        self.label_judul = tk.Label(self.frame_title, text="DELETE MATA KULIAH", font=("Helvetica", 17, "bold"), foreground="white", background="#1AA7EC")
        self.label_judul.pack(pady=10)
        self.input_button_frame = tk.Frame(self.frame_all, background="white")
        self.input_button_frame.pack(padx=20, pady=(25,10))
        self.input_frame = tk.LabelFrame(self.input_button_frame, text=" Input Data Semester ", background="white")
        self.input_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.label_semester = tk.Label(self.input_frame, text="Semester:", font=("Helvetica", 10), background="white")
        self.label_semester.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_semester = ttk.Combobox(self.input_frame, values=["1", "2", "3", "4", "5", "6", "7", "8"], font=("Helvetica", 10))
        self.combo_semester.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.button_delete_matkul = tk.Button(self.input_frame, text="Delete Matkul", command=self.delete_matkul, font=("Helvetica", 11, "bold"), foreground="white", background="#1AA7EC", activebackground='#0052cc', activeforeground='#aaffaa', relief="groove")
        self.button_delete_matkul.grid(row=0, column=2, padx=5, pady=5)
        self.table_frame = tk.LabelFrame(self.frame_all, text=" Tabel ", background="white")
        self.table_frame.pack(padx=20, pady=10)
        self.treeview = ttk.Treeview(self.table_frame, columns=("Mata Kuliah", "SKS"), show="headings")
        self.treeview.column("Mata Kuliah", width=200)
        self.treeview.column("SKS", width=50)
        self.treeview.heading("Mata Kuliah", text="Mata Kuliah")
        self.treeview.heading("SKS", text="SKS")
        self.treeview.pack(padx=10, pady=10)
        self.combo_semester.bind("<<ComboboxSelected>>", self.load_table_data)

    def delete_matkul(self):
        selected_item = self.treeview.focus()
        values = self.treeview.item(selected_item, "values")
        if values:
            mata_kuliah = values[0]
            semester = self.combo_semester.get()
            if not semester:
                messagebox.showerror("Error", "Pilih semester terlebih dahulu")
                return
            cursor = self.db.cursor()
            query = f"DELETE FROM semester{semester} WHERE mata_kuliah = %s"
            cursor.execute(query, (mata_kuliah,))
            self.db.commit()
            messagebox.showinfo("Success", f"Mata Kuliah {mata_kuliah} pada semester {semester} berhasil dihapus!")
            cursor.close()
            self.load_table_data()
        else:
            messagebox.showerror("Error", "Pilih mata kuliah yang ingin dihapus dari tabel!")

start_form = PilihMode(root=tk.Tk())
start_form.root.mainloop()