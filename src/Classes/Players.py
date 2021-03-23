

class Players:

    def __init__(self, name, first_percentage, double_fault, ace, first_serve_pts_won, second_serve_pts_won,
                 first_return_pts_won, second_return_pts_won):
        """
        :param name: String - name of player
        :param first_percentage: Float - between 0 and 1, num of 1st serves in
        :param double_fault: Float - between 0 and 1, num of points ending in double fault
        :param ace: Float - between 0 and 1, num of points ending in an ace
        :param first_serve_pts_won: Float - between 0 and 1, num of points won if first serve made
        :param second_serve_pts_won: Float - between 0 and 1, num of points won if second serve made
        :param first_return_pts_won: Float - between 0 and 1, num of points won if opponent first serve made
        :param second_return_pts_won: Float - between 0 and 1, num of points won if opponent made second serve
        """
        self.first_percentage = first_percentage
        self.double_fault = double_fault
        self.ace = ace
        self.first_serve_pts_won = first_serve_pts_won
        self.second_serve_pts_won = second_serve_pts_won
        self.first_return_pts_won = first_return_pts_won
        self.second_return_pts_won = second_return_pts_won

        self.name = name

        self.toText = {}

    def compile(self):
        """
        creates a dictionary of player category and respective number
        :return nothing
        """
        self.toText['first_percentage'] = str(self.first_percentage)
        self.toText['ace'] = str(self.ace)
        self.toText['double_fault'] = str(self.double_fault)
        self.toText['first_serve_pts_won'] = str(self.first_serve_pts_won)
        self.toText['second_serve_pts_won'] = str(self.second_serve_pts_won)
        self.toText['first_return_pts_won'] = str(self.first_return_pts_won)
        self.toText['second_return_pts_won'] = str(self.second_return_pts_won)
        self.toText['name'] = str(self.name)
