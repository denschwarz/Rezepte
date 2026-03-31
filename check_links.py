import os

receipe_files = os.listdir("data")

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

print("Files in data directory that are not linked in README.md:")
for f in receipe_files:
    if f not in content:
        print(f"  - {f}")