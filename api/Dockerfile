FROM python:latest

WORKDIR /app

COPY . /app/

# RUN apt install -y netcat
RUN python3 -m pip install --upgrade Pillow
RUN pip3 install -r requirements.txt

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "6868"]