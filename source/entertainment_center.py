import fresh_tomatoes #import of fresh_tomatoes file
import media          #import of media file

#Furious 7 Movie Instance
furious_seven = media.Movie("Furious 7",
                            "Deckard Shaw seeks revenge against Dominic Toretto and his family for his comatose brother.",
                            "http://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Furious_7_poster.jpg/220px-Furious_7_poster.jpg",
                            "https://www.youtube.com/watch?v=Skpu5HaVkOc")

#Interstellar Movie Instance
interstellar = media.Movie("Insterstellar",
                     "A team of explorers travel through a wormhole in an attempt to ensure humanity's survival.",
                     "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX214_AL_.jpg",
                     "https://www.youtube.com/watch?v=zSWdZVtXT7E")

#Romeo Must Die Movie Instance
romeo_must_die = media.Movie("Romeo Must Die",
                     "An avenging cop seeks out his brother's killer and falls for the daughter of a businessman who is involved in a money-deal with his father.",
                     "http://ia.media-imdb.com/images/M/MV5BMTI5Nzg1MjA5M15BMl5BanBnXkFtZTYwNzAxNzg2._V1_SY317_CR0,0,214,317_AL_.jpg",
                     "https://www.youtube.com/watch?v=w500paj_MPU")

#Gladiator Movie Instance
gladiator = media.Movie("Gladiator",
                     "When a Roman general is betrayed and his family murdered by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge.",
                     "http://ia.media-imdb.com/images/M/MV5BMTgwMzQzNTQ1Ml5BMl5BanBnXkFtZTgwMDY2NTYxMTE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                     "https://www.youtube.com/watch?v=uwTKRz-WmHU")

#Lord of the Rings One Movie Instance
lord_of_rings_one = media.Movie("The Lord of the Rings: Fellowship of the Ring",
                     "A meek hobbit of the Shire and eight companions set out on a journey to Mount Doom to destroy the One Ring and the dark lord Sauron.",
                     "http://ia.media-imdb.com/images/M/MV5BNTEyMjAwMDU1OV5BMl5BanBnXkFtZTcwNDQyNTkxMw@@._V1_SY317_CR1,0,214,317_AL_.jpg",
                     "https://www.youtube.com/watch?v=V75dMMIW2B4")

#Lord of the Rings Two Movie Instance
lord_of_rings_two = media.Movie("The Lord of the Rings: The Two Towers",
                     "While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided fellowship makes a stand against Sauron's new ally, Saruman, and his hordes of Isengard.",
                     "http://ia.media-imdb.com/images/M/MV5BMTAyNDU0NjY4NTheQTJeQWpwZ15BbWU2MDk4MTY2Nw@@._V1_SY317_CR1,0,214,317_AL_.jpg",
                     "https://www.youtube.com/watch?v=LbfMDwc4azU")

#Lord of the Rings Three Movie Instance
lord_of_rings_three = media.Movie("The Lord of the Rings: The Return of the King",
                     "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
                     "http://ia.media-imdb.com/images/M/MV5BMjE4MjA1NTAyMV5BMl5BanBnXkFtZTcwNzM1NDQyMQ@@._V1_SX214_AL_.jpg",
                     "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

#American Sniper Movie Instance
american_sniper = media.Movie("American Sniper",
                     "Navy SEAL sniper Chris Kyle's pinpoint accuracy saves countless lives on the battlefield and turns him into a legend. Back home to his wife and kids after four tours of duty, however, Chris finds that it is the war he can't leave behind.",
                     "http://ia.media-imdb.com/images/M/MV5BMTkxNzI3ODI4Nl5BMl5BanBnXkFtZTgwMjkwMjY4MjE@._V1_SX214_AL_.jpg",
                     "https://www.youtube.com/watch?v=5bP1f_1o-zo")

#Rocky Movie Instance
rocky = media.Movie("Rocky",
                     "Rocky Balboa, a small-time boxer gets a supremely rare chance to fight the heavy-weight champion, Apollo Creed, in a bout in which he strives to go the distance for his self-respect.",
                     "http://ia.media-imdb.com/images/M/MV5BMTY5MDMzODUyOF5BMl5BanBnXkFtZTcwMTQ3NTMyNA@@._V1_SX214_AL_.jpg",
                     "https://www.youtube.com/watch?v=3VUblDwa648")

#Create list containing movies
movies = [furious_seven, interstellar, romeo_must_die, gladiator, lord_of_rings_one, lord_of_rings_two,
          lord_of_rings_three, american_sniper, rocky]

#Call method passing list of movies as parameter
fresh_tomatoes.open_movies_page(movies)
