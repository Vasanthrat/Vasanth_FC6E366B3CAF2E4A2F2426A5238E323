'''Implement a class called player that represents a cricket player.The player class should have a
method called play() with prints "The payer is playing cricket.Derive two classes, Batsman and
Bower,from the player .Theclass.Override the play() method in each derived class to print"The batsman
is bating" and "The bowler is bowling", respectively.Write a program to create objects of both the 
Batsman and Bowler classes and call the play() mathod for each object.'''


#Define the base class player
class player:
  def player(self):
    print("The player is playing cricket.")

#Define the drived clas Batsman
class Batsman(player):
  def player(self):
    print("The Batsman is batting.")
#Define the derived class Bowler
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")

#create objects of Batsman and Bowler classes 
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object
batsman.player()
bowler. player()