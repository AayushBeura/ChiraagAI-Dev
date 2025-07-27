import os
import json
import tkinter as tk
from tkinter import messagebox, simpledialog
from dotenv import load_dotenv

class ConfigManager:
    def __init__(self):
        self.config_file = "user_config.json"
        self.api_keys = {}
        
    def load_config(self):
        """Load API keys from .env (dev) or prompt user (production)"""
        # Development: Try .env file first
        if os.path.exists('.env'):
            load_dotenv()
            gemini_key = os.getenv('GEMINI_API_KEY')
            murf_key = os.getenv('MURF_API_KEY')
            
            if gemini_key and murf_key:
                self.api_keys = {
                    'GEMINI_API_KEY': gemini_key,
                    'MURF_API_KEY': murf_key
                }
                return True
        
        # Production: Try saved config
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    self.api_keys = config.get('api_keys', {})
                    if self.api_keys.get('GEMINI_API_KEY') and self.api_keys.get('MURF_API_KEY'):
                        return True
            except:
                pass
        
        # No valid config - prompt user
        return self.prompt_for_keys()
    
    def prompt_for_keys(self):
        """Get API keys from user via GUI"""
        root = tk.Tk()
        root.withdraw()
        
        messagebox.showinfo(
            "ChiraagAI Setup", 
            "Welcome to ChiraagAI!\n\nPlease enter your API keys to continue.\n\n" +
            "Required:\n• Gemini AI API Key\n• Murf TTS API Key"
        )
        
        gemini_key = simpledialog.askstring(
            "API Setup", "Enter Gemini AI API Key:", show='*'
        )
        if not gemini_key:
            messagebox.showerror("Error", "Gemini API key required!")
            return False
            
        murf_key = simpledialog.askstring(
            "API Setup", "Enter Murf TTS API Key:", show='*'
        )
        if not murf_key:
            messagebox.showerror("Error", "Murf API key required!")
            return False
        
        self.api_keys = {
            'GEMINI_API_KEY': gemini_key,
            'MURF_API_KEY': murf_key
        }
        
        self.save_config()
        root.destroy()
        messagebox.showinfo("Success", "API keys saved!")
        return True
    
    def save_config(self):
        """Save config to file"""
        config = {'api_keys': self.api_keys}
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
    
    def get_api_key(self, key_name):
        return self.api_keys.get(key_name)
