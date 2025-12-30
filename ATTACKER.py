import os
import socket
import platform
import tkinter as tk
from PIL import Image, ImageTk
from PIL import ImageDraw
from tkinter import messagebox
import threading
import subprocess

# Global variable to store the scanned IPs
scanned_ips = []
last_ip = ""  # Initialize last_ip as an empty string

# Lock for thread-safe modification of scanned_ips
lock = threading.Lock()

# Function to create an image of a rounded button
def create_rounded_button_image(width, height, radius, color):
    """Create a rounded button image."""
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, width, height], radius=radius, fill=color, outline=color)
    return img

# Function to create a rounded button widget
def create_rounded_button(parent, text, command, color, width=150, height=40, radius=15):
    """Create a rounded button using a generated image as a background."""
    img = create_rounded_button_image(width, height, radius, color)
    img_tk = ImageTk.PhotoImage(img)
    button = tk.Button(parent, text=text, image=img_tk, compound="center", command=command, bd=0, relief="flat", width=width, height=height)
    button.image = img_tk  # Keep a reference to the image to prevent garbage collection
    return button

# Function to scan for available IPs in the LAN using simple ping (with threading)
def scan_ips():
    global scanned_ips
    if scanned_ips:  # Check if the list is already populated
        messagebox.showinfo("Scanned IPs", f"Available IPs (Already scanned):\n" + "\n".join(scanned_ips))
        return

    try:
        # Get the local IP address to determine the network (e.g., 192.168.1.x)
        local_ip = socket.gethostbyname(socket.gethostname())
        subnet = local_ip.rsplit('.', 1)[0] + '.'  # Get base subnet like "192.168.1."

        scanned_ips = []
        threads = []

        # Function to ping an individual IP address
        def ping_ip(ip):
            try:
                # Use subprocess to execute ping
                if platform.system().lower() == "windows":
                    command = ["ping", "-n", "1", "-w", "1000", ip]
                else:
                    command = ["ping", "-c", "1", "-W", "1", ip]

                # Run the ping command and capture output
                result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if result.returncode == 0:  # If ping is successful
                    with lock:  # Use lock to modify the list safely
                        scanned_ips.append(ip)
            except Exception as e:
                print(f"Error pinging {ip}: {e}")

        # Start multiple threads to ping IPs in parallel
        for i in range(1, 255):
            ip = subnet + str(i)
            thread = threading.Thread(target=ping_ip, args=(ip,))
            threads.append(thread)
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        if scanned_ips:
            messagebox.showinfo("Scanned IPs", f"Available IPs:\n" + "\n".join(scanned_ips))
        else:
            messagebox.showinfo("Scanned IPs", "No active devices found in the network.")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to scan IPs: {e}")

# Function to send the attack (Placeholder for attack logic)
def send_attack(attack_type, ip_address):
    try:
        # Establish socket connection to target
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip_address, 9999))  # Assuming the attack is on port 9999
        client.send(attack_type.encode())
        messagebox.showinfo("Success", f"{attack_type} attack has been done to {ip_address}")
        client.close()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send attack: {e}")

# Function to open a window for entering the target IP
def launch_attack_window(attack_type):
    global last_ip

    attack_window = tk.Toplevel(attacker_app)
    attack_window.title(f"Attack: {attack_type}")
    attack_window.configure(bg="#f0f0f0")

    tk.Label(attack_window, text=f"Enter IP Address for {attack_type}:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=10)
    ip_entry = tk.Entry(attack_window, font=("Helvetica", 12), width=30)
    ip_entry.pack(pady=5)

    def on_next():
        global last_ip
        ip_address = ip_entry.get()
        if not ip_address:
            messagebox.showerror("Error", "Please enter a valid IP address")
            return
        send_attack(attack_type, ip_address)
        last_ip = ip_address
        attack_window.destroy()

    def on_copy_previous_ip():
        if not last_ip:
            messagebox.showerror("Error", "No previous IP to copy")
            return
        ip_entry.delete(0, tk.END)
        ip_entry.insert(0, last_ip)

    def on_back():
        attack_window.destroy()

    button_frame = tk.Frame(attack_window, bg="#f0f0f0")
    button_frame.pack(pady=10)

    create_rounded_button(button_frame, "Next", on_next, "#2ecc71").grid(row=0, column=2, padx=5)
    copy_ip_button = create_rounded_button(button_frame, "Copy Previous IP", on_copy_previous_ip, "#f39c12")
    copy_ip_button.grid(row=0, column=1, padx=5)

    if not last_ip:
        copy_ip_button.config(state=tk.DISABLED)

    create_rounded_button(button_frame, "Back", on_back, "#e74c3c").grid(row=0, column=0, padx=5)

# Function to launch attack window
def launch_attack(attack_type):
    launch_attack_window(attack_type)

# Main GUI setup
attacker_app = tk.Tk()
attacker_app.title("Simulation of DoS and DDoS Attack (Attacker Side)")
attacker_app.geometry("600x400")
attacker_app.configure(bg="#FFC0CB")

#icon_image = Image.open("C:\\Users\\LENOVO\\Downloads\\is.jpg")  # Image ka path
#icon_image = icon_image.resize((100, 100))  # Icon size ko adjust karna (optional)

# Tkinter ke liye image ko convert karte hain
#icon_image_tk = ImageTk.PhotoImage(icon_image)

# Window ka icon set karna
#attacker_app.iconphoto(True, icon_image_tk)

tk.Label(attacker_app, text="Simulation of DoS and DDoS Attack", bg="#FFC0CB", fg="black", font=("Monotype Corsiva", 24, "bold")).pack(pady=20)

frame = tk.Frame(attacker_app, bg="white", bd=5)
frame.pack(fill="x", padx=10, pady=20)

tk.Label(frame, text="Select Attack Type:", bg="white", fg="black", font=("Arial", 14, "bold")).pack(pady=20)

light_blue = "#ADD8E6"
# Create rounded buttons for each attack
create_rounded_button(frame, "DoS", lambda: launch_attack("DoS"), light_blue).pack(pady=10)
create_rounded_button(frame, "DDoS Attack", lambda: launch_attack("DDoS"), light_blue).pack(pady=10)
create_rounded_button(frame, "SYN Flood", lambda: launch_attack("SYN Flood"), light_blue).pack(pady=10)
create_rounded_button(frame, "SQL Injection", lambda: launch_attack("SQL Injection"), light_blue).pack(pady=10)
create_rounded_button(frame, "UDP Flood", lambda: launch_attack("UDP Flood"), light_blue).pack(pady=10)

# Scan IP Button
create_rounded_button(attacker_app, "Scan IP", scan_ips, "#1abc9c").pack(pady=10)
# Exit Button
create_rounded_button(attacker_app, "Exit", attacker_app.quit, "#e74c3c").pack(pady=20)

attacker_app.mainloop()
