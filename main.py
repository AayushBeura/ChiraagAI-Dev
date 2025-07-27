from config_manager import ConfigManager

import tkinter as tk
from tkinter import scrolledtext, messagebox, font as tkfont
import sys
import os
import cv2
from PIL import Image, ImageTk
import threading
import time
import requests
import json
import speech_recognition as sr
import pygame
from io import BytesIO
import google.generativeai as genai
import pyautogui
import subprocess
import webbrowser
from urllib.parse import quote
import re
from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

class ChiraagAI:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("ChiraagAI Assistant")
        
        # Set window icon
        self.set_window_icon()
        
        # Configure window properties
        self.setup_window()
        
        # Initialize custom fonts
        self.setup_fonts()
        
        # Initialize AI components
        self.setup_ai_components()
        
        # Initialize PyAutoGUI settings
        self.setup_automation()
        
        # Media playback state
        self.video_label = None
        self.is_listening = False
        self.conversation_history = []
        self.pending_response = None
        self.current_task = None
        self.debug_mode = True
        self.email_input_mode = False  # Email AI mode tracking
        
        # Start with startup sequence
        self.start_startup_sequence()
    
    def setup_automation(self):
        """Initialize PyAutoGUI and automation settings"""
        pyautogui.PAUSE = 0.1  # Ultra-fast automation
        pyautogui.FAILSAFE = True
        
        # Enhanced application commands
        self.app_commands = {
            'chrome': 'chrome',
            'google chrome': 'chrome',
            'firefox': 'firefox',
            'brave': 'brave',
            'opera': 'opera',
            'edge': 'edge',
            'microsoft edge': 'edge',
            'notepad': 'notepad',
            'calculator': 'calc',
            'calc': 'calc',
            'file explorer': 'explorer',
            'explorer': 'explorer',
            'task manager': 'taskmgr',
            'taskmgr': 'taskmgr',
            'control panel': 'control panel',
            'settings': 'settings',
            'word': 'word',
            'microsoft word': 'word',
            'excel': 'excel',
            'microsoft excel': 'excel',
            'powerpoint': 'powerpoint',
            'microsoft powerpoint': 'powerpoint',
            'outlook': 'outlook',
            'microsoft outlook': 'outlook',
            'teams': 'teams',
            'microsoft teams': 'teams',
            'skype': 'skype',
            'discord': 'discord',
            'spotify': 'spotify',
            'steam': 'steam',
            'vlc': 'vlc',
            'vlc media player': 'vlc',
            'photoshop': 'photoshop',
            'adobe photoshop': 'photoshop',
            'illustrator': 'illustrator',
            'adobe illustrator': 'illustrator',
            'premiere': 'premiere',
            'adobe premiere': 'premiere',
            'after effects': 'after effects',
            'adobe after effects': 'after effects',
            'visual studio code': 'visual studio code',
            'vs code': 'code',
            'vscode': 'code',
            'code': 'code',
            'sublime': 'sublime',
            'sublime text': 'sublime',
            'atom': 'atom',
            'notepad++': 'notepad++',
            'pycharm': 'pycharm',
            'intellij': 'intellij',
            'android studio': 'android studio',
            'unity': 'unity',
            'blender': 'blender',
            '7zip': '7-zip',
            'winrar': 'winrar',
            'git bash': 'git bash',
            'cmd': 'cmd',
            'command prompt': 'cmd',
            'powershell': 'powershell',
            'terminal': 'terminal',
            'paint': 'paint',
            'mspaint': 'paint',
            'snipping tool': 'snipping tool',
            'sticky notes': 'sticky notes',
            'magnifier': 'magnifier',
            'on screen keyboard': 'osk',
            'narrator': 'narrator',
            'device manager': 'device manager',
            'disk cleanup': 'cleanmgr',
            'defrag': 'dfrgui',
            'registry editor': 'regedit',
            'system configuration': 'msconfig',
            'services': 'services',
            'event viewer': 'eventvwr',
            'resource monitor': 'resmon',
            'performance monitor': 'perfmon',
            'computer management': 'compmgmt',
            'disk management': 'diskmgmt',
            'group policy': 'gpedit',
            'gimp': 'gimp',
            'inkscape': 'inkscape',
            'audacity': 'audacity',
            'handbrake': 'handbrake',
            'obs': 'obs',
            'obs studio': 'obs',
            'zoom': 'zoom',
            'teamviewer': 'teamviewer',
            'anydesk': 'anydesk',
            'putty': 'putty',
            'wireshark': 'wireshark',
            'virtualbox': 'virtualbox',
            'vmware': 'vmware',
            'docker': 'docker',
            'postgresql': 'postgresql',
            'mysql': 'mysql',
            'mongodb': 'mongodb',
            'redis': 'redis',
            'node': 'node',
            'python': 'python',
            'java': 'java',
            'git': 'git',
            'github desktop': 'github desktop',
            'sourcetree': 'sourcetree',
            'postman': 'postman',
            'insomnia': 'insomnia',
            'xampp': 'xampp',
            'mamp': 'mamp',
            'laragon': 'laragon',
            'wamp': 'wamp',
            'filezilla': 'filezilla',
            'cyberduck': 'cyberduck',
            'telegram': 'telegram',
            'whatsapp': 'whatsapp',
            'signal': 'signal',
            'slack': 'slack'
        }
        
        # Enhanced website shortcuts
        self.website_urls = {
            'youtube': 'https://youtube.com',
            'gmail': 'https://gmail.com',
            'google': 'https://google.com',
            'facebook': 'https://facebook.com',
            'twitter': 'https://twitter.com',
            'instagram': 'https://instagram.com',
            'linkedin': 'https://linkedin.com',
            'github': 'https://github.com',
            'stackoverflow': 'https://stackoverflow.com',
            'reddit': 'https://reddit.com',
            'amazon': 'https://amazon.com',
            'netflix': 'https://netflix.com',
            'amazon prime': 'https://primevideo.com',
            'prime video': 'https://primevideo.com',
            'disney plus': 'https://disneyplus.com',
            'disney+': 'https://disneyplus.com',
            'hulu': 'https://hulu.com',
            'hbo max': 'https://hbomax.com',
            'paramount plus': 'https://paramountplus.com',
            'peacock': 'https://peacocktv.com',
            'apple tv': 'https://tv.apple.com',
            'crunchyroll': 'https://crunchyroll.com',
            'spotify': 'https://spotify.com',
            'apple music': 'https://music.apple.com',
            'pandora': 'https://pandora.com',
            'soundcloud': 'https://soundcloud.com',
            'twitch': 'https://twitch.tv',
            'discord': 'https://discord.com',
            'slack': 'https://slack.com',
            'zoom': 'https://zoom.us',
            'meet': 'https://meet.google.com',
            'teams': 'https://teams.microsoft.com',
            'skype': 'https://skype.com',
            'whatsapp web': 'https://web.whatsapp.com',
            'telegram': 'https://web.telegram.org',
            'dropbox': 'https://dropbox.com',
            'onedrive': 'https://onedrive.live.com',
            'google drive': 'https://drive.google.com',
            'icloud': 'https://icloud.com',
            'canva': 'https://canva.com',
            'figma': 'https://figma.com',
            'adobe': 'https://adobe.com',
            'notion': 'https://notion.so',
            'trello': 'https://trello.com',
            'asana': 'https://asana.com',
            'monday': 'https://monday.com',
            'clickup': 'https://clickup.com',
            'todoist': 'https://todoist.com',
            'evernote': 'https://evernote.com',
            'medium': 'https://medium.com',
            'quora': 'https://quora.com',
            'pinterest': 'https://pinterest.com',
            'tumblr': 'https://tumblr.com',
            'behance': 'https://behance.net',
            'dribbble': 'https://dribbble.com',
            'codepen': 'https://codepen.io',
            'khan academy': 'https://khanacademy.org',
            'coursera': 'https://coursera.org',
            'udemy': 'https://udemy.com',
            'edx': 'https://edx.org',
            'wikipedia': 'https://wikipedia.org',
            'imdb': 'https://imdb.com',
            'goodreads': 'https://goodreads.com',
            'yelp': 'https://yelp.com',
            'booking': 'https://booking.com',
            'airbnb': 'https://airbnb.com',
            'uber': 'https://uber.com',
            'lyft': 'https://lyft.com',
            'paypal': 'https://paypal.com',
            'ebay': 'https://ebay.com',
            'etsy': 'https://etsy.com',
            'shopify': 'https://shopify.com',
            'wordpress': 'https://wordpress.com',
            'wix': 'https://wix.com',
            'squarespace': 'https://squarespace.com'
        }
    
    def type_lightning_fast(self, text):
        """ULTRA LIGHTNING FAST typing - entire text typed in under 0.3 seconds"""
        chunk_size = 10  # Smaller chunks for better reliability
        for i in range(0, len(text), chunk_size):
            chunk = text[i:i+chunk_size]
            pyautogui.write(chunk, interval=0.005)  # Small interval between characters
            time.sleep(0.02)  # Slightly longer pause between chunks
    
    def type_instant(self, text):
        """INSTANT typing for short URLs - no delays"""
        pyautogui.write(text)
    
    def setup_fonts(self):
        """Initialize custom fonts for better text rendering"""
        try:
            self.title_font = tkfont.Font(family="Segoe UI", size=32, weight="bold")
            self.subtitle_font = tkfont.Font(family="Segoe UI", size=12, weight="normal")
            self.status_font = tkfont.Font(family="Segoe UI", size=13, weight="bold")
            self.button_font = tkfont.Font(family="Segoe UI", size=12, weight="bold")
            self.conversation_font = tkfont.Font(family="Consolas", size=11, weight="normal")
            self.label_font = tkfont.Font(family="Segoe UI", size=11, weight="normal")
        except:
            self.title_font = tkfont.Font(family="Arial", size=32, weight="bold")
            self.subtitle_font = tkfont.Font(family="Arial", size=12, weight="normal")
            self.status_font = tkfont.Font(family="Arial", size=13, weight="bold")
            self.button_font = tkfont.Font(family="Arial", size=12, weight="bold")
            self.conversation_font = tkfont.Font(family="Courier", size=11, weight="normal")
            self.label_font = tkfont.Font(family="Arial", size=11, weight="normal")
        
    def setup_ai_components(self):
        """Initialize AI and speech components with enhanced config management"""
        # Speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
        
        # FIXED: Initialize pygame properly
        try:
            pygame.mixer.quit()
        except:
            pass
        
        pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
        pygame.mixer.init()
        
        # Load configuration using ConfigManager
        config_manager = ConfigManager()
        if not config_manager.load_config():
            messagebox.showerror("Setup Failed", "API key configuration failed. Application will exit.")
            sys.exit(1)
        
        # Get API Keys from config manager
        self.gemini_api_key = config_manager.get_api_key('GEMINI_API_KEY')
        self.murf_api_key = config_manager.get_api_key('MURF_API_KEY')

        # Validation
        if not self.gemini_api_key:
            raise ValueError("GEMINI_API_KEY is required")
        if not self.murf_api_key:
            raise ValueError("MURF_API_KEY is required")
        
        # Configure Gemini
        genai.configure(api_key=self.gemini_api_key)
        self.gemini_model = genai.GenerativeModel('gemini-1.5-flash')
        
        self.generation_config = genai.types.GenerationConfig(
            candidate_count=1,
            max_output_tokens=150,
            temperature=0.2,
        )
        
        # Enhanced generation config for email content
        self.email_generation_config = genai.types.GenerationConfig(
            candidate_count=1,
            max_output_tokens=600,
            temperature=0.3,
        )
        
        self.chat_session = self.gemini_model.start_chat(history=[])

    
    def set_window_icon(self):
        """Set the window icon with dual format support"""
        try:
            if getattr(sys, 'frozen', False):
                base_path = sys._MEIPASS
            else:
                base_path = os.path.dirname(os.path.abspath(__file__))
            
            ico_path = os.path.join(base_path, "ChiraagAI-Icon.ico")
            png_path = os.path.join(base_path, "ChiraagAI-Icon.png")
            
            if os.path.exists(ico_path):
                try:
                    self.root.iconbitmap(ico_path)
                except:
                    if os.path.exists(png_path):
                        icon = tk.PhotoImage(file=png_path)
                        self.root.iconphoto(False, icon)
        except Exception as e:
            print(f"Icon loading error: {e}")
    
    def setup_window(self):
        """Configure window size and properties"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        self.window_width = int(screen_width * 0.7)
        self.window_height = int(screen_height * 0.8)
        
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        
        self.root.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")
        self.root.resizable(width=False, height=False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def start_startup_sequence(self):
        """Initialize startup sequence with video playback"""
        self.root.configure(bg="black")
        self.play_startup_sequence()
    
    def get_resource_path(self, filename):
        """Get the correct path for resources"""
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_path, filename)
    
    def play_startup_sequence(self):
        """Play MP4 video with MP3 audio (simple version)"""
        def media_sequence():
            try:
                mp4_path = self.get_resource_path("startup.mp4")
                mp3_path = self.get_resource_path("startup.mp3")
                
                # Start audio playback
                if os.path.exists(mp3_path):
                    try:
                        if not pygame.mixer.get_init():
                            pygame.mixer.init()
                        pygame.mixer.music.load(mp3_path)
                        pygame.mixer.music.play()
                    except Exception as e:
                        print(f"Audio playback error: {e}")
                
                # Start video playback
                if os.path.exists(mp4_path):
                    self.root.after(0, self.play_video, mp4_path)
                else:
                    # If no video, wait for audio to finish then show interface
                    self.root.after(8000, self.show_main_interface)  # Adjust based on your MP3 length
                    
            except Exception as e:
                print(f"Media sequence error: {e}")
                self.root.after(0, self.show_main_interface)
        
        threading.Thread(target=media_sequence, daemon=True).start()
    
    def play_video(self, video_path):
        """Play MP4 video inside the window"""
        try:
            cap = cv2.VideoCapture(video_path)
            
            if not cap.isOpened():
                print("Could not open video file")
                self.show_main_interface()
                return
            
            fps = cap.get(cv2.CAP_PROP_FPS)
            frame_delay = int(1000 / fps) if fps > 0 else 33
            
            self.video_label = tk.Label(self.root, bg="black")
            self.video_label.pack(fill=tk.BOTH, expand=True)
            
            def play_frame():
                ret, frame = cap.read()
                if ret:
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_resized = cv2.resize(frame_rgb, (self.window_width, self.window_height))
                    
                    pil_image = Image.fromarray(frame_resized)
                    photo = ImageTk.PhotoImage(pil_image)
                    
                    self.video_label.configure(image=photo)
                    self.video_label.image = photo
                    
                    self.root.after(frame_delay, play_frame)
                else:
                    cap.release()
                    # Stop audio when video ends
                    try:
                        pygame.mixer.music.stop()
                    except:
                        pass
                    self.show_main_interface()
            
            play_frame()
            
        except Exception as e:
            print(f"Video playback error: {e}")
            self.show_main_interface()
    
    def show_main_interface(self):
        """Show the main Jarvis-style interface"""
        try:
            if self.video_label:
                self.video_label.destroy()
                self.video_label = None
            
            self.root.configure(bg='#0a0a0f')
            self.create_interface_elements()
            
        except Exception as e:
            print(f"Interface setup error: {e}")
            self.root.configure(bg="#0a0a0f")
    
    def load_logo_image(self):
        """Load and resize the logo image"""
        try:
            logo_path = self.get_resource_path("logo.png")
            if os.path.exists(logo_path):
                # Load and resize logo
                logo_image = Image.open(logo_path)
                logo_image = logo_image.resize((80, 80), Image.Resampling.LANCZOS)
                return ImageTk.PhotoImage(logo_image)
        except Exception as e:
            print(f"Logo loading error: {e}")
        return None
    
    def create_interface_elements(self):
        """ENHANCED: Clean centered header with dropdown in status area"""
        # Main container with gradient-like effect
        main_frame = tk.Frame(self.root, bg='#0a0a0f')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # CLEAN Header section - NO dropdown interference
        header_frame = tk.Frame(main_frame, bg='#0a0a0f')
        header_frame.pack(fill=tk.X, pady=(0, 35))
        
        # CENTERED LOGO AND TEXT SECTION - Clean and elegant
        center_frame = tk.Frame(header_frame, bg='#0a0a0f')
        center_frame.pack(expand=True)  # This centers the content
        
        # Logo and title container - centered
        logo_title_frame = tk.Frame(center_frame, bg='#0a0a0f')
        logo_title_frame.pack()
        
        # Load and display logo - centered
        self.logo_image = self.load_logo_image()
        if self.logo_image:
            logo_label = tk.Label(
                logo_title_frame,
                image=self.logo_image,
                bg='#0a0a0f'
            )
            logo_label.pack(side=tk.LEFT, padx=(0, 20))
        
        # Title and subtitle container - centered
        text_container = tk.Frame(logo_title_frame, bg='#0a0a0f')
        text_container.pack(side=tk.LEFT)
        
        # Enhanced title - centered
        title_label = tk.Label(
            text_container, 
            text="ChiraagAI Assistant", 
            font=self.title_font, 
            fg="#ffffff", 
            bg='#0a0a0f'
        )
        title_label.pack()
        
        # Enhanced subtitle - centered
        subtitle_label = tk.Label(
            text_container, 
            text="🚀 Powered by Murf TTS and Gemini AI", 
            font=self.subtitle_font, 
            fg="#64b5f6", 
            bg='#0a0a0f'
        )
        subtitle_label.pack(pady=(8, 0))
        
        # Decorative line below header with cool gradient effect
        separator_frame = tk.Frame(header_frame, bg='#0a0a0f', height=6)
        separator_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Multiple thin lines for gradient effect
        tk.Frame(separator_frame, height=1, bg='#1e88e5').pack(fill=tk.X)
        tk.Frame(separator_frame, height=1, bg='#42a5f5').pack(fill=tk.X, pady=(1, 0))
        tk.Frame(separator_frame, height=1, bg='#64b5f6').pack(fill=tk.X, pady=(1, 0))
        
        # ENHANCED Status section with VOICE DROPDOWN integrated
        status_frame = tk.Frame(main_frame, bg='#0a0a0f')
        status_frame.pack(fill=tk.X, pady=(0, 25))
        
        # Status container with voice dropdown on the right
        status_container = tk.Frame(status_frame, bg='#1a1a24', relief="flat", bd=0)
        status_container.pack(fill=tk.X, pady=5, padx=10)
        
        # Status content frame to hold both status and dropdown
        status_content_frame = tk.Frame(status_container, bg='#1a1a24')
        status_content_frame.pack(fill=tk.X, padx=20, pady=15)
        
        # Left side - Status label
        self.status_label = tk.Label(
            status_content_frame, 
            text="● Ready to control your system", 
            font=self.status_font, 
            fg="#4caf50", 
            bg='#1a1a24'
        )
        self.status_label.pack(side=tk.LEFT)
        
        # Right side - VOICE DROPDOWN (perfectly positioned)
        voice_dropdown_frame = tk.Frame(status_content_frame, bg='#1a1a24')
        voice_dropdown_frame.pack(side=tk.RIGHT)
        
        # Voice selection label - compact
        voice_label = tk.Label(
            voice_dropdown_frame, 
            text="🎵 Voice:", 
            bg='#1a1a24', 
            fg="#64b5f6", 
            font=("Segoe UI", 10, "bold")
        )
        voice_label.pack(side=tk.LEFT, padx=(0, 8))
        
        # MURF VOICE DROPDOWN - PERFECTLY STYLED
        self.voice_var = tk.StringVar(value="en-US-marcus")
        
        # Valid Murf voice options (15 voices as requested)
        voice_options = [
            ("Marcus (US Male)", "en-US-marcus"),
            ("Natalie (US Female)", "en-US-natalie"),
            ("Amara (US Female)", "en-US-amara"),
            ("Charles (US Male)", "en-US-charles"),
            ("Freddie (UK Male)", "en-UK-freddie"),
            ("Emma (UK Female)", "en-UK-emma"),
            ("Oliver (UK Male)", "en-UK-oliver"),
            ("Sarah (US Female)", "en-US-sarah"),
            ("David (UK Male)", "en-UK-david"),
            ("Sophie (UK Female)", "en-UK-sophie"),
            ("Alex (US Male)", "en-US-alex"),
            ("Lily (US Female)", "en-US-lily"),
            ("James (UK Male)", "en-UK-james"),
            ("Grace (UK Female)", "en-UK-grace"),
            ("Ryan (US Male)", "en-US-ryan")
        ]
        
        # COOL STYLED DROPDOWN - Integrated with status bar
        self.voice_menu = tk.OptionMenu(voice_dropdown_frame, self.voice_var, *[option[1] for option in voice_options])
        self.voice_menu.config(
            bg="#2a2a3e",          # Slightly lighter than status bar
            fg="#64b5f6",          # Light blue text
            font=("Segoe UI", 9, "bold"),  # Compact font
            activebackground="#363651",    # Darker on hover
            activeforeground="#81c784",    # Green text on hover
            relief="raised",       # Slight raise for visibility
            borderwidth=1,         # Subtle border
            highlightthickness=0,  # No extra highlight
            pady=4,                # Compact padding
            padx=10,               # Compact padding
            cursor="hand2",
            width=13,              # Compact width
            anchor="w"             # Left align text
        )
        
        # Dropdown menu styling
        self.voice_menu["menu"].config(
            bg="#2a2a3e",          # Match button background
            fg="#e8eaed",          # Light text
            font=("Segoe UI", 9, "normal"),
            activebackground="#64b5f6",  # Blue selection
            activeforeground="#000000",  # Black text on selection
            bd=1,
            relief="solid",
            tearoff=0,
            selectcolor="#81c784"  # Green checkmark
        )
        
        # Clear existing menu and add options with display names
        menu = self.voice_menu["menu"]
        menu.delete(0, "end")
        
        for display_name, voice_id in voice_options:
            menu.add_command(
                label=display_name,
                command=lambda value=voice_id: self.voice_var.set(value)
            )
        
        self.voice_menu.pack(side=tk.LEFT)
        
        # ENHANCED Conversation section with modern styling
        conversation_frame = tk.Frame(main_frame, bg='#0a0a0f')
        conversation_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 25))
        
        # Conversation container with border effect
        conv_container = tk.Frame(conversation_frame, bg='#1976d2', relief="flat", bd=2)
        conv_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        inner_conv_frame = tk.Frame(conv_container, bg='#0a1420')
        inner_conv_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=3)
        
        self.conversation_display = scrolledtext.ScrolledText(
            inner_conv_frame,
            height=14,
            width=75,
            bg="#0a1420",
            fg="#e8eaed",
            font=self.conversation_font,
            wrap=tk.WORD,
            selectbackground="#1976d2",
            selectforeground="#ffffff",
            insertbackground="#64b5f6",
            relief="flat",
            borderwidth=0,
            padx=20,
            pady=15,
            state=tk.DISABLED
        )
        self.conversation_display.pack(fill=tk.BOTH, expand=True)
        
        # ENHANCED Control buttons with modern styling
        controls_frame = tk.Frame(main_frame, bg='#0a0a0f')
        controls_frame.pack(fill=tk.X, pady=(0, 25))
        
        button_container = tk.Frame(controls_frame, bg='#0a0a0f')
        button_container.pack()
        
        # Enhanced button styling
        self.voice_button = tk.Button(
            button_container,
            text="🎤  Start Listening",
            font=self.button_font,
            bg="#1976d2",
            fg="white",
            activebackground="#1565c0",
            activeforeground="white",
            relief="flat",
            padx=30,
            pady=15,
            cursor="hand2",
            command=self.toggle_listening,
            bd=0,
            highlightthickness=0
        )
        self.voice_button.pack(side=tk.LEFT, padx=(0, 20))
        
        text_button = tk.Button(
            button_container,
            text="💬  Type Command",
            font=self.button_font,
            bg="#388e3c",
            fg="white",
            activebackground="#2e7d32",
            activeforeground="white",
            relief="flat",
            padx=30,
            pady=15,
            cursor="hand2",
            command=self.open_text_input,
            bd=0,
            highlightthickness=0
        )
        text_button.pack(side=tk.LEFT, padx=(0, 20))
        
        clear_button = tk.Button(
            button_container,
            text="🗑️  Clear Chat",
            font=self.button_font,
            bg="#d32f2f",
            fg="white",
            activebackground="#c62828",
            activeforeground="white",
            relief="flat",
            padx=30,
            pady=15,
            cursor="hand2",
            command=self.clear_conversation,
            bd=0,
            highlightthickness=0
        )
        clear_button.pack(side=tk.LEFT)
        
        # Footer section
        footer_frame = tk.Frame(main_frame, bg='#0a0a0f')
        footer_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Status info
        automation_label = tk.Label(
            footer_frame, 
            text="🤖 Ready to automate your daily tasks", 
            bg='#0a0a0f', 
            fg="#4caf50", 
            font=self.label_font
        )
        automation_label.pack()
        
        # Enhanced welcome message
        self.add_to_conversation("ChiraagAI", "🚀 Welcome to ChiraagAI! How may I assist you today?")

    def add_to_conversation(self, speaker, message):
        """FIXED: Add message with read-only protection"""
        self.conversation_display.config(state=tk.NORMAL)  # Temporarily enable for writing
        
        timestamp = time.strftime("%H:%M:%S")
        
        # Enhanced color coding for different speakers
        if speaker == "ChiraagAI":
            speaker_color = "#64b5f6"
            message_color = "#ffffff"
        elif speaker == "You" or speaker.startswith("You ("):
            speaker_color = "#4caf50"
            message_color = "#e8f5e8"
        elif speaker == "System":
            speaker_color = "#ff9800"
            message_color = "#ffcc80"
        elif speaker == "ChiraagAI (AI Generated)":
            speaker_color = "#e91e63"
            message_color = "#f8bbd9"
        elif speaker == "ChiraagAI (Generated)":
            speaker_color = "#9c27b0"
            message_color = "#e1bee7"
        else:
            speaker_color = "#ff9800"
            message_color = "#ffcdd2"
        
        # Insert timestamp and speaker with color
        self.conversation_display.insert(tk.END, f"[{timestamp}] ", "timestamp")
        self.conversation_display.insert(tk.END, f"{speaker}: ", "speaker")
        self.conversation_display.insert(tk.END, f"{message}\n\n", "message")
        
        # Configure enhanced text tags for coloring
        self.conversation_display.tag_config("timestamp", foreground="#78909c", font=self.conversation_font)
        self.conversation_display.tag_config("speaker", foreground=speaker_color, font=self.conversation_font)
        self.conversation_display.tag_config("message", foreground=message_color, font=self.conversation_font)
        
        self.conversation_display.config(state=tk.DISABLED)  # FIXED: Make read-only again
        self.conversation_display.see(tk.END)
        
        # Add to conversation history for Gemini context
        self.conversation_history.append({"role": speaker.lower(), "content": message})

    # ================= NEW TTS AND TYPING EFFECT METHODS =================
    
    def start_murf_speech_async(self, text: str) -> bool:
        """Fetch TTS from Murf, start playback immediately, and return True on success."""
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
                pygame.mixer.init()

            url = "https://api.murf.ai/v1/speech/generate"
            headers = {
                "Content-Type": "application/json",
                "api-key": self.murf_api_key
            }
            payload = {
                "voiceId": self.voice_var.get(),
                "style": "Conversational",
                "text": text,
                "rate": 0,
                "pitch": 0,
                "sampleRate": 48000,
                "format": "MP3",
                "pronunciationDictionary": {},
                "encodeAsBase64": False
            }

            # Call Murf (blocking – a few 100 ms normally)
            res = requests.post(url, headers=headers, json=payload, timeout=15)
            if res.status_code != 200:
                if self.debug_mode:
                    print(f"[TTS] Murf HTTP {res.status_code}")
                return False

            audio_url = res.json().get("audioFile")
            if not audio_url:
                if self.debug_mode:
                    print("[TTS] audioFile missing")
                return False

            audio_bin = requests.get(audio_url, timeout=15).content
            pygame.mixer.music.load(BytesIO(audio_bin))
            pygame.mixer.music.play()           # <-- playback starts here
            
            # DISABLE BUTTONS when speech starts
            self.root.after(0, self.disable_buttons_during_speech)
            self.root.after(0, self.status_label.configure,
                            {"text": "● Speaking...", "fg": "#4caf50"})
            return True

        except Exception as exc:
            if self.debug_mode:
                print(f"[TTS] error: {exc}")
            return False


    def start_typing_effect(self, speaker: str, message: str):
        """Create a new entry in the chat and reveal `message` progressively."""
        ts = time.strftime("%H:%M:%S")

        # colour scheme
        if speaker == "ChiraagAI":
            speaker_colour, msg_colour = "#64b5f6", "#ffffff"
        else:
            speaker_colour, msg_colour = "#4caf50", "#e8f5e8"

        self.conversation_display.config(state=tk.NORMAL)
        self.conversation_display.insert(tk.END, f"[{ts}] ", ("timestamp",))
        self.conversation_display.insert(tk.END, f"{speaker}: ", ("speaker",))

        self.conversation_display.tag_config("timestamp", foreground="#78909c",
                                             font=self.conversation_font)
        self.conversation_display.tag_config("speaker", foreground=speaker_colour,
                                             font=self.conversation_font)
        self.conversation_display.tag_config("chatmsg", foreground=msg_colour,
                                             font=self.conversation_font)

        # kick-off incremental reveal
        self._type_message_step(message, 0)
        self.conversation_display.config(state=tk.DISABLED)
        self.conversation_display.see(tk.END)

    def _type_message_step(self, message: str, idx: int):
        """Recursive helper – appends one character and reschedules itself."""
        if idx < len(message):
            self.conversation_display.config(state=tk.NORMAL)
            self.conversation_display.insert(tk.END, message[idx], ("chatmsg",))
            self.conversation_display.config(state=tk.DISABLED)
            self.conversation_display.see(tk.END)

            char = message[idx]
            delay = 30 if char not in " .,!?;:\n" else 120
            self.root.after(delay, self._type_message_step, message, idx + 1)
        else:
            # finished typing
            self.conversation_display.config(state=tk.NORMAL)
            self.conversation_display.insert(tk.END, "\n\n", ("chatmsg",))
            self.conversation_display.config(state=tk.DISABLED)
            self.conversation_history.append({"role": "assistant", "content": message})
            # keep checking until audio stops
            self._poll_audio_done()

    def _poll_audio_done(self):
        """Set status back to 'Ready' as soon as the speech is finished."""
        if pygame.mixer.music.get_busy():
            self.root.after(300, self._poll_audio_done)
        else:
            # RE-ENABLE BUTTONS when speech finishes
            self.enable_buttons_after_speech()
            self.status_label.configure(text="● Ready to control your system",
                                        fg="#4caf50")


    def provide_voice_feedback(self, text: str):
        """Begin speaking `text` and display it with typing effect once audio starts."""
        def worker():
            success = self.start_murf_speech_async(text)
            if success:
                # show text immediately after playback begins
                self.root.after(0, self.start_typing_effect, "ChiraagAI", text)
            else:
                # fall-back: show instantly (no typing), mark failure
                self.root.after(0, self.add_to_conversation,
                                "System",
                                f"⚠️  Couldn't play audio – here's the text:\n{text}")

        threading.Thread(target=worker, daemon=True).start()

    # ================= END OF NEW METHODS =================
    
    def toggle_listening(self):
        """Toggle voice listening on/off"""
        if not self.is_listening:
            self.start_listening()
        else:
            self.stop_listening()
    
    def start_listening(self):
        """Start listening for voice commands"""
        self.is_listening = True
        self.voice_button.configure(text="🛑  Stop Listening", bg="#d32f2f", activebackground="#c62828")
        self.status_label.configure(text="● Listening for commands...", fg="#ff9800")
        
        threading.Thread(target=self.listen_for_speech, daemon=True).start()
    
    def stop_listening(self):
        """Stop listening for voice commands"""
        self.is_listening = False
        self.voice_button.configure(text="🎤  Start Listening", bg="#1976d2", activebackground="#1565c0")
        self.status_label.configure(text="● Ready to control your system", fg="#4caf50")
    
    def listen_for_speech(self):
        """Listen for speech input with auto-reset functionality"""
        try:
            with self.microphone as source:
                audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=5)
            
            self.root.after(0, self.stop_listening)
            
            self.status_label.configure(text="● Processing command...", fg="#2196f3")
            text = self.recognizer.recognize_google(audio)
            
            self.add_to_conversation("You", text)
            self.process_user_input(text)
            
        except sr.WaitTimeoutError:
            if self.is_listening:
                threading.Thread(target=self.listen_for_speech, daemon=True).start()
        except sr.UnknownValueError:
            self.root.after(0, self.stop_listening)
            self.status_label.configure(text="● Could not understand command", fg="#f44336")
            time.sleep(2)
            self.status_label.configure(text="● Ready to control your system", fg="#4caf50")
        except sr.RequestError as e:
            self.root.after(0, self.stop_listening)
            self.status_label.configure(text=f"● Speech recognition error: {e}", fg="#f44336")
    
    def open_text_input(self):
        """Enhanced text input dialog with Enter key support"""
        text_input = tk.Toplevel(self.root)
        text_input.title("Type Your Command")
        text_input.geometry("520x320")
        text_input.configure(bg='#0a0a0f')
        text_input.resizable(False, False)
        
        text_input.transient(self.root)
        text_input.grab_set()
        
        main_frame = tk.Frame(text_input, bg='#0a0a0f')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        tk.Label(
            main_frame,
            text="💬 Enter your command or request:", 
            bg='#0a0a0f', 
            fg="white", 
            font=self.subtitle_font
        ).pack(pady=(0, 20))
        
        text_entry = tk.Text(
            main_frame, 
            height=8, 
            width=50, 
            bg="#1a1a24", 
            fg="#e8eaed", 
            font=self.conversation_font,
            relief="flat",
            borderwidth=0,
            padx=20,
            pady=15,
            selectbackground="#1976d2",
            selectforeground="#ffffff",
            insertbackground="#64b5f6"
        )
        text_entry.pack(pady=(0, 25), fill=tk.BOTH, expand=True)
        text_entry.focus()
        
        def submit_text():
            user_text = text_entry.get("1.0", tk.END).strip()
            if user_text:
                self.add_to_conversation("You", user_text)
                self.process_user_input(user_text)
            text_input.destroy()
        
        def on_enter_key(event):
            # Check if Ctrl is held down
            if event.state & 0x4:  # Ctrl+Enter for new line
                return  # Allow default behavior (new line)
            else:  # Plain Enter submits
                submit_text()
                return "break"  # Prevent default Enter behavior
        
        def on_escape_key(event):
            text_input.destroy()
            return "break"
        
        # Bind keyboard events
        text_entry.bind("<Return>", on_enter_key)
        text_entry.bind("<Escape>", on_escape_key)
        text_input.bind("<Escape>", on_escape_key)
        
        button_frame = tk.Frame(main_frame, bg='#0a0a0f')
        button_frame.pack()
        
        tk.Button(
            button_frame,
            text="🚀 Execute Command",
            command=submit_text,
            bg="#1976d2",
            fg="white",
            font=self.button_font,
            activebackground="#1565c0",
            activeforeground="white",
            relief="flat",
            padx=25,
            pady=12,
            cursor="hand2",
            bd=0
        ).pack(side=tk.LEFT, padx=(0, 15))
        
        tk.Button(
            button_frame,
            text="❌ Cancel",
            command=text_input.destroy,
            bg="#424242",
            fg="white",
            font=self.button_font,
            activebackground="#303030",
            activeforeground="white",
            relief="flat",
            padx=25,
            pady=12,
            cursor="hand2",
            bd=0
        ).pack(side=tk.LEFT)
        
        # Add visual feedback
        instruction_label = tk.Label(
            main_frame,
            text="💡 Tip: Press Enter to execute, Ctrl+Enter for new line, Escape to cancel",
            bg='#0a0a0f',
            fg="#64b5f6",
            font=("Segoe UI", 9)
        )
        instruction_label.pack(pady=(5, 0))
    
    def process_user_input(self, user_input):
        """Enhanced: Process user input - detect email content requests vs system commands"""
        self.status_label.configure(text="● Analyzing command...", fg="#2196f3")
        
        # Check if we're in email input mode and this is content generation
        if self.email_input_mode:
            # This is email content - either direct dictation or content generation request
            threading.Thread(target=self.handle_email_content_input, args=(user_input,), daemon=True).start()
        else:
            # Normal command processing
            threading.Thread(target=self.analyze_and_execute_command, args=(user_input,), daemon=True).start()
    
    def handle_email_content_input(self, user_input):
        """RESTORED: Handle email content - either direct typing or AI generation"""
        try:
            # Check if it's a content generation request
            generation_keywords = [
                'write application', 'write email', 'compose', 'draft', 'generate',
                'write letter', 'write message', 'create email', 'write request',
                'write complaint', 'write resignation', 'write proposal', 'write report',
                'write invitation', 'write thank you', 'write apology', 'write follow up',
                'write meeting', 'write announcement', 'write reminder'
            ]
            
            is_generation_request = any(keyword in user_input.lower() for keyword in generation_keywords)
            
            if is_generation_request:
                if self.debug_mode:
                    print(f"DEBUG: Email content generation requested: {user_input}")
                
                self.root.after(0, self.add_to_conversation, "You (Email Request)", user_input)
                self.root.after(0, self.status_label.configure, {"text": "● Generating email with Gemini AI...", "fg": "#9c27b0"})
                
                # Generate email content using Gemini
                self.generate_email_content_with_gemini(user_input)
            else:
                if self.debug_mode:
                    print(f"DEBUG: Direct email dictation: {user_input}")
                
                # Direct dictation - type as-is
                self.process_email_content(user_input)
                
        except Exception as e:
            error_msg = f"Email content handling error: {str(e)}"
            if self.debug_mode:
                print(f"ERROR: {error_msg}")
            self.root.after(0, self.add_to_conversation, "System", f"❌ {error_msg}")
            self.stop_email_input_mode()

    def generate_email_content_with_gemini(self, content_request):
        """RESTORED: Generate professional email content using Gemini AI"""
        try:
            # Create a specialized prompt for email generation
            email_prompt = f"""You are a professional email writing assistant. Generate a complete, well-structured email based on this request:

REQUEST: {content_request}

Generate a professional email that includes:
1. Appropriate greeting
2. Clear, concise body text
3. Professional closing
4. Proper formatting

Make it appropriate, polite, and ready to send. Do not include subject line suggestions or metadata - just the email body content that can be typed directly into the compose window.

Email content:"""

            # Generate with enhanced email config
            response = self.chat_session.send_message(email_prompt, generation_config=self.email_generation_config)
            generated_content = response.text.strip()
            
            if self.debug_mode:
                print(f"DEBUG: Generated email content: {generated_content}")
            
            # Clean up the response
            cleaned_content = self.clean_email_content(generated_content)
            
            # Type the generated content
            self.root.after(0, self.type_generated_email_content, cleaned_content)
            
        except Exception as e:
            error_msg = f"Email generation error: {str(e)}"
            if self.debug_mode:
                print(f"ERROR: {error_msg}")
            self.root.after(0, self.add_to_conversation, "System", f"❌ {error_msg}")
            self.stop_email_input_mode()

    def type_generated_email_content(self, email_content):
        """ENHANCED: Type generated email, then add conversation entry AFTER typing"""
        try:
            if self.debug_mode:
                print(f"DEBUG: Typing generated email content")
            
            self.status_label.configure(text="● Typing generated email...", fg="#ff9800")
            
            # Ensure we're focused on the compose window
            pyautogui.click()
            time.sleep(0.5)
            
            # Clear any existing content
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.3)
            
            # Type the generated content using lightning fast method
            self.type_lightning_fast(email_content)
            time.sleep(0.5)
            
            # IMPROVED: Only add conversation AFTER typing is complete
            preview = email_content[:100] + "..." if len(email_content) > 100 else email_content
            success_msg = f"✅ Generated email typed successfully!\n\nPreview: {preview}\n\n(Review and send manually)"
            
            self.add_to_conversation("ChiraagAI (Generated)", success_msg)
            
            # NO voice feedback for generated content to avoid interruption
            # Stop email input mode
            self.stop_email_input_mode()
            
            if self.debug_mode:
                print(f"DEBUG: Generated email typing completed")
            
        except Exception as e:
            error_msg = f"Generated email typing error: {str(e)}"
            if self.debug_mode:
                print(f"ERROR: {error_msg}")
            self.add_to_conversation("System", f"❌ {error_msg}")
            self.stop_email_input_mode()

    def generate_and_type_email_direct(self, request_text):
        """STREAMLINED: Generate email with AI and type immediately - no dictation"""
        try:
            if self.debug_mode:
                print(f"DEBUG: Direct AI email generation for: {request_text}")
            
            self.root.after(0, self.status_label.configure, {"text": "● Generating email with Gemini AI...", "fg": "#e91e63"})
            
            # Create email generation prompt
            email_prompt = f"""Generate a complete, professional email based on this request: {request_text}

Write a business-appropriate email that includes:
- Professional greeting
- Clear, concise body content  
- Appropriate closing
- Proper formatting

Make it ready to send. Only return the email body content - no subject lines or metadata.

Email content:"""

            # Generate with Gemini AI
            response = self.chat_session.send_message(email_prompt, generation_config=self.email_generation_config)
            generated_content = response.text.strip()
            
            if self.debug_mode:
                print(f"DEBUG: Generated content: {generated_content}")
            
            # Clean the content
            cleaned_content = self.clean_email_content(generated_content)
            
            # Type immediately - cursor already in body field
            self.root.after(0, self.status_label.configure, {"text": "● Typing generated email...", "fg": "#ff9800"})
            
            # Type at lightning speed
            self.type_lightning_fast(cleaned_content)
            
            # Success feedback ONLY after typing is complete
            preview = cleaned_content[:100] + "..." if len(cleaned_content) > 100 else cleaned_content
            success_msg = f"✅ Email generated and typed!\n\nPreview: {preview}\n\n(Review and send manually)"
            
            self.root.after(0, self.add_to_conversation, "ChiraagAI (AI Generated)", f"✨ Generated email for: '{request_text}'")
            self.root.after(0, self.add_to_conversation, "ChiraagAI", success_msg)
            
            # Exit email mode
            self.exit_email_mode()
            
        except Exception as e:
            error_msg = f"Email AI generation error: {str(e)}"
            if self.debug_mode:
                print(f"ERROR: {error_msg}")
            self.root.after(0, self.add_to_conversation, "System", f"❌ {error_msg}")
            self.exit_email_mode()
    
    def clean_email_content(self, content):
        """Clean and format generated email content"""
        try:
            # Remove markdown formatting
            content = content.replace('**', '').replace('*', '')
            
            # Remove JSON structures
            content = re.sub(r'\{[^}]*\}', '', content)
            
            # Clean up extra newlines
            content = re.sub(r'\n\s*\n', '\n\n', content)
            
            # Remove system instructions
            lines = content.split('\n')
            cleaned_lines = []
            
            for line in lines:
                line = line.strip()
                if line and not line.startswith('Subject:') and not line.startswith('Requirements:'):
                    cleaned_lines.append(line)
            
            cleaned_content = '\n'.join(cleaned_lines).strip()
            return cleaned_content
            
        except Exception as e:
            if self.debug_mode:
                print(f"ERROR in clean_email_content: {e}")
            return content
    
    def extract_json_from_response(self, ai_response):
        """FIXED: Extract FIRST JSON object only, ignore extras"""
        try:
            # Remove markdown code blocks first
            cleaned_response = ai_response.replace("``````", "").strip()
            
            # Find the first complete JSON object
            start_idx = cleaned_response.find('{')
            if start_idx == -1:
                return cleaned_response
            
            # Find the matching closing brace
            brace_count = 0
            end_idx = start_idx
            
            for i in range(start_idx, len(cleaned_response)):
                if cleaned_response[i] == '{':
                    brace_count += 1
                elif cleaned_response[i] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        end_idx = i
                        break
            
            # Extract only the first JSON object
            first_json = cleaned_response[start_idx:end_idx+1]
            
            if self.debug_mode:
                print(f"DEBUG: Extracted first JSON: {first_json}")
            
            return first_json
            
        except Exception as e:
            if self.debug_mode:
                print(f"DEBUG: JSON extraction error: {e}")
            return ai_response.strip()
    
    def analyze_and_execute_command(self, user_input):
        """ENHANCED: Better analysis with improved question detection and chat responses"""
        try:
            # Enhanced question detection patterns
            explanation_patterns = [
                'explain', 'what is', 'what are', 'what do you mean', 'tell me about',
                'describe', 'define', 'how does', 'how do', 'why does', 'why do',
                'what does', 'can you explain', 'help me understand', 'what means',
                'meaning of', 'definition of', 'elaborate on', 'clarify', 'teach'
            ]
            
            question_patterns = [
                'who is', 'who are', 'when is', 'when was', 'where is', 'where are',
                'which is', 'which are', 'how much', 'how many', 'what time',
                'what year', 'what happened', 'why is', 'why are'
            ]
            
            # Check if it's a general question/explanation request
            user_lower = user_input.lower()
            is_explanation = any(pattern in user_lower for pattern in explanation_patterns)
            is_question = any(pattern in user_lower for pattern in question_patterns)
            
            # System command detection
            system_keywords = [
                'open', 'launch', 'start', 'run', 'search youtube', 'search google',
                'screenshot', 'take screenshot', 'write email', 'send email',
                'compose email', 'gmail'
            ]
            is_system_command = any(keyword in user_lower for keyword in system_keywords)
            
            if is_explanation or (is_question and not is_system_command):
                # Handle as direct conversation - provide explanation in chat
                if self.debug_mode:
                    print(f"DEBUG: Detected explanation/question request: {user_input}")
                
                self.status_label.configure(text="● Generating explanation...", fg="#9c27b0")
                
                # Create explanation prompt for Gemini
                explanation_prompt = f"""You are ChiraagAI assistant. The user asked: "{user_input}"

Provide a clear, helpful explanation directly. Be conversational but informative. Keep it concise (under 80-100 words) but comprehensive enough to answer their question properly.

Response:"""
                
                response = self.chat_session.send_message(explanation_prompt, generation_config=self.generation_config)
                ai_response = response.text.strip()
                
                # UPDATED: Use new voice feedback method
                self.provide_voice_feedback(ai_response)
                
                self.status_label.configure(text="● Ready to control your system", fg="#4caf50")
                return
            
            # Continue with existing system command logic
            system_prompt = """You are ChiraagAI. Respond with EXACTLY ONE JSON object for system commands, no extra text:

For system commands, respond with ONLY this format:
{"action": "SYSTEM_COMMAND", "task": "TASK_TYPE", "target": "EXACT_QUERY", "details": "description"}

Task types: open_website, open_app, search_youtube, search_google, take_screenshot, write_email

Examples:
"write email" -> {"action": "SYSTEM_COMMAND", "task": "write_email", "target": "compose", "details": "compose new email"}
"send email to john" -> {"action": "SYSTEM_COMMAND", "task": "write_email", "target": "john", "details": "compose email to john"}
"search cats on youtube" -> {"action": "SYSTEM_COMMAND", "task": "search_youtube", "target": "cats", "details": "search for cats on youtube"}
"open youtube" -> {"action": "SYSTEM_COMMAND", "task": "open_website", "target": "youtube", "details": "open youtube.com"}

For general chat, respond normally (under 80 words). DO NOT include JSON for chat responses."""
            
            full_prompt = f"{system_prompt}\n\nUser Request: {user_input}\n\nResponse:"
            
            response = self.chat_session.send_message(full_prompt, generation_config=self.generation_config)
            ai_response = response.text.strip()
            
            if self.debug_mode:
                print(f"DEBUG: AI Response: {ai_response}")
            
            # FIXED: Extract only the first JSON object
            json_content = self.extract_json_from_response(ai_response)
            
            try:
                command_data = json.loads(json_content)
                if self.debug_mode:
                    print(f"DEBUG: Parsed JSON: {command_data}")
                
                # FIXED: Only provide voice feedback for valid system commands, no JSON reading
                if command_data.get("action") == "SYSTEM_COMMAND":
                    target = command_data.get("target", "")
                    task = command_data.get("task", "")
                    
                    if task == "search_youtube":
                        speak_text = f"Searching YouTube for {target}"
                    elif task == "search_google":
                        speak_text = f"Searching Google for {target}"
                    elif task == "take_screenshot":
                        speak_text = "Taking screenshot now"
                    elif task == "open_website":
                        speak_text = f"Opening {target}"
                    elif task == "write_email":
                        if target == "compose":
                            speak_text = "Opening Gmail for email composition"
                        else:
                            speak_text = f"Opening Gmail to compose email to {target}"
                    else:
                        speak_text = f"Opening {target}"
                    
                    # UPDATED: Use new voice feedback method
                    self.provide_voice_feedback(speak_text)
                
                self.execute_system_command(command_data, user_input)
                
            except json.JSONDecodeError as je:
                if self.debug_mode:
                    print(f"DEBUG: JSON decode failed: {je}")
                    print(f"DEBUG: Attempted to parse: {json_content}")
                # UPDATED: Use new voice feedback method for regular conversation
                self.provide_voice_feedback(ai_response)
                
        except Exception as e:
            error_message = f"Error processing command: {str(e)}"
            if self.debug_mode:
                print(f"ERROR in analyze_and_execute_command: {error_message}")
            self.root.after(0, self.add_to_conversation, "System", error_message)
            self.root.after(0, self.status_label.configure, {"text": "● Ready to control your system", "fg": "#4caf50"})
    
    def generate_murf_speech_safe(self, text):
        """Standard Murf TTS generation (non-streaming) - KEPT FOR COMPATIBILITY"""
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
                pygame.mixer.init()
            
            url = "https://api.murf.ai/v1/speech/generate"  # Changed from /stream to /generate
            
            headers = {
                "Content-Type": "application/json",
                "api-key": self.murf_api_key
            }
            
            selected_voice = self.voice_var.get()
            
            payload = {
                "voiceId": selected_voice,
                "style": "Conversational",
                "text": text,
                "rate": 0,
                "pitch": 0,
                "sampleRate": 48000,  # Added back sampleRate
                "format": "MP3",
                "pronunciationDictionary": {},  # Added back
                "encodeAsBase64": False  # Added back
            }
            
            self.status_label.configure(text="● Generating speech...", fg="#9c27b0")
            
            response = requests.post(url, headers=headers, json=payload, timeout=15)  # Reduced timeout
            
            if response.status_code == 200:
                response_data = response.json()
                audio_url = response_data.get("audioFile")
                
                if audio_url:
                    audio_response = requests.get(audio_url)
                    
                    if audio_response.status_code == 200:
                        try:
                            audio_bytes = BytesIO(audio_response.content)
                            pygame.mixer.music.load(audio_bytes)
                            pygame.mixer.music.play()
                            
                            # Wait for audio to finish
                            while pygame.mixer.music.get_busy():
                                time.sleep(0.1)
                            
                            self.status_label.configure(text="● Ready with TTS", fg="#4caf50")
                        except pygame.error as pe:
                            if self.debug_mode:
                                print(f"Pygame audio error: {pe}")
                else:
                    if self.debug_mode:
                        print("No audio URL received")
            else:
                if self.debug_mode:
                    print(f"Murf API error: {response.status_code}")
                    
        except Exception as e:
            if self.debug_mode:
                print(f"Safe TTS error: {e}")
            self.status_label.configure(text="● Ready with TTS", fg="#4caf50")
    
    def execute_system_command(self, command_data, original_input):
        """Execute system commands with ENHANCED EMAIL support"""
        try:
            action = command_data.get("action", "")
            if action == "SYSTEM_COMMAND":
                task = command_data.get("task", "")
                target = command_data.get("target", "")
                details = command_data.get("details", "")
                
                if self.debug_mode:
                    print(f"DEBUG: Executing - Task: {task}, Target: {target}")
                
                if task == "open_app":
                    self.open_application_lightning_fast(target, original_input)
                elif task == "open_website":
                    self.open_website_lightning_fast(target, original_input)
                elif task == "search_youtube":
                    self.search_youtube_lightning_fast(target, original_input)
                elif task == "search_google":
                    self.search_google_lightning_fast(target, original_input)
                elif task == "take_screenshot":
                    self.take_screenshot_fixed(original_input)
                elif task == "write_email":  # Enhanced email functionality
                    if "alternative" in original_input.lower() or "direct" in original_input.lower():
                        self.write_email_alternative(target, original_input)
                    else:
                        self.write_email_streamlined(target, original_input)
                
        except Exception as e:
            error_msg = f"Command execution error: {str(e)}"
            if self.debug_mode:
                print(f"ERROR in execute_system_command: {error_msg}")
            self.root.after(0, self.add_to_conversation, "System", error_msg)
            self.root.after(0, self.status_label.configure, {"text": "● Ready to control your system", "fg": "#4caf50"})
    
    def write_email_streamlined(self, recipient, original_input):
        """ENHANCED: Direct Gmail opening with shortened wait time"""
        def execute_email():
            try:
                if self.debug_mode:
                    print(f"DEBUG: Enhanced streamlined email composition")
                
                self.root.after(0, self.status_label.configure, {"text": "● Opening Gmail...", "fg": "#ff9800"})
                
                # Force browser open with dummy website method
                webbrowser.open("https://www.google.com")
                time.sleep(1.5)
                
                # Open address bar and navigate to Gmail
                pyautogui.hotkey('ctrl', 'l')
                time.sleep(0.7)
                
                # LIGHTNING FAST: Type Gmail URL
                self.type_lightning_fast("mail.google.com")
                pyautogui.press('enter')
                
                # REDUCED wait for Gmail to load (from 8 to 6 seconds)
                self.root.after(0, self.status_label.configure, {"text": "● Waiting for Gmail to load...", "fg": "#ff9800"})
                time.sleep(6)  # Reduced from 8 seconds
                
                # Open compose
                pyautogui.press('c')
                time.sleep(2)
                
                # Navigate to body field (2 tabs as you mentioned)
                pyautogui.press('tab')  # To field
                time.sleep(0.5)
                pyautogui.press('tab')  # Body field - cursor ready
                time.sleep(0.5)
                
                # Ready for direct AI generation
                self.root.after(0, self.status_label.configure, {"text": "● Gmail ready - AI mode active!", "fg": "#2196f3"})
                self.root.after(0, self.add_to_conversation, "ChiraagAI", "✨ Gmail compose ready! Tell me what email to generate (e.g., 'sick leave application', 'meeting request')")
                
                # Enable direct AI mode (no dictation)
                self.enable_direct_ai_mode()
                
            except Exception as e:
                error_msg = f"Gmail setup failed: {str(e)}"
                if self.debug_mode:
                    print(f"ERROR: {error_msg}")
                self.root.after(0, self.add_to_conversation, "System", f"❌ {error_msg}")
                self.root.after(0, self.status_label.configure, {"text": "● Ready to control your system", "fg": "#4caf50"})
        
        threading.Thread(target=execute_email, daemon=True).start()

    def write_email_lightning_fast(self, recipient, original_input):
        """RESTORED: Lightning-fast email composition with better Gmail handling"""
        def execute_email():
            try:
                if self.debug_mode:
                    print(f"DEBUG: Enhanced email composition for: '{recipient}'")
                
                self.root.after(0, self.status_label.configure, {"text": "● Opening Gmail...", "fg": "#ff9800"})
                
                # Force browser open with dummy website method
                webbrowser.open("https://www.google.com")
                time.sleep(1.5)  # Slightly longer wait
                
                # Open address bar and navigate to Gmail
                pyautogui.hotkey('ctrl', 'l')
                time.sleep(0.7)  # More time for address bar
                
                # LIGHTNING FAST: Type Gmail URL
                self.type_lightning_fast("mail.google.com")
                pyautogui.press('enter')
                
                # REDUCED wait for Gmail to fully load (from 8 to 6 seconds)
                self.root.after(0, self.status_label.configure, {"text": "● Waiting for Gmail to fully load...", "fg": "#ff9800"})
                time.sleep(6)  # Reduced from 8 seconds
                
                # Multiple attempts to open compose
                compose_opened = False
                for attempt in range(3):
                    try:
                        if self.debug_mode:
                            print(f"DEBUG: Compose attempt {attempt + 1}")
                        
                        # Try keyboard shortcut first
                        pyautogui.press('c')
                        time.sleep(2)
                        
                        # Alternative: Try clicking compose button
                        # Look for compose button and click it
                        pyautogui.hotkey('ctrl', 'shift', 'c')  # Alternative Gmail shortcut
                        time.sleep(2)
                        
                        # Check if compose window opened by trying to focus on it
                        pyautogui.press('tab')  # Tab to navigate in compose window
                        time.sleep(1)
                        
                        compose_opened = True
                        break
                        
                    except Exception as e:
                        if self.debug_mode:
                            print(f"DEBUG: Compose attempt {attempt + 1} failed: {e}")
                        time.sleep(2)
                
                if not compose_opened:
                    # Final attempt with different approach
                    self.root.after(0, self.add_to_conversation, "System", "⚠️ Trying alternative compose method...")
                    
                    # Try pressing 'c' multiple times
                    for i in range(3):
                        pyautogui.press('c')
                        time.sleep(1)
                    
                    time.sleep(2)
                
                # Move to email body (skip To and Subject fields)
                pyautogui.press('tab')  # To field
                time.sleep(0.5)
                pyautogui.press('tab')  # Subject field
                time.sleep(0.5)
                pyautogui.press('tab')  # Body field
                time.sleep(0.5)
                
                self.root.after(0, self.status_label.configure, {"text": "● Gmail compose ready!", "fg": "#2196f3"})
                self.root.after(0, self.add_to_conversation, "ChiraagAI", "Gmail compose window is ready! Email body is focused. Say 'write [type] email' for AI generation or dictate directly.")
                
                # Auto-enable microphone for email content input
                self.auto_enable_email_input()
                
            except Exception as e:
                error_msg = f"Gmail setup failed: {str(e)}"
                if self.debug_mode:
                    print(f"ERROR: {error_msg}")
                self.root.after(0, self.add_to_conversation, "System", f"❌ {error_msg}")
                self.root.after(0, self.status_label.configure, {"text": "● Ready to control your system", "fg": "#4caf50"})
        
        threading.Thread(target=execute_email, daemon=True).start()

    def write_email_alternative(self, recipient, original_input):
        """RESTORED: Alternative Gmail compose URL opening"""
        def execute_email_alt():
            try:
                if self.debug_mode:
                    print(f"DEBUG: Alternative Gmail compose method")
                
                self.root.after(0, self.status_label.configure, {"text": "● Opening Gmail Compose directly...", "fg": "#ff9800"})
                
                # Open Gmail compose directly
                compose_url = "https://mail.google.com/mail/?view=cm&fs=1&tf=1"
                webbrowser.open(compose_url)
                
                # Wait for page to load - REDUCED from 6 to 4 seconds
                time.sleep(4)
                
                # Focus on email body (usually auto-focused on compose page)
                pyautogui.press('tab')  # Ensure we're in body
                time.sleep(1)
                
                self.root.after(0, self.add_to_conversation, "ChiraagAI", "Gmail compose opened directly! Ready for AI-generated email content.")
                self.auto_enable_email_input()
                
            except Exception as e:
                error_msg = f"Alternative Gmail method failed: {str(e)}"
                self.root.after(0, self.add_to_conversation, "System", f"❌ {error_msg}")
                
        threading.Thread(target=execute_email_alt, daemon=True).start()

    def enable_direct_ai_mode(self):
        """Enable direct AI generation mode (no dictation) with SHORTER wait time"""
        self.email_input_mode = True
        self.is_listening = True
        self.voice_button.configure(text="🤖 Email AI Mode", bg="#e91e63", activebackground="#c2185b")
        self.status_label.configure(text="● Email AI Mode - Listening...", fg="#e91e63")
        
        # SHORTER wait - 1.5 seconds instead of 3 seconds
        def delayed_listening():
            time.sleep(1.5)  # Reduced from 3 seconds
            self.root.after(0, self.add_to_conversation, "ChiraagAI", "🎤 Speak now!")
            # Start listening for AI generation requests
            threading.Thread(target=self.listen_for_ai_generation, daemon=True).start()
        
        threading.Thread(target=delayed_listening, daemon=True).start()

    def listen_for_ai_generation(self):
        """Listen for AI generation requests only - no dictation"""
        try:
            with self.microphone as source:
                if self.debug_mode:
                    print("DEBUG: Listening for AI email generation request...")
                
                audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=15)
            
            text = self.recognizer.recognize_google(audio)
            
            if self.debug_mode:
                print(f"DEBUG: AI generation request: {text}")
            
            # Send directly to AI for email generation (no user conversation entry)
            self.generate_and_type_email_direct(text)
            
        except sr.WaitTimeoutError:
            if self.email_input_mode and self.is_listening:
                threading.Thread(target=self.listen_for_ai_generation, daemon=True).start()
        except sr.UnknownValueError:
            self.root.after(0, self.add_to_conversation, "ChiraagAI", "❓ Could not understand. Please repeat your email request.")
            if self.email_input_mode:
                threading.Thread(target=self.listen_for_ai_generation, daemon=True).start()
        except Exception as e:
            error_msg = f"AI generation listening error: {str(e)}"
            if self.debug_mode:
                print(f"ERROR: {error_msg}")
            self.root.after(0, self.add_to_conversation, "System", f"❌ {error_msg}")
            self.exit_email_mode()

    def auto_enable_email_input(self):
        """RESTORED: Auto-enable microphone with SHORTER wait time"""
        self.email_input_mode = True
        self.is_listening = True
        self.voice_button.configure(text="🎤 Email AI Mode...", bg="#9c27b0", activebackground="#7b1fa2")
        self.status_label.configure(text="● Email AI Mode - Listening...", fg="#9c27b0")
        
        # Provide initial feedback
        self.add_to_conversation("ChiraagAI", "🤖 Email AI Mode activated! Say 'write [type] email' for generation or dictate directly...")
        
        # SHORTER wait - 1.5 seconds instead of 3 seconds before "Speak now"
        def delayed_listening():
            time.sleep(1.5)  # Reduced from 3 seconds
            self.root.after(0, self.add_to_conversation, "ChiraagAI", "🎤 Speak now!")
            # Start listening with longer timeout for email content
            threading.Thread(target=self.listen_for_email_content, daemon=True).start()
        
        threading.Thread(target=delayed_listening, daemon=True).start()

    def listen_for_email_content(self):
        """RESTORED: Better email content listening with REDUCED timeout"""
        try:
            with self.microphone as source:
                if self.debug_mode:
                    print("DEBUG: Listening for email content or generation request...")
                
                # REDUCED timeout from 3 to 2 seconds for faster response
                audio = self.recognizer.listen(source, timeout=2, phrase_time_limit=20)  # Reduced phrase time too
            
            if self.debug_mode:
                print("DEBUG: Processing email speech...")
            
            text = self.recognizer.recognize_google(audio)
            
            if self.debug_mode:
                print(f"DEBUG: Email input recognized: {text}")
            
            # Process through the enhanced handler
            self.handle_email_content_input(text)
            
        except sr.WaitTimeoutError:
            if self.email_input_mode and self.is_listening:
                self.root.after(0, self.add_to_conversation, "System", "⏱️ Still listening... Say 'write [type] email' for AI generation or dictate directly")
                threading.Thread(target=self.listen_for_email_content, daemon=True).start()
        except sr.UnknownValueError:
            self.root.after(0, self.add_to_conversation, "ChiraagAI", "❓ Could not understand. Try: 'write application for sick leave' or dictate directly")
            if self.email_input_mode:
                threading.Thread(target=self.listen_for_email_content, daemon=True).start()
        except Exception as e:
            error_msg = f"Email input error: {str(e)}"
            if self.debug_mode:
                print(f"ERROR: {error_msg}")
            self.root.after(0, self.add_to_conversation, "System", f"❌ {error_msg}")
            self.stop_email_input_mode()

    def process_email_content(self, email_text):
        """RESTORED: Better email content processing and typing"""
        try:
            if self.debug_mode:
                print(f"DEBUG: Processing direct email content: {email_text}")
            
            self.add_to_conversation("You (Email)", email_text)
            
            # Ensure we're in the email body field
            pyautogui.click()  # Click to ensure focus
            time.sleep(0.5)
            
            # Type email content with enhanced speed and reliability
            self.root.after(0, self.status_label.configure, {"text": "● Typing email content...", "fg": "#ff9800"})
            
            # Clear any existing content first
            pyautogui.hotkey('ctrl', 'a')  # Select all
            time.sleep(0.3)
            
            # Type the email content using lightning fast method
            self.type_lightning_fast(email_text)
            
            # Stop email input mode
            self.stop_email_input_mode()
            
            success_msg = f"✅ Email typed successfully! Content: '{email_text[:50]}{'...' if len(email_text) > 50 else ''}' (Review and send manually)"
            self.add_to_conversation("ChiraagAI", success_msg)
            # NO voice feedback to avoid interruption
            
            if self.debug_mode:
                print(f"DEBUG: Email typing completed successfully")
            
        except Exception as e:
            error_msg = f"Email typing error: {str(e)}"
            if self.debug_mode:
                print(f"ERROR: {error_msg}")
            self.root.after(0, self.add_to_conversation, "System", f"❌ {error_msg}")
            self.stop_email_input_mode()

    def stop_email_input_mode(self):
        """RESTORED: Clean email input mode termination"""
        if self.debug_mode:
            print("DEBUG: Stopping email input mode")
        
        self.email_input_mode = False
        self.is_listening = False
        self.voice_button.configure(text="🎤 Start Listening", bg="#1976d2", activebackground="#1565c0")
        self.status_label.configure(text="● Email composition complete", fg="#4caf50")
        
        # Reset status after a moment
        self.root.after(3000, lambda: self.status_label.configure(text="● Ready to control your system", fg="#4caf50"))

    def exit_email_mode(self):
        """Exit email AI mode and return to normal operation"""
        if self.debug_mode:
            print("DEBUG: Exiting email AI mode")
        
        self.email_input_mode = False
        self.is_listening = False
        self.voice_button.configure(text="🎤 Start Listening", bg="#1976d2", activebackground="#1565c0")
        self.status_label.configure(text="● Email generated successfully", fg="#4caf50")
        
        # Reset status after a moment
        self.root.after(3000, lambda: self.status_label.configure(text="● Ready to control your system", fg="#4caf50"))
    
    def open_website_lightning_fast(self, website, original_input):
        """LIGHTNING FAST website opening - under 0.3 seconds typing"""
        def execute_website():
            try:
                if self.debug_mode:
                    print(f"DEBUG: Lightning-fast opening website: {website}")
                
                self.root.after(0, self.status_label.configure, {"text": f"● Opening {website}...", "fg": "#ff9800"})
                
                # Force browser open with dummy website method
                webbrowser.open("https://www.google.com")
                time.sleep(1)
                
                # Open address bar
                pyautogui.hotkey('ctrl', 'l')
                time.sleep(0.5)
                
                # Get URL and type LIGHTNING FAST
                url = self.website_urls.get(website.lower(), f"https://{website}")
                clean_url = url.replace('https://', '').replace('http://', '')
                
                # LIGHTNING FAST typing - entire URL in under 0.3 seconds
                self.type_lightning_fast(clean_url)
                
                pyautogui.press('enter')
                time.sleep(0.8)
                
                self.root.after(0, self.add_to_conversation, "System", f"✅ {website} opened with lightning speed!")
                self.root.after(0, self.status_label.configure, {"text": "● Ready to control your system", "fg": "#4caf50"})
                
            except Exception as e:
                error_msg = f"Failed to open {website}: {str(e)}"
                if self.debug_mode:
                    print(f"ERROR: {error_msg}")
                self.root.after(0, self.add_to_conversation, "System", error_msg)
                self.root.after(0, self.status_label.configure, {"text": "● Ready to control your system", "fg": "#4caf50"})
        
        threading.Thread(target=execute_website, daemon=True).start()
    
    def search_youtube_lightning_fast(self, query, original_input):
        """LIGHTNING FAST: YouTube search with under 0.3-second typing"""
        def execute_search():
            try:
                if self.debug_mode:
                    print(f"DEBUG: Lightning-fast YouTube search for: '{query}'")
                
                self.root.after(0, self.status_label.configure, {"text": "● Searching YouTube...", "fg": "#ff9800"})
                
                # Force browser open with dummy website method
                webbrowser.open("https://www.google.com")
                time.sleep(1)
                
                # Open address bar
                pyautogui.hotkey('ctrl', 'l')
                time.sleep(0.5)
                
                # LIGHTNING FAST: Type YouTube URL
                self.type_lightning_fast("youtube.com")
                pyautogui.press('enter')
                time.sleep(2)
                
                # Click search box and search LIGHTNING FAST
                pyautogui.hotkey('ctrl', 'l')
                time.sleep(0.5)
                
                # Type search URL directly
                search_url = f"youtube.com/results?search_query={quote(query)}"
                self.type_lightning_fast(search_url)
                pyautogui.press('enter')
                
                self.root.after(0, self.add_to_conversation, "System", f"✅ YouTube search for '{query}' completed!")
                self.root.after(0, self.status_label.configure, {"text": "● Ready to control your system", "fg": "#4caf50"})
                
            except Exception as e:
                error_msg = f"YouTube search failed: {str(e)}"
                if self.debug_mode:
                    print(f"ERROR: {error_msg}")
                self.root.after(0, self.add_to_conversation, "System", error_msg)
                self.root.after(0, self.status_label.configure, {"text": "● Ready to control your system", "fg": "#4caf50"})
        
        threading.Thread(target=execute_search, daemon=True).start()
    
    def search_google_lightning_fast(self, query, original_input):
        """LIGHTNING FAST: Google search with under 0.3-second typing"""
        def execute_search():
            try:
                if self.debug_mode:
                    print(f"DEBUG: Lightning-fast Google search for: '{query}'")
                
                self.root.after(0, self.status_label.configure, {"text": "● Searching Google...", "fg": "#ff9800"})
                
                # Force browser open with dummy website method
                webbrowser.open("https://www.google.com")
                time.sleep(1)
                
                # Open address bar
                pyautogui.hotkey('ctrl', 'l')
                time.sleep(0.5)
                
                # Type search URL directly - LIGHTNING FAST
                search_url = f"google.com/search?q={quote(query)}"
                self.type_lightning_fast(search_url)
                pyautogui.press('enter')
                
                self.root.after(0, self.add_to_conversation, "System", f"✅ Google search for '{query}' completed!")
                self.root.after(0, self.status_label.configure, {"text": "● Ready to control your system", "fg": "#4caf50"})
                
            except Exception as e:
                error_msg = f"Google search failed: {str(e)}"
                if self.debug_mode:
                    print(f"ERROR: {error_msg}")
                self.root.after(0, self.add_to_conversation, "System", error_msg)
                self.root.after(0, self.status_label.configure, {"text": "● Ready to control your system", "fg": "#4caf50"})
        
        threading.Thread(target=execute_search, daemon=True).start()
    
    def open_application_lightning_fast(self, app_name, original_input):
        """LIGHTNING FAST application opening with enhanced typing"""
        def execute_open():
            try:
                if self.debug_mode:
                    print(f"DEBUG: Lightning-fast opening application: {app_name}")
                
                original_failsafe = pyautogui.FAILSAFE
                pyautogui.FAILSAFE = False
                
                self.root.after(0, self.status_label.configure, {"text": f"● Opening {app_name}...", "fg": "#ff9800"})
                
                pyautogui.press('win')
                time.sleep(0.8)
                
                search_term = self.app_commands.get(app_name.lower(), app_name)
                
                # LIGHTNING FAST typing for app search
                self.type_lightning_fast(search_term)
                
                time.sleep(0.8)
                pyautogui.press('enter')
                time.sleep(1.5)
                
                pyautogui.FAILSAFE = original_failsafe
                
                self.root.after(0, self.add_to_conversation, "System", f"✅ {app_name} opened with lightning speed!")
                self.root.after(0, self.status_label.configure, {"text": "● Ready to control your system", "fg": "#4caf50"})
                
            except Exception as e:
                pyautogui.FAILSAFE = original_failsafe
                error_msg = f"Failed to open {app_name}: {str(e)}"
                if self.debug_mode:
                    print(f"ERROR: {error_msg}")
                self.root.after(0, self.add_to_conversation, "System", error_msg)
                self.root.after(0, self.status_label.configure, {"text": "● Ready to control your system", "fg": "#4caf50"})
        
        threading.Thread(target=execute_open, daemon=True).start()
    
    def take_screenshot_fixed(self, original_input):
        """ENHANCED: Take screenshot with multiple save options"""
        def execute_screenshot():
            try:
                if self.debug_mode:
                    print("DEBUG: Taking enhanced screenshot")
                
                self.root.after(0, self.status_label.configure, {"text": "● Taking screenshot...", "fg": "#ff9800"})
                
                # Take screenshot using pyautogui
                screenshot = pyautogui.screenshot()
                
                # Generate filename with timestamp
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                filename = f"ChiraagAI_Screenshot_{timestamp}.png"
                
                # Try to save to multiple locations
                save_paths = [
                    os.path.join(os.path.expanduser("~"), "Desktop", filename),
                    os.path.join(os.path.expanduser("~"), "Pictures", filename),
                    os.path.join(os.path.expanduser("~"), "Downloads", filename),
                    filename  # Current directory as fallback
                ]
                
                saved_path = None
                for path in save_paths:
                    try:
                        screenshot.save(path)
                        saved_path = path
                        if self.debug_mode:
                            print(f"DEBUG: Screenshot saved to: {path}")
                        break
                    except Exception as e:
                        if self.debug_mode:
                            print(f"DEBUG: Failed to save to {path}: {e}")
                        continue
                
                if saved_path:
                    self.root.after(0, self.add_to_conversation, "System", f"✅ Screenshot saved successfully!\nLocation: {saved_path}")
                else:
                    self.root.after(0, self.add_to_conversation, "System", "❌ Failed to save screenshot to any location")
                
                self.root.after(0, self.status_label.configure, {"text": "● Ready to control your system", "fg": "#4caf50"})
                
            except Exception as e:
                error_msg = f"Screenshot failed: {str(e)}"
                if self.debug_mode:
                    print(f"ERROR: {error_msg}")
                self.root.after(0, self.add_to_conversation, "System", f"❌ {error_msg}")
                self.root.after(0, self.status_label.configure, {"text": "● Ready to control your system", "fg": "#4caf50"})
        
        threading.Thread(target=execute_screenshot, daemon=True).start()
    
    def clear_conversation(self):
        """Clear the conversation display"""
        self.conversation_display.config(state=tk.NORMAL)
        self.conversation_display.delete(1.0, tk.END)
        self.conversation_display.config(state=tk.DISABLED)
        
        # Reset conversation history
        self.conversation_history = []
        
        # Add welcome message back
        self.add_to_conversation("ChiraagAI", "🚀 Conversation cleared! How may I assist you today?")
    
    def on_closing(self):
        """Handle application closing"""
        try:
            # Stop any ongoing audio
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except:
            pass
        
        # Destroy the window
        self.root.destroy()
    
    def run(self):
        """Start the application"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.on_closing()
    
    def disable_buttons_during_speech(self):
        """Disable all control buttons when AI is speaking"""
        try:
            self.voice_button.config(state=tk.DISABLED)
            # Find and disable text and clear buttons
            for widget in self.root.winfo_children():
                self._disable_buttons_recursive(widget)
        except Exception as e:
            if self.debug_mode:
                print(f"DEBUG: Error disabling buttons: {e}")

    def enable_buttons_after_speech(self):
        """Re-enable all control buttons after AI finishes speaking"""
        try:
            self.voice_button.config(state=tk.NORMAL)
            # Find and enable text and clear buttons
            for widget in self.root.winfo_children():
                self._enable_buttons_recursive(widget)
        except Exception as e:
            if self.debug_mode:
                print(f"DEBUG: Error enabling buttons: {e}")

    def _disable_buttons_recursive(self, widget):
        """Recursively disable buttons in widget hierarchy"""
        try:
            if isinstance(widget, tk.Button):
                widget.config(state=tk.DISABLED)
            for child in widget.winfo_children():
                self._disable_buttons_recursive(child)
        except:
            pass

    def _enable_buttons_recursive(self, widget):
        """Recursively enable buttons in widget hierarchy"""
        try:
            if isinstance(widget, tk.Button):
                widget.config(state=tk.NORMAL)
            for child in widget.winfo_children():
                self._enable_buttons_recursive(child)
        except:
            pass


# Application entry point
if __name__ == "__main__":
    try:
        app = ChiraagAI()
        app.run()
    except Exception as e:
        print(f"Application startup error: {e}")
        messagebox.showerror("ChiraagAI Error", f"Failed to start ChiraagAI:\n{e}")

