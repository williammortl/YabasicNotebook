import os
import sys
import json
from jupyter_client.kernelspec import install_kernel_spec

def install():
    kernel_dir = os.path.dirname(os.path.abspath(__file__))
    kernel_json_path = os.path.join(kernel_dir, "kernel.json")
    with open(kernel_json_path, "r") as f:
        kernel_json = json.load(f)
    # Ensure argv[0] is sys.executable for venv portability
    kernel_json["argv"][0] = sys.executable
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        with open(os.path.join(td, "kernel.json"), "w") as f:
            json.dump(kernel_json, f)
        # Use sys.prefix to install into the venv's Jupyter directory
        install_kernel_spec(td, kernel_name="yabasic", prefix=sys.prefix, replace=True)
    print("YaBasic kernel installed in venv Jupyter directory!")

if __name__ == "__main__":
    install()