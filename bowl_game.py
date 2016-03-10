class BowlGame:

    def score_game(self,game):
        game_list = game.split("|")

        score = 0
        strike = list()
        spare = list()
        bowls = list()

        while len(game_list) != 0:
            
            cur_score = game_list.pop(0)
            score_to_add = 0
            
            if cur_score == "X":
                pass
            
            
            #TEST THIS BEFORE MOVING FORWARD
            if "/" in cur_score:
                score_to_add = 10
                bowls = [int(cur_score[0]), 10 - int(cur_score[0])]
                
                try:
                    if spare[-1] == True:
                        score_to_add += bowls[0]
                except IndexError:
                    pass
                spare.append(True)
                
            #no pins
            elif cur_score == "--":
                continue
                
            #end of game, no strikes/spares
            #need to add ability to bowl more
            elif cur_score == "":
                break
            
            #some pins
            else:
                try:
                    score_to_add = int(cur_score[0]) + int(cur_score[1])
                    bowls = [int(cur_score[0]), int(cur_score[1])]
                    
                except ValueError:
                    if cur_score[0] == "-":
                        score_to_add = int(cur_score[1])
                        bowls = [0,int(cur_score[1])]
                        
                    else:
                        score_to_add = int(cur_score[0])
                        bowls = [int(cur_score[0]),0]
                        
                #spare previously
                try:
                    if spare[-1] == True:
                        score_to_add += bowls[0]
                except IndexError:
                    pass
                #strike previously
                try:
                    if strike[-1] == True:
                        score_to_add += bowls[0] + bowls[1]
                        
                except IndexError:
                    pass
                
                strike = list()
                spare = list()
                bowls = list()

           #if prev bowl was spare:
            #try:
            #    if spare[-2] == True:
            #        score_to_add += bowls[0]
            #except IndexError:
            #    pass
                
            #if prev two bowls was strike
                
            score += score_to_add
            #print(score)            
        return score