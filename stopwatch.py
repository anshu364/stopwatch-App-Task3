import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Stopwatch")
root.geometry("300x200")
root.resizable(False, False)

# Global variables
hours = 0
minutes = 0
seconds = 0
running = False

# Update time display
def update_time():
    if running:
        global hours, minutes, seconds
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1

        time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
        label.config(text=time_str)
        root.after(1000, update_time)

# Start the stopwatch
def start():
    global running
    if not running:
        running = True
        update_time()

# Stop the stopwatch
def stop():
    global running
    running = False

# Reset the stopwatch
def reset():
    global running, hours, minutes, seconds
    running = False
    hours = minutes = seconds = 0
    label.config(text="00:00:00")

# GUI Widgets
label = tk.Label(root, text="00:00:00", font=("Arial", 36))
label.pack(pady=20)

btn_frame = tk.Frame(root)
btn_frame.pack()

start_btn = tk.Button(btn_frame, text="Start", width=8, command=start)
start_btn.grid(row=0, column=0, padx=5)

stop_btn = tk.Button(btn_frame, text="Stop", width=8, command=stop)
stop_btn.grid(row=0, column=1, padx=5)

reset_btn = tk.Button(btn_frame, text="Reset", width=8, command=reset)
reset_btn.grid(row=0, column=2, padx=5)

root.mainloop()