---
layout: default
title: Archive
permalink: /archive/
---

## Archive 

Following is the list of all writings.

---

{% if site.posts.size > 0 %}
{% for post in site.posts %}
* {{ post.date | date: "%d/%m/%Y" }} — [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
{% else %}
* None published.
{% endif %}
