Movie Search Engine
Abdullah Alfawaz (aalfawaz@wisc.edu), Daniel Bradford (dcbradford@wisc.edu),
Salsabil Arabi (arabi2@wisc.edu)
Introduction
Motivation and project description
In this project, we built a web-based application focusing on movies and user interaction with
movie-related information. Specifically, the application served as a movie search engine for
users, driven by the need to address the lack of search engines capable of combining unique
constraints—such as displaying movies featuring specific actor and director combinations, or
filtering movies by actors within a particular genre or time frame. As film enthusiasts ourselves,
we were motivated by our own desire to discover more detailed and personalized information
about movies, which further inspired us to create a more comprehensive and user-friendly
platform.
The application provided a robust database of movies and movie-related data, allowing users to
search for films based on their preferred genre, user ratings, actors, directors, tags, and other
attributes. The ability to search movies based on a wide range of criteria significantly improved
the user experience, making it easier for audiences to find content tailored to their specific
interests. Given the universal appeal of movies across diverse audiences, such a comprehensive
movie database proved to be invaluable.
In the movie search application, users could search for movies based on any combination of their
preferences for genre, director, actor, and other attributes. They could also find the average rating
for any movie. Additionally, users were able to add new movies and movie-related details to the
database. The app required users to log in, and for those without an account, it provided the
ability to create one, granting them access to the full features of the movie search engine.
In this report, we describe the architecture of our application. We describe the dataset, ER
diagram, and relational schema of our database. We describe the implementation detail and
functionalities of our application and describe 5 test case for evaluation. At the end, we discussed
what we learnt while doing this project in the conclusion.
Team Organization
Daniel:
- creating the login and signup pages and linking them to the database and the rest of the
application.
- Implementing 4 search queries that he wrote
- General Interface improvements
Salsabil:
- Implement 5 search queries with sql queries
- implement database update and add movie
- merging the entire project
- creating the models and adding data to the models
Abdullah:
- Designing and updating the ER diagram
- Implementing a general “search by title” page, a movie information/details page, and the
“add rating” feature. Writing and implementing SQL queries for these features to handle
information retrieval, and insertion.
Implementation
System Architecture
Frontend: HTML/CSS, User Requests
- HTML files define the structure and content of the web pages. These templates are
rendered by Django views and include various interactive elements like forms, search
boxes, and buttons.
- CSS styles are used to define the visual appearance of the application, such as the layout,
colors, and typography.
-
Backend: Django Views, Models, and URL Routing
- The backend is powered by the Django web framework, which handles the
application’s logic, URL routing, and interaction with the database.
- Django views process requests, interact with the database, and render HTML templates to
generate the response sent to the user’s browser.
Database: SQLite
- SQLite is used to store movie data, user accounts, ratings, and other relevant
information.
Fig 1: Architecture of the application
Dataset
Link: https://files.grouplens.org/datasets/hetrec2011/hetrec2011-movielens-readme.txt
We used the MovieLens dataset created by the GroupLens research group, which has a variety of
information about movies, including user ratings. It contains information about over 2000 users
and 10000 movies such as: genres, directors, actors, countries, filming locations, ratings, and
tags. This dataset does not require us to integrate data from multiple sources. We wanted to
access information about a wide variety of movies, and this dataset provides most of the
information we were looking for in an easy to understand way. To define the scope of the
application, we’ve omitted certain attributes from our model such as movie titles in Spanish,
filming locations, timestamps related to individual instances of rating or tagging movies, and
exact dates and times of a rating or tagging by a user. The dataset also included rating data from
both IMDb and Rotten Tomatoes. We’ve chosen to only include IMDb ratings as we wanted the
ability to add ratings to the pre-existing pool and needed them to have a single source. Also,
Rotten Tomatoes’ ratings included distinctions between critic and user ratings which did not suit
our implementation of user-focused ratings.
This dataset is relatively clean. No null values were found. However, certain movie titles
appeared multiple times under different movie IDs (key used in original dataset). Addressing
duplicate data has been analyzed, but did not fall in the scope of this prototype due to its
complexity. Extra copies could still be tied to ratings and removing them would’ve removed
valuable rating data as well. Duplicates were observed to fall into two categories: a) “True
duplicates”, or separate entries that represent the same movie, and b) Unique movies that happen
to share the same title. To eliminate duplicate search results, the application (or some data
“cleaning” pre-process) would need to distinguish between a) and b), as well as consolidate
ratings and tags placed under separate instances of the same movie.
ER Diagram (Updated after checkpoint#2 for final prototype)
Fig 2: ER diagram
Relational Schema (Updated after checkpoint#2 for final prototype)
1. Movie(movieID:Real, IMDBpictureURL:String, year:Real, title:String, genre:String,
directorID:Real)
○ movieID is the primary key
○ No other keys
2. User(userID:Real, userName:String)
○ userID is the primary key
○ userName is also a key
3. Tag(tagID:Real, tagName:String)
○ tagID is the primary key
○ No other keys
4. Director(directorID:Real, directorName:String)
○ directorID is the primary key
○ No other keys
5. Actor(actorID:Real, actorName:String)
○ actorID is the primary key
○ No other keys
6. WatchedBy(movieID:Real, rating:Real, userID:Real)
○ (movieID, userID) is the primary key
○ No other keys
7. TaggedAs(movieID:Real, tagWeight:Real, tagID:Real)
○ (movieID, tagID) is the primary key
○ No other keys
8. Features(movieID:Real, actorRankInMovie:Real, actorID:Real)
○ (movieID, actorID) is the primary key
ALL NON TRIVIAL FUNCTIONAL DEPENDENCIES
1. movieID → {IMDBpictureURL, year, title, genre, directorID}
2. actorID → {actorName}
3. directorID → {directorName}
4. tagID → {tagName}
5. userID → {userName}
6. {actorID, movieID} → actorRankInMovie
7. {tagID, movieID} → tagWeight
8. {userID, movieID} → rating
From the schema we created and functional dependencies we detected above, we verified that all
tables were in the 3NF format. (i.e. for all FDs, the LHS is a candidate key OR the RHS is part of
a candidate key).
Implementation of prototype
We implement our application using Django, HTML, CSS, and SQLite database. Among the 15
level 2 and level 3 queries we included in checkpoint 4, we implemented 13 SQL queries in our
project. We have 8 database tables including the user table. The login/signup page saves the
information of the users in a user model and authenticates a user using his/her saved password.
Database search: We have 12 different pages in the app that users can interact with. The movie
detail page shows the detailed information of a movie including year, genre, average user rating,
tags and actors associated with the movie given the name of a movie title. There are 9 different
search pages where users can give a combination of criteria and the application shows the
movies that satisfy the criteria. It includes search by actor, director, tag, actor and director pair
etc. Users can insert a rating and find movies having average rating higher than or equal to that
rating. Users can also insert a genre and year and find top 10 highly rated movies in that
particular year and genre in descending order of their rating. The application also lets users do
complex queries like finding movies of an actor within a timeframe where users insert the actor
name and years. Also, users can search for lead actors and actresses associated with a movie
selected by the user.
Adding or modifying database: The app lets the user add any movie and relevant information
to the database. Based on the input of the users, the app also creates a new director if the specific
director doesn’t exist in the database. Therefore, adding a movie updates the movie table as well
as the director table. Users can also modify the information of a movie already existing in the
database. When a user adds an existing movie again, it updates the instance of the movie in the
database with the new information, but does not create multiple instances with the same title.
We also have an “add rating” page that lets an user give a rating to a specific movie or update
his/her previously given rating.
Evaluation
We want to assess if the application is extracting the correct information from the database and
working the way we expect it to work. To assess that, we search with the same criteria and match
the search result with the raw query done on the actual dataset in python.
Test case 1: Find the movies directed by John Lasseter;
Fig 3(a): screenshot of result from search in the database Fig 3(b): search in app
Test case 2: Find the movies in which Gillian Barber acted;
Fig 4(a): screenshot of result from search Fig 4(b): search in the app
in the database
Test case 3: Add a new dummy movie and check if the movie details page shows the
information. If the new movie is properly added in the database, the movie details page with that
particular movie should be able to show the newly added movie and associated information. It
tests both the add movie and movie details page.
Fig 5(a): movie add to the database Fig 5(b): an instance of test08 is created in movie
database and it is displayed in the Movie detail page
Test case 4: Find the top 10 highly rated movies in genre “Comedy” and year 1995 (Des order).
Fig 6(a): screenshot of top rated movies from database Fig 6(b): search result in app
Test case 5: We test if the database is being updated properly by adding a movie that is already
in the database with new information. If the information in the movie details page gets updated
with the new data, we can assume existing entries in the database are being updated/modified
properly.
Fig 7(a): Movie details of “test208” before database update
Fig 7(b): database update Fig 7(c): Movie details of “test208” after database update (the director
name and year has changed with the updated information)
Conclusion
Throughout this project, we learnt many lessons that are useful in real world application and
development scenarios as every type of development is somewhat connected with data and
database. We learnt how to convert a large bulk of data into relational models and schema so that
we do not store redundant data in the model. While implementing the project, we realized the
importance of robust data modeling. We realized how crucial it is to design the data models that
accurately represent relationships between movies, directors, actors, and genres was crucial for
ensuring efficient queries and a flexible application structure. We also realized the importance of
maintaining "clean" information storage because redundancy and missing information can make
information retrieval and analysis difficult. The concept of primary key was extremely useful as
it helps the model store unique data based on the key. Through the course, we learnt advanced
SQL queries that knowledge was extremely handy as we were running queries on 8 different
models and joining the models for complex search functions.
