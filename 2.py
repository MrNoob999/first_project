import subprocess
import os
import re

# ANSI Color Codes
BOLD = "\033[1m"
RESET = "\033[0m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
GREEN = "\033[1;32m"
MAGENTA = "\033[1;35m"
BLUE = "\033[1;34m"

home_dir = os.path.expanduser("~")
yt_dlp_path = os.path.join(home_dir, "yt-dlp")

# Colored Input / Output

# Colored Input / Output

# Video link input
url = input(f"{BOLD}{CYAN}Enter The video Link: {RESET}")

# Vide title fetch (subprocess clean, no color in command)
result = subprocess.run([yt_dlp_path, "--get-title", url], capture_output=True, text=True)
title = result.stdout.strip()

# Display title with color
print(f"{BOLD}{CYAN}Video Title: {title}{RESET}")

# Title edit input
new_title = input(f"{BOLD}{YELLOW}You Can Change Video Title: {RESET}")
if new_title.strip():
    title = new_title.strip()




# Download type
print(f"{BOLD}{GREEN}Select Download Type:{RESET}")
print("1. Video")
print("2. Audio")
choice = input(f"{BOLD}{GREEN}Enter 1 or 2: {RESET}")

# Get available formats
formats = subprocess.run([yt_dlp_path, "-F", url], capture_output=True, text=True)
formats_output = formats.stdout

# Parse formats for Video or Audio
video_formats = []
audio_formats = []

for line in formats_output.splitlines():
    if re.match(r"^\d+", line):
        parts = line.split()
        format_id = parts[0]
        ext = parts[1]
        res = parts[2] if len(parts) > 2 else ""
        filesize = ""
        for p in parts:
            if "MB" in p or "KB" in p or "GB" in p:
                filesize = p
        if "audio" in line.lower() and "video" not in line.lower():
            audio_formats.append((format_id, ext, filesize))
        elif "video" in line.lower():
            video_formats.append((format_id, res, filesize))

# Display formats
if choice == "1" and video_formats:
    print(f"{BOLD}{MAGENTA}Video Format{RESET}")
    for i, f in enumerate(video_formats, 1):
        print(f"{BOLD}{MAGENTA}{i}. {f[1]}  {f[2]}{RESET}")
    sel = int(input(f"{BOLD}{YELLOW}Enter The Serial Number: {RESET}")) - 1
    format_code = video_formats[sel][0]

elif choice == "2" and audio_formats:
    print(f"{BOLD}{MAGENTA}Audio Format{RESET}")
    for i, f in enumerate(audio_formats, 1):
        print(f"{BOLD}{MAGENTA}{i}. {f[1]}  {f[2]}{RESET}")
    sel = int(input(f"{BOLD}{YELLOW}Enter The Serial Number: {RESET}")) - 1
    format_code = audio_formats[sel][0]

else:
    print(f"{BOLD}{YELLOW}Wrong Input or Couldn't Find{RESET}")
    exit()

# Download
print(f"{BOLD}{BLUE}Download Starting...{RESET}")
subprocess.run([
    yt_dlp_path,
    "-f", format_code,
    "-o", os.path.join(home_dir, f"{title}.%(ext)s"),
    url
])

print(f"{BOLD}{BLUE}Download Completed{RESET}")



