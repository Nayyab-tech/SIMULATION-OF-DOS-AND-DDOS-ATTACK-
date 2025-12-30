import tkinter as tk
import socket
import threading
from datetime import datetime
from PIL import Image, ImageTk, ImageDraw
import os
import webbrowser

# List to store all attack logs
attack_logs = []


def create_rounded_button(parent, text, command, color, width=150, height=40, radius=15):
    """Create a rounded button using a generated image as a background."""
    img = create_rounded_button_image(width, height, radius, color)
    img_tk = ImageTk.PhotoImage(img)
    button = tk.Button(parent, text=text, image=img_tk, compound="center", command=command, bd=0, relief="flat", width=width, height=height)
    button.image = img_tk  # Keep a reference to the image to prevent garbage collection
    return button


def create_rounded_button_image(width, height, radius, color):
    """Create a rounded button image."""
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, width, height], radius=radius, fill=color, outline=color)
    return img


def update_log_text():
    """Update the GUI log text widget with the latest attack logs."""
    log_text.delete(1.0, tk.END)  # Clear the text area before updating
    log_text.insert(tk.END, "".join(attack_logs))  # Insert all logs into the text widget
    log_text.yview(tk.END)  # Scroll the text area to the bottom


def start_server():
    """Start the server to listen for attack alerts."""
    def handle_client(client_socket, addr):
        try:
            # Receive the attack type from the client
            attack_type = client_socket.recv(1024).decode()

            # Get current time and date
            current_time = datetime.now().strftime("%H:%M:%S")  # Time of the attack
            current_day = datetime.now().strftime("%A, %d %B %Y")  # Day of the attack

            # Get the attacker's IP and port
            attacker_ip = addr[0]
            attacker_port = addr[1]

            # Action Taken Message
            action_taken_message = f"Action taken against attacker {attacker_ip} on port {attacker_port} for {attack_type} attack at {current_time} on {current_day}"

            # Log message formatted as a string
            log_message = f"\n\nNEW ATTACK DETECTED!\n" \
                          f"{'-'*50}\n" \
                          f"Attack Type: {attack_type}\n" \
                          f"Attacker IP: {attacker_ip}\n" \
                          f"Attacker Port: {attacker_port}\n" \
                          f"Time of Attack: {current_time}\n" \
                          f"Day of Attack: {current_day}\n" \
                          f"{'-'*50}\n" \
                          f"Action Taken: {action_taken_message}\n" \
                          f"{'-'*50}\n"

            # Append the log message to the list of attack logs
            attack_logs.append(log_message)

            # Safely update the GUI with a new attack alert
            mitigator_app.after(0, update_log_text)  # Schedule the update_log_text method to run in the main thread

            # Save log to file
            save_log_to_file()
        except Exception as e:
            log_text.insert(tk.END, f"Error handling client: {e}\n")
        finally:
            # Close the client connection after handling
            client_socket.close()

    def save_log_to_file():
        """Append logs to a file on the Desktop."""
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        log_filename = "MITIGATOR_LOG.txt"
        log_filepath = os.path.join(desktop_path, log_filename)

        # Append all attack logs to the text file instead of overwriting
        with open(log_filepath, "a") as log_file:  # Changed from "w" to "a" for append mode
            log_file.writelines(attack_logs)

    def server_loop():
        """Start the server loop to listen for incoming connections."""
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("0.0.0.0", 9999))  # Listening on all interfaces and port 9999
        server.listen(5)
        log_text.insert(tk.END, "Mitigator Server started. Waiting for attacks...\n")
        log_text.yview(tk.END)  # Scroll the text area to the bottom
        while True:
            client_socket, addr = server.accept()
            threading.Thread(target=handle_client, args=(client_socket, addr)).start()

    threading.Thread(target=server_loop, daemon=True).start()


# Function to download the log file with a unique name
def download_log_file():
    """Download logs as a new file to the Desktop."""
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Create a unique timestamp
    log_filename = f"MITIGATOR_LOG_{timestamp}.txt"  # New file name with timestamp
    log_filepath = os.path.join(desktop_path, log_filename)

    # Write all attack logs to the downloaded file with a unique name
    with open(log_filepath, "w") as log_file:
        log_file.writelines(attack_logs)

    # Display the message with the file path and make the file path clickable
    download_message.set(f"File has been downloaded! Click here to open: {log_filepath}")

    # Store the file path for later use
    global downloaded_file_path
    downloaded_file_path = log_filepath


# Function to open the downloaded file when the label is clicked
def open_downloaded_file(event):
    """Open the downloaded file with the default program."""
    if 'downloaded_file_path' in globals():
        webbrowser.open(f"file:///{downloaded_file_path}")


# GUI setup
mitigator_app = tk.Tk()
mitigator_app.configure(bg="#FFC0CB")
mitigator_app.title("MITIGATOR")

# Set window icon
icon_image = Image.open("C:\\Users\\yz\\Downloads\\is.jpg")
icon_image = icon_image.resize((100, 100))  # Resize icon (optional)
icon_image_tk = ImageTk.PhotoImage(icon_image)
mitigator_app.iconphoto(True, icon_image_tk)

# Log display section
tk.Label(mitigator_app, text="Attack Logs:", font=("Monotype Corsiva", 25, "bold"), bg="#FFC0CB").pack(pady=20)
log_frame = tk.Frame(mitigator_app, bg="#FFC0CB")
log_frame.pack(pady=10)
log_scrollbar = tk.Scrollbar(log_frame)
log_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
log_text = tk.Text(log_frame, width=80, height=20, wrap=tk.WORD, yscrollcommand=log_scrollbar.set, bg="white", fg="black", font=("Courier", 10))
log_text.pack()
log_scrollbar.config(command=log_text.yview)

# Automatically start the server when the app launches
start_server()

# Buttons
download_message = tk.StringVar()
create_rounded_button(mitigator_app, "Download Log File", download_log_file, "#1E90FF").pack(pady=10)
download_label = tk.Label(mitigator_app, textvariable=download_message, font=("Helvetica", 10), bg="#FFC0CB", fg="green", cursor="hand2")
download_label.pack(pady=5)
download_label.bind("<Button-1>", open_downloaded_file)
create_rounded_button(mitigator_app, "Exit", mitigator_app.quit, "#FF6347").pack(pady=20)

mitigator_app.mainloop()
