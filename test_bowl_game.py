import bowl_game
import unittest

class TestBowlGame(unittest.TestCase):

    def test_life_the_universe_and_everything(self):
        douglas = bowl_game.BowlGame()
        
        #Testing helper functions
        self.assertEqual(["0","1"],douglas.score_game_helper("-1"))
        self.assertEqual(["X","0","1"],douglas.score_game_helper("X|-1"))
        self.assertEqual(['0','0','1','0','1','1','0','2','3','0','4','0','0','5','8','1','9','0','1','0',"",""], 
            douglas.score_game_helper("--|1-|11|-2|3-|4-|-5|81|9-|1-||"))
        self.assertEqual(['X','5','5/','1','1','0','2','3','0','4','0','0','5','8','1','9','0','1','0',"","5","5"], 
            douglas.score_game_helper("X|5/|11|-2|3-|4-|-5|81|9-|1-||55"))
            
        self.assertEqual(10,douglas.str_to_score("X"))
        self.assertEqual(6, douglas.str_to_score("6"))
        self.assertEqual(6, douglas.str_to_score("6/"))        
        #Testing Actual games
        
        #no pins
        """
        self.assertEqual(0, douglas.score_game("--|--|--|--|--|--|--|--|--|--||"))
        print("--------")
        
        #some pins, no strikes/spares
        self.assertEqual(36, douglas.score_game("--|1-|11|-2|3-|4-|-5|81|9-|1-||"))
        print("--------")
                
        #spares, not last bowl
        self.assertEquals(20 ,douglas.score_game("5/|5-|--|--|--|--|--|--|--|--||"))
        print("--------")
        """
if __name__ == '__main__':
    unittest.main()