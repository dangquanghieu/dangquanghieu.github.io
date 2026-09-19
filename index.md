---
layout: default
---

# Chào mừng đến với trang web của tôi!

Đây là bài viết đầu tiên của tôi sử dụng Jekyll và giao diện Minimal. 

### Các chủ đề yêu thích:
* Chụp ảnh
* Đọc sách
* Chia sẻ trải nghiệm

---

### Các bài viết mới nhất

<ul>
  {% for post in site.posts %}
    <li>
      <span style="color: #666; font-size: 0.9em;">{{ post.date | date: "%d/%m/%Y" }}</span> — 
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </li>
  {% empty %}
    <li>Chưa có bài viết nào được xuất bản.</li>
  {% endfor %}
</ul>
