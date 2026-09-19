---
layout: default
title: Homepage
---

### About

Hieu is a lazy employee (at [HUST](http://www.hust.edu.vn/)) and a devoted dreamer. 
He used to be a prolific blogger, a street photographer, and a reluctant translator. 
He likes playing, creating things and doing nothing :-)  

### Stuffs
* [Signals and Systems](https://www.dropbox.com/sh/x83lkx5cynld9gm/AAAZrMx13lmI6A8h6eUTdDnca?dl=0)
* [Digital Signal Processing](https://www.dropbox.com/scl/fo/y7jkblp6xa8zcyq6nntzh/AN-HDuQl4-esSACCzj6WHC8?rlkey=qkfpolduoiscqb68i542yc2rs&dl=0)
* SPCOM
* UWB
* Playing go (also called as weiqi, baduk or "cờ vây")
* [Tea drinking](https://trachieu.tumblr.com/)

---

### Recents

{% if site.posts.size > 0 %}
{% for post in site.posts limit:10 %}
* **{{ post.date | date: "%d/%m/%Y" }}** — [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
{% else %}
* No published post yet.
{% endif %}

**[All posts]({{ "/archive/" | relative_url }})**
