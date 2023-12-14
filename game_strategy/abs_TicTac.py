import abc

class absTicTac(abc.ABC):
    @abc.abstractproperty
    def launch_game(self):
        pass

    @abc.abstractproperty
    def check_if_game_finish(self):
        pass

    @abc.abstractproperty
    def check_if_rows_taken(self):
        pass

    @abc.abstractproperty
    def check_if_cols_taken(self):
        pass

    @abc.abstractproperty
    def check_if_diagonal_taken(self):
        pass

    @abc.abstractproperty
    def check_if_all_fields_taken(self):
        pass
