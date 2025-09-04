import subprocess
import os

# ========================
# ANSI Color Codes
# ========================
BOLD = "\033[1m"
RESET = "\033[0m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
GREEN = "\033[1;32m"
MAGENTA = "\033[1;35m"
BLUE = "\033[1;34m"

# ========================
# Paths
# ========================
home_dir = os.path.expanduser("~")
project_dir = os.path.join(home_dir, "first_project")
yt_dlp_path = os.path.join(project_dir, "yt-dlp")
os.chmod(yt_dlp_path, 0o755)

# ========================
# User input
# ========================
url = input(f"{BOLD}{CYAN}Enter The Video Link: {RESET}")

# ========================
# Fetch video title
# ========================
result = subprocess.run([yt_dlp_path, "--get-title", url], capture_output=True, text=True)
title = result.stdout.strip()
print(f"{BOLD}{CYAN}Video Title: {title}{RESET}")

new_title = input(f"{BOLD}{YELLOW}You Can Change Video Title: {RESET}")
if new_title.strip():
    title = new_title.strip()

# ========================
# Download type
# ========================
print(f"{BOLD}{GREEN}Select Download Type:{RESET}")
print("1. Video (with audio, single file)")
print("2. Audio only")
choice = input(f"{BOLD}{GREEN}Enter 1 or 2: {RESET}")

# ========================
# Download
# ========================
if choice == "1":
    output_file = os.path.join(project_dir, f"{title}.mp4")
    subprocess.run([
        yt_dlp_path,
        "-f", "best",           # single file, video + audio
        "-o", output_file,
        url
    ])
elif choice == "2":
    output_file = os.path.join(project_dir, f"{title}.%(ext)s")
    subprocess.run([
        yt_dlp_path,
        "-f", "bestaudio",      # only audio
        "-o", output_file,
        url
    ])
else:
    print(f"{BOLD}{YELLOW}Invalid choice!{RESET}")
    exit()

print(f"{BOLD}{GREEN}Download Completed!{RESET}")
