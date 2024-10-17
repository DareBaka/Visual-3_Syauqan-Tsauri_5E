import PySimpleGUI as sg

sg.theme("DarkGreen5")
sg.theme_text_color("#FFFF00") 

# Create a window
window = sg.Window(
    title="Contoh Button",
    layout=[
        [sg.Text("Contoh Button")],
        [sg.Button("Button Simpan")],
        [sg.Button("Button Keluar")]
    ],
    size=(400, 200),
    font=("Times", 18) 
)

kejadian, nilai = window.read()

print(kejadian, "=>", nilai)

window.close()