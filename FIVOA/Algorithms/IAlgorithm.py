class IAlgorithm(object):

    def run(self, initial_point):
        raise NotImplementedError

    def get_logger(self):
        raise NotImplementedError