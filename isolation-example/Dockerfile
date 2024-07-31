FROM python:3.8-slim

# Set working directory
WORKDIR /workspace

# Update and install build tools, compilers, and libcap2-bin
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    build-essential \
    cmake \
    libcap2-bin && \
    rm -rf /var/lib/apt/lists/*

# Install Requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Expose Jupyter port
EXPOSE 8888

# Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
