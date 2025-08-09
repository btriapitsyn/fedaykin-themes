# Fedaykin Themes for VS Code

A comprehensive collection of Dune-inspired themes for Visual Studio Code - from dark atmospheric palettes to warm light themes.

## Themes Included (17 Total)

### House & Faction Themes
- **Dune Giedi Prime** - A stark industrial monochrome theme with subtle pastel accents
- **Dune Harkonnen** - A dark industrial theme with cold blues and purples inspired by the brutalist Harkonnen homeworld
- **Dune House Atreides** - The noble house from oceanic Caladan - deep ocean blues, sea greens, silver nobility, and misty grays
- **Dune Sardaukar Imperial** - The Emperor's elite forces - imperial purple and gold with crimson ruthlessness
- **Dune Bene Gesserit** - The mystical sisterhood - midnight blues, silver robes, and subtle gold wisdom

### Character Themes
- **Dune Muad'Dib** - Paul's desert leadership - fierce Fremen blue eyes, royal purples, and survival greens
- **Dune Fremen Sietch** *(Light Theme)* - Desert survival - warm beige backgrounds with earth tones and precious water blues

### Planet Themes  
- **Dune Arrakis Incandescent** - A warm desert theme with glowing incandescent tones - golden spice and sunset rose
- **Dune Sandworm** - Inspired by the great makers - sandy beiges, deep earth browns, and electric spice blue
- **Dune Caladan Storm** - The tempestuous Atreides homeworld - storm grays, ocean navy, and lightning blues
- **Dune Salusa Secundus** - The prison planet that forged the Sardaukar - volcanic reds, ash grays, and molten metal
- **Dune Ix Technology** - The machine planet - sleek metallics, circuit greens, and holographic purples

### Guild & Commerce Themes
- **Dune Guild Navigator** - Spice-mutated navigators - deep space blacks, nebula purples, and bright orange spice gas
- **Dune Spacing Guild** - Interstellar commerce - corporate steel grays, gold wealth accents, and technology blues

### Mystical & Mental Themes
- **Dune Water of Life** - The sacred transformation - luminous blues, ethereal whites, and transcendent purples
- **Dune Mentat** *(Light Theme)* - Human computers - clean whites, Sapho juice reds, and precise computational blues
- **Dune Spice Vision** - Prescient visions and spice trance - golden amber base, electric blue flashes, mystical purples, and shifting oranges

## Installation

### From VS Code Marketplace

1. Open VS Code
2. Go to Extensions (Cmd+Shift+X / Ctrl+Shift+X)
3. Search for "Fedaykin"
4. Click Install

### Manual Installation

1. Download the `.vsix` file from the releases
2. Open VS Code
3. Go to Extensions
4. Click the "..." menu and select "Install from VSIX..."
5. Select the downloaded file

### From Source

1. Clone this repository
2. Run `npm install -g vsce` if you don't have it
3. Run `vsce package` to build the extension
4. Install the generated `.vsix` file

## Selecting a Theme

1. Open VS Code
2. Press `Cmd+K, Cmd+T` (Mac) or `Ctrl+K, Ctrl+T` (Windows/Linux)
3. Search for "Dune" to see all available themes
4. Select your preferred theme

## Features

- 🎨 Unified 46-color palette for consistency
- 👁️ Optimized contrast for reduced eye strain
- 🔧 Complete VS Code UI theming
- 📝 Enhanced support for JavaScript, TypeScript, Python, HTML/CSS, JSON, Markdown, and more
- 🌙 15 dark themes and 2 light themes
- 🏜️ Each theme tells a story from the Dune universe

## Development

### Adding New Themes

1. Create a color palette file in `color_palettes/`:
   - Use `color_palettes/palette-template.json` as a base
   - Define all 46 required colors
   - Add descriptive comments for each color's purpose

2. Generate the theme:
```bash
python3 generate_theme.py color_palettes/your-palette.json
```

3. Update `package.json` to include the new theme

### Color Palette System

The themes use a unified 46-color system:
- **Colors 1-6**: Background colors (darkest to lightest)
- **Colors 7-8**: Borders and dividers
- **Colors 9-13**: Text hierarchy (brightest to dimmest)
- **Colors 14-19**: Syntax highlighting (different token types)
- **Colors 20-24**: Semantic state colors (errors, warnings, info, success)
- **Colors 25-26**: UI accent colors
- **Colors 27-29**: Terminal special colors
- **Colors 30-46**: Transparencies and overlays

## Design Philosophy

These themes follow the principle of **narrative-driven design**:
- Carefully calibrated contrast for reduced eye strain
- Semantic color consistency across all themes
- Color intensity that matches each theme's inspiration - from subtle monochromes to vibrant spice oranges
- Context-aware contrast levels for different UI elements
- Accessibility through proper luminance ratios
- Each theme tells a story from the Dune universe through its color choices

## Customization

Override specific colors in your settings:

```json
{
  "workbench.colorCustomizations": {
    "[Dune Arrakis Incandescent]": {
      "editor.background": "#0A0A0A"
    }
  }
}
```

## Links

- [GitHub Repository](https://github.com/btriapitsyn/fedaykin-themes)
- [Report Issues](https://github.com/btriapitsyn/fedaykin-themes/issues)

## License

MIT

## Author

FedaykinDev

---

**"The spice must flow"**