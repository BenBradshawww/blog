# My Blog

**Sections**
- [Summary](#summary)
- [Hugo](#hugo)
- [Key Features](#key-features)

---

### Summary
Welcome to my blog hosted at [www.mathstoml.com](www.mathstoml.com). There I share articles about mathematics, data science, machine learning, and data engineering. 

---

### Hugo
My site is built using Hugo, a powerful static site generator written in Go. I selected the [Niello theme](https://github.com/guangmean/Niello) by guangmean and made a few customizations to suit my style. Here's a screenshot of the final design:

![Website Screenshot](static/images/website_screenshot.png)

---

### Key Features
The highlight of my blog is its automated workflow. It seamlessly integrated with my Obsidian notes. Adding a new blog post is as simple as running:

```bash
bash scripts/bash_scripts/update_blogs.sh
```

This script:
	1.	Syncs the latest blog content from my Obsidian notes.
	2.	Updates the website directory.
	3.	Regenerates the static site with Hugo.
	4.	Pushes the updated site to GitHub.

This efficient process ensures my blog stays updated with minimal effort.

If I have applied other changes to the website, I can deploy these changes using:

```bash
bash scripts/bash_scripts/update_website.sh
```

Special thanks to Network Chuck for inspiration from his video ![here](https://www.youtube.com/watch?v=dnE7c0ELEH8&t=981s). 