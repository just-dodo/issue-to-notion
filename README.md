# issue-to-notion
This action make **ISSUEs affect TO NOTION cards**.
1. When an issue OPENed, notion card will be created.
2. When an issue CLOSEed, notion card will be closed tag.
3. When an issue EDITed, notion card will be edited.
4. When an issue get TAGs, notion card will get them all. (comming soon)

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
```

| Input Key | Description |
|-------|-------|
| NOTION_TOKEN | Auth token called token_v2 from cookie in your browser. Put it your repository secret, and name it NOTION_TOKEN |
| DATABASE_URL | The url of the database you are trying to access |





## Dependency 
This action uses  
+ [notion-py](https://github.com/jamalex/notion-py)   
+ [md2notion](https://github.com/Cobertos/md2notion)
