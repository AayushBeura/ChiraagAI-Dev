# 🚀 ChiraagAI

A modern, intelligent AI desktop assistant built with Python and Tkinter, featuring a sleek GUI, multimedia startup, voice interaction, and real-time automation. Designed to feel futuristic yet functional — your personal productivity booster.

![ChiraagAI Banner](logo.png)

---

## 🌟 Features

- 🎨 **Modern UI** — Beautiful, responsive Tkinter interface with custom fonts and themes  
- 🎞️ **Multimedia Startup** — Animated intro using MP4 + MP3 (just like JARVIS 😉)  
- 🎙️ **Voice Recognition** — Speak commands using your mic, powered by Google Speech  
- 🤖 **AI-Powered** — Integrates Gemini API for smart responses and Murf TTS for realistic voice  
- 🧠 **Custom Automation** — Control apps, open websites, take screenshots, and more  
- 🔧 **Configurable** — Use `config_manager.py` to manage API keys and preferences  
- 📦 **One-Click Executable** — Available as a single `.exe` (see [Releases](https://github.com/AayushBeura/ChiraagAI-Dev/releases))

---

## 📸 Demo

> Coming soon in the GitHub Releases page.

---

## 📁 File Structure

```
ChiraagAI-Dev/
├── ChiraagAI.py             # Main application
├── config_manager.py        # Handles API key & config management
├── startup.mp4              # Startup intro video
├── startup.mp3              # Startup audio
├── logo.png                 # App logo
├── ChiraagAI-Icon.ico       # Windows icon
├── ChiraagAI-Icon.png       # Fallback icon
├── README.md                # This file
└── requirements.txt         # Required dependencies
```

---

## 💻 Installation

### Prerequisites
- Python 3.7+
- pip

### Steps

```bash
git clone https://github.com/AayushBeura/ChiraagAI-Dev.git
cd ChiraagAI-Dev
pip install -r requirements.txt
python ChiraagAI.py
```

---

## 🛠️ Building Executable (Optional)

You can build a standalone `.exe` using PyInstaller:

### 🔹 Windows:

```bash
pyinstaller --onefile --windowed --icon=ChiraagAI-Icon.ico ^
--add-data "startup.mp3;." ^
--add-data "startup.mp4;." ^
--add-data "logo.png;." ^
--add-data "ChiraagAI-Icon.png;." ^
--add-data "ChiraagAI-Icon.ico;." ^
--add-data "config_manager.py;." ^
--name ChiraagAI ChiraagAI.py
```

### 🔸 macOS/Linux:

```bash
pyinstaller --onefile --windowed --icon=ChiraagAI-Icon.ico \
--add-data "startup.mp3:." \
--add-data "startup.mp4:." \
--add-data "logo.png:." \
--add-data "ChiraagAI-Icon.png:." \
--add-data "ChiraagAI-Icon.ico:." \
--add-data "config_manager.py:." \
--name ChiraagAI ChiraagAI.py
```

> 📦 The built executable will be available in the `dist/` folder.

---

## 📦 Download Executable

Head over to the [**Releases Page**](https://github.com/AayushBeura/ChiraagAI-Dev/releases) to download the latest version of the `.exe` — no setup required. Just download and run!

✅ All necessary files are embedded  
✅ No need to install Python or dependencies  
✅ Works out-of-the-box on most Windows machines

---

## 🧪 Development Mode

```bash
# Create a virtual environment
python -m venv .venv
.venv\Scripts\activate     # (on Windows)

# Install dependencies
pip install -r requirements.txt

# Run
python ChiraagAI.py
```

---

## ⚙️ Configuration

Edit `config_manager.py` to provide your:

- 🌐 Gemini API key
- 🔊 Murf TTS API key
- 🛠 Additional settings (voice, model parameters, etc.)

> You may optionally use `.env` files for keeping keys secure.

---

## 🧠 Future Enhancements

- ☁️ Cloud sync for user preferences  
- 🧩 Plugin-based command modules  
- 🎮 Game Mode assistant integration  
- 🌍 Multilingual support  
- 🎤 Natural language pipelines (OpenVoice, Whisper)

---

## 👨‍💻 Contributing

Want to contribute? Fork this repo and:

```bash
git checkout -b feature/amazing-idea
git commit -m "✨ Implemented amazing idea"
git push origin feature/amazing-idea
```

Then open a pull request!

---

## 📃 License

Licensed under the [MIT License](LICENSE)

---

## 🙋 Support

If you face any issues:
- Create a [GitHub Issue](https://github.com/AayushBeura/ChiraagAI-Dev/issues)
- Ping me on [GitHub](https://github.com/AayushBeura)

---

## ✨ Author

**Aayush Beura**  
🔗 [@AayushBeura](https://github.com/AayushBeura)  
📧 Passionate about AI + Automation + Experience Design
