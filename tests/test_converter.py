#!/usr/bin/env python3
"""Tests for prompt2json converter module."""

import pytest
import json
from prompt2json import PromptConverter, convert_prompt_to_json


class TestPromptConverter:
    """Test cases for PromptConverter class."""
    
    def test_basic_conversion(self):
        """Test basic prompt conversion."""
        converter = PromptConverter()
        prompt = "Create a Python function"
        result = converter.convert(prompt)
        
        assert result["prompt"] == prompt
        assert result["length"] == len(prompt)
        assert result["word_count"] == 4
        assert "metadata" in result
        assert "analysis" in result
    
    def test_without_metadata(self):
        """Test conversion without metadata."""
        converter = PromptConverter(include_metadata=False)
        result = converter.convert("Test prompt")
        
        assert "metadata" not in result
        assert "analysis" in result
    
    def test_analysis_features(self):
        """Test prompt analysis features."""
        converter = PromptConverter()
        
        # Test question detection
        result = converter.convert("How do I create a function?")
        assert result["analysis"]["has_questions"] is True
        
        # Test instruction detection
        result = converter.convert("Please create a function")
        assert result["analysis"]["has_instructions"] is True
        
        # Test code detection
        result = converter.convert("Here is code: ```python\nprint('hello')\n```")
        assert result["analysis"]["contains_code"] is True
        
        # Test language hints
        result = converter.convert("Create a Python script")
        assert "python" in result["analysis"]["language_hints"]
    
    def test_batch_processing(self):
        """Test batch processing functionality."""
        converter = PromptConverter()
        prompts = ["First prompt", "Second prompt", "Third prompt"]
        results = converter.convert_batch(prompts)
        
        assert len(results) == 3
        for i, result in enumerate(results):
            assert result["prompt"] == prompts[i]
    
    def test_json_string_output(self):
        """Test JSON string output."""
        converter = PromptConverter()
        prompt = "Test prompt"
        json_string = converter.to_json_string(prompt)
        
        # Should be valid JSON
        parsed = json.loads(json_string)
        assert parsed["prompt"] == prompt
    
    def test_custom_metadata(self):
        """Test custom metadata inclusion."""
        converter = PromptConverter()
        result = converter.convert(
            "Test prompt",
            custom_field="custom_value",
            project_type="test"
        )
        
        metadata = result["metadata"]
        assert metadata["custom_field"] == "custom_value"
        assert metadata["project_type"] == "test"
    
    def test_empty_prompt(self):
        """Test handling of empty prompts."""
        converter = PromptConverter()
        result = converter.convert("")
        
        assert result["prompt"] == ""
        assert result["length"] == 0
        assert result["word_count"] == 0
    
    def test_invalid_input(self):
        """Test handling of invalid input."""
        converter = PromptConverter()
        
        with pytest.raises(ValueError):
            converter.convert(None)
        
        with pytest.raises(ValueError):
            converter.convert(123)


class TestConvenienceFunction:
    """Test cases for convenience function."""
    
    def test_convert_prompt_to_json(self):
        """Test the convenience function."""
        prompt = "Test prompt"
        result = convert_prompt_to_json(prompt)
        
        assert result["prompt"] == prompt
        assert "metadata" in result
        assert "analysis" in result
    
    def test_convert_without_metadata(self):
        """Test convenience function without metadata."""
        result = convert_prompt_to_json("Test", include_metadata=False)
        assert "metadata" not in result
    
    def test_convert_with_custom_metadata(self):
        """Test convenience function with custom metadata."""
        result = convert_prompt_to_json(
            "Test",
            custom_field="value"
        )
        assert result["metadata"]["custom_field"] == "value"


if __name__ == "__main__":
    pytest.main([__file__])