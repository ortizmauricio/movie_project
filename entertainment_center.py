import movies
import fresh_tomatoes
                         
a_Team = movies.Movie("The A-Team",
                      "A group of long time friend go on an adventure",
                      "https://upload.wikimedia.org/wikipedia/en/e/e8/A_team_poster_10.jpg",
                      "https://www.youtube.com/watch?v=VAnl1BTAP8U")

bourne_Identity = movies.Movie("The Bourne Identity",
                               "A man suffering amnesia struggles to find who he is",
                               "https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
                               "https://www.youtube.com/watch?v=FpKaB5dvQ4g")

despicable_Me = movies.Movie("Despicable Me",
                             "A villian faces an unexpected challenge",
                             "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
                             "https://www.youtube.com/watch?v=nVwae09eSpo")

whiplash = movies.Movie("Whiplash",
                        "A young drummer's journey to play to perfection",
                        "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",
                        "https://www.youtube.com/watch?v=Oe2aD3Px9wg")

social_Network = movies.Movie("The Social Network",
                              "The story behind the biggest network in the world",
                              "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                              "https://www.youtube.com/watch?v=oxXj-h0ELwA")

dark_Knight_rises = movies.Movie("The Dark Knight Rises",
                           "The completion to the Gotham trilogy",
                           "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
                           "https://www.youtube.com/watch?v=yFT9r3Zwtek")

movies = [a_Team, bourne_Identity, despicable_Me, whiplash, social_Network, dark_Knight_rises]

fresh_tomatoes.open_movies_page(movies)
