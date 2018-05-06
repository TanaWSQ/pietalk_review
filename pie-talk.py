from tkinter import *

from Classes import Chat

chat = Chat.Chat()
print(chat.config.getKey('testkey'))


def window_print_line(txt):
    TXTConsole.config(state=NORMAL)
    TXTConsole.insert(END, (cas.strftime('[%Y-%m-%d %H:%M:%S]')) + ' ' + txt + "\n")
    TXTConsole.config(state=DISABLED)


## Cas
import datetime
cas = datetime.datetime.now()
print(cas.strftime('%Y-%m-%d %H:%M:%S'))

def process_command_logic(cmd):
    if cmd == 'bye':
        on_window_close()



# ##ESCAPE
def koniec(event):
    on_window_close()

# TkInter callback functions
#
def process_command_entry():
    cmd = TXTCommand.get()
    window_print_line(cmd)
    TXTCommand.delete(0, END)
    process_command_logic(cmd)


# handle push of Send button
def send_button_callback():
    process_command_entry()


# handle enter in command bar
def on_key_press(event):
    process_command_entry()


def on_window_close():
    ptWindow.destroy()


def on_user_select(event):
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    stat = 'You have selected item %d: "%s"' % (index, value)
    window_print_line(stat)


#
# TkInter initialization
#
#
ptWindow = Tk()
ptWindow.winfo_toplevel().title('PieTalk 3000!')
ptWindow.resizable(1, 1)
ptWindow.protocol('WM_DELETE_WINDOW', on_window_close)

#
# main chat text window
#
TXTConsole = Text(ptWindow, height=25, width=80)
TXTConsole.grid(row=0, column=0)
TXTConsole.insert(END, 'PieTalk 3000 started\n')
TXTConsole.insert(END, 'please, enter message or command to lime text area and press enter/send button\n')
TXTConsole.bind('<Escape>', koniec)
TXTConsole.config(state=DISABLED)

#
# side panel - channel / user view
#
LBUsers = Listbox(ptWindow, height=20, width=20)
LBUsers.grid(row=0, column=1)
LBUsers.bind('<<ListboxSelect>>', on_user_select)

for x in chat.get_rooms(1, 0):
    LBUsers.insert(END, x)

#
# text input - command
#
TXTCommand = Entry(ptWindow, bd=2, width=80)
TXTCommand.bind('<Return>', on_key_press)
TXTCommand.grid(row=1, column=0)
TXTCommand.config({'background': 'Lime'})
TXTCommand.focus()

#
# send button
#
BTN = Button(ptWindow, text='Send', command=send_button_callback, width=20)
BTN.grid(row=1, column=1)

#
# TkInter main event loop
#
try:
    while True:
        ptWindow.update_idletasks()
        ptWindow.update()

except:
    print('PieTalk finished!')
