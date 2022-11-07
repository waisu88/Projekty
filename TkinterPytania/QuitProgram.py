
class QuitProgram:
    def __init__(self):
        self.confirm_exit = False
        self.confirm()

    def confirm(self):
        confirm = str.lower(input("Wciśnij klawisz 'T' aby opuścić program "))
        if confirm == "t":
            self.confirm_exit = True

    def quit(self):
        if self.confirm_exit:
            return True
        else:
            return False
