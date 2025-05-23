from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter as tk
from .packager import create_intune_package


def main():
    root = TkinterDnD.Tk()
    root.title("Intune Packager")
    frame = tk.Frame(root, width=400, height=200, bg="lightgray")
    frame.pack(padx=10, pady=10, fill="both", expand=True)
    label = tk.Label(frame, text="Drag and drop .exe or .msi here", bg="lightgray")
    label.pack(expand=True)

    def drop(event):
        file_path = event.data.strip('{}')
        create_intune_package(file_path)

    frame.drop_target_register(DND_FILES)
    frame.dnd_bind("<<Drop>>", drop)

    root.mainloop()


if __name__ == "__main__":
    main()
