# Watcher

**Watcher** is a lightweight Python package designed for developers who prefer hot-reloading files from the terminal. It uses the `entr` package with Python's `subprocess` module to watch files for changes and automatically execute them, displaying real-time output and tracebacks directly in the terminal. Unlike pytest, **Watcher** provides a minimal setup for running and debugging your scripts in real-time.

## Features

- **Hot-reloading**: Automatically re-execute your script whenever changes are detected.
- **Real-time feedback**: See output and tracebacks immediately in the terminal.
- **Lightweight**: No need for complex configurations or dependencies like pytest.

## Installation

1. **Install `entr`**:
   Ensure that the `entr` utility is installed on your system:

   ```bash
   # On Debian/Ubuntu
   sudo apt-get install entr

   ```

2. **Install Watcher**:
   You can install the Watcher package using pip:

   ```bash
   pip install watcher
   ```

## Usage

Once installed, you can use the `watcher` command to monitor and execute a script whenever it changes:

```bash
watcher /path/to/your/script.py
```

This command will monitor the specified file and automatically re-run it each time you save changes, providing real-time feedback in the terminal.

## Example

If you have a Python script called `example.py`:

```python
# example.py
print("Hello, World!")
```

Run the following command to start watching the file:

```bash
watcher example.py
```

Now, every time you edit and save `example.py`, **Watcher** will re-run it, and you’ll immediately see the output in your terminal.

## Why Watcher?

- **Simplify debugging**: Skip the overhead of test frameworks when you just need quick feedback.
- **Terminal-friendly**: Stay in your terminal environment and avoid switching contexts.
- **Minimal setup**: Just install and start using it—no configuration required