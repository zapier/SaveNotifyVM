import sublime
import sublime_plugin
import subprocess
import threading

class SaveNotifyVM(sublime_plugin.EventListener):
    def on_post_save(self, view):

        settings = sublime.load_settings('SaveNotifyVM.sublime-settings')
        file = view.file_name()

        if not settings == None:
            path = settings.get('path_to_repo', '')
            print(file.startswith(path), file, path)
            if file.startswith(path):
                def notify():
                    from http import client
                    filename = file.replace(path+'/', '')
                    ip = settings.get('vm_ip', '127.0.0.1')
                    port = settings.get('vm_port', '8080')
                    headers = {"X-File": filename}
                    conn = client.HTTPConnection(ip, port, False, 2)
                    try:
                        conn.request("POST", "/", "", headers)
                        response = conn.getresponse()
                        conn.close()
                        print("Save notify:", filename)
                    except:
                        print("Save did not notify (exception)")
                        pass
                thread = threading.Thread(target=notify)
                thread.start()
