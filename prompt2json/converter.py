"""Core converter module for prompt2json library.

This module contains the main functionality for converting natural language prompts
into structured JSON format.
"""

import json
import re
from typing import Dict, Any, List, Optional
from datetime import datetime


class PromptConverter:
    """Main class for converting prompts to JSON format."""
    
    def __init__(self, include_metadata: bool = True):
        """Initialize the PromptConverter.
        
        Args:
            include_metadata (bool): Whether to include metadata in the output JSON.
        """
        self.include_metadata = include_metadata
    
    def convert(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """Convert a prompt to JSON format.
        
        Args:
            prompt (str): The input prompt to convert.
            **kwargs: Additional metadata to include in the JSON.
            
        Returns:
            Dict[str, Any]: The prompt converted to JSON format.
        """
        if not isinstance(prompt, str):
            raise ValueError("Prompt must be a string")
        
        # Basic JSON structure
        result = {
            "prompt": prompt.strip(),
            "length": len(prompt.strip()),
            "word_count": len(prompt.strip().split())
        }
        
        # Add metadata if enabled
        if self.include_metadata:
            result["metadata"] = {
                "timestamp": datetime.now().isoformat(),
                "version": "0.1.0",
                **kwargs
            }
        
        # Analyze prompt structure
        result["analysis"] = self._analyze_prompt(prompt)
        
        return result
    
    def _analyze_prompt(self, prompt: str) -> Dict[str, Any]:
        """Analyze the prompt structure and extract useful information.
        
        Args:
            prompt (str): The prompt to analyze.
            
        Returns:
            Dict[str, Any]: Analysis results.
        """
        analysis = {
            "has_questions": bool(re.search(r'\?', prompt)),
            "has_instructions": bool(re.search(r'\b(please|create|make|generate|write|build)\b', prompt, re.IGNORECASE)),
            "sentences": len(re.split(r'[.!?]+', prompt.strip())),
            "contains_code": bool(re.search(r'```|`[^`]+`', prompt)),
            "language_hints": self._detect_language_hints(prompt)
        }
        
        return analysis
    
    def _detect_language_hints(self, prompt: str) -> List[str]:
        """Detect programming language hints in the prompt.
        
        Args:
            prompt (str): The prompt to analyze.
            
        Returns:
            List[str]: List of detected programming languages.
        """
        languages = []
        language_patterns = {
            'python': r'\b(python|py|pip|django|flask|pandas)\b',
            'javascript': r'\b(javascript|js|node|npm|react|vue)\b',
            'java': r'\b(java|maven|gradle|spring)\b',
            'html': r'\b(html|css|web|website)\b',
            'sql': r'\b(sql|database|mysql|postgresql)\b',
            'json': r'\b(json|api|rest)\b'
        }
        
        for lang, pattern in language_patterns.items():
            if re.search(pattern, prompt, re.IGNORECASE):
                languages.append(lang)
        
        return languages
    
    def convert_batch(self, prompts: List[str], **kwargs) -> List[Dict[str, Any]]:
        """Convert multiple prompts to JSON format.
        
        Args:
            prompts (List[str]): List of prompts to convert.
            **kwargs: Additional metadata to include in each JSON.
            
        Returns:
            List[Dict[str, Any]]: List of converted prompts.
        """
        return [self.convert(prompt, **kwargs) for prompt in prompts]
    
    def to_json_string(self, prompt: str, indent: Optional[int] = 2, **kwargs) -> str:
        """Convert prompt to JSON string.
        
        Args:
            prompt (str): The prompt to convert.
            indent (Optional[int]): JSON indentation level.
            **kwargs: Additional metadata to include.
            
        Returns:
            str: JSON string representation.
        """
        result = self.convert(prompt, **kwargs)
        return json.dumps(result, indent=indent, ensure_ascii=False)


def convert_prompt_to_json(prompt: str, include_metadata: bool = True, **kwargs) -> Dict[str, Any]:
    """Convenience function to convert a prompt to JSON format.
    
    Args:
        prompt (str): The prompt to convert.
        include_metadata (bool): Whether to include metadata.
        **kwargs: Additional metadata to include.
        
    Returns:
        Dict[str, Any]: The converted prompt in JSON format.
    """
    converter = PromptConverter(include_metadata=include_metadata)
    return converter.convert(prompt, **kwargs)