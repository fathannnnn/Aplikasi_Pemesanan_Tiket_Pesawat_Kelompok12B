import json
import os
import hashlib
from Booking import clear_screen

class UserManager:
    def __init__(self):
        self.users_file = 'users.json'
        self.users = self.load_users()
        self.max_attempts = 3
        
    def load_users(self):
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as file:
                return json.load(file)
        return {}
    
    def save_users(self):
        with open(self.users_file, 'w') as file:
            json.dump(self.users, file, indent=4)
            
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register(self):
        clear_screen()
        print("\n=== REGISTRASI PENGGUNA BARU ===")
        while True:
            username = input("Masukkan username: ").strip()
            if not username:
                print("Username tidak boleh kosong!")
                continue
            if username in self.users:
                print("Username sudah terdaftar!")
                continue
                
            password = input("Masukkan password: ")
            if len(password) < 6:
                print("Password harus minimal 6 karakter!")
                continue
                
            self.users[username] = {
                'password': self.hash_password(password),
                'attempts': 0,
                'locked': False
            }
            self.save_users()
            print("Registrasi berhasil! Silakan login.")
            return True
    
    def login(self):
        clear_screen()
        print("\n=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ")
        
        if username not in self.users:
            print("Username tidak ditemukan!")
            return None
            
        user = self.users[username]
        if user['locked']:
            print("Akun terkunci! Silakan hubungi admin.")
            return None
            
        if user['password'] == self.hash_password(password):
            user['attempts'] = 0
            self.save_users()
            return username
        else:
            user['attempts'] += 1
            if user['attempts'] >= self.max_attempts:
                user['locked'] = True
                print(f"Akun terkunci karena {self.max_attempts} kali gagal login!")
            else:
                print(f"Password salah! Sisa percobaan: {self.max_attempts - user['attempts']}")
            self.save_users()
            return None
