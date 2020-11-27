# issue-to-notion
This action make **ISSUEs affect TO NOTION cards**.   
Issue OPEN/CLOSE/EDIT/REOPEN event will make a corresponding action to your Notion DB

## :rocket: WHAT's NEW? (v1.1.1)

### 1. Custom property & status
you can choose which DB property set to which status, when issue OPEN/CLOSE
### 2. Edit/Close/Reopen will work nicely
Edit/Close/Reopen will work even though there isn't a corresponding card.   
It will create notion card when there isn't!

## Usage

Create `.github/workflows/issue-to-notion.yml` in your repository.
And copy&paste following, and edit appropriately.

```
name: issue_to_notion
on:
  issues:
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Notion Card Creator
        uses: dodo4114/issue-to-notion@v1.1.0
        env:
          NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
          DATABASE_URL: {YOUR DB URL}
          PROPERTY_NAME : {YOUR PROPERTY NAME}
          STATE_OPEN : {YOUR OPEN STATE NAME}
          STATE_CLOSED : {YOUR CLOSED STATE NAME}
```

| Input Key | Required | Default value | Description |
|:-----:|:-----:|:-----:|-----|
| NOTION_TOKEN | O | X | Auth token called token_v2 from cookie in your browser. Put it your repository secret, and name it NOTION_TOKEN(Recommended) |
| DATABASE_URL | O | X | The url of the database you are trying to access |
| PROPERTY_NAME | X | status | Name of your PROPERTY which will be changed |
| STATE_OPEN | X | open | Your OPEN state name |
| STATE_CLOSED | X | closed | Your CLOSED state name |





## Dependency 
This action uses  
+ [notion-py](https://github.com/jamalex/notion-py)   
+ [md2notion](https://github.com/Cobertos/md2notion)

## Reference
https://developer.github.com/webhooks/event-payloads/#issues
