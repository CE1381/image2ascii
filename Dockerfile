FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Change work directory
WORKDIR /usr/src/app

# Install application dependencies
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application files into the image
COPY . .

ENTRYPOINT [ "./entry-point.sh" ]
