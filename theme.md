# Helium Forest: Syntax Highlighting Specification

The "Helium Forest" theme is designed to evoke a modern, minimalist, and lush atmosphere using a palette of greens.

| Token Category | Recommended Color | Hex Code | Visual Description |
| :--- | :--- | :--- | :--- |
| **Keywords** (`func`, `let`, `if`, `else`, `return`) | Highland Emerald Pastel | `#66DDAA` | A vibrant yet soft emerald green. |
| **Strings** | Soft Mint Green | `#AAFFCC` | A very light, refreshing mint. |
| **Numbers & Literals** (`true`, `false`, `null`) | Lime Neon Green | `#CCFF00` | A high-contrast, energetic lime green. |
| **Variables & Identifiers** | Off-White / Sage White | `#F0FDF4` | A neutral with a tiny hint of green. |
| **Comments** | Faded Moss Green | `#8FA98F` | A muted, desaturated green for low visibility. |
| **Operators** (`=`, `+`, `{`, `}`) | Dark Forest Accent | `#2D5A27` | Deep green for structural elements. |
| **Background** | Deep Jungle Night | `#0B120B` | A near-black with deep green undertones. |

## Implementation Tips (VS Code / Prism.js)
For a truly "Forest" feel:
1.  **Glow Effect**: Add a subtle `text-shadow` or `drop-shadow` to the Lime Neon tokens to make them feel "electric".
2.  **Font**: Use a clean, sans-serif monospace font like *JetBrains Mono* or *Fira Code* to maintain the minimalist philosophy.
