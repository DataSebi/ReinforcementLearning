## TODO __ALL__
## k armed bandit.py
class k_armed_bandit(object):

    self.mean=0
    self.variance = 1

    def __init__(self,k):
        super().__init__()
        self.k = k

    def pull_lever(self, lever_index):
        reward = 0
        return reward

    def print_bandit(self):
        print("{} armed bandit:".format(self.k))


bandit = k_armed_bandit(10)

# TODO testbench