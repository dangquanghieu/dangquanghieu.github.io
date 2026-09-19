---
layout: default
title: Trang chủ
---

# Chào mừng đến với trang web của tôi!

Đây là bài viết đầu tiên của tôi sử dụng Jekyll và giao diện Minimal. 

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