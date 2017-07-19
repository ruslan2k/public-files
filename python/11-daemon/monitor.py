import os
import sys
import time
import subprocess
import config
from datetime import datetime


def playload():
    subprocess.Popen(config.DEF_PROG)


def daemon():
    tmp_dir = os.getenv('TMP')
    log_file = os.path.join(tmp_dir, 'monitor.log');
    for x in range(24):
        with open(log_file, 'a+') as f:
            f.write(datetime.now().isoformat() + "\n")
        time.sleep(3600)


def main():
    if (len(sys.argv) > 1) and (sys.argv[1] == '-d'):
        subprocess.Popen([sys.executable, os.path.abspath(__file__)])
        return
    #print(os.path.abspath(__file__))
    #print(sys.executable)
    daemon()


if __name__ == "__main__":
    main()

