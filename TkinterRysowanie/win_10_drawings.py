import tkinter as tk


class Drawings(tk.Tk):
    def __init__(self):
        super().__init__()
        # screen cover
        self.title("Narysuj co chcesz")
        self.wm_attributes("-alpha", 0.05)
        self.wm_attributes("-fullscreen", True)

        # self.wm_attributes("-topmost", True)

        self.state("zoomed")
        # drawing screen
        self.drawing_screen = tk.Toplevel(self)
        self.title_bar = tk.Frame(self, bg="white", height=20)
        self.title_bar.grid(row=0, column=1)
        self.drawing_screen.wm_attributes("-transparentcolor", "ivory2")
        self.drawing_screen.wm_attributes("-topmost", True)


        # coordinates
        self.x = 0
        self.y = 0
        self.previous_x = 0
        self.previous_y = 0
        # line default parameters
        self.line_colour = "red"
        self.line_width = 4
        # # buttons,labels
        self.button_black = tk.Button(self.drawing_screen, bg="black", width=4, height=1,
                                      command=lambda: self.set_marker_colour("black")).grid(row=1, column=0)
        self.button_brown = tk.Button(self.drawing_screen, bg="brown", width=4, height=1,
                                      command=lambda: self.set_marker_colour("brown")).grid(row=2, column=0)
        self.button_red = tk.Button(self.drawing_screen, bg="red", width=4, height=1,
                                    command=lambda: self.set_marker_colour("red")).grid(row=3, column=0)
        self.button_orange = tk.Button(self.drawing_screen, bg="orange", width=4, height=1,
                                       command=lambda: self.set_marker_colour("orange")).grid(row=4, column=0)
        self.button_yellow = tk.Button(self.drawing_screen, bg="yellow", width=4, height=1,
                                       command=lambda: self.set_marker_colour("yellow")).grid(row=5, column=0)
        self.button_green = tk.Button(self.drawing_screen, bg="green", width=4, height=1,
                                      command=lambda: self.set_marker_colour("green")).grid(row=6, column=0)
        self.button_blue = tk.Button(self.drawing_screen, bg="blue", width=4, height=1,
                                     command=lambda: self.set_marker_colour("blue")).grid(row=7, column=0)
        self.button_purple = tk.Button(self.drawing_screen, bg="purple", width=4, height=1,
                                       command=lambda: self.set_marker_colour("purple")).grid(row=8, column=0)
        self.button_white = tk.Button(self.drawing_screen, bg="white", width=4, height=1,
                                      command=lambda: self.set_marker_colour("white")).grid(row=9, column=0)
        self.button_clear_all = tk.Button(self.drawing_screen, text="WYCZYŚĆ", wraplength=1, width=4, height=7,
                                          command=self.clear_all_drawings).grid(row=10, column=0)
        self.button_clear_by_mouse = tk.Button(self.drawing_screen, text="GUMKA", wraplength=1, width=4, height=5,
                                               command=self.clear_by_mouse).grid(row=11, column=0)
        self.label_size = tk.Label(self.drawing_screen, text="ROZMIAR", wraplength=2, width=4,
                                   height=7).grid(row=12, column=0)
        self.button_line_1 = tk.Button(self.drawing_screen, bg="black", height=1, width=4, text="1", fg="white",
                                       command=lambda: self.set_marker_size(4)).grid(row=13, column=0)
        self.button_line_2 = tk.Button(self.drawing_screen, bg="black", height=1, width=4, text="2", fg="white",
                                       command=lambda: self.set_marker_size(8)).grid(row=14, column=0)
        self.button_line_3 = tk.Button(self.drawing_screen, bg="black", height=1, width=4, text="3", fg="white",
                                       command=lambda: self.set_marker_size(16)).grid(row=15, column=0)
        self.button_line_4 = tk.Button(self.drawing_screen, bg="black", height=1, width=4, text="4", fg="white",
                                       command=lambda: self.set_marker_size(32)).grid(row=16, column=0)
        # drawing screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.fake_buttons = tk.Button(self, width=5).grid(row=0, column=0)
        self.canvas = tk.Canvas(self, bg="ivory2", width=screen_width, height=screen_height)
        self.canvas.grid(row=1, column=1, columnspan=150, rowspan=150)
        self.width2 = self.winfo_screenwidth()
        self.height2 = self.winfo_screenheight()
        self.canvas2 = tk.Canvas(self.drawing_screen, bg="ivory2", width=self.width2, height=self.height2)
        self.canvas2.grid(row=0, column=1, columnspan=150, rowspan=150)
        # events
        self.canvas.bind("<Motion>", self.give_coordinates)
        self.canvas.bind("<B1-Motion>", self.draw_line)
        self.bind("<Key>", self.quit_program)
        # self.canvas2.bind("<Button-1>", self.quit_program)
        self.bind('<Escape>', self.quit_program)

    def quit_program(self, event):
        self.destroy()

    def set_marker_colour(self, colour):
        if self.line_width == 100:
            self.line_width = 4
        self.line_colour = colour

    def set_marker_size(self, marker_size):
        self.line_width = marker_size

    def give_coordinates(self, event):
        self.previous_x = event.x
        self.previous_y = event.y

    def draw_line(self, event):
        self.x = event.x
        self.y = event.y
        # self.canvas.create_line(self.previous_x, self.previous_y, self.x, self.y,
        #                         width=self.line_width, fill="ivory2", smooth=True) #TODO może spróbować przechwycić i kopiować na drugie tło
        self.canvas2.create_line(self.previous_x, self.previous_y, self.x, self.y,
                                width=self.line_width, fill=self.line_colour, smooth=True)
        self.previous_x = self.x
        self.previous_y = self.y

    def clear_by_mouse(self):
        self.line_width = 100
        self.line_colour = "ivory2"

    def clear_all_drawings(self):
        self.canvas2.delete("all")


# created by Szymon Wais 2022.10.22
