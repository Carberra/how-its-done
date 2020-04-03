from datetime import timedelta
from sys import argv
from time import time

import psutil as psu

NAME = argv[0]


def system_info():
	info = {
		"Uptime": timedelta(seconds=time()-psu.boot_time()),
		"CPU in use": f"{psu.cpu_percent(interval=.1)}%",
		"Time on CPU": timedelta(seconds=psu.cpu_times().system+psu.cpu_times().user),
		"Memory in use": f"{psu.virtual_memory().percent}%",
		"Memory available": f"{psu.virtual_memory().available/(1024**3):,.3f} GiB",
		"Disk in use": f"{psu.disk_usage('/').percent}%",
		"Disk free": f"{psu.disk_usage('/').free/(1024**3):,.3f} GiB",
	}
	print("\n\n    SYSTEM INFO\n\n" + "\n".join([f"{key}: {value}" for key, value in info.items()]))


def process_info():
	for proc in psu.process_iter(attrs=("name", "cmdline", "pid", "create_time", "cpu_percent", "cpu_times", "num_threads", "memory_percent")):
		if "python" in proc.info["name"] and (cl := proc.info["cmdline"]) is not None and len(cl) > 0 and NAME in cl[-1]:
			info = {
				"PID": proc.info["pid"],
				"Uptime": timedelta(seconds=time()-proc.info["create_time"]),
				"CPU in use": f"{proc.info['cpu_percent']}%",
				"Time on CPU": timedelta(seconds=proc.info["cpu_times"].system+proc.info["cpu_times"].user),
				"Nº of threads": proc.info["num_threads"],
				"Memory in use": f"{(mem := proc.info['memory_percent']):.3f}%",
				"Memory usage": f"{psu.virtual_memory().total*(mem/100)/(1024**3):,.3f} GiB",
			}
			print("\n\n    PROCESS INFO\n\n" + "\n".join([f"{key}: {value}" for key, value in info.items()]))


system_info()
process_info()