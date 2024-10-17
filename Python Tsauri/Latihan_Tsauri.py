import PySimpleGUI as sg
sg.theme("DarkPurple5")
sg.theme_text_color("#00FF00")
window = sg.Window(title="Profile",
layout=[[sg.Text("SELAMAT DATANG DI KELAS",
font=("Times New Roman",25,"italic","bold","underline"))],
[sg.Text("NPM : 2210010192 ")],
[sg.Text("Nama : Syauqan Tsauri ")],
[sg.Text("Kelas : 5E Regular Banjarmasin ")],
[sg.Text("Mata Kuliah : Pemrograman Visual 3 ")]
],
size=(510,200),
font=("Times", 18))
window()
window.close()