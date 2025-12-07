---
marp: true
title: Product Documentation Presentation
author: 23f3001018@ds.study.iitm.ac.in
theme: default
paginate: true
header: "**Product Docs – v1.0**"
footer: "© 2025 Software Division"
---

<!-- _class: lead -->
<!-- _backgroundColor: #ffffff -->

# Product Documentation  
### Technical Presentation (Marp)

**Author:** 23f3001018@ds.study.iitm.ac.in

---

<!-- Custom theme & styling -->
<style>
section {
  font-family: "Segoe UI", sans-serif;
  background-color: #f9fafc;
}
h1 {
  color: #1a73e8;
}
h2 {
  color: #0b5394;
}
blockquote {
  border-left: 5px solid #1a73e8;
  padding-left: 12px;
  font-style: italic;
}
</style>

# Documentation Overview

- Maintainable in version control  
- Exportable to HTML, PDF, PPTX  
- Markdown-based workflow  
- Customizable themes and layouts  

---

<!-- Background Image Slide -->
<!-- Replace bg.jpg with an actual image in your repo -->
![bg cover](https://marp.app/assets/hero-background.jpg)

# System Architecture

This slide uses a **full background image**.

---

# Algorithmic Complexity

Marp supports **math equations** using KaTeX:

Inline example:  
`Time ≈ O(n \log n)`

Block math:

$$
T(n) = n \log n + 2n + 5
$$

---

# Code Example

```python
def process_data(data):
    # O(n) example
    total = 0
    for x in data:
        total += x
    return total
