import os
import sys
import json
from jupyter_client.kernelspec import install_kernel_spec

def install():
    kernel_dir = os.path.dirname(os.path.abspath(__file__))
    install_kernel_spec(kernel_dir, kernel_name='yabasic', user=True)
    print('Yabasic kernel installed!')

if __name__ == '__main__':
    install()
