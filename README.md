# Auto Rename Bot ⚡️

A powerful Telegram bot that automatically renames, cleans, and uploads files without asking any questions!

## ✨ Features
- **Zero-Prompt Workflow**: Just send a file, and the bot handles the rest instantly.
- **Smart Cleaning**: Automatically replaces dots (`.`), hyphens (`-`), and underscores (`_`) with spaces in filenames.
- **Tag Removal**: Automatically removes unwanted tags and @mentions from filenames and captions.
- **Extension Preservation**: Cleans files while keeping their original extensions (like `.mkv`, `.mp4`).
- **Automatic Cleanup**: Background task deletes files/folders in `downloads/` older than 6 hours to save disk space.
- **Admin-Only Access**: Restricted to authorized IDs by default (comma-separated IDs supported in `.env`).
- **Public Mode Toggle**: Admins can open the bot to all users using the `/public` command.
- **Configurable Upload Type**: Set your default preference between **Document** and **Video**.
- **Custom Thumbnails & Captions**: Full support for persistent custom thumbnails and caption templates.

## 🛠 Commands
- `/start` - Start the bot.
- `/public [on|off]` - (Admin Only) Toggle bot access for all users.
- `/set_type [document|video]` - Set your default upload preference.
- `/view_type` - Check your current upload mode.
- `/set_caption [text]` - Set a global caption template (supports `{filename}`, `{filesize}`, `{duration}`).
- `/see_caption` - View your saved caption.
- `/del_caption` - Delete your custom caption.
- `/view_thumb` - View your saved thumbnail.
- `/del_thumb` - Delete your saved thumbnail.

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
   - `ADMIN`: Comma-separated admin IDs (e.g., `123,456`).
   - `DB_URL`: Your MongoDB URL.
   - `DB_NAME`: Your MongoDB Database Name.
   - `IS_PUBLIC`: Set to `True` to allow all users by default (optional).

3. Build and run:
   ```bash
   docker compose up -d --build
   ```

## 📜 Credits
Based on the @PYRO_BOTZ rename bot, modified for full automation and advanced security.
