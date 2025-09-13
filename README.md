# AgentAstra

**AgentAstra** is an intelligent desktop automation agent powered by powerful LLMs and LangChain. It provides a conversational interface to control your computer through natural language commands, enabling you to automate web browsing, system operations, media control, and more.

## Features

### AI-Powered Automation
- **Natural Language Interaction**
- **LLM Integration**
- **Real-time Chat Interface**


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



## 🔧 Configuration

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
