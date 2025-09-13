# AgentAstra

**AgentAstra** is an intelligent desktop automation agent powered by Google's Gemini AI and LangChain. It provides a conversational interface to control your computer through natural language commands, enabling you to automate web browsing, system operations, media control, and more.

## Features

### AI-Powered Automation
- **Natural Language Interface**: Control your computer using conversational commands
- **Google Gemini Integration**: Powered by Google's advanced Gemini 2.5 Flash model
- **Real-time Chat Interface**: Modern PyQt5-based GUI with typing indicators

### Comprehensive Tool Suite

#### 📋 Clipboard Operations
- Copy text to clipboard
- Paste from clipboard
- Get currently selected text

#### 🖥️ GUI Automation
- Application control (open/close)
- Window and tab management
- Keyboard shortcuts and key presses
- Screenshot capture
- Text input and scrolling
- Search functionality

#### 🌐 Web Automation (Selenium)
- Browser launch and management
- Tab navigation and switching
- URL navigation
- Web search capabilities
- Element interaction by description
- Form filling and clicking

#### 🎵 Media Control
- Play/pause/resume songs
- Skip to next/previous tracks
- Volume control

#### 🔧 System Utilities
- File and folder operations
- Application launching
- Command execution
- Date/time information

## 🏗️ Project Structure

```
AgentAstra/
├── agent.py                 # Main agent initialization and execution
├── astra.py                 # PyQt5 GUI application (chat interface)
├── all_tools.py             # Tool registry and configuration
├── utils.py                 # Utility functions and helpers
├── requirements.txt         # Python dependencies
├── agent_tools/             # Tool implementations
│   ├── clipboard_tools.py   # Clipboard operations
│   ├── gui_tools.py         # GUI automation
│   ├── media_tools.py       # Media control
│   ├── selenium_tools.py    # Web automation
│   ├── utility_tools.py     # System utilities
│   └── web_tools.py         # Web operations
└── langchain_tools/         # LangChain integrations
    └── web_model.py         # AI-powered XPath detection
```

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Google API key for Gemini
- Chrome browser (for web automation)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AgentAstra.git
   cd AgentAstra
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   GENIE_MODEL=gemini-2.5-flash
   ```

4. **Run the application**
   ```bash
   python astra.py
   ```

## 💡 Usage Examples

### Basic Commands
- **"Take a screenshot"** - Captures the current screen
- **"Open Google Chrome"** - Launches the browser
- **"Search for Python tutorials"** - Performs web search
- **"Copy this text to clipboard"** - Copies selected text

### Web Automation
- **"Navigate to https://github.com"** - Opens a website
- **"Click the login button"** - Interacts with web elements
- **"Type 'hello world' in the search box"** - Fills form fields
- **"Open a new tab"** - Manages browser tabs

### System Control
- **"Open Notepad"** - Launches applications
- **"Close the current window"** - Window management
- **"Press Ctrl+C"** - Keyboard shortcuts
- **"Scroll down 300 pixels"** - Page navigation

## 🔧 Configuration

### Environment Variables
- `GOOGLE_API_KEY`: Your Google API key for Gemini access
- `GENIE_MODEL`: Gemini model to use (default: gemini-2.5-flash)

### Customization
You can extend the agent by adding new tools in the `agent_tools/` directory and registering them in `all_tools.py`.

## Security Considerations

- **API Key Protection**: Never commit your `.env` file to version control
- **System Access**: The agent has broad system access - use responsibly
- **Web Automation**: Be cautious with automated web interactions
- **Permissions**: Ensure proper file system permissions for operations

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


---

**Made with ❤️ for intelligent desktop automation**
