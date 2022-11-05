class GameStats():
    def __init__(self,setting):
        self.setting =setting
        self.reset_stats()
        # can use not only first create but for later reset
        self.game_active=False
    def reset_stats(self):
        self.mouth_left=self.setting.mouth_n_limit
