import requests
import json

# get all the PRs
list_pr_response = requests.get("https://api.github.com/repos/sayakpaul/wine/pulls",
	headers={
		"Accept": "application/vnd.github.v3+json"
	}
)

# get the latest PR and fetch its id
if list_pr_response.status_code == 200:
	latest_pr = list_pr_response.json()[0]
	pr_id = latest_pr["url"].split("/")[-1]
	print(pr_id)

# get details about it
single_pr_response = requests.get("https://api.github.com/repos/sayakpaul/wine/pulls/{}".format(pr_id),
	headers={
		"Accept": "application/vnd.github.v3+json"
	}
)

# get the comment URL to issue PR comment
if single_pr_response.status_code == 200:
	description = single_pr_response.json()
	issue_comment_url = description["_links"]["comments"]["href"]
	print(issue_comment_url)

# create the comment
data = {
	"body": "Hello!"
}
comment_response = requests.post(issue_comment_url,
	headers={
	"Accept": "application/vnd.github.v3+json",
	"Authorization": "token"
	} ,
	data=json.dumps(data)
)
if comment_response.status_code == 201:
	print("We are good!")
