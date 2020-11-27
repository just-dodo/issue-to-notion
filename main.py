import sys
import os
import json
from notion.client import NotionClient
from notion.block import PageBlock, BookmarkBlock
from md2notion.upload import upload, convert, uploadBlock

# Get data from github environment
path = os.environ.get("GITHUB_EVENT_PATH")
token = os.environ.get("NOTION_TOKEN")
database_url = os.environ.get("DATABASE_URL")
property_name = os.environ.get("PROPERTY_NAME","status")
state_open = os.environ.get("STATE_OPEN","open")
state_closed = os.environ.get("STATE_CLOSED","closed")


# Get the event string from github
with open(path,"r") as f:
    github_event_str = f.read()

# Convert event string to json
github_event_json = json.loads(github_event_str)

# Login and go into collection
client = NotionClient(token_v2=token)
cv = client.get_collection_view(database_url)

def main():
    print("main() is excuted")

    global github_event_json
    global cv

    # Get issue title, body and link
    action_type = github_event_json["action"]
    issue_number = github_event_json["issue"]["number"]
    issue_title = github_event_json["issue"]["title"]
    issue_link = github_event_json["issue"]["html_url"]

    print("action_type is",action_type)

    # Check action type
    if action_type == "opened":

        row = createRow(cv,issue_number,issue_title)

        # Add Bookmark for issue
        row.children.add_new(BookmarkBlock, title=issue_title, link=issue_link)
        upload_body_with_markdown(row)
    else:
        row = get_or_create_row(cv,issue_number,issue_title)

        if action_type == "edited":
            clear_page(row)
            row.children.add_new(BookmarkBlock, title=issue_title, link=issue_link)
            upload_body_with_markdown(row)

        elif action_type == "closed":
            setattr(row,property_name,state_closed)

        elif action_type == "deleted":
            pass
        # TODO
        elif action_type == "reopened":
            setattr(row,property_name,state_open)

        elif action_type == "labeled" or action_type == "unlabeled":
            pass
        # TODO


def upload_body_with_markdown(row):
    global github_event_json

    body = github_event_json["issue"]["body"]
        
    # Make markdown file from issue body
    f= open("body.md","w+")
    f.write(body)
    f.close()

    # Upload issue body markdown file to row
    with open("body.md", "r", encoding="utf-8") as mdFile:
        upload(mdFile,row)

def clear_page(row):
    for child in row.children:
        child.remove()

def get_row_with_IssueNumber(number):
    global cv
    inputNumber ="[#"+str(number)+"]"
    print('issue number is',inputNumber)

    exact_ID_filter_params = {
        'filters': [{'property': "title", 'filter': {'operator': "string_starts_with", 'value': {'type': "exact", 'value': inputNumber}}}],
        'operator': "and"
    }
    rows = list(filter(lambda row : row.title.startswith(inputNumber),cv.build_query(filter=exact_ID_filter_params).execute()))
    print('filtered rows :',rows)
    if len(rows) == 0:
        return None
    return rows[0]

def createRow(cv, issue_number, issue_title):
    # Add row to notion collection
    row = cv.collection.add_row()
    row.name = "[#"+str(issue_number)+"] "+issue_title
    setattr(row,property_name,state_open)

    return row

def get_or_create_row(cv, issue_number, issue_title):
    row = get_row_with_IssueNumber(issue_number)
    if not row:
        row = createRow(cv, issue_number, issue_title)
    return row

main()