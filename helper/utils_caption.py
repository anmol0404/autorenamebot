import re

def clean_name(text):
    # Remove @ADrama_Lovers
    text = text.replace("@ADrama_Lovers", "")
    
    # Replace dots, hyphens, and underscores with spaces
    text = text.replace(".", " ").replace("-", " ").replace("_", " ")
    
    # Remove URLs (http/https/ftp)
    text = re.sub(r'(?:https?|ftp)://[\n\S]+', '', text)
    
    # Remove other @mentions
    text = re.sub(r'@\w+\s?', '', text)
    
    # Truncate at specific keywords
    for key in ["🔘 SIZE", "Plot:"]:
        index = text.find(key)
        if index != -1:
            text = text[:index]

    return text.strip()

def process_caption(old_caption, join_channel=None):
    new_caption = clean_name(old_caption)

    if not join_channel:
        return new_caption
    else:
        return f"{new_caption}\nＪＯＩＮ : @{join_channel}"
