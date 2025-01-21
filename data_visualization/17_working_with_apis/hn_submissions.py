from operator import itemgetter

import requests

import plotly.express as px

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    try:
        comment = response_dict['descendants']
        title = response_dict['title']
        hn_link = f"https://news.ycombinator.com/item?id={submission_id}"
        submission_dict = {
            'title': title,
            'hn_link': hn_link,
            'comments': comment,
        }
    except:
        print(f"Error while building dict for {submission_id}")
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

links = []
comments = []
for dict in submission_dicts:
    title = dict['title']
    hn_link = dict['hn_link']
    comment = dict['comments']
    link = f"<a href='{hn_link}'>{title}</a>"
    comments.append(comment)
    links.append(f"<a href='{hn_link}'>{title}</a>")

# Make visualization.
title = "Most-Commented Posts on Hacker News"
labels = {'x': 'Posts', 'y': 'Comments'}
fig = px.bar(x=links, y=comments, title=title, labels=labels)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='Orange', marker_opacity=0.6)

fig.show()