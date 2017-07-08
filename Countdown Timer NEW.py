import tkinter as tk
import sys
import datetime
import winsound

#default config
user_count = 5
timer_name = 'Default Countdown'

#acquire current time and trim for display
time_now = str(datetime.datetime.now().time())
time_now = time_now[:-6]

#countdown function that changes label text as well
def countdown(count):
    # change text in label        
    label2['text'] = count
    #for normal countdown
    if count > 0:
        main_window.after(1000, countdown, count - 1)
    #handle ending
    elif count == 0:
        label2['text'] = 'TIME IS UP: Ended at ' + time_now
        winsound.Beep(3000, 1000)
    #error handling
    else:
        label2['text'] = 'Input Not Accepted'

#proceed button function
def proceed_func():
    global user_count 
    user_count = entry01.get()
    global timer_name
    timer_name = entry02.get()
    config_window.destroy()

#window_0 config
config_window = tk.Tk()
config_window.geometry('250x150')
frame01 = tk.Frame()
frame02 = tk.Frame()
label01 = tk.Label(config_window, text = '\nCountdown Configuration\n')

label02_hr = tk.Label(frame01, text = 'Hr:\t')
label02_min = tk.Label(frame01, text = 'Min:\t')
label02_sec = tk.Label(frame01, text = 'Sec:\t')

entry01 = tk.Entry(frame01, width = 15)
label03 = tk.Label(frame02, text = 'Project Name:\t')
entry02 = tk.Entry(frame02, width = 15)
label04 = tk.Label(config_window)
button01 = tk.Button(config_window, text = 'Proceed', command = proceed_func)

label01.pack()
frame01.pack()
label02_hr.pack(side = 'left')
label02_min.pack(side= 'left')
label02_sec.pack(side='left')
entry01.pack(side='left')
frame02.pack()
label03.pack(side='left')
entry02.pack(side='left')
label04.pack()
button01.pack()

config_window.mainloop()

#main_window config
main_window = tk.Tk()
main_window.geometry('500x400')
label1 = tk.Label(main_window, text = '\n' + timer_name + '\n', font = 'Helvetica 60')
label2 = tk.Label(main_window, text = 'SYSTEM HALTED', font = 'Helvetica 60 bold')
label1.pack()
label2.pack()

#Start countdown function with error detector
try:
    test = int(user_count)
except ValueError:
    print('The input must be an integer. If this is followed but the error still occurs, please contact Andy for technical repair')
    main_window.destroy()
    exitnotice = input('The program is now terminated')
    sys.exit()

countdown(int(user_count))

#beep sound at the end of countdown (freq, dur)

main_window.mainloop()