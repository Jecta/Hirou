import platform

# Time for windows.
import ctypes

lib = ctypes.windll.kernel32

t = lib.GetTickCount64()

t = int(str(t)[:-3])

mins, sec = divmod(t, 60)
hour, mins = divmod(mins, 60)
days, hour = divmod(hour, 24)

# Time for macos and linux
import os
from os import system

clearConsole = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")

t = os.popen("uptime -p").read()[:-1]

import ctypes

clearConsole()

# Hirou
ctypes.windll.kernel32.SetConsoleTitleW("意味")
print("-" * 5, "H1R0U", "-" * 5)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Machine: {uname.machine}")
print(f"System-Name: {uname.node}")
print(f"System-OS: {platform.system()}")
print(f"Processor: {uname.processor}")
print(f"Architecture: {platform.architecture()}")
print(f"Python-Version: {platform.python_version()}")
print(f"System-Uptime: {days} days, {hour:02}:{mins:02}:{sec:02}")
print(t)
print(f"Made by https://github.com/jecta")

k = input("")
