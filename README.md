## 🌙 Namaz Time Reminder Bot

A **Python-based Telegram bot** that provides **daily Namaz (prayer) times** for Tashkent and allows users to **set reminders** for prayer times. Stay spiritually connected with timely prayer notifications. 🙏

Built using **PyTelegramBotAPI**, **BeautifulSoup**, and **Schedule**, this bot ensures **accurate** and **automated** reminders for all five daily prayers.

## Features

## Prayer Time Notifications  
- **Real-Time Namaz Timings** for Tashkent  
- **Automated Daily Prayer Updates**  
- **Accurate Data Scraped from Trusted Sources**  
- **User-Friendly Reminder System**  

## 🔔 Reminder System  
- **Set Automatic Reminders** for prayer times  
- **Timely Alerts Before Each Prayer**  
- **Customizable Notifications**  
- **Error Handling & Smooth User Flow**  

## 📅 Daily Prayer Schedule  
- **Fajr (Bomdod)** ⏰  
- **Sunrise (Quyosh chiqish)** ☀️  
- **Dhuhr (Peshin)** 🕰️  
- **Asr** ⌚  
- **Maghrib (Shom)** 🌅  
- **Isha (Xufton)** 🌙  

## Requirements  

- **Python 3.x**  
- **Libraries:**  
  - `telebot` (Telegram API)  
  - `beautifulsoup4` (Web Scraping)  
  - `requests` (HTTP Requests)  
  - `schedule` (Task Scheduling)  
  - `datetime` (Time & Date Handling)  
  
## Installation  

1. Clone the Repository  
```bash
git clone https://github.com/GhostKX/Namaz-Time-Reminder-bot.git
```

2. Install required dependencies
```bash
pip install -r requirements.txt
```

3. Configure the bot

- Create a .env file to store your Telegram API Key and OpenWeatherMap API Key
- Add your Telegram Bot Token:

```
API_KEY=your-telegram-bot-token
```

4. Navigate to the project directory
```bash
cd Namaz-Time-Reminder-bot
```

5. Run the bot
```bash
python Namaz_time_bot.py
```

---

## Usage  

### Initial Setup  
- Start the bot by sending `/start` in Telegram.  
- Choose an option:  
   - 💸 **Tashkent Namaz Times**
   - ⏰ **Set Prayer Reminders**


### Getting Prayer Times  
- **Select the Tashkent option**   
- The bot will scrape the latest Namaz times and display them in a formatted message


---

## Setting Reminders
- Choose ✅ Yes to enable automatic prayer reminders
- The bot will notify you at the exact prayer time every day


### Example Output:  

```
📅 15 February 2025  
______________________________  
🏩 Bomdod: 05:45 AM  
☀️ Sunrise: 07:10 AM  
🕰️ Peshin: 12:30 PM  
⌚ Asr: 04:15 PM  
🌅 Shom: 06:45 PM  
🌙 Xufton: 08:00 PM  
______________________________
```

---

## Author

- Developed by **GhostKX**
- GitHub: **[GhostKX](https://github.com/GhostKX/Namaz-Time-Reminder-bot)**