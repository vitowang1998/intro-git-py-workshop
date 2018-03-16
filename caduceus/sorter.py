class SnakeSorter:
    def __init__(self, snakes):
        self.snakes = snakes
        self.sorted_snakes = []

    '''
    sort_by_weight sorts the snakes by their weight in ascending order.

    Args:
        self: A SnakeSorter object.

    Returns:
        Function mutates the sorted_sankes of the self object and returns
        nothing.
    '''
    def sort_by_weight(self):
        self.sorted_snakes = sorted(self.snakes, key=lambda snek: snek.weight)

    '''
    sort_by_length sorts the snakes by their length in ascending order.

    Args:
        self: A SnakeSorter object.

    Returns:
        Function mutates the sorted_sankes part of the self object and returns
        nothing.
    '''
    def sort_by_length(self):
        self.sorted_snakes = sorted(self.snakes, key=lambda snek: snek.length)
