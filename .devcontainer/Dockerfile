# Use Ubuntu as the base image

FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu

# Install yabasic and Python tools
RUN apt-get update && \
    apt-get install -y yabasic python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Create a Python virtual environment and install Jupyter and kernel tools
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install jupyter notebook ipykernel && \
    /opt/venv/bin/python -m ipykernel install --user

# Add venv bin to PATH
ENV PATH="/opt/venv/bin:$PATH"

# Expose Jupyter Notebook port
EXPOSE 8888

# Set default shell to bash
SHELL ["/bin/bash", "-c"]
