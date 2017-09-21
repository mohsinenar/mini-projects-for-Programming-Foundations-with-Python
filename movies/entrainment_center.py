import fresh_tomatoes
import media 

toy_story =  media.Movie("toy story","a story of a boy ..." ,"https://static.pexels.com/photos/67636/rose-blue-flower-rose-blooms-67636.jpeg","https://www.youtube.com/watch?v=gINb4S3-Ebc")
#print(toy_story.storyline)



avatar =  media.Movie("avatar","avatar story line" ,"https://static.pexels.com/photos/67636/rose-blue-flower-rose-blooms-67636.jpeg","https://www.youtube.com/watch?v=gINb4S3-Ebc")

#print(avatar.storyline)
#avatar.show_trailer()

fightclub = media.Movie("flight club " ,
                        "A depressed man (Edward Norton) suffering from insomnia meets a strange soap salesman named Tyler Durden (Brad Pitt) and soon finds himself living in his squalid house after his perfect apartment is destroyed",
                        "http://www.gstatic.com/tv/thumb/movieposters/23069/p23069_p_v8_af.jpg",
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg")
#fightclub.show_trailer() 



v_for_vendetta= media.Movie("v for vendetta " ,
                        "Following world war, London is a police state occupied by a fascist government....",
                        "http://www.theimaginativeconservative.org/wp-content/uploads/2014/08/v-for-vendetta-art.png",
                        "https://www.youtube.com/watch?v=k_13fFIrhPk")


movies = [avatar,fightclub,v_for_vendetta]

#fresh_tomatoes.open_movies_page(movies)

#print(avatar.valid_ratings)

#print(avatar.__doc__)

#print(avatar.__name__)
