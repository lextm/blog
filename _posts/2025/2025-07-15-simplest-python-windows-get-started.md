---
layout: post
title: "The Simplest Python on Windows Get Started Guide"
description: "A step-by-step, beginner-friendly guide to installing and running Python on Windows 10/11, avoiding common pitfalls like the Windows Store version, and getting your first script running in minutes. Perfect for new developers, students, and anyone curious about Python."
tags: python windows
categories: [Tools and Platforms]
excerpt_separator: <!--more-->
---

## The Simplest Python on Windows Get Started Guide

Getting started with Python on Windows can be confusing, especially with multiple installation options and the Windows Store version lurking in the background. This guide walks you through the cleanest, most reliable way to install and run Python on Windows 10 or 11—only some prior experience required.

<!--more-->

### Why Use Python on Windows?

Python is a powerful, easy-to-learn programming language used for automation, data analysis, web development, and more. Windows users can take advantage of Python’s versatility for both personal and professional projects.

### Step 1: Download Python (Official Website Only)

Go to the [official Python website][python-download] and download the latest stable Windows installer (choose the 64-bit version unless you have a specific reason not to).

- **Do not use the Microsoft Store version.** It can cause confusion due to Windows “app execution aliases” and the isolation feature from Microsoft Store apps.
- Save the installer to your Downloads folder.

### Step 2: Install Python (No PATH Option)

Run the installer. On the first screen:

- **Do NOT check “Add Python to PATH.”**
- Click “Install Now” (or “Customize installation” if you want to change the install location).

> **Why not add Python to PATH?**
> Adding Python to PATH can cause conflicts with the Windows Store version or other Python installations, leading to confusing errors. For beginners, it's safer to avoid this option and use the full path or Start Menu shortcuts.

This avoids conflicts with the Windows Store version and keeps your system PATH clean at least for now.

### Step 3: Run Python

After installation, you can run Python in several ways:

- Use the **Start Menu**: Search for “Python” and select the version you just installed (e.g., “Python 3.12 (64-bit)”).
- Or, open Command Prompt and run Python using its full path, e.g.:

```sh
"C:\Users\YourName\AppData\Local\Programs\Python\Python312\python.exe"
```

Replace `YourName` and `Python312` with your actual username and Python version.

> 💡 **Hint:** For portability, you can use Windows environment variables in your command. For example:
>
> ```sh
> "%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
> ```

### Step 4: Write and Run Your First Script

Open Notepad, type:

```python
print("Hello, Python on Windows!")
```

Save as `hello.py` in your Documents folder. Then, in Command Prompt:

```sh
"C:\Users\YourName\AppData\Local\Programs\Python\Python312\python.exe" hello.py
```

You should see your message printed.

### Step 5: Installing Packages with pip

To install packages, use the full path to `pip.exe` (in the same folder as `python.exe`):

```sh
"C:\Users\YourName\AppData\Local\Programs\Python\Python312\Scripts\pip.exe" install requests
```

This method is especially helpful if you have multiple Python versions installed or want to avoid issues with `pip.exe` not being found.

> 💡 **Hint:** Alternatively, you can run `pip` via Python to ensure you're using the correct installation:
>
> ```sh
> "C:\Users\YourName\AppData\Local\Programs\Python\Python312\python.exe" -m pip install requests
> ```

### Step 6: Using IDLE or VS Code (Optional)

- **IDLE**: Comes with Python. Find it in the Start Menu.
- **VS Code**: Download from [Visual Studio Code][vscode-download] and install the [Python extension][vscode-python]. Then finish this great [get started guide][vscode-python-get-started] to set up Python development.

### Troubleshooting: Windows Store Python & PATH Issues

If you see errors like “Python not found” or a Microsoft Store window opens when you type `python`, you may have the Windows Store “app execution alias” enabled. To fix:

1. Open **Settings > Apps > Advanced app settings > App execution aliases**.
2. Turn off the toggles for `python.exe` and `python3.exe` (They might show as App Installer items).
3. Always use the full path to your installed Python, or launch from the Start Menu.

### Next Steps: Virtual Environments and Better Python Management

Once you're comfortable running Python scripts, you'll want to learn about virtual environments. Virtual environments let you isolate project dependencies, making your Python work more reliable and organized.

Popular tools to explore next:

- **venv**: Built-in tool for creating virtual environments ([docs][venv-docs]).
- **poetry**: Modern dependency and packaging manager for Python ([docs][poetry-docs]).
- **uv**: A fast Python package installer and environment manager ([docs][uv-docs]).

These tools help you avoid dependency conflicts and keep your projects tidy. Check out their documentation to level up your Python workflow!

### Conclusion

You’re now ready to explore Python on Windows! For more tips and guides, check out my other posts tagged [Python](/tags/python/).

Have questions or tips to share? Leave a comment below—your feedback helps others!

[python-download]: https://www.python.org/downloads/windows/
[vscode-download]: https://code.visualstudio.com/
[vscode-python]: https://marketplace.visualstudio.com/items?itemName=ms-python.python
[vscode-python-get-started]: https://code.visualstudio.com/docs/python/python-quick-start
[venv-docs]: https://docs.python.org/3/library/venv.html
[poetry-docs]: https://python-poetry.org/docs/
[uv-docs]: https://github.com/astral-sh/uv#readme
