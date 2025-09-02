from .yabasic_kernel import YabasicKernel
from ipykernel.kernelapp import IPKernelApp

IPKernelApp.launch_instance(kernel_class=YabasicKernel)
