import PySimpleGUI as sg

sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF0e")

layout = [
    [sg.Text("TEKNOLOGI INFORMASI", size=(25, 1), justification="center")],
    [sg.Text("TEKNOLOGI INFORMASI", size=(25, 1), justification="left")],
    [sg.Text("TEKNOLOGI INFORMASI", size=(25, 1), justification="right")],
    [sg.Text(("TEKNOLOGI INFORMASI " + " ") * 2, size=(25, 2), justification="center")],
    [sg.Text("UNISKA MAB BANJARMASIN", text_color="#FFCC00")]
]

window = sg.Window("Profile", layout, size=(400, 250), font=("Times", 18))

window.read()

window.close()