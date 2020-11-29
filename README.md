# issue-to-notion
This action make **ISSUEs affect TO NOTION cards**.   
Issue OPEN/CLOSE/EDIT/REOPEN event will make a corresponding action to your Notion DB

## :wink: Pre-order of Notion-to-Github and get discount!
We provide issue-to-notion for free! But it's hard to make <b>Notion-to-Github</b>...   
So we need to check its demand is enough. If you want it, plz answer below typeform.  
If you answer, you will get 10% discount a year. If you pre-pay 9.9$, you will get 30% discount a year.  
(Surely it can be free if it doesn't use any paid resource)   
Answer HERE : [typeform Link](https://dodo41142727.typeform.com/to/mPP7d1hV)

## :rocket: WHAT's NEW? (v1.1.1)

### 1. Custom property & status
you can choose which DB property set to which status, when issue OPEN/CLOSE
### 2. Edit/Close/Reopen will work nicely
Edit/Close/Reopen will work even though there isn't a corresponding card.   
It will create notion card when there isn't!

## :upside_down_face: Usage
### Your DB should have "name" property

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
        uses: dodo4114/issue-to-notion@v1.1.1
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

## Example
this repo and [this notion DB](https://www.notion.so/dodo4114/aebe312a066c465494fb1eb6997060b0?v=95652d72244a44bd97d39b6057c51dc0)


## Dependency 
This action uses  
+ [notion-py](https://github.com/jamalex/notion-py)   
+ [md2notion](https://github.com/Cobertos/md2notion)

## Reference
https://developer.github.com/webhooks/event-payloads/#issues

## HELP?
dodo4114@naver.com

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fmarketplace%2Factions%2Fissue-to-notion&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
