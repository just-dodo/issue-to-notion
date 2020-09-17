FROM python:3.7-slim

LABEL "com.github.actions.name"="Issue to Notion"
LABEL "com.github.actions.description"="From github Issue Make Notion Card"
LABEL "com.github.actions.icon" = "activity"
LABEL "com.github.actions.color" = "yellow"

LABEL "repository"="https://github.com/dodo4114/issue-to-notion"
LABEL "maintainer"="Dohyeon Park <dodo4114@naver.com>"

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY main.py ./
RUN ls
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "/usr/src/app/main.py"]