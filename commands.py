import subprocess
from typing import Optional
import os

def get_home_dir() -> Optional[str]:
    try:
        home_dir = os.environ['HOME']
        if home_dir == "/root":
            return None
        return home_dir
    except:
        return None


def execute(cmd: list[str]) -> None:
    subprocess.run(cmd, capture_output=False, check=True)


