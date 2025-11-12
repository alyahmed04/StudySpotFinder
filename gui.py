import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error
import bcrypt

# ======================
# Database Connection
# ======================
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="studyspot",
        )
        return conn
    except Error as e:
        messagebox.showerror("Error", f"Database connection failed:\n{e}")
        return None

# ======================
# Password Verification
# ======================
def verify_password(plain, hashed):
    try:
        return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))
    except Exception:
        return False

def hash_password(plain):
    return bcrypt.hashpw(plain.encode("utf-8"), bcrypt.gensalt(rounds=12)).decode("utf-8")

# ======================
# Login Window
# ======================
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Study Spots Finder - Login")
        self.root.geometry("400x300")
        
        self.center_window()
        
        # Title
        title = tk.Label(root, text="Study Spots Finder", font=("Arial", 24, "bold"), fg="#4A90E2")
        title.pack(pady=20)
        
        subtitle = tk.Label(root, text="Find Your Perfect Study Location", font=("Arial", 10))
        subtitle.pack()
        
        # Login Frame
        login_frame = ttk.Frame(root, padding=20)
        login_frame.pack(pady=20)
        
        ttk.Label(login_frame, text="Username:").grid(row=0, column=0, sticky="w", pady=5)
        self.username_entry = ttk.Entry(login_frame, width=25)
        self.username_entry.grid(row=0, column=1, pady=5)
        
        ttk.Label(login_frame, text="Password:").grid(row=1, column=0, sticky="w", pady=5)
        self.password_entry = ttk.Entry(login_frame, width=25, show="*")
        self.password_entry.grid(row=1, column=1, pady=5)
        
        # Buttons
        btn_frame = ttk.Frame(root)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Login", command=self.login, width=12).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Create Account", command=self.create_account, width=18).grid(row=0, column=1, padx=5)
        
        self.password_entry.bind('<Return>', lambda e: self.login())
        
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showwarning("Input Error", "Please enter both username and password.")
            return
        
        conn = connect_db()
        if not conn:
            return
        
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
            
            if user and verify_password(password, user['hashedPassword']):
                messagebox.showinfo("Success", f"Welcome, {username}!")
                self.root.withdraw()
                self.open_user_dashboard(user)
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")
        except Error as e:
            messagebox.showerror("Error", f"Login error:\n{e}")
        finally:
            conn.close()
    
    def create_account(self):
        CreateAccountWindow(self.root)
    
    def open_user_dashboard(self, user):
        dashboard = tk.Toplevel(self.root)
        UserDashboard(dashboard, user, self.root)

# ======================
# Create Account Window
# ======================
class CreateAccountWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Create Account")
        self.window.geometry("400x250")
        
        frame = ttk.Frame(self.window, padding=20)
        frame.pack(fill="both", expand=True)
        
        ttk.Label(frame, text="Create New Account", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        ttk.Label(frame, text="Username:").grid(row=1, column=0, sticky="w", pady=5)
        self.username_entry = ttk.Entry(frame, width=25)
        self.username_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Email:").grid(row=2, column=0, sticky="w", pady=5)
        self.email_entry = ttk.Entry(frame, width=25)
        self.email_entry.grid(row=2, column=1, pady=5)
        
        ttk.Label(frame, text="Password:").grid(row=3, column=0, sticky="w", pady=5)
        self.password_entry = ttk.Entry(frame, width=25, show="*")
        self.password_entry.grid(row=3, column=1, pady=5)
        
        ttk.Label(frame, text="Confirm Password:").grid(row=4, column=0, sticky="w", pady=5)
        self.confirm_entry = ttk.Entry(frame, width=25, show="*")
        self.confirm_entry.grid(row=4, column=1, pady=5)
        
        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=15)
        
        ttk.Button(btn_frame, text="Create", command=self.create, width=12).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Cancel", command=self.window.destroy, width=12).pack(side="left", padx=5)
    
    def create(self):
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()
        
        if not all([username, email, password, confirm]):
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return
        
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        
        if len(password) < 6:
            messagebox.showwarning("Weak Password", "Password must be at least 6 characters.")
            return
        
        conn = connect_db()
        if not conn:
            return
        
        try:
            cursor = conn.cursor()
            hashed = hash_password(password)
            cursor.execute(
                "INSERT INTO users (username, hashedPassword, email) VALUES (%s, %s, %s)",
                (username, hashed, email)
            )
            conn.commit()
            messagebox.showinfo("Success", "Account created successfully! You can now login.")
            self.window.destroy()
        except Error as e:
            if "Duplicate entry" in str(e):
                messagebox.showerror("Error", "Username or email already exists.")
            else:
                messagebox.showerror("Error", f"Account creation failed:\n{e}")
        finally:
            conn.close()

# ======================
# User Dashboard
# ======================
class UserDashboard:
    def __init__(self, window, user, login_window):
        self.window = window
        self.user = user
        self.login_window = login_window
        
        self.window.title(f"Study Spots Finder - Welcome {user['username']}")
        self.window.geometry("600x400")
        
        self.window.protocol("WM_DELETE_WINDOW", self.logout)
        
        # Top bar with user info
        top_frame = tk.Frame(window, bg="#4A90E2", height=60)
        top_frame.pack(fill="x")
        
        tk.Label(top_frame, text="Study Spots Finder", font=("Arial", 16, "bold"), 
                bg="#4A90E2", fg="white").pack(side="left", padx=20, pady=15)
        
        user_info_text = f"Logged in as: {user['username']} | Kudos: {user['kudos']}"
        tk.Label(top_frame, text=user_info_text, 
                font=("Arial", 10), bg="#4A90E2", fg="white").pack(side="right", padx=20)
        
        # Main content area
        content_frame = tk.Frame(window)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Welcome message
        welcome_label = tk.Label(content_frame, 
                                text=f"Welcome, {user['username']}!", 
                                font=("Arial", 18, "bold"),
                                fg="#4A90E2")
        welcome_label.pack(pady=20)
        
        # User info
        info_frame = ttk.LabelFrame(content_frame, text="Account Information", padding=15)
        info_frame.pack(fill="x", pady=10)
        
        tk.Label(info_frame, text=f"User ID: {user['userID']}", 
                font=("Arial", 10)).pack(anchor="w", pady=2)
        tk.Label(info_frame, text=f"Username: {user['username']}", 
                font=("Arial", 10)).pack(anchor="w", pady=2)
        tk.Label(info_frame, text=f"Email: {user['email']}", 
                font=("Arial", 10)).pack(anchor="w", pady=2)
        tk.Label(info_frame, text=f"Kudos: {user['kudos']}", 
                font=("Arial", 10)).pack(anchor="w", pady=2)
        
        # Button frame
        button_frame = tk.Frame(content_frame)
        button_frame.pack(pady=20)
        
        # Logout button
        logout_btn = tk.Button(button_frame, text="Logout", 
                              command=self.logout,
                              font=("Arial", 12),
                              bg="#4A90E2", fg="white",
                              padx=20, pady=5,
                              cursor="hand2")
        logout_btn.pack()
        
    
    def logout(self):
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.window.destroy()
            self.login_window.deiconify()
            
            # Clear login fields
            for widget in self.login_window.winfo_children():
                if isinstance(widget, ttk.Frame):
                    for child in widget.winfo_children():
                        if isinstance(child, ttk.Entry):
                            child.delete(0, tk.END)

# ======================
# Main
# ======================
if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()