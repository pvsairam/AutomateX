# Twitter X Automation

An automated script that posts bullish Web3 project updates every hour to Farcaster using ChatGPT, Gemini, or DeepSeek. It avoids repetition, logs to Telegram, and supports fallback AI models.

---

## 🚀 How to Run This Project

### ✅ 1. Clone the Repo & Set Up the Environment
If you haven't already, navigate to the project directory.

```bash
cd bull-post-automation
```

---

### ✅ 2. Install Required Python Packages
Make sure you're using **Python 3.9+**, then run:

```bash
pip install -r requirements.txt
```

---

### ✅ 3. Set Up Environment Variables
Rename `.env.example` to `.env`:

```bash
cp .env.example .env
```

Open `.env` and fill in all your API keys:

```env
# LLMs
CHATGPT_API_KEY=sk-...
GEMINI_API_KEY=...
DEEPSEEK_API_KEY=...

# Farcaster (via Neynar)
NEYNAR_API_KEY=...
FARCASTER_BOT_MNEMONIC=...
SIGNER_UUID=...

# Telegram
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
```

---

### ✅ 4. Customize Your Projects
Edit `data/projects.txt` to include any Web3 projects you want bullish posts about.  
One project name per line.

---

### ✅ 5. Run the Script
You can start the script manually:

```bash
python main.py
```

It will:
- Run once immediately
- Then run **every 1 hour**
- Generate bullish content
- Post to **Farcaster**
- Log to your **Telegram channel**
- Avoid reposting the same content

---

### 🛠 Optional: Run it in Background (Linux/WSL)

#### `tmux` or `screen` (recommended):
```bash
tmux new -s bullposter
python main.py
# then press Ctrl+B then D to detach
```

#### Or use `nohup`:
```bash
nohup python main.py &
```

---

### 📦 File Summary

| File | Description |
|------|-------------|
| `main.py` | Main loop that posts every hour |
| `config.py` | Toggle platforms like Twitter/Farcaster |
| `.env` | Stores API keys securely |
| `data/projects.txt` | Web3 project list |
| `data/posted_log.txt` | Keeps track of what was already posted |
| `poster/*.py` | LLM, Farcaster, Telegram, memory logic |
