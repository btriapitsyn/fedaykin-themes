#!/usr/bin/env python3
"""
Convert SVG icon to PNG for VS Code extension.
Requires: pip install cairosvg pillow
"""

try:
    import cairosvg
    from PIL import Image
    import io
    
    # Convert SVG to PNG
    png_data = cairosvg.svg2png(
        url='images/icon.svg',
        output_width=128,
        output_height=128
    )
    
    # Save as PNG
    with open('images/icon.png', 'wb') as f:
        f.write(png_data)
    
    print("✅ Successfully converted icon.svg to icon.png")
    
except ImportError:
    print("❌ Missing required packages. Please install:")
    print("   pip install cairosvg pillow")
    print("\nAlternatively, you can:")
    print("1. Use an online SVG to PNG converter")
    print("2. Open the SVG in a browser and take a screenshot")
    print("3. Use ImageMagick: convert images/icon.svg images/icon.png")