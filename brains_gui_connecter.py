import GUI


def actually_activate_sif():
    GUI.choose_song_frame.place_forget()
    GUI.sif_frame.place(rely=0.5, relx=0.5, anchor='center')
