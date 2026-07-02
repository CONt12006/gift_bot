import sqlite3

conn = sqlite3.connect("gift_bot.db")
cur = conn.cursor()



conn.commit()
conn.close()