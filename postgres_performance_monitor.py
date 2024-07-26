from time import sleep
from config import cpu_usage_limit, memory_usage_limit
import psutil

def get_pid():
    process_name = "postgres.exe"
    for proc in psutil.process_iter():
        if process_name in proc.name():
            pid = proc.pid
            return pid


def monitor(pid: int):
    p = psutil.Process(pid=pid)
    cpu_usage = p.cpu_percent(interval=1)
    if cpu_usage > cpu_usage_limit:
        print(f"[ALARM] CPU usage is above {cpu_usage_limit}%: {cpu_usage}")
        sleep(10)

    memory_usage = p.memory_percent()
    if memory_usage > memory_usage_limit:
        print(f"[ALARM] Memory usage is above {memory_usage_limit}%: {memory_usage}")
        sleep(10)


if __name__ == '__main__':
    pid = get_pid()

    while True:
        monitor(pid)

