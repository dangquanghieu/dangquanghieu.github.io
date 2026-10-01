---
layout: default
title: Homepage
---

### About

Hieu is a lazy employee (at [HUST](http://www.hust.edu.vn/)) and a devoted dreamer. 
He used to be a prolific blogger, a street photographer, and a reluctant translator. 
He likes playing, creating things and doing nothing :-)  

### Stuffs
* [Signals and Systems]({{ "/ss/" | relative_url }})
* [Digital Signal Processing]({{ "/dsp/" | relative_url }})
* SPCOM
* UWB
* Pattern recognition
* AI (who doesn't? it is complicated ...)
* Playing go (also called as weiqi, baduk or "cờ vây")
* [Tea drinking](https://trachieu.tumblr.com/)
* Photography (taking snapshots of things around me, again!)

---

### Recents

{% if site.posts.size > 0 %}
{% for post in site.posts limit:10 %}
* {{ post.date | date: "%d/%m/%Y" }} — [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
{% else %}
* No published post yet.
{% endif %}

**[View all posts]({{ "/archive/" | relative_url }})**
