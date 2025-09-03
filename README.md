# YabasicNotebook
A Jupyter notebook kernel for Yabasic by William M Mortl

## Requirements
Make sure to have the following packages installed

1. [YaBasic](https://2484.de/yabasic/)
1. python3-venv
1. python3-notebook (needs to be in the venv)

## Setup

1. Create the venv
1. Activate the new venv
1. Install requirements
1. Install the kernel package
1. Install the new kernel

```bash
python3 -m venv ~/yabasic-venv
source ~/yabasic-venv/bin/activate
pip install notebook
pip install -e ./jupyter_yabasic_kernel
python3 jupyter_yabasic_kernel/install.py
```

Run the following to make sure the kernel was installed into Jupyter:

```bash
jupyter kernelspec list
```

## Running

Open up the venv & sStart the Jupyter server:

```bash
source ~/yabasic-venv/bin/activate
jupyter notebook --port=1604
```
