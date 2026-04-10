# NOVA - Personal AI Assistant

A comprehensive Python-based AI assistant featuring voice recognition, face recognition, GUI interface, and various automation capabilities.

## 🌟 Features

### Core Functionality
- **Voice Recognition & Speech Synthesis** - Natural language interaction with text-to-speech capabilities
- **Face Recognition** - Secure user authentication and identification
- **GUI Interface** - Modern PyQt-based graphical user interface
- **Email Integration** - Send and manage emails through voice commands
- **Web Automation** - Control various web applications and services

### Smart Capabilities
- **Weather Updates** - Real-time weather information
- **News Integration** - Latest news updates through API
- **YouTube Integration** - Search, play, and download videos
- **Google Maps Integration** - Navigation and location services
- **WhatsApp Automation** - Send messages through voice commands
- **Gmail Integration** - Email management and composition

### Advanced Features
- **Gesture Control** - Hand gesture recognition for system control
- **Object Detection** - Computer vision for object identification
- **File Search** - Intelligent file searching and management
- **System Control** - OS-level operations and application management
- **Brightness & Volume Control** - System parameter adjustments
- **Scheduled Tasks** - Reminders and alarms functionality

### Security & User Management
- **Multi-user Support** - Individual user profiles and authentication
- **Voice Authentication** - Speaker verification for added security
- **Face Recognition Login** - Biometric authentication system
- **User Registration** - New user signup and profile creation

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- Webcam (for face recognition)
- Microphone (for voice commands)
- Internet connection (for web services)

### Dependencies
Install the required packages using pip:

```bash
pip install -r requirements.txt
```

Key dependencies include:
- PyQt5/PyQt6 (GUI framework)
- OpenCV (Computer vision)
- SpeechRecognition (Voice processing)
- pyttsx3 (Text-to-speech)
- face_recognition (Face detection and recognition)
- requests (API communication)
- selenium (Web automation)
- pywhatkit (WhatsApp automation)

## 🚀 Quick Start

### 1. Initial Setup
```bash
# Clone the repository
git clone <https://github.com/harriik/Jarvis.git>
cd jarvis-ai-assistant

# Install dependencies
pip install -r requirements.txt

# Run the main application
python jarvisMAIN.py
```

### 2. First Time User Setup
1. Launch the application
2. Click "New User" to register
3. Complete face registration for biometric login
4. Configure voice settings and preferences

### 3. Login

<img width="930" height="640" alt="image" src="https://github.com/user-attachments/assets/77bf3034-f61a-433d-a6ba-939dd06f50aa" />

- Use face recognition for quick login

<img width="1020" height="676" alt="image" src="https://github.com/user-attachments/assets/b339b6ae-bd52-4130-b5bf-7f001c8e5b20" />

- Alternative: Username/password authentication

<img width="990" height="705" alt="image" src="https://github.com/user-attachments/assets/62dccb48-ade2-41c4-979b-c3b931b1490d" />

- Voice authentication for enhanced security

<img width="1186" height="646" alt="image" src="https://github.com/user-attachments/assets/d2c5cc83-522e-4d16-94c0-a4071fc996e3" />


## 📁 Project Structure

```
jarvis-ai-assistant/
├── JarvisGUI/                 # Main GUI application
│   ├── jarvisMAIN.py         # Primary application entry point
│   ├── loginWindowGUI.py     # Login interface
│   ├── signUpGUI.py          # User registration
│   └── FaceRecogGUI/         # Face recognition modules
├── Gesture Control/          # Hand gesture recognition
├── FaceRecognition.py        # Core face recognition
├── AdvancedSpeech.py        # Speech processing
├── WeatherUpdates.py        # Weather API integration
├── NewsApi.py               # News service integration
├── web_*.py                 # Web automation modules
├── Email.py                 # Email functionality
└── requirements.txt         # Project dependencies
```

## 🎯 Usage

### Voice Commands
- "Hello Jarvis" - Wake up command
- "What's the weather?" - Get weather updates
- "Send email to [contact]" - Email composition
- "Play [song] on YouTube" - Music playback
- "Open [application]" - Launch applications
- "Set reminder for [time]" - Schedule reminders

### GUI Features
- **Dashboard** - Central control panel
- **Settings** - Customize preferences and configurations
- **User Management** - Add/remove users and manage profiles
- **Voice Training** - Improve speech recognition accuracy
- **System Monitor** - View system status and performance

### Gesture Controls
- Hand gestures for volume control
- Navigation gestures for presentations
- System control through hand movements

## 🔧 Configuration

### API Keys
Configure the following API keys in your environment or config files:
- Weather API (OpenWeatherMap)
- News API
- Google Maps API
- Email service credentials

### Voice Settings
- Adjust speech rate and volume
- Select voice gender and accent
- Configure wake word sensitivity

### Face Recognition
- Register multiple faces per user
- Adjust recognition threshold
- Configure fallback authentication

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by Marvel's JARVIS AI assistant
- Built with Python and open-source libraries
- Thanks to the computer vision and speech recognition communities

## 🔮 Future Enhancements

- [ ] Smart home integration (IoT devices)
- [ ] Natural language processing improvements
- [ ] Mobile app companion
- [ ] Cloud synchronization
- [ ] Advanced machine learning capabilities
- [ ] Multi-language support

---

*"Sometimes you gotta run before you can walk."* - Tony Stark
