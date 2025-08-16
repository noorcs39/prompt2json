"""prompt2json - A Python library for converting prompts to JSON format.

This library provides utilities to convert natural language prompts into structured JSON format,
making it easier to work with AI prompts in a standardized way.
"""

__version__ = "0.1.0"
__author__ = "Nooruddin Noonari"
__email__ = "noor.cs2@yahoo.com"
__description__ = "Convert prompts to JSON format"

from .converter import PromptConverter, convert_prompt_to_json

__all__ = ["PromptConverter", "convert_prompt_to_json"]