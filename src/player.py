import numpy as np
import random

class Player():
    '''
    Class to create players
    '''
    
    def __init__(self, style):
        self.style = style
        
    def playing_style(self):
#         styles = {'dove': [, 'hawk': , 'random': }
        pass
        
    def make_move(self, p_score):
        p_move = 'check'
        d = {}
        self.d = d
        
        if self.style == 'dove':               
            if p_score <= 7462 and p_score >=2985:
                p_move = 'check'
                return p_move
            else:
                p_move = 'raise'
                return p_move
            
        elif self.style == 'hawk':
            if p_score <= 7462 and p_score >=5970:
                p_move = 'check'
                return p_move      
            else:
                p_move = 'raise'
                return p_move
        
        elif self.style == 'random':
            moves = ['check', 'raise']
            p_move = random.choice(moves)
            return p_move
    
    def make_second_move(self, p_score, p_name, d):
        p_move = d[p_name]
        d_copy = d.copy()
        del d_copy[p_name]
        
        if self.style == 'dove':
            if 'raise' in d_copy.values():
                if p_score > 5969:
                    p_move = 'fold'
                    return p_move
                elif p_score <5970:
                    p_move = 'check'
                    return p_move
                
        if self.style == 'hawk' and p_score < 5970:
            p_move = 'raise'
            return p_move
        else:
            p_move = 'check'
            return p_move
        
        if self.style == 'random':
            moves = ['check', 'raise', 'fold']
            p_move = random.choice(moves)
            return p_move
        
            