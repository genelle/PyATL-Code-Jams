import bowl_game
import unittest

class TestBowlGame(unittest.TestCase):

    def test_life_the_universe_and_everything(self):
        '''simple example to start you off'''
        douglas = bowl_game.BowlGame()
        #no pins
        self.assertEqual(0, douglas.score_game("--|--|--|--|--|--|--|--|--|--||"))
        print("--------")
        
        #some pins, no strikes/spares
        self.assertEqual(36, douglas.score_game("--|1-|11|-2|3-|4-|-5|81|9-|1-||"))
        print("--------")
                
        #spares, not last bowl
        self.assertEquals(20 ,douglas.score_game("5/|5-|--|--|--|--|--|--|--|--||"))
        print("--------")

if __name__ == '__main__':
    unittest.main()