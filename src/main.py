import subprocess
import sys
import os

def monitor_and_run(file_path):
    # Determine the interpreter based on the file extension
    ext = os.path.splitext(file_path)[1]
    interpreter = None

    if ext == '.py':
        interpreter = 'python3'
    elif ext == '.sh':
        interpreter = 'bash'
    elif ext == '.js':
        interpreter = 'node'
    else:
        print(f"Unsupported file type: {ext}")
        sys.exit(1)

    # Use subprocess to run `entr`
    try:
        print(f"Monitoring {file_path} for changes...")
        subprocess.run(f"ls {file_path} | entr -r {interpreter} {file_path}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 live_run.py <filename>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)

    monitor_and_run(file_path)


if __name__ == "__main__":
    main()