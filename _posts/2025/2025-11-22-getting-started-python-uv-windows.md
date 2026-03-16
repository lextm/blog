---
layout: post
title: "Get Started with Python on Windows Using uv"
description: "Learn how to install uv on Windows, manage CPython versions, bootstrap a project, add dependencies, and run scripts with uv run and uv sync."
image:
  path: /images/office-lights-downtown-toronto.jpg
  alt: Copyright © Lex Li. Office lights glowing over downtown Toronto at dusk.
tags: python windows
categories: [Tools and Platforms]
excerpt_separator: "<!--more-->"
---

This short guide shows how to use `uv` on Windows to manage Python versions, create a tiny virtual environment, and run a small script. `uv` is a lightweight utility that makes it easy to install specific Python builds and set up per-project environments without heavy installers. If you prefer the classic tooling approach, see [my earlier walkthrough that sticks to the traditional Python workflow]({% post_url 2025/2025-07-15-simplest-python-windows-get-started %}).

<!--more-->

## Why `uv`?

- **Small and focused**: `uv` installs specific CPython builds without extra baggage.
- **Fast**: Downloads pre-built artifacts and sets up environments quickly.
- **Scriptable**: Works well in CI or scripted developer workflows once you get more familiar with Python.

## Install `uv` on Windows

`uv` ships as a standalone Rust binary, and the official Windows installer is a PowerShell script hosted by the project. Open an elevated terminal and run:

```powershell
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

> The script downloads the latest release and places `uv.exe` under `%USERPROFILE%\.local\bin`. If that directory is not on your `PATH`, follow the prompt the installer prints or add it manually via *System Properties → Environment Variables*.

Once the script finishes, close and reopen PowerShell, then confirm the installation:

```powershell
uv --version
```

## Install a specific Python version

List available versions:

```powershell
uv list
```

Install a specific version (for example CPython 3.11.6):

```powershell
uv install 3.11.6
```

Make that version the default for the current shell session:

```powershell
uv use 3.11.6
```

Verify:

```powershell
python --version
```

> Note that Python releases older than 3.10 are deprecated right now, so you should pick versions accordingly.
>
> Also note that people used to use other ways to install Python on Windows, such as the Microsoft Store or the official installer from python.org, or `pyenv-windows`. `uv` provides a unified way as it also supports virtual environments and dependency management.

## Build a tiny project with `uv`

`uv` likes to manage everything through a project file and lockfile. Create a folder, initialize the project, and add dependencies in one go:

```powershell
mkdir hello-uv
cd hello-uv
uv init
uv add requests
```

`uv` generates `pyproject.toml` and `uv.lock` to capture the dependencies.

Create a simple script (`app.py`) in this `hello-uv` folder that uses `requests`:

```python
import requests

def main():
    response = requests.get('https://astral.sh/uv')
    print(f'Status: {response.status_code}')
    print(f'Body: {response.text[:60]}...')

if __name__ == '__main__':
    main()
```

Run the script using `uv run`. `uv` resolves dependencies, creates an isolated environment on the fly, and executes the script:

```powershell
uv run python app.py
```

> Equivalent commands are `uv run app.py` or `uv run python3 app.py`.

## (Optional) Cleanup

To remove a Python version installed by `uv`, run:

```powershell
uv uninstall 3.11.6
```

Remove the `.venv` folder if you want a fresh install next time.

## Notes and alternatives

- Add development-only dependencies with commands like `uv add --dev pytest` and run them via `uv run pytest`. To sync dev dependencies for CI, include the `--dev` flag: `uv sync --dev`.
- Read the official `uv` docs for deeper dives: [installation guide](https://docs.astral.sh/uv/getting-started/installation/), [projects workflow](https://docs.astral.sh/uv/guides/projects/), and the [command reference](https://docs.astral.sh/uv/reference/cli/).
- Explore more commands such as `uv self update`, `uv tool`, and the drop-in `uv pip` interface to cover advanced scenarios.
- Note that for production or CI, resolve everything once and sync environments from the lockfile:

  ```powershell
  uv sync
  ```

  That installs dependencies into `.venv` automatically (no manual activation required). Subsequent `uv run python app.py` executions reuse that environment.
