# Virtual Piano Auto Player (Performance Edition)

An AutoHotkey-based assistant tool that automatically plays Virtual Piano (virtualpiano.net) sheet music with high precision.

## Features

- **Advanced Parser**: Accurately analyzes VP format notes, chords (`[6fj]`), modifiers, and rests (`-`, `|`).
- **Precision Timing**: High-precision beat engine powered by QPC (Query Performance Counter).
- **Real-time BPM Control**: Adjust the tempo (BPM) on the fly during playback.
- **Loop Mode**: Seamlessly repeat your favorite tracks.
- **Customizable Hotkeys**: Bind Play/Pause and Stop commands to any key you prefer.
- **Screen Capture Protection**: Option to hide the GUI while recording or streaming.

## Folder Structure

- `pn.ahk`: Main application script.
- `sheets/`: Folder containing all sheet music files.
- `LICENSE`: MIT License file.
- `README.md`: Project documentation.

## How to Use

1. Run `pn.ahk` (Requires [AutoHotkey](https://www.autohotkey.com/) to be installed).
2. Paste your sheet music into the input area.
3. Adjust the BPM as needed.
4. Press `PLAY` or use your assigned hotkey (Default: `F1`).

## License

This project is licensed under the [MIT License](LICENSE).
