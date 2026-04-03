# Helium (.ium) 🌿

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Minimalist](https://img.shields.io/badge/Style-Minimalist-green.svg)](https://github.com/alanthecoderishere/Helium)

Helium is a minimalist, hybrid programming language that combines the readability of **JSON** for data with the simplicity of **Python** for logic. It's designed to be lightweight, stable, and incredibly easy to read.

## ✨ Key Features
- **Clean Style**: Declarations use `=` without `let` for maximum clarity.
- **JSON-Native**: Handle complex data structures naturally with curly braces `{}` and optional trailing commas.
- **Cross-Platform**: Unified `ium` launcher for Windows, Linux, and macOS.
- **VS Code Support**: Syntax highlighting with the official **Helium Forest** theme.

---

## 🎨 VS Code Syntax Highlighting

To enable the lush **Helium Forest** theme and syntax highlighting for `.ium` files:

1.  Navigate to your VS Code extensions folder:
    - **macOS/Linux**: `~/.vscode/extensions/`
    - **Windows**: `%USERPROFILE%\.vscode\extensions\`
2.  Copy the `vscode-helium` folder from this repository into that extensions folder.
3.  Restart VS Code.
4.  Open any `.ium` file and select the **Helium Forest** theme from the Command Palette (`Ctrl/Cmd + Shift + P` -> "Color Theme").

---

## 🚀 Quick Start

### 1. Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/alanthecoderishere/Helium.git
cd Helium
pip install -r requirements.txt
```

### 2. Setup the `ium` Command
Run the setup script for your operating system:

**For Linux & macOS:**
```bash
chmod +x setup.sh
./setup.sh
# Then restart your terminal or run: source ~/.zshrc
```

**For Windows:**
- Run `setup.bat` and follow the instructions to add the folder to your **Path**.

### 3. Run an Example
```bash
ium examples/test.ium
```

---

## 📖 Language Syntax at a Glance

### Variables & Data
```helium
# Simple assignment
name = "Helium"
version = 1.0

# Nested Objects (JSON Style)
config = {
    "status": "ready",
    "tags": ["hybrid", "clean",]
}
```

### Functions & Logic
```helium
func greet(target) {
    print("Welcome to " + target)
}

if version > 0 {
    greet(name)
}
```

---

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📄 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

*Made with 💚 by alanthecoderishere and the Helium Community.*
