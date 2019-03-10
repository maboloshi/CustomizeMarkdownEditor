import os
import sys
import subprocess
import sublime
import sublime_plugin

class OpenMarkdownFileCommand(sublime_plugin.WindowCommand):
    def run(self):
        filename = self.window.active_view().file_name()
        if filename is None:
            return

        app_name = sublime.load_settings('Customize Markdown Editor (OSX).sublime-settings').get('name', None)

        proc_env = os.environ.copy()
        encoding = sys.getfilesystemencoding()
        for k, v in proc_env.items():
            proc_env[k] = os.path.expandvars(v).encode(encoding)

        subprocess.call(['open', '-a', app_name, filename], env=proc_env)

    def is_enabled(self):
        return True
