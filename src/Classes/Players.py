

class Players:

    def __init__(self, name, first_percentage, double_fault, ace, first_serve_pts_won, second_serve_pts_won):
        self.first_percentage = first_percentage
        self.double_fault = double_fault
        self.ace = ace
        self.first_serve_pts_won = first_serve_pts_won
        self.second_serve_pts_won = second_serve_pts_won

        self.name = name

        self.toText = {}

    def compile(self):

        self.toText['first_percentage'] = str(self.first_percentage)
        self.toText['ace'] = str(self.ace)
        self.toText['double_fault'] = str(self.double_fault)
        self.toText['first_serve_pts_won'] = str(self.first_serve_pts_won)
        self.toText['second_serve_pts_won'] = str(self.second_serve_pts_won)
        self.toText['name'] = str(self.name)
