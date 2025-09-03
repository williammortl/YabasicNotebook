# Yabasic Notebook
A [Jupyter Notebook](https://jupyter.org/) kernel for YaBasic by William M Mortl.

Learning how to program in [BASIC](https://en.wikipedia.org/wiki/BASIC) used to be a right of passage for aspiring programmers. BASIC an excellent language for learning simple imperative programming before diving into deeper concepts. This custom Jupyter Notebook kernel allows for writing and running simple BASIC programs inside a Jupyter Notebook.

Included in the **examples** directory are a couple simple programs.

Link: [YaBasic Github repository](https://github.com/marcIhm/yabasic)

## Requirements
Make sure to have the following packages installed:

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

Run the following to verify that the kernel was installed into Jupyter:

```bash
jupyter kernelspec list
```

## Running

In order to run the Jupyter Notebook with the YaBasic kernel, make sure to activate the custom venv and then start the Jupyter server:

```bash
source ~/yabasic-venv/bin/activate
jupyter notebook --port=1604
```
