import customtkinter as ctk
import tkinter as tk


class EasyCustomTkinterApp:
    def __init__(self, title="EasyCustomTkinter App", width=300, height=200):
        self.root = ctk.CTk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")

    def add_button(self, text, command=None, **kwargs):
        button = ctk.CTkButton(self.root, text=text, command=command, **kwargs)
        button.pack(padx=10, pady=10)

    def add_checkbox(self, text, command=None, **kwargs):
        checkbox = ctk.CTkCheckBox(self.root, text=text, command=command, **kwargs)
        checkbox.pack(padx=10, pady=10)

    def add_combobox(self, values, **kwargs):
        combobox = ctk.CTkComboBox(self.root, values=values, **kwargs)
        combobox.pack(padx=10, pady=10)

    def add_entry(self, placeholder="", **kwargs):
        entry = ctk.CTkEntry(self.root, placeholder_text=placeholder, **kwargs)
        entry.pack(padx=10, pady=10)

    def add_frame(self, **kwargs):
        frame = ctk.CTkFrame(self.root, **kwargs)
        frame.pack(padx=10, pady=10, fill='both', expand=True)
        return frame

    def add_label(self, text, **kwargs):
        label = ctk.CTkLabel(self.root, text=text, **kwargs)
        label.pack(padx=10, pady=10)

    def add_optionmenu(self, values, **kwargs):
        optionmenu = ctk.CTkOptionMenu(self.root, values=values, **kwargs)
        optionmenu.pack(padx=10, pady=10)

    def add_progressbar(self, **kwargs):
        progressbar = ctk.CTkProgressBar(self.root, **kwargs)
        progressbar.pack(padx=10, pady=10, fill='x')
        return progressbar

    def add_radiobutton(self, text, variable, value, **kwargs):
        radiobutton = ctk.CTkRadioButton(self.root, text=text, variable=variable, value=value, **kwargs)
        radiobutton.pack(padx=10, pady=10)

    def add_scrollable_frame(self, **kwargs):
        canvas = tk.Canvas(self.root, **kwargs)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        frame = ctk.CTkFrame(canvas)
        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        canvas.config(yscrollcommand=scrollbar.set)

        return frame, canvas

    def add_scrollbar(self, **kwargs):
        scrollbar = tk.Scrollbar(self.root, **kwargs)
        scrollbar.pack(side="right", fill="y")
        return scrollbar

    def add_segmented_button(self, segments, **kwargs):
        segmented_button = ctk.CTkSegmentedButton(self.root, values=segments, **kwargs)
        segmented_button.pack(padx=10, pady=10)
        return segmented_button

    def add_switch(self, **kwargs):
        switch = ctk.CTkSwitch(self.root, **kwargs)
        switch.pack(padx=10, pady=10)
        return switch

    def add_slider(self, **kwargs):
        slider = ctk.CTkSlider(self.root, **kwargs)
        slider.pack(padx=10, pady=10, fill='x')
        return slider

    def add_textbox(self, **kwargs):
        textbox = ctk.CTkTextbox(self.root, **kwargs)
        textbox.pack(padx=10, pady=10, fill='both', expand=True)
        return textbox

    def run(self):
        self.root.mainloop()


# Example Usage
if __name__ == "__main__":
    app = EasyCustomTkinterApp()

    # Add a variety of widgets
    app.add_button("Click Me", command=lambda: print("Button Clicked"))
    app.add_checkbox("Check Me")
    app.add_combobox(values=["Option 1", "Option 2", "Option 3"])
    app.add_entry(placeholder="Enter text here")
    frame = app.add_frame()
    app.add_label("This is a label")
    app.add_optionmenu(values=["Choice 1", "Choice 2", "Choice 3"])
    progressbar = app.add_progressbar()
    app.add_radiobutton("Option 1", tk.IntVar(), value=1)
    scrollable_frame, canvas = app.add_scrollable_frame()
    app.add_switch()
    app.add_slider()
    app.add_textbox()

    app.run()