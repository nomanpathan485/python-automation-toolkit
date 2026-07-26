<div align="center">

# 🐍 Python Automation Toolkit

**A curated collection of practical Python automation scripts — built while learning AI Systems Engineering.**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)]()
[![Maintenance](https://img.shields.io/badge/Maintained-Yes-green?style=for-the-badge)]()

[Overview](#-overview) • [Features](#-features) • [Quick Start](#-quick-start) • [Automations](#-current-automations) • [Roadmap](#-roadmap) • [Contributing](#-contributing) • [License](#-license)

</div>

---

## 📌 Overview

A growing collection of real-world Python automation scripts designed to eliminate repetitive tasks. Every tool follows modern Python best practices: type hints, safe defaults, and built-in dry-run modes so you can preview changes before they happen.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📂 **Smart Organization** | Auto-categorize files by extension into structured folders |
| 🛡️ **Dry-Run Mode** | Preview every action before any file is moved |
| 🔁 **Duplicate Safety** | Auto-rename to prevent accidental overwrites |
| ⚡ **Zero Dependencies** | Built entirely on the Python standard library |
| 🧩 **Modular Design** | Each tool lives in its own script — easy to extend |
| 🎯 **Type-Hinted** | Clean, self-documenting code throughout |

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/nomanpathan485/python-automation-toolkit.git
cd python-automation-toolkit
```

### 2. Run any script directly

```bash
python scripts/organize_folder.py
```

> 💡 **No external dependencies required** — everything runs on the Python standard library.

---

## 🛠️ Current Automations

### 📁 1. Smart Folder Organizer
> Sorts messy folders into clean, categorized subdirectories in one command.

**Supported categories:**

<table>
  <tr>
    <td>🖼️ <b>Images</b></td>
    <td><code>.jpg</code> <code>.jpeg</code> <code>.png</code> <code>.gif</code> <code>.webp</code></td>
  </tr>
  <tr>
    <td>📄 <b>Documents</b></td>
    <td><code>.pdf</code> <code>.doc</code> <code>.docx</code> <code>.txt</code></td>
  </tr>
  <tr>
    <td>📊 <b>Data</b></td>
    <td><code>.csv</code> <code>.xlsx</code> <code>.xls</code> <code>.json</code></td>
  </tr>
  <tr>
    <td>🎬 <b>Videos</b></td>
    <td><code>.mp4</code> <code>.mkv</code> <code>.avi</code> <code>.mov</code></td>
  </tr>
  <tr>
    <td>🎵 <b>Audio</b></td>
    <td><code>.mp3</code> <code>.wav</code> <code>.m4a</code></td>
  </tr>
  <tr>
    <td>🗜️ <b>Archives</b></td>
    <td><code>.zip</code> <code>.rar</code> <code>.7z</code></td>
  </tr>
  <tr>
    <td>📦 <b>Others</b></td>
    <td>Any uncategorized file</td>
  </tr>
</table>

**Enable dry-run mode** — open `scripts/organize_folder.py` and set:

```python
DRY_RUN = True
```

**Example output:**

```
[DRY RUN] report.pdf → Documents/
[DRY RUN] photo.jpg  → Images/
[DRY RUN] data.csv   → Data/
Moved: archive.zip   → Archives/
```

---

## 🗂️ Project Structure

```
python-automation-toolkit/
├── 📂 scripts/
│   └── 🐍 organize_folder.py     # Smart folder organizer
├── 📂 src/                       # Reserved for shared utilities
├── 📄 README.md
├── 📄 requirements.txt
└── 🙈 .gitignore
```

---

## 🧰 Tech Stack

- **Language:** Python 3.8+
- **Core modules:** `pathlib`, `shutil`
- **External libs:** None — 100% standard library

---

## 🗺️ Roadmap

| Status | Automation | Description |
|:---:|---|---|
| ✅ | **Folder Organizer** | Sort files by extension into categories |
| 📝 | **Bulk File Renamer** | Pattern-based renaming across folders |
| 📝 | **CSV Processor** | Clean, merge, and transform CSV files |
| 📝 | **PDF Merger** | Combine multiple PDFs into one |
| 📝 | **API Data Fetcher** | Pull and cache data from REST APIs |
| 📝 | **Image Converter** | Batch format/size conversion |
| 📝 | **Duplicate Finder** | Detect and remove duplicate files |

> ✅ Complete &nbsp;&nbsp; 🚧 In Progress &nbsp;&nbsp; 📝 Planned

---

## 🤝 Contributing

Contributions, ideas, and feedback are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-tool`)
3. Commit your changes (`git commit -m 'Add amazing tool'`)
4. Push to the branch (`git push origin feature/amazing-tool`)
5. Open a Pull Request

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](./LICENSE) for more information.

---

## 👤 Author

**Built as part of an AI Systems Engineer learning journey.**

⭐ If this toolkit helped you automate something tedious, consider giving it a star!

</div>
