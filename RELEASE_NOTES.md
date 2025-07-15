# llm-digitalocean v0.1.0 - Initial Release

🎉 **First release of the llm-digitalocean plugin!**

This plugin brings DigitalOcean AI models to the [LLM](https://llm.datasette.io/) command-line tool, providing seamless access to powerful AI models through DigitalOcean's inference API.

## 🚀 Key Features

### ✨ Model Support
- **13+ AI Models** including:
  - 🦙 **Llama 3.3 70B Instruct** - Meta's latest large language model
  - 🤖 **Claude 3.5 Sonnet** - Anthropic's advanced reasoning model
  - 🧠 **GPT-4o & GPT-4o Mini** - OpenAI's multimodal models
  - 🔍 **DeepSeek R1 Distill** - Efficient reasoning model
  - 👁️ **Vision Models** - Support for image analysis with Claude and GPT-4o models

### 💾 Smart Caching
- **Automatic caching** in `llm.user_dir()` with 1-hour timeout
- **Offline fallback** - works even when API is unavailable
- **Cache management** commands for monitoring and refreshing

### 🛠️ CLI Commands
```bash
llm digitalocean models      # List all available models
llm digitalocean refresh     # Refresh cached models
llm digitalocean cache-info  # Show cache status
```

### 🔧 Developer Features
- **Full test coverage** (10/10 tests passing)
- **GitHub Actions** for CI/CD
- **Python 3.9-3.13** support
- **Async/sync** model support
- **Vision model detection**

## 📦 Installation

```bash
pip install llm-digitalocean
```

## ⚙️ Setup

```bash
# Set your DigitalOcean API key
export DIGITAL_OCEAN="your-api-key-here"
# or
llm keys set digitalocean
```

## 🎯 Quick Start

```bash
# List available models
llm digitalocean models

# Use a model
llm -m digitalocean/llama3.3-70b-instruct "Explain quantum computing"

# Use with vision (for supported models)
llm -m digitalocean/openai-gpt-4o "What's in this image?" -a image.jpg

# Set up an alias for easier use
llm aliases set llama digitalocean/llama3.3-70b-instruct
llm -m llama "Hello, world!"
```

## 🔗 Links

- **PyPI Package**: https://pypi.org/project/llm-digitalocean/
- **Documentation**: See README.md
- **Issues**: Report bugs and feature requests
- **LLM Framework**: https://llm.datasette.io/

## 🙏 Acknowledgments

Built for the [LLM](https://llm.datasette.io/) ecosystem by Simon Willison. Inspired by the `llm-requesty` plugin architecture.

---

**Full Changelog**: https://github.com/yourusername/llm-digitalocean/blob/main/CHANGELOG.md