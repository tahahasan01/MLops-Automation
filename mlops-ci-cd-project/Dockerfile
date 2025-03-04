FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt first (for efficient caching)
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project directory into /app
COPY . /app

# Set working directory inside /app/app because app.py is inside app/
WORKDIR /app/app

# Run Flask API
CMD ["python", "app.py"]
