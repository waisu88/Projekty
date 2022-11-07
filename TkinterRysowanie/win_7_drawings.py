import tkinter as tk


class Drawings(tk.Tk):
    def __init__(self):
        super().__init__()
        # window attributes
        self.title("Narysuj co chcesz")
        self.wm_attributes("-transparentcolor", "ivory2")
        self.state("zoomed")
        # coordinates
        self.x = 0
        self.y = 0
        self.previous_x = 0
        self.previous_y = 0
        self.start_x = 0
        self.start_y = 0
        # line default parameters
        self.line_colour = "red"
        self.line_width = 4
        # buttons,labels
        self.button_black = tk.Button(self, bg="black", width=4, height=1,
                                      command=lambda: self.set_marker_colour("black")).grid(row=0, column=0)
        self.button_brown = tk.Button(self, bg="brown", width=4, height=1,
                                      command=lambda: self.set_marker_colour("brown")).grid(row=1, column=0)
        self.button_red = tk.Button(self, bg="red", width=4, height=1,
                                    command=lambda: self.set_marker_colour("red")).grid(row=2, column=0)
        self.button_orange = tk.Button(self, bg="orange", width=4, height=1,
                                       command=lambda: self.set_marker_colour("orange")).grid(row=3, column=0)
        self.button_yellow = tk.Button(self, bg="yellow", width=4, height=1,
                                       command=lambda: self.set_marker_colour("yellow")).grid(row=4, column=0)
        self.button_green = tk.Button(self, bg="green", width=4, height=1,
                                      command=lambda: self.set_marker_colour("green")).grid(row=5, column=0)
        self.button_blue = tk.Button(self, bg="blue", width=4, height=1,
                                     command=lambda: self.set_marker_colour("blue")).grid(row=6, column=0)
        self.button_purple = tk.Button(self, bg="purple", width=4, height=1,
                                       command=lambda: self.set_marker_colour("purple")).grid(row=7, column=0)
        self.button_white = tk.Button(self, bg="white", width=4, height=1,
                                      command=lambda: self.set_marker_colour("white")).grid(row=8, column=0)
        self.label_size = tk.Label(self, text="ROZMIAR", wraplength=20, width=4, height=3).grid(row=11, column=0)
        self.button_line_1 = tk.Button(self, bg="black", height=1, width=4, text="1", fg="white",
                                       command=lambda: self.set_marker_size(4)).grid(row=12, column=0)
        self.button_line_2 = tk.Button(self, bg="black", height=1, width=4, text="2", fg="white",
                                       command=lambda: self.set_marker_size(8)).grid(row=13, column=0)
        self.button_line_3 = tk.Button(self, bg="black", height=1, width=4, text="3", fg="white",
                                       command=lambda: self.set_marker_size(16)).grid(row=14, column=0)
        self.button_line_4 = tk.Button(self, bg="black", height=1, width=4, text="4", fg="white",
                                       command=lambda: self.set_marker_size(32)).grid(row=15, column=0)
        self.button_clear_all = tk.Button(self, text="WYCZYŚĆ", wraplength=25, width=4, height=3,
                                          command=self.clear_all_drawings).grid(row=9, column=0)
        self.button_clear_by_mouse = tk.Button(self, text="GUMKA", wraplength=30, width=4, height=3,
                                               command=self.clear_by_mouse).grid(row=10, column=0)
        self.button_create_rectangle = tk.Button(self, text="PROSTOKĄT", wraplength=30, height=3, width=4, bd=4, bg="white",
                                                 command=self.start_rectangle).grid(row=16, column=0)
        self.button_create_line = tk.Button(self, text="LINIA", height=2, width=4, bg="white",
                                                 command=self.start_line).grid(row=17, column=0)
        self.button_create_oval = tk.Button(self, text="OKRĄG", height=2, width=4, bg="white",
                                            command=self.start_oval).grid(row=18, column=0)
        # drawing screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.canvas = tk.Canvas(self, bg="ivory2", width=screen_width, height=screen_height)
        self.canvas.grid(row=0, column=1, columnspan=150, rowspan=150)
        # events
        self.canvas.bind("<Motion>", self.give_coordinates)
        self.canvas.bind("<Button-1>", self.give_start_coords)
        self.canvas.bind("<B1-Motion>", self.draw_line)
        # self.canvas.bind("<Button-1>", self.give_start_coords)
        # self.canvas.bind("<ButtonRelease-1>", self.give_last_coords)

    def set_marker_colour(self, colour):
        if self.line_width == 100:
            self.line_width = 4
        self.line_colour = colour

    def set_marker_size(self, marker_size):
        self.line_width = marker_size

    def give_coordinates(self, event):
        self.previous_x = event.x
        self.previous_y = event.y

    def start_line(self):
        if self.line_colour == "ivory2":
            self.line_colour = "red"
        self.canvas.bind("<B1-Motion>", self.draw_line)

    def draw_line(self, event):
        self.x = event.x
        self.y = event.y
        self.canvas.create_line(self.previous_x, self.previous_y, self.x, self.y,
                                width=self.line_width, fill=self.line_colour)
        self.previous_x = self.x
        self.previous_y = self.y

    def start_rectangle(self):
        if self.line_colour == "ivory2":
            self.line_colour = "red"
        self.canvas.bind("<B1-Motion>", self.draw_rectangle)

    def draw_rectangle(self, event):
        self.start_x = self.previous_x
        self.start_y = self.previous_y
        self.last_x = event.x
        self.last_y = event.y
        self.canvas.create_rectangle(self.start_x, self.start_y, self.last_x, self.last_y, fill="ivory2",
                                     outline=self.line_colour, width=self.line_width)

    def give_start_coords(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def start_oval(self):
        if self.line_colour == "ivory2":
            self.line_colour = "red"
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<Motion>")
        self.canvas.bind("<ButtonRelease-1>", self.draw_oval)

    def draw_oval(self, event):
        self.last_x = event.x
        self.last_y = event.y
        self.canvas.create_oval(self.start_x, self.start_y, self.last_x, self.last_y, fill="ivory2",
                                     outline=self.line_colour, width=self.line_width)

    def clear_by_mouse(self):
        self.line_width = 100
        self.line_colour = "ivory2"

    def clear_all_drawings(self):
        self.canvas.delete("all")


# created by Szymon Wais 2022.10.22