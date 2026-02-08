import os

def overwrite_file(path, passes):
    size = os.path.getsize(path)
    with open(path, "ba+", buffering=0) as f:
        for _ in range(passes):
            f.seek(0)
            f.write(os.urandom(size))
            f.flush()
            os.fsync(f.fileno())
    os.remove(path)
