#!/usr/bin/env python3
"""
🎩 WHITE HAT PASS AUDITOR - UST TALCA
Herramienta ética de análisis de contraseñas
Patente: MATÍAS VALLADARES © 2024
"""

import hashlib
import time
import math
import itertools
import sys
import os
from datetime import datetime

class WhiteHatPasswordAuditor:
    def __init__(self):
        self.charsets = {
            'numeric': '0123456789',
            'lowercase': 'abcdefghijklmnopqrstuvwxyz', 
            'uppercase': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'symbols': '!@#$%^&*()_+-=[]{}|;:,.<>?'
        }
        
    def show_animated_banner(self):
        """Muestra banner ."""
        frames = [
            r"""
    ██╗    ██╗██╗  ██╗██╗████████╗███████╗     ██╗  ██╗ █████╗ ████████╗
    ██║    ██║██║  ██║██║╚══██╔══╝██╔════╝     ██║  ██║██╔══██╗╚══██╔══╝
    ██║ █╗ ██║███████║██║   ██║   █████╗       ███████║███████║   ██║   
    ██║███╗██║██╔══██║██║   ██║   ██╔══╝       ██╔══██║██╔══██║   ██║   
    ╚███╔███╔╝██║  ██║██║   ██║   ███████╗     ██║  ██║██║  ██║   ██║   
     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
            """,
            r"""
    ██████╗ ██╗  ██╗██████╗ ███████╗██████╗     ██╗  ██╗ █████╗ ████████╗
    ██╔══██╗██║  ██║██╔══██╗██╔════╝██╔══██╗    ██║  ██║██╔══██╗╚══██╔══╝
    ██████╔╝███████║██████╔╝█████╗  ██████╔╝    ███████║███████║   ██║   
    ██╔═══╝ ██╔══██║██╔══██╗██╔══╝  ██╔══██╗    ██╔══██║██╔══██║   ██║   
    ██║     ██║  ██║██████╔╝███████╗██║  ██║    ██║  ██║██║  ██║   ██║   
    ╚═╝     ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
            """,
            r"""
    ██╗    ██╗██╗  ██╗██╗████████╗███████╗     ██╗  ██╗ █████╗ ████████╗
    ██║    ██║██║  ██║██║╚══██╔══╝██╔════╝     ██║  ██║██╔══██╗╚══██╔══╝
    ██║ █╗ ██║███████║██║   ██║   █████╗       ███████║███████║   ██║   
    ██║███╗██║██╔══██║██║   ██║   ██╔══╝       ██╔══██║██╔══██║   ██║   
    ╚███╔███╔╝██║  ██║██║   ██║   ███████╗     ██║  ██║██║  ██║   ██║   
     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
            """
        ]
        
        colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[95m']
        
        # Animación de entrada
        for i in range(10):
            os.system('cls' if os.name == 'nt' else 'clear')
            frame = frames[i % len(frames)]
            color = colors[i % len(colors)]
            print(f"{color}{frame}\033[0m")
            print("🔓 CARGANDO SISTEMA" + "." * (i % 4))
            time.sleep(0.1)
        
        # Banner final
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[92m" + frames[0] + "\033[0m")
        print("🎩 WHITE HAT PASS AUDITOR - UST TALCA")
        print("⚡ HACKING ÉTICO - ENTORNO CONTROLADO")
        print("🔐 PATENTE: MATÍAS VALLADARES © 2025")
        print("="*60)
        
        # Mensaje legal
        print("\033[93m")
        print("⚠️  AVISO LEGAL: Este es un entorno controlado para")
        print("   hacking ético. Todas las actividades son legales")
        print("   y se realizan con fines educativos y de investigación.")
        print("   Prohibido su uso para actividades maliciosas.")
        print("\033[0m")
        print("="*60)
        
        time.sleep(2)
    
    def typewriter_effect(self, text, delay=0.05):
        """Efecto máquina de escribir."""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def calculate_entropy(self, password):
        """Calcula la entropía de la contraseña en bits."""
        charset_size = 0
        if any(c.islower() for c in password): charset_size += 26
        if any(c.isupper() for c in password): charset_size += 26  
        if any(c.isdigit() for c in password): charset_size += 10
        if any(not c.isalnum() for c in password): charset_size += 33
        
        entropy = len(password) * math.log2(charset_size) if charset_size > 0 else 0
        return round(entropy, 2)
    
    def estimate_cracking_time(self, entropy):
        """Estima tiempo real de crackeo."""
        hashes_per_second = 1000000000
        seconds = (2 ** entropy) / hashes_per_second
        
        if seconds < 1:
            return f"{seconds*1000:.2f} milisegundos"
        elif seconds < 60:
            return f"{seconds:.2f} segundos"
        elif seconds < 3600:
            return f"{seconds/60:.2f} minutos"
        elif seconds < 86400:
            return f"{seconds/3600:.2f} horas"
        elif seconds < 31536000:
            return f"{seconds/86400:.2f} días"
        else:
            return f"{seconds/31536000:.2f} años"
    
    def analyze_single_password(self, password):
        """Analiza una contraseña individual."""
        print(f"\n🎯 ANALIZANDO: '{password}'")
        print("="*50)
        
        entropy = self.calculate_entropy(password)
        crack_time = self.estimate_cracking_time(entropy)
        
        print(f"📏 Longitud: {len(password)} caracteres")
        print(f"🧠 Entropía: {entropy} bits")
        print(f"⏰ Tiempo crackeo: {crack_time}")
        
        # Simular fuerza bruta para contraseñas cortas
        if len(password) <= 6:
            self.simulate_brute_force(password)
        else:
            print(f"🔒 Nivel seguridad: ALTO (resistiría {crack_time})")
    
    def analyze_multiple_passwords(self, passwords):
        """Analiza múltiples contraseñas."""
        print(f"\n🔍 ANALIZANDO {len(passwords)} CONTRASEÑAS")
        print("="*60)
        
        results = []
        for i, password in enumerate(passwords, 1):
            print(f"\n{i}. '{password}'")
            entropy = self.calculate_entropy(password)
            crack_time = self.estimate_cracking_time(entropy)
            
            results.append({
                'password': password,
                'entropy': entropy,
                'crack_time': crack_time,
                'vulnerable': entropy < 40
            })
            
            print(f"   📏 Longitud: {len(password)}")
            print(f"   🧠 Entropía: {entropy} bits")
            print(f"   ⏰ T. crackeo: {crack_time}")
            print(f"   🔒 Seguridad: {'BAJA' if entropy < 40 else 'ALTA'}")
        
        # Resumen
        vulnerable = sum(1 for r in results if r['vulnerable'])
        print(f"\n📊 RESUMEN: {vulnerable}/{len(passwords)} vulnerables")
    
    def simulate_brute_force(self, target_password):
        """Simula fuerza bruta para contraseñas cortas."""
        print(f"\n⚡ SIMULANDO FUERZA BRUTA...")
        print("-"*40)
        
        target_hash = hashlib.sha256(target_password.encode()).hexdigest()
        charset = self.determine_charset(target_password)
        start_time = time.time()
        attempts = 0
        cracked = False
        
        for length in range(1, len(target_password) + 1):
            for combination in itertools.product(charset, repeat=length):
                attempt = ''.join(combination)
                attempts += 1
                if hashlib.sha256(attempt.encode()).hexdigest() == target_hash:
                    cracked = True
                    break
            if cracked:
                break
        
        elapsed_time = time.time() - start_time
        
        if cracked:
            print(f"❌ VULNERABLE - Crackeada en {elapsed_time:.6f}s")
            print(f"🔓 Contraseña encontrada: '{attempt}'")
            print(f"📈 Intentos: {attempts}")
        else:
            print(f"✅ RESISTIÓ - No crackeada en {elapsed_time:.2f}s")
    
    def determine_charset(self, password):
        """Determina el charset necesario."""
        charset = ''
        if any(c.isdigit() for c in password): charset += self.charsets['numeric']
        if any(c.islower() for c in password): charset += self.charsets['lowercase']
        if any(c.isupper() for c in password): charset += self.charsets['uppercase']
        if any(not c.isalnum() for c in password): charset += self.charsets['symbols']
        return charset if charset else self.charsets['numeric']
    
    def main_menu(self):
        """Menú principal interactivo."""
        self.show_animated_banner()
        
        while True:
            print("\n🔧 MODO DE ANÁLISIS:")
            print("1. 🔍 Analizar UNA contraseña")
            print("2. 📊 Analizar MÚLTIPLES contraseñas")
            print("3. 🚪 Salir")
            
            choice = input("\n🎮 Selecciona opción (1-3): ").strip()
            
            if choice == "1":
                password = input("🔐 Ingresa la contraseña a analizar: ").strip()
                if password:
                    self.analyze_single_password(password)
                else:
                    print("⚠️  Ingresa una contraseña válida")
            
            elif choice == "2":
                print("🔐 Ingresa múltiples contraseñas (escribe 'fin' para terminar):")
                passwords = []
                while True:
                    pwd = input("Contraseña: ").strip()
                    if pwd.lower() == 'fin':
                        break
                    if pwd:
                        passwords.append(pwd)
                
                if passwords:
                    self.analyze_multiple_passwords(passwords)
                else:
                    print("⚠️  No ingresaste contraseñas")
            
            elif choice == "3":
                print("\n👋 ¡White Hat auditing completado!")
                print("🔐 PATENTE: MATÍAS VALLADARES © 2024")
                break
            
            else:
                print("⚠️  Opción no válida")

# Ejecución principal
if __name__ == "__main__":
    auditor = WhiteHatPasswordAuditor()
    auditor.main_menu()
