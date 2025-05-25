# 🧠 openFlask — OpenManus Flask API  
### Part of **Platform-IO** (Salam Hack 2025)

---

## 🔍 Overview

This is a **lightweight Flask API wrapper** for [OpenManus](https://github.com/mannaandpoem/OpenManus), created as part of the larger **Platform-IO** system during **Salam Hack 2025**.

It allows users to send natural language-style commands (e.g., `"Create a file named report.py"`) to OpenManus via HTTP. The command is passed to `OpenManus/main.py`, executed, and the result is returned.

---

## ⚠️ Disclaimer

⚠️ This project uses OpenManus, which was not created by us.  
This Flask wrapper (`server.py`) is simply a bridge built for quick integration during Salam Hack 2025.  
All credit for OpenManus goes to its original developers.

---

## ✨ Features

- 🪶 Minimal HTTP bridge to OpenManus
- 💬 Accepts user commands and runs them through the OpenManus interface
- 🧩 Simple structure, no extra layers — just enough to connect and test

---

## 📁 File Structure

openFlask/  
├── server.py # Flask API server  
├── requirements.txt # Python dependencies  
├── output/ # Output folder for generated files  
└── OpenManus/ # Cloned OpenManus repo (required for execution)

---

## 📦 Installation

This project requires [OpenManus](https://github.com/mannaandpoem/OpenManus) to be installed and configured separately.  
Below are two official installation methods from the OpenManus documentation. **Method 2 (using `uv`) is recommended.**

🛑 **You must follow all steps in the OpenManus repo first before coming back here.**

---

## 🚀 Run the Flask API

After setting up OpenManus, navigate to this project:

```bash
cd ~/openFlask
pip install -r requirements.txt
python server.py
```

Your API will be live at: [http://localhost:5000](http://localhost:5000)

---

## 🔌 API Endpoint

**POST /process**

Send a natural language-style command for processing via OpenManus.

### Example Request

```json
{
  "command": "Create a file named hello.txt"
}
```

### Example cURL

```bash
curl -X POST http://localhost:5000/process \
     -H "Content-Type: application/json" \
     -d '{"command": "Create a file named hello.txt"}'
```

### Example Response

```json
{
  "output": "...stdout or error from OpenManus...",
  "success": true
}
```

---

## 📄 License

- **OpenManus:** Subject to its own license — see their repository.
- **This Flask wrapper (server.py, etc.):** MIT License

---

## 🙏 Credits

- ✍️ OpenManus by [@mannaandpoem](https://github.com/mannaandpoem)
- 🚀 Built as part of Platform-IO @ Salam Hack 2025
