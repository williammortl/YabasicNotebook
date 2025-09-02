# YabasicNotebook
A Jupyter notebook kernel for Yabasic by William M Mortl

## Requirements
Make sure to have the following packages installed

1. python3-pip
1. python3-notebook
1. python3-venv

## Installation
Run:

`python3 install.py`

Install the YabasicNotebook package

```
python3 -m venv ~/yabasic-venv
source ~/yabasic-venv/bin/activate
pip install -e ./jupyter_yabasic_kernel
jupyter notebook --port=1604
```