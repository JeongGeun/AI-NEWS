---
icon: fas fa-robot
order: 1
title: "AI 뉴스"
topic_category: "ai"
---

{% assign topic_posts = site.posts | where_exp: "p", "p.categories contains 'ai'" %}
{% if topic_posts.size == 0 %}
<p>아직 포스트가 없습니다.</p>
{% else %}
<ul class="post-list">
{% for post in topic_posts %}
  <li>
    <span class="post-meta">{{ post.date | date: "%Y-%m-%d" }}</span>
    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
  </li>
{% endfor %}
</ul>
{% endif %}
