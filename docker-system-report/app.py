import platform
import socket
import os
from datetime import datetime

def main():
    print("=" * 50)
    print("DOCKER SYSTEM REPORT")
    print("=" * 50)

    hostname = socket.gethostname()
    os_name = platform.system()
    os_version = platform.release()
    architecture = platform.machine()
    python_version = platform.python_version()
    current_time = datetime.now().strftime("%d %B %Y, %I:%M:%S %p")
    cpu_count = os.cpu_count()

    print(f"Hostname: {hostname}")
    print(f"Operating System: {os_name}")
    print(f"OS Version: {os_version}")
    print(f"Architecture: {architecture}")
    print(f"Python Version: {python_version}")
    print(f"CPU Count: {cpu_count}")
    print(f"Current Time: {current_time}")

    print("\nPerforming sample calculation...")
    numbers = [12, 18, 25, 30, 45]
    total = sum(numbers)
    average = total / len(numbers)

    print(f"Numbers: {numbers}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")

    report = f"""
DOCKER SYSTEM REPORT

Hostname: {hostname}
Operating System: {os_name}
OS Version: {os_version}
Architecture: {architecture}
Python Version: {python_version}
CPU Count: {cpu_count}
Current Time: {current_time}

Numbers: {numbers}
Total: {total}
Average: {average:.2f}
"""

    with open("system_report.txt", "w") as file:
        file.write(report)

    print("\nReport saved to system_report.txt")
    print("Application completed successfully.")

if __name__ == "__main__":
    main()