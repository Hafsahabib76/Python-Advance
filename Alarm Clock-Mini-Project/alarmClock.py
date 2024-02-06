# Import Packages
import pyttsx3
import datetime
import threading
import os
import time
from tkinter import Tk, Label, Button, OptionMenu, StringVar
from tkcalendar import DateEntry

root = Tk()
root.title("Voice Alarm Clock")
root.geometry("350x500")
root.configure(bg='#000028')

# Date Time Setting Heading
heading1 = Label(root, text="Date & Time Settings", font=("Helvetica", 14), fg="white", bg="#000028")
heading1.grid(row=0, column=0, padx=50, pady=20, sticky='n')

# Date Entry
date_label = Label(root, text="Select Alarm Date:", font=("Helvetica", 11), fg="white", bg="#000028")
date_label.grid(row=1, column=0, padx=25, pady=5, sticky='w')

date_entry = DateEntry(root, width=25, background='#000028', foreground='white', borderwidth=2)
date_entry.grid(row=2, column=0, padx=28, pady=5, sticky='w')

# Time Entry
time_label = Label(root, text="Enter Alarm Time:", font=("Helvetica", 11), fg="white", bg="#000028")
time_label.grid(row=3, column=0, padx=25, pady=5, sticky='w')

# Hour Selection
hour_var = StringVar(root)
hour_var.set("1")
hour_label = Label(root, text="Hour:", font=("Helvetica", 11), fg="white", bg="#000028")
hour_label.grid(row=4, column=0, padx=25, pady=5, sticky='w')
# Hours range should be from 1 to 12
hour_menu = OptionMenu(root, hour_var, *list(range(1, 13)))
hour_menu.grid(row=5, column=0, padx=25, pady=5, sticky='w')

# Minute Selection
minute_var = StringVar(root)
minute_var.set("0")
minute_label = Label(root, text="Minute:", font=("Helvetica", 11), fg="white", bg="#000028")
minute_label.grid(row=4, column=0, padx=90, pady=5, sticky='w')
# Minutes range should be from 0 to 60
minute_menu = OptionMenu(root, minute_var, *list(range(0, 60)))
minute_menu.grid(row=5, column=0, padx=90, pady=5, sticky='w')

# AM/PM Selection
amp_var = StringVar(root)
amp_var.set("AM")
amp_label = Label(root, text="AM/PM:", font=("Helvetica", 11), fg="white", bg="#000028")
amp_label.grid(row=4, column=0, padx=150, pady=5, sticky='w')
amp_menu = OptionMenu(root, amp_var, "AM", "PM")
amp_menu.grid(row=5, column=0, padx=150, pady=5, sticky='w')

# Alarm Tone Setting Heading
heading2 = Label(root, text="Alarm Ringtone Settings", font=("Helvetica", 14), fg="white", bg="#000028")
heading2.grid(row=6, column=0, padx=50, pady=20, sticky='n')

# Custom Tone Entry
custom_tone_label = Label(root, text="Select Custom Alarm Tone:", font=("Helvetica", 11), fg="white", bg="#000028")
custom_tone_label.grid(row=7, column=0, padx=25, pady=5, sticky='w')

custom_tone_var = StringVar(root)
custom_tone_var.set("default_alarm_tone.mp3")
custom_tone_menu = OptionMenu(root, custom_tone_var, "default-alarm-tone.mp3", "custom-alarm-tone.mp3", "custom-alarm-assitant-voice.mp3")
custom_tone_menu.grid(row=8, column=0, padx=25, pady=5, sticky='w')


# Function to set the alarm when user press the set alarm button on the screen
def set_alarm():
    # Get the date that user input
    selected_date = date_entry.get_date()
    # Get the hour
    selected_hour = int(hour_var.get())
    # Get the minute
    selected_minute = int(minute_var.get())
    # Get the AM/PM
    selected_amp = amp_var.get()
    # Get the alarm tone
    selected_custom_tone = custom_tone_var.get()

    if selected_amp == "PM" and selected_hour != 12:
        selected_hour += 12

    if selected_hour == 12 and selected_amp == "AM":
        selected_hour = 00

    # Combine all the data into single alarm date time
    alarm_datetime = datetime.datetime(selected_date.year, selected_date.month, selected_date.day, selected_hour, selected_minute)

    # Get the current time
    current_time = datetime.datetime.now()
    # Check the time difference
    time_difference = alarm_datetime - current_time

    # Condition: if the time difference is less than 0.
    # Inform user to select the future date
    if time_difference.total_seconds() <= 0:
        speak("Please set a future date and time for the alarm.")
        return

    # Convert the alarm time to string format
    alarm_datetime_str = alarm_datetime.strftime("%Y-%m-%d %I:%M %p")
    # Inform the user that is Alarm is set for the particular date time
    speak("Alarm set for " + alarm_datetime_str)

    # Thread which call the wait_and_ring function to start the alarm for the particular time
    alarm_thread = threading.Thread(target=wait_and_ring, args=(time_difference.total_seconds(), selected_custom_tone))
    alarm_thread.start()


# Function to wait for the set time and then ring the tone for the alarm
def wait_and_ring(seconds, custom_tone):
    time.sleep(seconds)
    os.system(f"start {custom_tone}")


# Function to perform the speak operation as an assistant voice
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# Set Alarm Button that calls the set_alarm function
set_alarm_button = Button(root, text="Set Alarm", command=set_alarm, font=("Helvetica", 11), fg="#000028", bg="#00CCCC", width=14)
set_alarm_button.grid(row=9, column=0, padx=15, pady=20, sticky='n')

# Footer Label
footer_label = Label(root, text="Hafsa-Habib © 2024 Voice Alarm Clock. All rights reserved.", font=("Helvetica", 8), fg="white", bg="#000028")
footer_label.grid(row=11, column=0, padx=5, pady=5, sticky='s')

# To disable the full-screen option
root.overrideredirect(True)

root.mainloop()
