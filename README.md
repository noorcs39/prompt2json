# prompt2json

A Python library for converting natural language prompts to structured JSON format. This tool helps standardize prompt handling for AI applications, data processing, and prompt engineering workflows.

## Features

- 🔄 Convert text prompts to structured JSON format
- 📊 Analyze prompt characteristics (questions, instructions, code blocks)
- 🔍 Detect programming language hints in prompts
- 📝 Include metadata and timestamps
- 🚀 Command-line interface for easy integration
- 📦 Batch processing support
- 🎯 Zero external dependencies for core functionality

## Installation

### From PyPI (recommended)

```bash
pip install prompt2json
```

### From source

```bash
git clone https://github.com/noorcs39/prompt2json.git
cd prompt2json
pip install -e .
```

## Quick Start

### Python API

```python
from prompt2json import convert_prompt_to_json, PromptConverter

# Simple conversion
prompt = "Create a Python function that calculates fibonacci numbers"
result = convert_prompt_to_json(prompt)
print(result)
```

**Output:**
```json
{
  "prompt": "Create a Python function that calculates fibonacci numbers",
  "length": 56,
  "word_count": 8,
  "metadata": {
    "timestamp": "2024-01-15T10:30:00.123456",
    "version": "0.1.0"
  },
  "analysis": {
    "has_questions": false,
    "has_instructions": true,
    "sentences": 1,
    "contains_code": false,
    "language_hints": ["python"]
  }
}
```

### Advanced Usage

```python
from prompt2json import PromptConverter

# Create converter with custom settings
converter = PromptConverter(include_metadata=True)

# Convert with additional metadata
result = converter.convert(
    "Write a REST API in Python using Flask",
    project_type="web_api",
    difficulty="intermediate"
)

# Get JSON string directly
json_string = converter.to_json_string(
    "Explain machine learning concepts",
    indent=4
)

# Batch processing
prompts = [
    "Create a database schema",
    "Write unit tests",
    "Deploy to AWS"
]
results = converter.convert_batch(prompts)
```

### Command Line Interface

```bash
# Convert a prompt directly
prompt2json "Create a web scraper in Python"

# Read from file and save to output
echo "Build a chatbot" | prompt2json -o output.json

# Exclude metadata
prompt2json "Simple prompt" --no-metadata

# Custom indentation
prompt2json "Another prompt" --indent 4
```

## API Reference

### `PromptConverter`

Main class for converting prompts to JSON format.

#### Constructor

```python
PromptConverter(include_metadata: bool = True)
```

- `include_metadata`: Whether to include metadata in output

#### Methods

##### `convert(prompt: str, **kwargs) -> Dict[str, Any]`

Convert a single prompt to JSON format.

- `prompt`: Input prompt string
- `**kwargs`: Additional metadata to include
- Returns: Dictionary with converted prompt data

##### `convert_batch(prompts: List[str], **kwargs) -> List[Dict[str, Any]]`

Convert multiple prompts at once.

##### `to_json_string(prompt: str, indent: int = 2, **kwargs) -> str`

Convert prompt and return as JSON string.

### `convert_prompt_to_json(prompt: str, include_metadata: bool = True, **kwargs)`

Convenience function for quick conversions.

## Output Format

The JSON output includes:

- `prompt`: Original prompt text
- `length`: Character count
- `word_count`: Word count
- `metadata`: Timestamp, version, and custom metadata (optional)
- `analysis`: Structural analysis of the prompt
  - `has_questions`: Boolean indicating if prompt contains questions
  - `has_instructions`: Boolean indicating if prompt contains instructions
  - `sentences`: Number of sentences
  - `contains_code`: Boolean indicating if prompt contains code blocks
  - `language_hints`: List of detected programming languages

## Development

### Setup Development Environment

```bash
git clone https://github.com/noorcs39/prompt2json.git
cd prompt2json
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black prompt2json/
flake8 prompt2json/
mypy prompt2json/
```

### Building and Publishing

```bash
# Build the package
python -m build

# Upload to PyPI (requires credentials)
twine upload dist/*
```

## Use Cases

- **Prompt Engineering**: Standardize and analyze prompts for AI models
- **Data Processing**: Convert text inputs to structured format for databases
- **API Development**: Structure prompt data for REST APIs
- **Research**: Analyze prompt characteristics and patterns
- **Automation**: Integrate with CI/CD pipelines for prompt processing

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### v0.1.0
- Initial release
- Basic prompt to JSON conversion
- Command-line interface
- Prompt analysis features
- Batch processing support

## Support

If you encounter any issues or have questions:

- Open an issue on [GitHub](https://github.com/yourusername/prompt2json/issues)
- Check the [documentation](https://github.com/yourusername/prompt2json#readme)

---

**Made with ❤️ for the AI and developer community**
