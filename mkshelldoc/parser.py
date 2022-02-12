import re
import io
import os

PATTERN_TYPE_BASH = "bash"
PATTERN_FORMAT_REST = "rest"
PATTERN_VAR_READONLY = "readonly"
PATTERN_VAR_EXPORT = "export"


class Content(object):
    def __init__(self, source, type, format):

        self.source = source
        self.type = type
        self.format = format

        self.content = {
            "script": {"type": "", "name": ""},
            "functions": [],
            "globals": [],
        }
        self.content_functions_item = {
            "name": "",
            "overview": "",
            "parameters": {},
            "outputs": {},
            "returns": {},
        }
        self.content_globals_item = {"type": "", "name": ""}

        self.encoding = "utf-8"

    def __del__(self):
        return None

    def get(self):
        return self.content

    def analyze(self):

        pattern_shell = None
        pattern_text = None
        line = ""
        file = None
        match = ""
        function_block = self.content_functions_item.copy()

        self.content["script"]["type"] = self.type
        self.content["script"]["name"] = os.path.basename(self.source)

        if self.type == PATTERN_TYPE_BASH:
            pattern_shell = PatternBash()

        if self.format == PATTERN_FORMAT_REST:
            pattern_text = PatternRST()

        with io.open(self.source, "r", encoding=self.encoding) as file:
            for line in file:
                match = pattern_shell.search_function_start(line)
                if match:
                    function_block["name"] = match
                    next
                match = pattern_shell.search_globals(line)
                if match:
                    self.content["globals"].append(match)
                    next
                match = pattern_text.search_function_purpose(line)
                if match:
                    function_block["overview"] = match
                    next
                match = pattern_text.search_function_purpose(line)
                if match:
                    function_block["overview"] = match
                    next
                if pattern_shell.search_function_end(line):
                    self.content["functions"].append(function_block)
                    function_block = self.content_functions_item.copy()
                    next

        return self.content


class PatternText(object):
    def __init__(self):
        pass

    def __del__(self):
        return None

    def search_function_purpose(self, line):
        pass


class PatternRST(PatternText):
    def __init__(self):
        self.field_purpose = re.compile(
            "^[ \t]*\#+[ \t]*:purpose:[ \t]*", flags=re.IGNORECASE
        )
        self.field_stdout = re.compile(
            "^[ \t]*\#+[ \t]*:stdout:[ \t]*", flags=re.IGNORECASE
        )
        self.field_stderr = re.compile(
            "^[ \t]*\#+[ \t]*:stderr:[ \t]*", flags=re.IGNORECASE
        )

    def search_function_purpose(self, line):
        content = ""
        match = self.field_purpose.match(line)
        if match:
            content = line[match.end() :]
        if len(content) > 0:
            return content

    def search_function_outputs(self, line):
        content = ""
        record = {}
        match = self.field_stdout.match(line)
        if match:
            content = line[match.end() :]
            if len(content) > 0:
                record["stdout"] = content
        match = self.field_stderr.match(line)
        if match:
            content = line[match.end() :]
            if len(content) > 0:
                record["stderr"] = content


class PatternShell(object):
    def __init__(self):
        pass

    def __del__(self):
        return None

    def search_function_start(self, line):
        pass

    def search_function_end(self, line):
        pass

    def search_globals(self, line):
        pass


class PatternBash(PatternShell):
    def __init__(self):
        self.function_start_full = re.compile("^function ")
        self.function_start_simple = re.compile("^[a-zA-Z0-9-_]+ *\(\)")
        self.function_end = re.compile("^[}]$")
        self.identifier = re.compile("[a-zA-Z0-9-_]+")
        self.var_readonly = re.compile("^[ \t]*readonly ")
        self.var_export = re.compile("^[ \t]*export ")

    def search_function_start(self, line):
        name = None
        match = self.function_start_full.match(line)
        if match:
            name = self.identifier.match(line[match.end() :])
        else:
            match = self.function_start_simple.match(line)
            if match:
                name = self.identifier.match(match.group())
        if name:
            return name.group()

    def search_function_end(self, line):
        match = self.function_end.match(line)
        return match != None

    def search_globals(self, line):
        name = None
        type = ""
        match = self.var_readonly.match(line)
        if match:
            name = self.identifier.match(line[match.end() :])
            type = PATTERN_VAR_READONLY
        else:
            match = self.var_export.match(line)
            if match:
                name = self.identifier.match(line[match.end() :])
                type = PATTERN_VAR_EXPORT
        if name:
            return dict([("name", name.group()), ("type", type)])
