import json
import os


class Movie():

    DIR_DATA = os.path.join(os.path.dirname(__file__), 'data', 'movie.json')

    if not os.path.exists(DIR_DATA) :
        with open(DIR_DATA,"w") as f :
            json.dump([],f)
    


    def __init__(self, movie_name : str):
        self.movie_name = movie_name.title()
    
    def __str__(self) -> str:
        return self.movie_name

    def get_movies(self) :
        try :
            with open(self.DIR_DATA,"r") as f :
                return json.load(f)
        except json.decoder.JSONDecodeError :
            pass

    def set_movies(self,movie):
        contenu = []
        try :
            with open(self.DIR_DATA,"r") as f :
                contenu = json.load(f)
        except json.decoder.JSONDecodeError :
            pass
        contenu.append(movie)
        with open(self.DIR_DATA,"w") as f :
            json.dump(contenu, f, indent=4 , ensure_ascii=False)







if __name__ == "__main__" :

    m = Movie("harry potter")

    print(m)

    
    m.set_movies("STAR WARS")
    print(m.get_movies())


    m.set_movies("LOTR")
    print(m.get_movies())






        
