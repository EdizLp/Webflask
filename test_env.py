import sys
import os

# This finds where the "Python Brain" is actually located
executable = sys.executable
print(f"\nLocation: {executable}")

if "Webflask\\.venv" in executable:
    print("✅ SUCCESS: VS Code is using your project box!")
else:
    print("❌ FAIL: VS Code is still using the Global Python.")