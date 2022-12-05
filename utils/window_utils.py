def disable_event():
    pass


def unclose_window(window):
    window.protocol("WM_DELETE_WINDOW", disable_event)
    window.mainloop()
