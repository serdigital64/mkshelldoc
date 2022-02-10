import parser as p

FORMATTER_OUTPUT_MARKDOWN = "markdown"

_FORMATTER_TEXT_SCRIPT = "Script"
_FORMATTER_TEXT_VAR_RO = "Read-Only"
_FORMATTER_TEXT_VAR_EXPORT = "Export"
_FORMATTER_TEXT_FUNCTION = "Function"
_FORMATTER_TEXT_FUNCTIONS = "Functions"
_FORMATTER_TEXT_GLOBALS = "Globals"


class Formatter(object):
    def __init__(self, content):
        self.content = content

    def compose_header(self):
        pass

    def compose_globals(self):
        pass

    def compose_functions(self):
        pass


class FormatterMarkDown(Formatter):
    def compose_header(self):
        print(
            "# " + _FORMATTER_TEXT_SCRIPT + ": " + self.content["script"]["name"] + "\n"
        )

    def compose_globals(self):
        record = None

        if len(self.content["globals"]) > 0:
            print("## " + _FORMATTER_TEXT_GLOBALS + "\n")
            for record in self.content["globals"]:
                if record["type"] == p.PATTERN_VAR_READONLY:
                    print(
                        "### " + _FORMATTER_TEXT_VAR_RO + ": `" + record["name"] + "`\n"
                    )
                elif record["type"] == p.PATTERN_VAR_EXPORT:
                    print(
                        "### "
                        + _FORMATTER_TEXT_VAR_EXPORT
                        + ": `"
                        + record["name"]
                        + "`\n"
                    )

    def compose_functions(self):
        record = ""
        if len(self.content["functions"]) > 0:
            print("## " + _FORMATTER_TEXT_FUNCTIONS + "\n")
            for record in self.content["functions"]:
                print(
                    "### " + _FORMATTER_TEXT_FUNCTION + ": `" + record["name"] + "()`\n"
                )
                if "overview" in record and len(record["overview"]) > 0:
                    print("> " + record["overview"] )
