import customtkinter as ctk
import the_brains as brns
import os
import External as ex
import sys

app = ctk.CTk()
app.title('Rush E Generator')
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')
app.geometry('500x500')
app.iconbitmap('icon.ico')


def obtain_song():
    selected_song = choose_song_ddm.get()
    brns.get_song(selected_song)


def show_in_folder():
    folder_path = os.path.dirname(ex.file_path)
    os.startfile(folder_path)
    sys.exit()


choose_song_frame = ctk.CTkFrame(master=app, fg_color='#242424')
choose_song_frame.place(rely=0.5, relx=0.5, anchor='center')

choose_song_label = ctk.CTkLabel(master=choose_song_frame, text='Choose your song', font=('FOT-Rodin Pro EB', 40))
choose_song_label.pack(pady=20)

choose_song_ddm = ctk.CTkComboBox(master=choose_song_frame, values=['Rush E (For SF2 users, by SMB & MinDagger)',
                                                                    'Rush E (For VST users, by SMB)',
                                                                    'Rush E (Embers, For VST users, by SMB & Tactical)',
                                                                    'Rush E 2 (For SF2 users, by SMB & Tactical)',
                                                                    'Rush E 2 (For VST users, by SMB)',
                                                                    'Rush E 3 (For SF2 & VST users, by SMB & Tactical)',
                                                                    'Rush E 3 (DEBUG, original by SMB)'],
                                  font=('FOT-Rodin Pro EB', 15),
                                  width=450)
choose_song_ddm.pack(pady=10)

choose_song_button = ctk.CTkButton(master=choose_song_frame, text='Next', font=('FOT-Rodin Pro EB', 20),
                                   command=obtain_song)
choose_song_button.pack(pady=10)

sif_frame = ctk.CTkFrame(master=app, fg_color='#242424')

sif_label = ctk.CTkLabel(master=sif_frame, text='Your MIDI has been created',
                         font=('FOT-Rodin Pro EB', 30))
sif_label.pack(pady=20)

sif_button = ctk.CTkButton(master=sif_frame, text='Show in folder and close', font=('FOT-Rodin Pro EB', 15),
                           command=show_in_folder)
sif_button.pack(pady=10)

app.mainloop()
