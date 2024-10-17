import PySimpleGUI as sg

sg.theme("DarkGreen3")
sg.theme_text_color("#FFFF00")

window = sg.Window(
    title="Profile",
    layout=[
        [sg.Text("FTI UNISKA", font=("Helvetica", 24))],  # Perbaikan tanda kurung
        [sg.Text("FAKULTAS TEKNOLOGI INFORMASI")],
        [sg.Text("UNISKA MAB BANJARMASIN")]
    ],
    size=(430, 200),
    font=("Times", 18)
)

while True:
    event, values = window.read() 
    if event == sg.WIN_CLOSED: 
        break

window.close()
