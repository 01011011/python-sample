class ToDo:
    base_id = 0  #static item used to keep track of last id used

    def __init__(self, recommendations):
        ToDo.base_id += 1  #increment the id
        self._id = ToDo.base_id
        self._recommendations = recommendations


    id = property(lambda self: self._id)
    recommendations = property(lambda self: self._recommendations, lambda self, value: setattr(self, '_recommendations', value))

