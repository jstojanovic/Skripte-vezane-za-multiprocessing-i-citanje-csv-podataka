#!/usr/bin/env python
import subprocess
import time
start_time = time.time()
subprocess.call([ 'rsync', '-arq', 'a/', 'backup/'])
duration = time.time() - start_time
print(f"duracija: {duration} sec")

