FROM python:latest

WORKDIR ./clean-hangman-cli

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 46857

CMD ["python3", "packages/main.py", "start"]