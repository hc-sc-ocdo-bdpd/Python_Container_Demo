FROM python:3.8-slim

# Set working directory
WORKDIR /workspace

# Install Requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Expose Jupyter port
EXPOSE 8888

# Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
