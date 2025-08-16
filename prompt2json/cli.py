"""Command-line interface for prompt2json."""

import argparse
import json
import sys
from typing import Optional

from .converter import PromptConverter


def main() -> None:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Convert prompts to JSON format",
        prog="prompt2json"
    )
    
    parser.add_argument(
        "prompt",
        nargs="?",
        help="The prompt to convert (if not provided, reads from stdin)"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Output file path (if not provided, prints to stdout)"
    )
    
    parser.add_argument(
        "--no-metadata",
        action="store_true",
        help="Exclude metadata from the output"
    )
    
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="JSON indentation level (default: 2)"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )
    
    args = parser.parse_args()
    
    # Get the prompt
    if args.prompt:
        prompt = args.prompt
    else:
        # Read from stdin
        try:
            prompt = sys.stdin.read().strip()
            if not prompt:
                print("Error: No prompt provided", file=sys.stderr)
                sys.exit(1)
        except KeyboardInterrupt:
            print("\nOperation cancelled", file=sys.stderr)
            sys.exit(1)
    
    # Convert the prompt
    try:
        converter = PromptConverter(include_metadata=not args.no_metadata)
        result = converter.convert(prompt)
        json_output = json.dumps(result, indent=args.indent, ensure_ascii=False)
        
        # Output the result
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(json_output)
            print(f"Output written to {args.output}")
        else:
            print(json_output)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()