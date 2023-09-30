import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set the path for the directory to track changes
from_dir = "<\kanis\OneDrive\Desktop>"

# Create a FileEventHandler class to track file system events
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"looks like Someone created {event.src_path} !")
    def on_modified(self, event):
        print(f"looks like Someone modified {event.src_path} !")
    def on_moved(self, event):
        print(f"Oops! Someone moved {event.src_path} !")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path} !")

# Set up the observer to watch for changes
if __name__ == "__main__":
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path=from_dir, recursive=True)
    observer.start()

    try:
        print(f"Watching for changes in {from_dir}. Press any key to stop...")
        while True:
            time.sleep(2)
            print('running....')
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
