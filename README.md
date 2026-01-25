# Auto Rename Bot ⚡️

A powerful Telegram bot that automatically renames, cleans, and uploads files without asking any questions!

## ✨ Features
- **Zero-Prompt Workflow**: Just send a file, and the bot handles the rest instantly.
- **Smart Cleaning**: Automatically replaces dots (`.`), hyphens (`-`), and underscores (`_`) with spaces in filenames.
- **Tag Removal**: Automatically removes unwanted tags and @mentions from filenames and captions.
- **Extension Preservation**: Cleans files while keeping their original extensions (like `.mkv`, `.mp4`).
- **Automatic Cleanup**: Background task deletes files/folders in `downloads/` older than 6 hours to save disk space.
- **Configurable Upload Type**: Set your default preference between **Document** and **Video**.
- **Custom Thumbnails & Captions**: Full support for persistent custom thumbnails and caption templates.

## 🛠 Commands
- `/start` - Start the bot.
- `/set_type [document|video]` - Set your default upload preference.
- `/view_type` - Check your current upload mode.
- `/set_caption [text]` - Set a global caption template.
- `/set_thumb` - Send a photo followed by `/set_thumb` to save it.

## 🚀 Deployment (Docker)
1. Clone the repo:
   ```bash
   git clone https://github.com/anmol0404/autorenamebot.git
   cd autorenamebot
   ```
2. Create a `.env` file based on `.env.sample` and fill in your details:
   - `API_ID`: Your Telegram API ID.
   - `API_HASH`: Your Telegram API HASH.
   - `BOT_TOKEN`: Your Bot Token from @BotFather.
   - `DB_URL`: Your MongoDB URL.
   - `DB_NAME`: Your MongoDB Database Name.
   - `ADMIN`: Your Telegram User ID (for admin access).
   - `LOG_CHANNEL`: ID of the channel where bot logs will be sent.

3. Build and run:
   ```bash
   docker compose up -d --build
   ```

## 📜 Credits
Based on the @PYRO_BOTZ rename bot, modified for full automation.
