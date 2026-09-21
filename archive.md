---
layout: default
title: Archive
permalink: /archive/
---

## Archive 

Following is the list of all posts, ordered by date and time.

---

{% if site.posts.size > 0 %}
{% for post in site.posts %}
* {{ post.date | date: "%d/%m/%Y" }} — [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
{% else %}
* None published.
{% endif %}
