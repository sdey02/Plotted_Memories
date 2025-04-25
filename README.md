<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<!-- <br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
-->
<h3 align="center">Photo Plotter</h3>

<!-- ABOUT THE PROJECT -->
## About The Project

This project is what we came up for the nostolgia theme at UofT Hacks 11. The project allows users to upload a photo along with a short paragraph about what they did at that location. The photo is converted to base 64. Then using spaCY we parse the text to find the location and Cohere to generate a simple caption for the photo. The location is then passed to geopy to get the latitude and longitude which get sent a SQLAlchemy database along with the the base64 image for storage. The location data is also passed to leaflet where we create a pointer on the map that contains the photo and the cpation that was generated for that location. We also use a relational database to store a users login details.  

Contact details for the entire team, (Maxence, Hamza and me) can be found below.

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Project Demo
https://drive.google.com/file/d/1b5GzM2NIWVbllz4it4PbFUGiSXsnaOuZ/view?usp=sharing

<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Flask
* Geopy
* Cohere API
* SQLAlchemy
* ssl
* certifi
* spacy
* python-dotenv (for PostgreSQL support)
* psycopg2-binary (for PostgreSQL support)
  ```sh
  pip3 install cohere
  pip3 install geopy
  pip3 install flask
  pip3 install ssl
  pip3 install certifi
  pip3 install spacy
  pip3 install python-dotenv psycopg2-binary
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/sdey02/Plotted_Memories.git
   ```

2. Start the application
   ```sh
   python3 app.py
   ```

### Database Configuration

By default, the application uses SQLite. To switch to PostgreSQL:

1. Install PostgreSQL on your system
2. Create a database and user (see `postgres_setup_guide.md` for details)
3. Configure the `.env` file with your PostgreSQL connection string:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/plotted_memories
   ```
4. Run the application - it will automatically use PostgreSQL and create the necessary tables

To verify which database is in use, navigate to `/db_info` in the application.
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Plotted Memories lets you uplaod an image along with text about where you were and what you did that day. It can be used as a photo album or as a way to track all the palces you have been to.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Maxence Gilloteaux - https://www.linkedin.com/in/maxenceglt/
<br>
Shreyans Dey - https://www.linkedin.com/in/sdey02/
<br>
Hamza Zadi - https://www.linkedin.com/in/hmzzaidi/

<p align="right">(<a href="#readme-top">back to top</a>)</p>
