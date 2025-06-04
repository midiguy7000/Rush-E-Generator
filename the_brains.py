import External as ex
import os


def remove_bytes():
    if not ex.file_path or not os.path.isfile(ex.file_path):
        exit()

    blank_midi_bytes = bytes([
        # Header chunk ("MThd")
        0x4D, 0x54, 0x68, 0x64,  # 'MThd'
        0x00, 0x00, 0x00, 0x06,  # Header length = 6
        0x00, 0x00,  # Format 0
        0x00, 0x01,  # One track
        0x00, 0x60,  # 96 ticks per quarter note

        # Track chunk ("MTrk")
        0x4D, 0x54, 0x72, 0x6B,  # 'MTrk'
        0x00, 0x00, 0x00, 0x04,  # Length = 4 bytes
        0x00, 0xFF, 0x2F, 0x00  # End of track
    ])

    with open(str(ex.file_path), "wb") as f:
        f.write(blank_midi_bytes)


def get_song(song):
    import hex_bytes
    import hex_bytes_2
    if song == 'Rush E (For VST users, by SMB)':
        re1b = hex_bytes.e1
        print("Processing...")

        with open(str(ex.file_path), "wb") as f:
            f.write(re1b)
        print('Done!')
        activate_sif()

    elif song == 'Rush E (For SF2 users, by SMB & MinDagger)':
        re1mb = hex_bytes.e1m
        print("Processing...")

        with open(str(ex.file_path), "wb") as f:
            f.write(re1mb)
        print('Done!')
        activate_sif()

    elif song == 'Rush E (Embers, For VST users, by SMB & Tactical)':
        re1eb = hex_bytes.e1e
        print("Processing...")

        with open(str(ex.file_path), "wb") as f:
            f.write(re1eb)
        print('Done!')
        activate_sif()

    elif song == 'Rush E 2 (For VST users, by SMB)':
        re2b = hex_bytes.e2
        print('Processing...')

        with open(str(ex.file_path), "wb") as f:
            f.write(re2b)
        print('Done!')
        activate_sif()

    elif song == 'Rush E 2 (For SF2 users, by SMB & Tactical)':
        re2mb = hex_bytes.e2m
        print("Processing...")

        with open(str(ex.file_path), "wb") as f:
            f.write(re2mb)
            print("Done!")
        activate_sif()

    elif song == 'Rush E 3 (For SF2 & VST users, by SMB & Tactical)':
        re3mb = hex_bytes.e3m
        print("Processing...")

        with open(str(ex.file_path), "wb") as f:
            f.write(re3mb)
            print("Done!")
        activate_sif()

    elif song == 'Rush E 3 (DEBUG, original by SMB)':
        re3b = hex_bytes_2.e3
        print("Processing...")

        with open(str(ex.file_path), "wb") as f:
            f.write(re3b)
            print("Done!")
        activate_sif()


def activate_sif():
    import brains_gui_connecter as bgc
    bgc.actually_activate_sif()
