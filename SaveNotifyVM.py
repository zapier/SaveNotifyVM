import sublime
import sublime_plugin
import subprocess
import urllib
from httplib import client

class SaveNotifyVM(sublime_plugin.EventListener):
    def on_post_save(self, view):

        settings = sublime.load_settings('SaveNotifyVM.sublime-settings').get('commands')
        file = view.file_name()

        if not settings == None:
            path = settings.get('path_to_repo', '')
            if file.startswith(path):
                command.replace('{{file}}', file)
                fielname = file.replace(path+'/', '')
                ip = settings.get('vm_ip', '127.0.0.1')
                port = settings.get('vm_port', '8080')
                params = urllib.urlencode({})
                headers = {"X-File": filename}
                conn = client.HTTPConnection(ip, port)
                conn.request("POST", "/", params, headers)
                response = conn.getresponse()
                conn.close()
                print("Save notify:", filename)
