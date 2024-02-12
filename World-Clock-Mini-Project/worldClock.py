import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
import pytz

timezones = [
    'Asia/Karachi',
    'America/New_York',
    'Europe/London',
    'Asia/Tokyo',
    'Australia/Sydney',
    'Asia/Shanghai',
    'Asia/Dubai',
    'Europe/Berlin',
    'Pacific/Auckland',
    'Australia/Melbourne',
    'Asia/Jakarta',
    'Asia/Tehran',
    'Africa/Johannesburg',
    'America/Los_Angeles',
    'America/Vancouver',
    'America/Mexico_City'
]

root = tk.Tk()
# Set background color to black
root.configure(bg="black")
# Set the Window title
root.title('World Clock')

# set the deafult timezone i.e., Karachi
default_tz = pytz.timezone(timezones[0])
# To store the selected timezone
current_tz = None

# Load the image
img = Image.open("worldmap.jpg")
# Resize the image to fit the screen
img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))

# Convert Image object to PhotoImage
photo = ImageTk.PhotoImage(img)

# Create a label with the image and pack it to fill the window
label = tk.Label(root, image=photo)
label.image = photo
label.pack(fill=tk.BOTH, expand=tk.YES)


# Update Time function, to update it each second
def update_time():
    tz = current_tz if current_tz else default_tz
    current_time = datetime.now(tz)
    hour = current_time.strftime('%I')
    minute = current_time.strftime('%M')
    second = current_time.strftime('%S')
    am_pm = current_time.strftime('%p')

    timeBox.config(text=f"{hour}:{minute}:{second} {am_pm}")
    countryBox.config(text=tz)

    # Call update_time again after 1000ms (1 second)
    root.after(1000, update_time)


# On Click function - to update time the based on the clicked point
def on_click(event):
    global current_tz
    current_tz = pytz.timezone(event.widget.tz)
    update_time()


# Function to create clickable red square at different x, y positions
def create_square(x, y, tz):
    square_label = tk.Label(root, width=2, height=1, bg="red", fg="white")
    square_label.tz = tz  # Store timezone info in the label widget
    square_label.bind('<Button-1>', on_click)  # Binding left-click event
    square_label.place(x=x, y=y)


# Function to get the city name
def get_city_name(timezone):
    parts = timezone.split('/')
    if len(parts) > 1:
        return parts[1]
    return parts[0]


# create_city_label function displays city name at different x, y positions
def create_city_label(x, y, tz):
    city = get_city_name(tz)
    city_label = tk.Label(root, text=city, bg="#0A3651", fg="white", font=('arial', 8))
    city_label.place(x=x, y=y)


# city name labels
create_city_label(790, 380, timezones[0]) # Karachi
create_city_label(290, 360, timezones[1]) # New York
create_city_label(570, 260, timezones[2])  # London
create_city_label(1035, 380, timezones[3])  # Tokyo
create_city_label(1100, 550, timezones[4])  # Sydney
create_city_label(880, 330, timezones[5])  # Shanghai
create_city_label(760, 430, timezones[6])  # Dubai
create_city_label(630, 320, timezones[7])  # Berlin
create_city_label(1180, 580, timezones[8])  # Auckland
create_city_label(1050, 600, timezones[9])  # Melbourne
create_city_label(940, 510, timezones[10])  # Jakarta
create_city_label(720, 370, timezones[11])  # Tehran
create_city_label(660, 500, timezones[12])  # Johannesburg
create_city_label(145, 370, timezones[13]) # Los_Angeles
create_city_label(140, 320, timezones[14]) # Vancouver
create_city_label(240, 420, timezones[15]) # Mexico_City


# squares for different time zones
create_square(800, 400, timezones[0])  # Karachi
create_square(350, 360, timezones[1])  # New York
create_square(580, 280, timezones[2])  # London
create_square(1040, 360, timezones[3])  # Tokyo
create_square(1080, 550, timezones[4])  # Sydney
create_square(900, 350, timezones[5])  # Shanghai
create_square(760, 410, timezones[6])  # Dubai
create_square(630, 300, timezones[7])  # Berlin
create_square(1160, 580, timezones[8])  # Auckland
create_square(1060, 580, timezones[9])  # Melbourne
create_square(940, 490, timezones[10])  # Jakarta
create_square(720, 350, timezones[11])  # Tehran
create_square(680, 520, timezones[12])  # Johannesburg
create_square(220, 370, timezones[13]) # Los_Angeles
create_square(200, 320, timezones[14]) # Vancouver
create_square(260, 400, timezones[15]) # Mexico_City

# Create Country Name box
countryBox = tk.Label(root, bg="#0A3651", fg="white", font=('arial', 12))
countryBox.place(relx=0.5, y=80, anchor='n')  # Centered horizontally, 10 pixels from the top

# Create Time Box
timeBox = tk.Label(root, bg="#0A3651", fg="white", font=('arial', 35, 'bold'), width=12)
timeBox.place(relx=0.5, y=20, anchor='n')
# Footer Box
footerText = "© 2023 Hafsa Habib. All rights reserved."
footerBox = tk.Label(root, text=footerText, bg="#0A3651", fg="white", font=('arial', 12))
footerBox.place(relx=0.5, rely=1.0, y=-15, anchor='s')
# Full screen mode
root.attributes('-fullscreen', True)
# Start the clock with the default timezone
update_time()
root.mainloop()
