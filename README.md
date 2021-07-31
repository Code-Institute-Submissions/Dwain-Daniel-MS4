<h1>Milestone Project</h1>

My site can be viewed at https://dwain-power-gym.herokuapp.com/ 


This project will be used to display all that I have learned so far. I will be using this project to build a website for those trying to get fit and purchase a series of workouts. User of the site will be able view, buy and comment on all of these workouts. Admin will be able to add, delete and edit the workouts being displayed. I want the website to be easily accessible, simple to navigate and user friendly. 
It must also be displayed for various devices (desktop ,Tablet, Mobile Phone) whilst maintaining a great user experience . Links within the website directing me to other pages either within this website 


<h3>UX</h3>

<h4>User Stories</h4>

New users

<li>I want the user to easily understand the main purpose of the site and view recipes</li>
<li>I want the user to be able to easily navigate throughout the site to find content.</li>
<li>I want the user to be intrigued enough to register an account</li>
<li>I want the user to be able to view the workouts available</li>
<li>I want the user to be able to search for the category of workout they want</li>


Returning users

<li>I want the user to be able to log in easily</li>
<li>I want the user to be able to view their own profile</li>
<li>I want the user to be able to comment on the blog and save these</li>
<li>I want the user to be able to search for the category of workout they want</li>
<li>I want the user to be able to view the workouts available</li>
<li>I want the user to be able to view their previous orders</li>
   
<h3> Design </h3>

<h4>Colour Scheme</h4>

I have used an bloack and white theme. I have used this as it is quite bold and portrays strength and hard work. The theme is consistent throughout the site which is good for the UI/UX. The header and footers 
are both black with white text and icons.The background is white, with black text. 

<h4>Icons </h4>

I have incorporated icons from Font Awesome, thes have a functional purpose of highlighting certain input fields for the user.

<h4>Defensive Design</h4>

<li>To submit and edit a workout, the user must be a authenticated super user</li>
<li>To submit a comment on a blog, the user must be a authenticated user</li>
<li>A recipe or category can't be deleted by just one click.</li>

<h4>Wireframe</h4>

The final version whilst similar doesnt match exactly. My wireframes can be found in my wireframes folder.

<h4>Features</h4>

<li>The links on the site all take you to the pages described.</li>
<li>Site is responsive to different device sizes.</li>
<li>Power Gym logo is found in the top left of all pages, this will take the user to the home page.</li>
<li>The links are located to the right of the page, with an additional header containing links to the workout catergories, these will colapse into a navigation tab one smaller devices.</li>
<li>The navigation links and buttons show a slight shadowing to let the user know that they are above a clickable button.</li>
<li>Flash messages appear to let the user know what they have done for example a successful purchase or moving a workout to the bag.</li>
<li>Once the user is signed in they have full functionality of the site. Non registered users can only see the Log In, the workouts and the bag.</li>
<li>The submit and edit recipe workouts have fully functioning forms with defensive programming</li>
 

<h3>Features left to implement</h3>

I would like to add a number of features going forward such as: <br>
<li>A better stylized blog and comments page</li>
<li>Send automatic confirmation emails</li>
<li>Allow users to submit requests</li>

<h3>Languages Used</h3>

<li>CSS</li> 
<li>HTML</li>
<li>jQuery</li>
<li>Python</li>


<h3>Technologies Used </h3>

I have built my site using: 

[<h4>CSS</h4>](https://en.wikipedia.org/wiki/CSS) 
I have used CSS to style my website

[<h4>HTML</h4>](https://en.wikipedia.org/wiki/HTML) 
I have used HTML as the main language to create my website.

[<h4>Materialize</h4>](https://materializecss.com/)
I have used this for the responsive layout as well as custom components such as header, images, icons,footer, cards, and collapse element.

[<h4>Balsamiq</h4>](https://balsamiq.com/#)
I used Balsamiq to help create my template and design a quality site 

[<h4>Jinja</h4>](https://jinja.palletsprojects.com/en/3.0.x/)
I have used Jinja for my Python template

[<h4>GitHub</h4>](https://github.com/)
I have used Github as the hosting site for my code.

[<h4>SQLite</h4>](https://www.sqlite.org/index.html)
She project uses SQLite as the relational database to hold the backend information for the varions models used, when running locally.

[<h4>Stripe API</h4>](https://stripe.com/gb)
The project uses Stripe to make secure payments for logging and upvoting Feature Requests. The project uses Stripe's test payment functionality.

[<h4>Django</h4>](https://www.djangoproject.com/)
The project uses Django as the Python web framework.

[<h4>Heroku</h4>](https://www.heroku.com/)
I have used Heroku to deploy my app 

[<h4>Gunicorn 20.0.4</h4>](https://docs.gunicorn.org/en/stable/)
Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server. The Gunicorn server is broadly compatible with a number of web frameworks, simply implemented, light on server resources, and fairly speedy. https://docs.gunicorn.org/en/stable/

[<h4>MongoDB</h4>](https://www.mongodb.com/)
I have used MongoDB as the database service for my project

<h4>Git</h4>
Git is used as version control software to commit and push code to the GitHub repository where the source code is stored.

[<h4>Techsini</h4>](http://techsini.com/multi-mockup/index.php)
I have used this to create a mock up of the site on different devices


<h3>Testing</h3> 

I have tested my site thoroughly, all the links are working and take the user to the correct pages. 
The webpage will respond when used on smaller devices, the nav bar will shrink down into a drop down menu. 

<li>I placed my site throught a CSS Validator which returned no errors</li>
<li>I have placed all pages through a HTML Validator which returned one warning</li>>
<li>I have tested my webpage using [Google Mobile Testing](https://search.google.com/test/mobile-friendly) This returned no errors</li>
<li>I have tested the Javascript on my webpage, this returned two warnings, no errors.</li>
<li>I have placed all pages through a Python Validator. It returned a Pass mark.
<li>I have also tested my page using Chrome Dev Lighthouse


<h3>Test User Stories</h3>

<h4>New Users</h4>

I want to easily understand the main purpose of the site and begin a fitness journey by picking a workout best suited for me.
Upon entering the site, users will see the website name in the top left corner, Power Gym, followed by a variety of links in the top right.
Below that there is a text section detailing what the site is about and its aims. This should have enough information to get me to register an account.
I want to be able to easily navigate throughout the site to find content.
The header will contain links to the other pages, this will be a responsive menu that will collapse on a mobile device. 


<h4>Returning Users</h4>
 
I can find the log in section quite easily both with the log in button in the nav bar but also the link on the register page.
Submitting a order is very easy with all text fields clearly labelled and formatted to only allow the relevant text.
The search function works very well, if I want a workout containing the word 'bulk' for example all bulking workouts will appear 
All other workouts will be listed on the workouts page.


<h4>Deployment</h4>

The web-site is designed in the Gitpod environment and regularly committed to GitHub after each crucial piece of coding. 
Using this method as a sanity check for the development enabled me to restore the site back to previous stages when it 
functioned correctly or easily find lost pieces of code. 

<h3>To deploy the project to Github the following steps were taken:</h3>

  1. created a `master` branch in Github repository 
  2. Used Local AWS Cloud9 and Gitpod environment used to build the site
  3. Committed files to the staging area using bash terminal commands: `git status`; `git add .`; `git commit -m"add message"`
  4. Pushed files to the working environment using `git push`, which then updates the repository.
  5. Published site from `master` branch using `settings` tab in the main page of the repository, select `source` as `master branch`, then `save`
  6. The repository can be cloned by clicking `Clone or Download` on the main page of the repository 
  7. In the Clone with HTTPs section, click the clipboard icon to copy the clone URL for the repository
  8. Open Git Bash Terminal
  9. Type `git clone`, and then paste the URL
  10. Press `Enter`. A local clone will be created.

<h3>To set gitignore environment variables the following steps were taken:</h3>

  1. Create a file named env.py in the root directory of your project. This is the file you will use to define your environment variables.
  2. If you don't have one already, create a file named .gitignore  in the root directory of your project.
  3. Next we need to stop git from pushing this file to github, and so keep your environment variables secret. To do this, open your .gitignore  file add the following text: env.py
  4. At the top of your env.py  file, you need to import os so that you can set the environment variables in the operating system. Once you have added the line “import os” 
     underneath you can assign your environment variables using the following syntax:  
     `os.environ["Variable Name Here"] = "Value of Variable Goes Here"`
  5. Then the following code imports this new env.py file where you need to use your environment variables. For example your app.py file for flask project. Add this under your 
     other imports at the top of the file  
     `from os import path`
      `if path.exists("env.py"):`
      `import env` 
  6. Now that your environment variables have been set in your env.py file, and the file has been imported into your project, you can use them as needed, for example using the following syntax:  
     `DATABASES = {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),}`

### To deploy the project to Heroku the following steps were taken:

  1. created a Heroku account @ https://signup.heroku.com/
  2. Create `requirements.txt` file in Gitpod workspace for Heroku to understand installation files to run app. From CLI type type 
     `pip3 freeze --local > requirements.txt`.
  3. To install the Heroku command line on Gitpod, use the following command `npm install -g heroku`
  4. Using the `New` buton, Create a new app with apropriate title and server in Heroku. This creates a connection between the Gitpod application and Heroku that would allow us 
     to push our changes using Git to update the application at any given time. 
  5. To login to Heroku from the CLI, use the command `heroku login -i`
  6. To get the application up and running a `Procfile` is required that istructs Heroku which file is the entry point. Use the following command to create this: 
     `echo web: python app.py`
  7. Code that is prepared to be pushed from Github to Heroku can be executed following the CLI commands:
     `git add .`
     `git commit -m "first Heroku commit"`
     `git push`
  8. Now that the relevant code is pushed to Github, it can also be pushed to Heroku from the chosen branch (e.g. Master)
  9. To connect an existing repository from Github to Heroku use the following CLI syntax: `heroku git:remote -a dwain-power-gym`
  10. To push to Heroku Master Branch, then simply use `git push heroku master`
  11. To scale dynos and run the app in Heroku, use the CLI command: `heroku ps:scale web=1`
  12. In order for the server instance on Heroku to know how to run our application, we need to specify a few Config Vars in Heroku. To do this go to `Settings` 
      tab > `Config Variables` and input: `AWS_ACCESS_KEY_ID`; `AWS_SECRET_ACCESS_KEY`; `DATABASE_URL`; `DISABLE_COLLECTSTATIC`; `EMAIL_ADDRESS`; `EMAIL_PASSWORD`
      `EMAIL_PASSWORD`; `SECRET_KEY`; `STRIPE_PUBLISHABLE`; `STRIPE_SECRET`.  
  13. The following syntax will need to be added to your settings.py file to access the SECRET KEY for the new database URL `DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}`
  14. The Database can then be migrated to the Heroku Postgres (postgresql) database using the the commands `mmakemigrations` and `migrate` from the command line.      
  15. Once the build in Heroku is complete, click the `Open app` button.
  16. Objects can then be added to the new postgres database using the Admin Panel and logging in with your superuser credentials.  


<h3>Credits</h3>
The Boutique Ado project was my initial inspiration for my project, I then tailored this to a gym website after viewing gym website templates on https://colorlib.com/
All of the images used were taken from https://www.pexels.com/

<h3>Acknowledgements</h3> 

I need to thank my mentor Spencer Barriball for helping me and providing the guidance I needed. I would not have made it this far on the course without his advice and support. Absolutely brilliant tutor/mentor. 
Tutor support was also a great help on occasion as well as Slack.
