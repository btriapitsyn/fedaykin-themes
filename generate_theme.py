#!/usr/bin/env python3
"""
Theme Generator for VS Code
Generates a VS Code theme from a color palette and template file.
"""

import json
import sys
import os
import re
from pathlib import Path


def load_json_with_comments(file_path):
    """Load a JSON file that may contain comments."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Remove single-line comments
        content = re.sub(r'//.*?$', '', content, flags=re.MULTILINE)
        # Remove multi-line comments
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        return json.loads(content)


def replace_placeholders(template_content, colors):
    """Replace color placeholders in template with actual color values."""
    result = template_content
    
    # Replace color placeholders
    for color_key, color_value in colors.items():
        placeholder = f"{{{{{color_key}}}}}"
        result = result.replace(placeholder, color_value)
    
    # Replace theme name placeholder
    return result


def generate_theme(palette_path, template_path='themes/theme-template.json', output_dir='themes'):
    """Generate a theme file from a color palette and template."""
    
    # Load color palette
    try:
        palette = load_json_with_comments(palette_path)
    except Exception as e:
        print(f"Error loading color palette: {e}")
        sys.exit(1)
    
    # Extract palette name and colors
    palette_name = palette.get('name', 'Generated Theme')
    colors = palette.get('colors', {})
    
    # Load template
    template_path_full = Path(__file__).parent / template_path
    try:
        with open(template_path_full, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except Exception as e:
        print(f"Error loading template: {e}")
        sys.exit(1)
    
    # Replace placeholders
    theme_content = replace_placeholders(template_content, colors)
    
    # Replace theme name placeholder
    theme_content = theme_content.replace('{{THEME_NAME}}', palette_name)
    
    # Generate output filename from palette filename
    palette_basename = Path(palette_path).stem
    output_filename = f"{palette_basename}-color-theme.json"
    output_path = Path(__file__).parent / output_dir / output_filename
    
    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write theme file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(theme_content)
        print(f"✅ Successfully generated theme: {output_path}")
        print(f"   Theme name: {palette_name}")
        print(f"   Colors replaced: {len(colors)}")
    except Exception as e:
        print(f"Error writing theme file: {e}")
        sys.exit(1)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python generate_theme.py <color_palette_file>")
        print("Example: python generate_theme.py color_palettes/fedaykin-dark.json")
        sys.exit(1)
    
    palette_path = sys.argv[1]
    
    # Check if palette file exists
    if not os.path.exists(palette_path):
        print(f"Error: Color palette file not found: {palette_path}")
        sys.exit(1)
    
    # Generate theme
    generate_theme(palette_path)


if __name__ == "__main__":
    main()