from multiprocessing import cpu_count

def max_workers():
    return cpu_count() * 2 + 1

bind = ["unix:///tmp/gunicorn.sock"]
#worker_class = "gevent"
workers = max_workers()
