import json

from parsers.parser import Parser


class DotaFileParser(Parser):

    def parse(self, data):
        json_text = data[data.find('\t') + 1:]
        return json.loads(json_text)
