---
layout: default
title: Trang chủ
---

# About

Hieu is a lazy employee (at <a href="http://www.hust.edu.vn/">HUST</a>) and a devoted dreamer. 
He used to be a prolific blogger, a street photographer, and a reluctant translator. 
He likes playing, creating things and doing nothing :-)  

### Các chủ đề yêu thích:
* Chụp ảnh
* Đọc sách
* Chia sẻ trải nghiệm

---

### Các bài viết mới nhất

{% if site.posts.size > 0 %}
{% for post in site.posts %}
* **{{ post.date | date: "%d/%m/%Y" }}** — [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
{% else %}
* Chưa có bài viết nào được xuất bản.
{% endif %}