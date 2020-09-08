import requests
import json
import os

# Get all the PRs
list_pr_response = requests.get("https://api.github.com/repos/sayakpaul/wine/pulls",
	headers={
		"Accept": "application/vnd.github.v3+json"
	}
)

# Get the latest PR and fetch its id
if list_pr_response.status_code == 200:
	latest_pr = list_pr_response.json()[0]
	pr_id = latest_pr["url"].split("/")[-1]
	print(pr_id)

# Get details about it
single_pr_response = requests.get("https://api.github.com/repos/sayakpaul/wine/pulls/{}".format(pr_id),
	headers={
		"Accept": "application/vnd.github.v3+json"
	}
)

# Get the comment URL to issue PR comment
if single_pr_response.status_code == 200:
	description = single_pr_response.json()
	issue_comment_url = description["_links"]["comments"]["href"]
	print(issue_comment_url)

# Load the run URL
run_url = open("run.txt", "r").read()

# Create the comment and make the request
data = {
	"body": run_url
}
comment_response = requests.post(issue_comment_url,
	headers={
		"Accept": "application/vnd.github.v3+json",
		"Authorization": "token {}".format(os.environ['TOKEN'])
	} ,
	data=json.dumps(data)
)
print(comment_response.text)
