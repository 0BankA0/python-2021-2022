
from PyQt5 import QtWidgets
from binder_form import Ui_MainWindow
import sys
import keyboard
import threading
import os
import re
import time

program_status = False

def file_clear():
    if os.path.exists('hotkey.dt'):
        os.remove('hotkey.dt')
    open('hotkey.dt', 'w')

def file_save(bind_dict):
    file_clear()
    text_to_save = ''
    for key, value in bind_dict.items():
        text_to_save += f'{key}:{value}\n'
    with open('hotkey.dt', 'w') as ouf:
        ouf.write(text_to_save[:-1])

def file_read():
    bind_dict = {}
    if os.path.exists('hotkey.dt'):
        with open('hotkey.dt') as inf:
            for line in inf:
                if re.match(r'([^:]+):([^:]+)', line):
                    bind_dict[line[:line.find(':')]] = line[line.find(':')+1:].strip()
                else:
                    file_clear()
    else:
        file_clear()
    return bind_dict

def file_get_hotkey_list():
    hotkey_list = []
    with open('hotkey.dt') as inf:
        for line in inf:
            hotkey_list.append(line[:line.find(':')])
    return hotkey_list

def bind_thread(bind_dict):
    global program_status
    hotkey_list = [keyboard.add_hotkey(key, keyboard.write, args=(value,)) for key, value in bind_dict.items()]
    while program_status:
        pass
    for hotkey in hotkey_list:
        keyboard.remove_hotkey(hotkey)

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.can_return = False
        self.button_list = [self.ui.key1, self.ui.key2, self.ui.key3, self.ui.key4, self.ui.key5, self.ui.key6, self.ui.key7, self.ui.key8]
        self.lineEdit_list = [self.ui.bind1, self.ui.bind2, self.ui.bind3, self.ui.bind4, self.ui.bind5, self.ui.bind6, self.ui.bind7, self.ui.bind8]
        self.draw_values()
        for button in self.button_list:
            button.clicked.connect(self.on_key_click)
        self.ui.clearButton.clicked.connect(self.clear_elements)
        self.ui.saveButton.clicked.connect(self.save_elements)
        self.ui.startButton.clicked.connect(self.start_program)

    #Functions for hotkey read PushButtons

    def button_hotkey_read(self, button):
        hotkey = keyboard.read_hotkey(suppress=False)
        if not hotkey in file_get_hotkey_list():
            if self.button_is_selected(button):
                button.setText(hotkey)
        self.button_remove_selected(button)


    def on_key_click(self):
        button = self.sender()
        if self.button_is_selected(button):
            self.button_remove_selected(button)
            button.setText('')
        else:
            threading.Thread(target=self.button_hotkey_read, args=(button,)).start()
            self.button_make_selected(button)

    def button_is_selected(self, button):
        return button.styleSheet()

    def button_make_selected(self, button):
        if self.button_is_any_selected():
            self.button_remove_all_selected()
        button.setStyleSheet('background-color: #C3C3C3;')

    def button_remove_selected(self, button):
        button.setStyleSheet('')

    def button_remove_all_selected(self):
        for button in self.button_list:
            self.button_remove_selected(button)

    def button_is_any_selected(self):
        for button in self.button_list:
            if self.button_is_selected(button):
                return button
        return False

    #Functions for save/clear/start PushButtons

    def clear_elements(self):
        threading.Thread(target=self.animate_button, args=(self.sender(),)).start()
        self.can_return = not self.can_return
        if self.can_return:
            self.ui.clearButton.setText('Вернуть')
            for element in self.button_list + self.lineEdit_list:
                element.setText('')
        else:
            self.ui.clearButton.setText('Очистить')
            self.draw_values()

    def save_elements(self):
        self.return_off()
        threading.Thread(target=self.animate_button, args=(self.sender(),)).start()
        bind_dict = {self.button_list[i].text():self.lineEdit_list[i].text() for i in range(len(self.button_list)) if self.lineEdit_list[i].text() and self.button_list[i].text()}
        file_save(bind_dict)

    def start_program(self):
        self.return_off()
        threading.Thread(target=self.animate_button, args=(self.sender(),)).start()
        global program_status
        program_status = not program_status
        if program_status:
            self.ui.startButton.setText('Остановить')
            self.save_elements()
            threading.Thread(target=bind_thread, args=(file_read(),)).start()
        else:
            self.ui.startButton.setText('Запустить')

    #Other Functions

    def draw_values(self):
        k = 0
        for key, value in file_read().items():
            self.button_list[k].setText(key)
            self.lineEdit_list[k].setText(value)
            k += 1

    def animate_button(self, button):
        button.setStyleSheet('background-color: #D3D3D3;')
        time.sleep(0.5)
        button.setStyleSheet('')

    def return_off(self):
        self.ui.clearButton.setText('Очистить')
        self.can_return = False

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())











#4
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete