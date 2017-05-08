import os
from os.path import dirname, realpath
import sublime, sublime_plugin
from pprint import pprint

from DeleteFile.send2trash import send2trash

class delete_fileCommand(sublime_plugin.WindowCommand):
    def run(self):
        activeView = sublime.Window.active_view(sublime.active_window())
        send2trash(activeView.file_name())
        activeView.close()
