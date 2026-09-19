---
layout: default
title: Trang chủ
---

# About

Hieu is a lazy employee (at [HUST](http://www.hust.edu.vn/)) and a devoted dreamer. 
He used to be a prolific blogger, a street photographer, and a reluctant translator. 
He likes playing, creating things and doing nothing :-)  

### Stuffs
* [Signals and Systems](https://www.dropbox.com/sh/x83lkx5cynld9gm/AAAZrMx13lmI6A8h6eUTdDnca?dl=0)
* SPCOM
* UWB
* Playing go
* Tea drinking

---

### Các bài viết mới nhất

{% if site.posts.size > 0 %}
{% for post in site.posts %}
* **{{ post.date | date: "%d/%m/%Y" }}** — [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
{% else %}
* Chưa có bài viết nào được xuất bản.
{% endif %}