FROM python:latest

WORKDIR ./clean-hangman-cli

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 46857

ENTRYPOINT ["python3", "packages/main.py"]
