import re

def parse(s):
    if not s:
        return None
    match = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"', s)
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    return None
