# 1. Create a class to represent a Video Game or Movie Collection
# 2. Create a constructor method __init__()
# 3. Create a list for the video game and movies each
# 4. Create a instance variable for the users favorite movie and video game
# 5. Create the following functions for your class
# - A function to display all the movies
# - A function to display all the video games
# - A function to add a movie/video game
# - A function to remove a movie/video game
# - A function to select a favorite movie/video game
# 6. Create a seperate file to test your class/code

class Collection:
    def __init__(self, movieList, gameList):
        self.movieList = []
        self.gameList = []
        self.favGame = ""
        self.favMovie = ""

        self.movieList = movieList
        self.gameList = gameList

    def displayMovies(self):
        print("Movies in the collection:")
        for movie in self.movieList:
            print(movie)

    

    def displayGames(self):
        print("Games in the collection:")
        for game in self.gameList:
            print(game)

    def displayFavMovie(self):
        print(f'Fav Movie: {self.favMovie}')


    def displayFavGame(self):
        print(f'Fav Game: {self.favGame}')

    def displayCollection(self):
        self.displayMovies()
        self.displayFavMovie()
        self.displayGames()
        self.displayFavGame()
       
    def SetFavMovie(self, movie):
        if movie not in self.movieList:
            self.addMovie(movie)
        self.favMovie = movie

    def SetFavGame(self, game):
        if game not in self.gameList:
            self.addGame(game)
        self.favGame = game

    def addMovie(self, movie):
        if movie in self.movieList:
            print(f"{movie} is already in the collection.")
        else:
            self.movieList.append(movie)
        
          



    def addGame(self, game):
        if game in self.gameList:
            print(f"{game} is already in the collection.")
        else:
            self.gameList.append(game)
        

    
    def removeMovie(self, movie):
        if movie in self.movieList:
            self.movieList.remove(movie)
        else:
            print(f"{movie} not found in the collection.")





    def removeGame(self, game):
        if game in self.gameList:
            self.gameList.remove(game)
        else:
            print(f"{game} not found in the collection.")


    
    def selectFavMovie(self, movie):
        self.favMovie = movie


    
    def selectFavGame(self, game):
        self.favGame = game
        
 

    
    