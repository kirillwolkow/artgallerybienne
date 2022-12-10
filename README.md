# Art Gallery Bienne

### Video Demo: [Link to YouTube](https://youtu.be/sGxh1NSIMJs)


<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Art Gallery Bienne</h3>

  <p align="center">
    An online art gallery for local artists.
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is the final project of CS50s Introduction to Computer Science.

It's an online art gallery for local artists. I live in Biel/Bienne, it's a bilingual city near the capital Bern in Switzerland. Bilingual means we speak two languages in this city (german and french). Biel is the german name, Bienne the french one.

In Biel/Bienne we have a lot of creative artists from different domains. That's how I came up with this idea. I wanted to create a platform only for artists in my home town. A place where they can share their creative work to the world.

Also other people can upvote their work and comment on it.

First I created a finished design in Figma. I wanted to create a minimalistic, modern design with a touch of the high snobiety.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- EXPLAIN THE PROJECT -->
## Project Structure Explained

### **Apps**
A Django project consists of at least one, but mostly multiple apps. In this project I used three apps.
The gallery consists everything which has to do with the art pieces. Mainly the "Show Room". Django comes with a built-in user model. But for this project I decided to extend the user model and created the custom_auth app.
Last but not least the theme app. This app is created when installing TailwindCSS.

### **Templates Folders**
In every app there are templates folders. In those folders, the templates are stored. These are .html files which handle the HTML, CSS and also Django template syntax.

### **Forms.py**
In forms.py files are the forms defined. Speaking of sign up, login and submit art. This is for extending and customizing the forms.

### **Views.py**
The views.py files handle all the routing and rendering of every view (page) in the project. Every view stands for one page view or a submisison.

### **Models.py**
In models.py file are the database models defined. Django comes with a built-in ORM to create models, which are then translated to SQL statements.

### **Urls.py**
In the urls.py files, the routing and path structure are defined.

### **Settings.py**
The settings.py file consists of general settings and definitions for the project. For example where to store media and static files.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Django][Djangoproject.com]][Django-url]
* [![Tailwindcss][Tailwindcss.com]][Tailwindcss-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

In order to run this project on your local setup, follow the below instructions:

### Prerequisites

You need Python on your machine installed (Python version 3) and node/npm.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/kirillwolkow/artgallerybienne.git
   ```
2. Install python dependencies with:
   ```sh
   pip install -r requirements.txt
   ```

3. cd in to the project/theme/static_src folder and install NPM packages
   ```sh
   npm install
   ```
4. Replace your SECRET_KEY in `settings.py`
   ```python
   SECRET_KEY = 'ENTER YOUR SECRET KEY'
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To run the project you need the start the backend server and the frontend (Tailwind).

Backend Django Server in /project where the manage.py file is:
```sh
python manage.py runserver
```

Frontend TailwindCSS in /project/theme/static_src where the package.json file is:
```sh
npm run dev
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Kenny Wolf - [@kennyrogerwolf](https://twitter.com/kennyrogerwolf) - contact@kennywolf.info

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/kenny-wolf-744a6a227/
[Djangoproject.com]: https://img.shields.io/badge/Django-0C4B33?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://djangoproject.com
[Tailwindcss.com]: https://img.shields.io/badge/Tailwindcss-38BDF8?style=for-the-badge&logo=tailwindcss&logoColor=white
[Tailwindcss-url]: https://tailwindcss.com
