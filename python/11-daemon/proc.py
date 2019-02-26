import os
import psutil

lock_file = "/dev/shm/proc"

def run_task(name, max_load=50):
    pass

def is_process_running(file_name=None):
    if not file_name:
        file_name = lock_file
    if not os.path.isfile(file_name):
        return False
    with open(file_name, "r") as f:
        pid = int(f.read())
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True

def create_lock_file(file_name=None):
    pid = os.getpid()
    if not file_name:
        file_name = lock_file
    with open(file_name, "w") as f:
        f.write(str(pid))


if __name__ == '__main__':
    print(is_process_running())
    create_lock_file()

