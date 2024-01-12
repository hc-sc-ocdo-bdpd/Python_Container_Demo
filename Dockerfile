FROM python:3.8-slim

# Set working directory
WORKDIR /workspace

# Install Jupyter
RUN pip install notebook

# Expose Jupyter port
EXPOSE 8888

# Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
