import CreateClass

movies = ["Spider-Man", "Deadpool",]
games = ["Persona 5", "Minecraft", "Rust", "Persoan 3", "Titanfall 2"]
myCollection = CreateClass.Collection(movies, games)

myCollection.SetFavGame("Persona 4")
myCollection.SetFavMovie("Spider-Man 3")
myCollection.displayCollection()