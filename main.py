import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write("Honestly, I'm just Googling your problem while you watch me Google your problem.")
