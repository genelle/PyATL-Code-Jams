class BowlGame:

    def score_game(self,game):
        bowls = score_game_helper(game)
        
        score = 0
        
        #Need to separate out first 10 frames and rest of game, will make below 
        #functionality work a lot better
        """
        for index, bowl in enumerate(bowls):
            if bowl == "X":
                score += str_to_score(bowl) + str_to_score(bowls[index + 1]) + str_to_score(bowls[index+2])
                
            elif "/" in bowl:
                score += str_to_score(bowl) + str_to_score(bowls[index + 1])
                
            elif bowl == "":
                if bowls[index + 1] == "":
                    break
                else:
                    score +=  
        """
    
    
    def str_to_score(self,score_str):
        score_num = 0
        if score_str == "X":
            score_num = 10
        elif "/" in score_str:
            score_num = int(score_str[0])
        else:
            score_num = int(score_str) 
            
        return score_num
            
    
    def score_game_helper(self,game):
        '''
        Helper function to set up list for easy scoring
        Broke it out to test separately
        '''
        
        #split up the frames
        game_list = game.split("|")
        
        #split up the throws
        bowls = list()
        for frame in game_list:
            if frame == "X":
                bowls.append("X")
            elif frame == "":
                bowls.append("")
            else:
                new_frame = frame.replace("-", "0")
                
                if "/" in new_frame:
                    bowls.extend(( new_frame[0] , str(10 - int( new_frame[0] )) + "/"))
            
                else:
                    bowls.extend(( new_frame[0] , new_frame[1] ))
                
        
        return bowls
