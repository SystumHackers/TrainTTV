import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        super(MyFrame, self).__init__(parent, id, title, pos, size, style)
        
        panel = wx.Panel(self)
        
        
        choices = ["Weather ", "Arrival", "Departure", "Announcements"]
          # Create a dropdown menu
        self.dropdown = wx.Choice(panel, choices=choices)

        # Bind an event handler to the dropdown menu
        self.Bind(wx.EVT_CHOICE, self.on_dropdown_select, self.dropdown)

    def on_dropdown_select(self, event):
        selected_option = self.dropdown.GetString(self.dropdown.GetSelection())

        # Save the selected option to a text file
        with open("Chosen_Information.txt", "w") as file:
            file.write(selected_option)

        wx.MessageBox("Redirecting.", "Option selected")
        
        

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, title="Choose your Information Type", size=(300, 150))
    frame.Show()
    app.MainLoop()
