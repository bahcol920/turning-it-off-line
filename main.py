import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write("Have you tried turning it off, turning it on, and whispering 'please' to it? At this point the printer and I are both just pretending this is a plan.")
