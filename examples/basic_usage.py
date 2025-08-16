#!/usr/bin/env python3
"""Basic usage examples for prompt2json library."""

from prompt2json import convert_prompt_to_json, PromptConverter
import json


def example_basic_conversion():
    """Demonstrate basic prompt conversion."""
    print("=== Basic Conversion Example ===")
    
    prompt = "Create a Python function that calculates fibonacci numbers"
    result = convert_prompt_to_json(prompt)
    
    print(f"Original prompt: {prompt}")
    print("\nConverted JSON:")
    print(json.dumps(result, indent=2))
    print()


def example_advanced_usage():
    """Demonstrate advanced converter usage."""
    print("=== Advanced Usage Example ===")
    
    # Create converter with custom settings
    converter = PromptConverter(include_metadata=True)
    
    prompt = "Write a REST API in Python using Flask with authentication"
    result = converter.convert(
        prompt,
        project_type="web_api",
        difficulty="intermediate",
        framework="flask"
    )
    
    print(f"Prompt: {prompt}")
    print("\nResult with custom metadata:")
    print(json.dumps(result, indent=2))
    print()


def example_batch_processing():
    """Demonstrate batch processing."""
    print("=== Batch Processing Example ===")
    
    prompts = [
        "Create a database schema for an e-commerce site",
        "Write unit tests for a calculator class",
        "Deploy a web application to AWS using Docker",
        "Implement user authentication with JWT tokens"
    ]
    
    converter = PromptConverter(include_metadata=False)
    results = converter.convert_batch(prompts, category="development")
    
    print(f"Processing {len(prompts)} prompts...")
    for i, result in enumerate(results, 1):
        print(f"\nPrompt {i}:")
        print(f"  Text: {result['prompt'][:50]}...") 
        print(f"  Word count: {result['word_count']}")
        print(f"  Has instructions: {result['analysis']['has_instructions']}")
        print(f"  Language hints: {result['analysis']['language_hints']}")
    print()


def example_json_string_output():
    """Demonstrate JSON string output."""
    print("=== JSON String Output Example ===")
    
    converter = PromptConverter(include_metadata=False)
    prompt = "Explain machine learning concepts for beginners"
    
    # Get formatted JSON string
    json_string = converter.to_json_string(prompt, indent=4)
    
    print(f"Prompt: {prompt}")
    print("\nFormatted JSON string:")
    print(json_string)
    print()


def example_analysis_features():
    """Demonstrate prompt analysis features."""
    print("=== Analysis Features Example ===")
    
    test_prompts = [
        "How do I create a web scraper in Python?",
        "Build a chatbot using TensorFlow and deploy it.",
        "```python\ndef hello():\n    print('world')\n```",
        "What is the difference between SQL and NoSQL databases?"
    ]
    
    converter = PromptConverter(include_metadata=False)
    
    for prompt in test_prompts:
        result = converter.convert(prompt)
        analysis = result['analysis']
        
        print(f"Prompt: {prompt[:40]}...")
        print(f"  Has questions: {analysis['has_questions']}")
        print(f"  Has instructions: {analysis['has_instructions']}")
        print(f"  Contains code: {analysis['contains_code']}")
        print(f"  Language hints: {analysis['language_hints']}")
        print(f"  Sentences: {analysis['sentences']}")
        print()


if __name__ == "__main__":
    print("prompt2json Library Examples\n")
    
    example_basic_conversion()
    example_advanced_usage()
    example_batch_processing()
    example_json_string_output()
    example_analysis_features()
    
    print("All examples completed!")