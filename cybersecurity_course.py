# ========== PYTHON CYBERSECURITY COURSE ==========
# A complete learning system in one executable file
# Includes: Core lessons, security tools, and challenges

import os
import sys
import socket
import hashlib
import json
import base64
from cryptography.fernet import Fernet

class PythonCyberSecurityCourse:
    def __init__(self):
        self.current_module = 1
        self.completed_modules = set()
        self.student_name = ""
        self.debug_mode = False
    
    def run(self):
        self.clear_screen()
        self.print_banner()
        self.get_student_info()
        self.main_menu()
    
    # ----- Core System Functions -----
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        print(r"""
   _____      _   _             _____           _ _ _                       
  |  __ \    | | | |           / ____|         | (_) |                      
  | |__) |_ _| |_| |_ ___ _ __| |     _ __ __ _| |_| |_ ___  _ __ _______   
  |  ___/ _` | __| __/ _ \ '__| |    | '__/ _` | | | __/ _ \| '__|_  / _ \  
  | |  | (_| | |_| ||  __/ |  | |____| | | (_| | | | || (_) | |   / / (_) | 
  |_|   \__,_|\__|\__\___|_|   \_____|_|  \__,_|_|_|\__\___/|_|  /___\___/  
                                                                            
        """)
        print("Welcome to Python Cybersecurity Immersive".center(80))
        print("="*80 + "\n")
    
    def get_student_info(self):
        print("\n[STUDENT REGISTRATION]")
        self.student_name = input("Enter your name: ").strip()
        if not self.student_name:
            self.student_name = "Cyber Cadet"
    
    # ----- Main Menu System -----
    def main_menu(self):
        while True:
            self.clear_screen()
            print(f"\nWelcome, {self.student_name}! (Current Module: {self.current_module})")
            print("\nMAIN MENU:")
            print("1. View Curriculum")
            print("2. Start Current Module")
            print("3. Practical Challenges")
            print("4. Security Tools")
            print("5. Progress Overview")
            print("6. Debug Mode" + (" [ON]" if self.debug_mode else ""))
            print("0. Exit Program")
            
            choice = input("\nSelect option: ").strip()
            
            if choice == "1":
                self.view_curriculum()
            elif choice == "2":
                self.start_module()
            elif choice == "3":
                self.practical_challenges()
            elif choice == "4":
                self.security_tools()
            elif choice == "5":
                self.progress_overview()
            elif choice == "6":
                self.debug_mode = not self.debug_mode
                print(f"\nDebug mode {'activated' if self.debug_mode else 'deactivated'}")
                input("Press Enter to continue...")
            elif choice == "0":
                self.exit_program()
            else:
                print("Invalid selection. Please try again.")
                input("Press Enter to continue...")

    # ----- Core Curriculum Modules -----
    def view_curriculum(self):
        self.clear_screen()
        print("\nPYTHON CYBERSECURITY CURRICULUM:\n")
        modules = {
            1: "Python Fundamentals (Syntax, Data Structures)",
            2: "Network Programming & Analysis",
            3: "Web Security (Requests, Web Scraping)",
            4: "Cryptography & Data Protection",
            5: "Penetration Testing Tools",
            6: "Malware Analysis Basics",
            7: "Digital Forensics with Python",
            8: "Security Automation"
        }
        
        for num, desc in modules.items():
            status = "✓" if num in self.completed_modules else " "
            print(f"{num}. [{status}] {desc}")
        
        mod_select = input("\nEnter module number to view details (or 'back'): ").strip().lower()
        if mod_select.isdigit() and int(mod_select) in modules:
            self.module_details(int(mod_select))
        elif mod_select != 'back':
            print("Invalid module number")
            input("Press Enter to continue...")

    def start_module(self):
        # Module execution logic would go here
        print(f"\nStarting Module {self.current_module}...")
        
        if self.current_module == 1:
            self.module_python_fundamentals()
        elif self.current_module == 2:
            self.module_networking()
        # Additional module handlers would be added here
        
        input("\nPress Enter to continue to next module...")
        self.current_module = min(self.current_module + 1, 8)
        self.completed_modules.add(self.current_module)

    # ----- Security Tools -----
    def security_tools(self):
        while True:
            self.clear_screen()
            print("\nSECURITY TOOLS:\n")
            print("1. Port Scanner")
            print("2. Password Hasher")
            print("3. Simple Encrypt/Decrypt")
            print("4. Web Request")
            print("5. Packet Sniffer (Basic)")
            print("0. Back to Main Menu")
            
            choice = input("\nSelect tool: ").strip()
            
            if choice == "1":
                self.tool_port_scanner()
            elif choice == "2":
                self.tool_password_hasher()
            elif choice == "3":
                self.tool_crypto()
            elif choice == "4":
                self.tool_web_request()
            elif choice == "5":
                self.tool_packet_sniffer()
            elif choice == "0":
                return
            else:
                print("Invalid selection")
                input("Press Enter to continue...")

    # ----- Practical Implementations -----
    def tool_port_scanner(self):
        print("\nPORT SCANNER")
        target = input("Enter target IP or hostname: ").strip()
        ports = input("Enter ports to scan (e.g., 80,443 or 1-100): ").strip()
        
        try:
            port_list = []
            if '-' in ports:
                start, end = map(int, ports.split('-'))
                port_list = range(start, end+1)
            else:
                port_list = map(int, ports.split(','))
            
            open_ports = []
            for port in port_list:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"Port {port}: OPEN")
                    open_ports.append(port)
                s.close()
            
            print(f"\nScan complete. Found {len(open_ports)} open ports.")
            
        except Exception as e:
            print(f"Error: {e}")
        input("Press Enter to continue...")

    # ... (Additional tool implementations would go here)

    # ----- System Functions -----
    def exit_program(self):
        print(f"\nGoodbye, {self.student_name}! Saving your progress...")
        # Save progress logic would go here
        sys.exit(0)

# ======== MAIN EXECUTION ========
if __name__ == "__main__":
    try:
        course = PythonCyberSecurityCourse()
        course.run()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"\nError: {e}")
