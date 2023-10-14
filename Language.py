import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition, size=(300, 150)):
        super(MyFrame, self).__init__(parent, id, title, pos, size)

        panel = wx.Panel(self)

        # Create a list of options for the dropdown menu
        choices = ["Bengali", "Gujurati", "Hindi", "Kannada", "Malayalam", "Marathi", "Tamil", "Telugu", "Urdu"]

        # Create a dropdown menu
        self.dropdown = wx.Choice(panel, choices=choices)

        # Bind an event handler to the dropdown menu
        self.Bind(wx.EVT_CHOICE, self.on_dropdown_select, self.dropdown)

    def on_dropdown_select(self, event):
        selected_option = self.dropdown.GetString(self.dropdown.GetSelection())

        # Save the selected option to a text file
        with open("selected_option.txt", "w") as file:
            file.write(selected_option)

        wx.MessageBox("Your language has been saved.", "Language Saved")

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, title="Choose the language to be displayed", size=(300, 150))
    frame.Show()
    app.MainLoop()