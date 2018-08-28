import os


def sample(name: str, **kw) -> str:
    base_path = os.environ["SAMPLES_BASE_PATH"]
    path = os.path.join(base_path, name)
    return open(path, "r", **kw).read()
