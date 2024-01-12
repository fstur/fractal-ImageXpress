import fractal_imagexpress
import json
from pathlib import Path


PACKAGE = "fractal_imagexpress"
PACKAGE_DIR = Path(fractal_imagexpress.__file__).parent
MANIFEST_FILE = PACKAGE_DIR / "__FRACTAL_MANIFEST__.json"
with MANIFEST_FILE.open("r") as f:
    MANIFEST = json.load(f)
    TASK_LIST = MANIFEST["task_list"]
