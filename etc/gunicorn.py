from multiprocessing import cpu_count

def max_workers():
    return cpu_count() * 2

bind = ["unix:///tmp/gunicorn.sock"]
workers = max_workers()
