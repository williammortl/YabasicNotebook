# Yabasic Notebook
A [Jupyter Notebook](https://jupyter.org/) kernel for YaBasic by William M Mortl.

Learning how to program in [BASIC](https://en.wikipedia.org/wiki/BASIC) used to be a right of passage for aspiring programmers. BASIC an excellent language for learning simple imperative programming before diving into deeper concepts. This custom Jupyter Notebook kernel allows for writing and running simple BASIC programs inside a Jupyter Notebook.

Included in the **examples** directory are a couple of simple BASIC programs.

Link: [YaBasic Github repository](https://github.com/marcIhm/yabasic)

## Depedencies

YaBasic Notebook the following package dependancies:

1. [YaBasic](https://2484.de/yabasic/)
1. python3-notebook (needs to be in the venv)

Optional dependancies:

1. python3-venv

## Setup

Select either basic setup or venv setup first, then proceed to the final step

### Basic

Install Jupyter Notebook system-wide:

```bash
pip install notebook
```

### Python Virtual Environment

1. Install venv
1. Create the venv
1. Activate the new venv
1. Install Jupyter Notebook in the venv

```bash
sudo apt install -y python3-venv
python3 -m venv ~/yabasic-venv
source ~/yabasic-venv/bin/activate
pip install notebook
```

### Final Steps

Install the new notebook kernel:

```bash
pip install -e ./jupyter_yabasic_kernel
python3 jupyter_yabasic_kernel/install.py
```

Run the following to verify that the kernel was installed into Jupyter properly:

```bash
jupyter kernelspec list
```

## Running 

In order to run the Jupyter Notebook with the YaBasic kernel, make sure to activate the custom venv (if needed)and then start the Jupyter server:

```bash
jupyter notebook 
```

## Notes

All steps in this README apply to Linux systems only. For this to run on macOS, YaBasic needs to be ported (which shouldn't be too difficult).
