import parser as p
import formatter as f

MKSHELLDOC_TYPE_BASH = p.PATTERN_TYPE_BASH
MKSHELLDOC_FORMAT_REST = p.PATTERN_FORMAT_REST
MKSHELLDOC_OUTPUT_MARKDOWN = f.FORMATTER_OUTPUT_MARKDOWN


class MkShellDoc(object):
    def __init__(self, source, type, format, destination, output):

        self.source = source
        self.type = type
        self.format = format
        self.destination = destination
        self.output = output

        self.content = p.Content(self.source, self.type, self.format)

        return None

    def __del__(self):
        return None

    def __write(self):
        formatter = None
        if self.output == MKSHELLDOC_OUTPUT_MARKDOWN:
            formatter = f.FormatterMarkDown(self.content.get())
        formatter.compose_header()
        formatter.compose_globals()
        formatter.compose_functions()

    def create(self):
        self.content.analyze()
        self.__write()
