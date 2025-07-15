# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-01-15

### Added
- Initial release of llm-digitalocean plugin
- Support for DigitalOcean AI inference API (`https://inference.do-ai.run/v1/`)
- Automatic model discovery and registration with LLM framework
- JSON caching in `llm.user_dir()` with 1-hour cache timeout
- Refresh functionality to update cached models
- CLI commands:
  - `llm digitalocean models` - List available models
  - `llm digitalocean refresh` - Refresh cached models
  - `llm digitalocean cache-info` - Show cache information
- Support for both sync and async chat models
- Vision model detection and support
- Comprehensive test suite with 100% test coverage
- GitHub Actions workflows for CI/CD
- Automatic PyPI publishing on releases
- Support for Python 3.9-3.13

### Features
- **Model Support**: 13+ DigitalOcean AI models including:
  - Llama 3.3 70B Instruct
  - Claude 3.5 Sonnet
  - GPT-4o and GPT-4o Mini
  - DeepSeek R1 Distill
  - Anthropic Claude models with vision support
  - OpenAI models with vision support
- **Caching**: Intelligent caching system to reduce API calls
- **Error Handling**: Comprehensive error handling for network issues, API errors, and missing keys
- **Documentation**: Complete README with installation and usage instructions
- **Testing**: Full test coverage with pytest

### Technical Details
- Built using LLM plugin framework
- Uses OpenAI-compatible chat interface
- Supports streaming and non-streaming responses
- Automatic attachment type detection for vision models
- Proper authentication with Bearer token
- Fallback to cached data when API is unavailable

[0.1.0]: https://github.com/yourusername/llm-digitalocean/releases/tag/0.1.0