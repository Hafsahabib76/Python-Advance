import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

def blink_lights():
    for i in range(1, 11):
        # schedules the toggle_opacity() function to be executed with a time delay
        root.after(i * 500, lambda index=i: toggle_opacity(index % 2))
    # schedules the blink_lights() function to run after 6 seconds
    root.after(6000, blink_lights)


def toggle_opacity(state):
    global photo
    # new_img is the copy of the room image
    new_img = img.copy()
    draw = ImageDraw.Draw(new_img)
    # White bulb state = 1
    if state == 1:
        # Draw bulb with White light
        draw.ellipse((x_top_center - 40, y_top_center - 50, x_top_center + 40, y_top_center + 50), fill="#FFFFFF")
        # A semi-transparent black rectangle overlay
        black_overlay = Image.new('RGBA', new_img.size, (0, 0, 0, 100))
        new_img = Image.alpha_composite(new_img.convert("RGBA"), black_overlay)
    else:
        # Draw bulb with Yellow light
        draw.ellipse((x_top_center - 40, y_top_center - 50, x_top_center + 40, y_top_center + 50), fill="#F7CD3C")
    photo = ImageTk.PhotoImage(new_img)
    label.config(image=photo)
    label.image = photo

# root configuration
root = tk.Tk()
root.title("Blinking Light")
root.attributes('-fullscreen', True)  # Set fullscreen mode

# Load the image
img = Image.open("room.jpg")
# Resize the image to fit the screen
img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))

# Convert Image object to PhotoImage
photo = ImageTk.PhotoImage(img)

# Create a label with the image and pack it to fill the window
label = tk.Label(root, image=photo)
label.image = photo
label.pack(fill=tk.BOTH, expand=tk.YES)

# Bulb positions: x & y
x_top_center = 667
y_top_center = 170

# Footer
footerText = "© 2023 Hafsa Habib. All rights reserved. Image licensed under https://www.vecteezy.com/ Author: PITI"
footerFrameBox = tk.Label(root, bg="black", height=30)
footerFrameBox.place(x=0, y=root.winfo_screenheight() - 30, width=root.winfo_screenwidth())
footerBox = tk.Label(footerFrameBox, text=footerText, bg="black", fg="white", font=('arial', 10))
footerBox.pack(pady=4)

# Function calling
blink_lights()
root.mainloop()
