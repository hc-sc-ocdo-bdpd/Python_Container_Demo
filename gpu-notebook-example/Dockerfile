FROM nvidia/cuda:12.2.2-runtime-ubuntu22.04

# Set working directory
WORKDIR /workspace

# Set non-interactive installation mode and configure timezone
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# Install Python, build tools, and compilers
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# Update pip
RUN python3 -m pip install --upgrade pip

# Install Requirements
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

# Expose Jupyter port
EXPOSE 8888

# Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
