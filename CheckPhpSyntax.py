import sublime, sublime_plugin, subprocess

class CheckPhpSyntax(sublime_plugin.EventListener):
    def on_post_save(self, view):
        if not view.settings().get("made_php_syntax_check_enabled"):
            return

        fileName = view.file_name()
        if fileName.endswith(".php") or fileName.endswith(".phtml"):
            command = "php -l " + fileName
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            stdOut = process.communicate()[0]
            returnCode = process.returncode
            if returnCode != 0:
                sublime.error_message(stdOut);
