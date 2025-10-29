# blog_platform
## Internboot Task: Blog Platform 

- 📌 Description:
   - This project is a fully functional **Blogging Platform** built using Django, where users can create, manage, and publish blog posts. It supports secure authentication, role-based access, and interactive      features for readers.

- 🚀 Features:
   - 🔐 Secure sign-up, login, and role-based access (Admin, Author, Reader).
   - 🗂️ Organize posts by **categories** and **tags** for easy navigation.
   - 💬 Readers can **comment** on posts and **like** content.
   - 📊 Admins can manage users, posts, comments, and tags via Django Admin.

- 🛠️ Tech Stack:
   - | Framework | Language | Database |
   - |-----------|----------|----------|
   - | Django / WordPress | Python / PHP | SQLite / PostgreSQL / MySQL |

- 📂 Folder Structure:
   - blog_platform/
   -   ├── blog_platform/ # Project settings
   -   │    └── settings.py
   -   ├── blog/ # Main app
   -   │    ├── models.py    # Database models (Post, Comment, Tag, Like, User)
   -   │    ├── views.py     # View logic for post display, comment, like, etc.
   -   │    ├── urls.py      # URL routing
   -   │    ├── forms.py     # Forms for post creation and commenting
   -   │    ├── static/      # CSS/JS
   -   │    └── templates/
   -   │         └── blog/
   -   │              ├── base.html           # Base layout
   -   │              ├── post_list.html      # List of all posts
   -   │              ├── post_detail.html    # Single post view with comments and likes
   -   │              ├── post_form.html      # Form to create/edit posts
       │              └── login.html          # Login page
   -   │                    ......
   -   ├── db.sqlite3        # SQLite database
   -   └── manage.py         # Django management script

- 📊 Dataset:
   - This project uses a **custom database** with the following models:
     - 📝 Posts
     - 👥 Users (Admin, Author, Reader)
     - 💬 Comments
     - ❤️ Likes
     - 🏷️ Tags and Categories.
         > The dataset is embedded in Django models and migrations.

- 📽️ LinkedIn Submission:
     - A recorded video has been uploaded to LinkedIn explaining:
       - What I built
       - How I cleaned and structured the data
       - My storytelling process during development
- 🔗 [LinkedIn Video Link](https://www.linkedin.com/posts/asmatullah-khan-04babb220_video-submission-internboot-challenge-activity-7389240392631664640-eW8C? utm_source=share&utm_medium=member_desktop&rcm=ACoAADexPXsBMjzGH9QUyOEgTfz-ZPqeViCx8hM)  
- 🔗 [GitHub Repo Link] (https://github.com/asmat72/blog_platform.git)

- 🎯 Learning Outcomes:
     - ✅ Experience in CMS development or custom web apps using Django or WordPress
     - ✅ Understanding of user roles and permissions
     - ✅ Database design for posts, comments, likes, and user interactions
     - ✅ Real-world deployment and GitHub workflow

- 🙌 Credits:
      Developed by **Asmatullah Khan**  
      Tagged: **@InternBoot** and **@E2V (Employment Express Verband LLP)**
