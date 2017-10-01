import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story 3", "A group of toys come to life.", "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450","https://www.youtube.com/watch?v=ZZv1vki4ou4")

school_of_rock = media.Movie("School of Rock", "An unemployable man who's passionate for rock music trains fifth graders to become a band worthy of entering a rock competition", "https://www.visitmuskogee.com/wp-content/uploads/2017/08/School-of-Rock-poster-iii.jpg", "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

last_airbender = media.Movie("Avatar: The Last Airbender", "Aang attempts to defeat the Firelord utilizing skills acquired in four elemental magic kung fu practices.", "https://resizing.flixster.com/NGDEUhnmpjgLkiE5VIMGjV4S38g=/206x305/v1.dDsyMzk3NDg7ajsxNzQ3ODsxMjAwOzEwNjQ7MTU5Ng", "https://www.youtube.com/watch?v=dMnDkFktGF4")


movies = [toy_story, school_of_rock, last_airbender]

fresh_tomatoes.open_movies_page(movies)