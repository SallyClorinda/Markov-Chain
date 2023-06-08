import PySimpleGUI as sg

# Membuat tampilan GUI menggunakan PySimpleGUI
layout = [
    [sg.Text('Kalkulator Markov Chain')],
    [sg.Text('Jumlah Kemunculan Pola "C" ke "C" Berikutnya:'), sg.Input(key='-CC-')],
    [sg.Text('Jumlah Kemunculan Pola "C" ke "M" Berikutnya:'), sg.Input(key='-CM-')],
    [sg.Text('Jumlah Kemunculan Pola "C" ke "H" Berikutnya:'), sg.Input(key='-CH-')],
    [sg.Text('Jumlah Kemunculan Pola "M" ke "C" Berikutnya:'), sg.Input(key='-MC-')],
    [sg.Text('Jumlah Kemunculan Pola "M" ke "M" Berikutnya:'), sg.Input(key='-MM-')],
    [sg.Text('Jumlah Kemunculan Pola "M" ke "H" Berikutnya:'), sg.Input(key='-MH-')],
    [sg.Text('Jumlah Kemunculan Pola "H" ke "C" Berikutnya:'), sg.Input(key='-HC-')],
    [sg.Text('Jumlah Kemunculan Pola "H" ke "M" Berikutnya:'), sg.Input(key='-HM-')],
    [sg.Text('Jumlah Kemunculan Pola "H" ke "H" Berikutnya:'), sg.Input(key='-HH-')],
    [sg.Button('Hitung'), sg.Button('Reset')],
    [sg.Text('Hasil:'), sg.Output(size=(30, 10), key='-OUTPUT-')]
]

window = sg.Window('Kalkulator Markov Chain', layout)

# Fungsi untuk menghitung probabilitas transisi
def hitung_probabilitas(values):
    cc = int(values['-CC-'])
    cm = int(values['-CM-'])
    ch = int(values['-CH-'])
    mc = int(values['-MC-'])
    mm = int(values['-MM-'])
    mh = int(values['-MH-'])
    hc = int(values['-HC-'])
    hm = int(values['-HM-'])
    hh = int(values['-HH-'])

    total_c = cc + cm + ch
    total_m = mc + mm + mh
    total_h = hc + hm + hh

    # Menghitung probabilitas transisi
    probabilitas_cc = cc / total_c
    probabilitas_cm = cm / total_c
    probabilitas_ch = ch / total_c
    probabilitas_mc = mc / total_m
    probabilitas_mm = mm / total_m
    probabilitas_mh = mh / total_m
    probabilitas_hc = hc / total_h
    probabilitas_hm = hm / total_h
    probabilitas_hh = hh / total_h

    return (
        probabilitas_cc, probabilitas_cm, probabilitas_ch,
        probabilitas_mc, probabilitas_mm, probabilitas_mh,
        probabilitas_hc, probabilitas_hm, probabilitas_hh
    )

# Loop utama GUI
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Hitung':
        probabilitas = hitung_probabilitas(values)
        print('Probabilitas Transisi:')
        print('C -> C:', probabilitas[0])
        print('C -> M:', probabilitas[1])
        print('C -> H:', probabilitas[2])
        print('M -> C:', probabilitas[3])
        print('M -> M:', probabilitas[4])
        print('M -> H:', probabilitas[5])
        print('H -> C:', probabilitas[6])
        print('H -> M:', probabilitas[7])
        print('H -> H:', probabilitas[8])
    elif event == 'Reset':
        window['-CC-'].update('')
        window['-CM-'].update('')
        window['-CH-'].update('')
        window['-MC-'].update('')
        window['-MM-'].update('')
        window['-MH-'].update('')
        window['-HC-'].update('')
        window['-HM-'].update('')
        window['-HH-'].update('')
        window['-OUTPUT-'].update('')

window.close()
