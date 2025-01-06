from django.shortcuts import render, get_object_or_404, redirect
from movies.models import Director, Movieproject, Directorproject, Actorproject, Featuresproject, Tagproject, Taggedasproject, Watchedbyproject
from django.http import HttpResponse
from django.db import connection
from .forms import TitleForm

# Handles a "search by title" page. Takes movie title input from user and displays database entries that match. 
# Each search result can be clicked to transport to the display movie page.
def title_search_project(request):
    results = []
    title = '' 
    message = ''
    
    if request.method == 'POST':
        form = TitleForm(request.POST)
        if form.is_valid():   
            title = form.cleaned_data['title']
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT DISTINCT title, year, movieID
                    FROM movies_Movieproject 
                    WHERE title LIKE %s
                    GROUP BY title, year
                """, [title.lower()]) 
                results = cursor.fetchall()
            results = [{'title': row[0], 'year': row[1], 'movieID': row[2]} for row in results]
            
            if not results:
                message = 'No movies found for this title in the database.'
        else:
            message = 'Title is whitespace-sensitive'
    else:
        form = TitleForm()
        message = 'Title is whitespace-sensitive'
    
    return render(request, 'movie_by_title.html', {'form': form, 'results': results, 'title': title, 'message': message})

# Handles an "add rating" feature
def add_rating(request, movieID):
    message = ''
    
    if request.method == 'POST':
        rating = request.POST.get('rating')
        userID = request.POST.get('userID')
        
        with connection.cursor() as cursor:
            # check if the rating already exists 
            cursor.execute("""
                SELECT COUNT(*) FROM movies_watchedbyproject
                WHERE movieID = %s AND userID = %s
            """, [movieID, userID])
            exists = cursor.fetchone()[0] > 0
            
            if exists:
                # update existing rating
                cursor.execute("""
                    UPDATE movies_watchedbyproject
                    SET rating = %s
                    WHERE movieID = %s AND userID = %s
                """, [rating, movieID, userID])
                message = 'Movie has already been rated by this user. Previous rating overwritten.'
            else:
                # add new rating
                cursor.execute("""
                    INSERT INTO movies_watchedbyproject (movieID, userID, rating)
                    VALUES (%s, %s, %s)
                """, [movieID, userID, rating])
                message = 'Rating added'
    
    return render(request, 'add_rating.html', {'message': message, 'movieID': movieID})


# Handles the page that deisplays all details for a specific movie
def displayMovie(request, movieID):

    info = get_movie_info(movieID)
    director = get_movie_director(movieID)
    rating = get_movie_rating(movieID)
    tags = get_movie_tags(movieID)
    actors = get_movie_actors(movieID)

    movie = {
        'info': info,
        'director': director,
        'rating': rating,
        'tags': tags,
        'actors': actors,
        'movieID': movieID,

    }
    
    return render(request, 'displayMovie_copy.html' , {'movie': movie})


def get_movie_info(movieID):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT imdbPictureURL, year, title, genre, directorID 
            FROM movies_Movieproject 
            WHERE movieID = %s
        """, [movieID])
        row = cursor.fetchone()

    if row:
        info = {
            'imdb_picture_url': row[0], 
            'year': row[1],
            'title': row[2],
            'genre': row[3],
            'director_id': row[4]
        }
    else:
        info = None

    return info


def get_movie_director(movieID):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT d.directorName 
            FROM movies_movieproject AS m
            INNER JOIN movies_directorproject AS d ON m.directorID = d.directorID
            WHERE m.movieID = %s
        """, [movieID])
        row = cursor.fetchone()

    director = row[0] if row else None
    return director


def get_movie_rating(movieID):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT AVG(rating)
            FROM movies_watchedbyproject
            WHERE  movieID = %s
        """, [movieID])
        row = cursor.fetchone()

    rating = row[0] if row else None
    return rating


def get_movie_tags(movieID):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT tagName
            FROM movies_taggedasproject ta
            INNER JOIN movies_tagproject as t ON ta.tagID = t.tagID
            WHERE ta.movieID = %s
            ORDER BY ta.tagweight DESC
            LIMIT 6
        """, [movieID])
        rows = cursor.fetchall()

    tags = [row[0] for row in rows]
    return tags

def get_movie_actors(movieID):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT actorName
            FROM movies_featuresproject f
            INNER JOIN movies_actorproject as a ON f.actorID = a.actorID
            WHERE f.movieID = %s
            ORDER BY f.actorRankInMovie DESC
        """, [movieID])
        rows = cursor.fetchall()

    actors = [row[0] for row in rows]
    return actors



    