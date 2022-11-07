from __future__ import annotations
from ParseTxt import ParseTxt
from open_read_file import open_read_file
from abc import ABC, abstractmethod
from typing import Dict


class ParseFile:
    def __init__(self, parser: Parser) -> None:
        self._parser = parser

    def parse_file(self, file) -> None:
        result = self._parser.parse_file(file)
        return result

    @staticmethod
    def choose_parser(file):
        parsers = [ParserTxt(), ParserXls(), ParserPy()]
        for parser in parsers:
            if file.extension == parser.parser_file_type:
                return parser


class Parser(ABC):
    @abstractmethod
    def parse_file(self, file):
        pass


class ParserTxt(Parser):
    parser_file_type = "txt"

    def parse_file(self, file) -> Dict:
        readed_file = open_read_file(file.filename)
        data_for_building_questions = ParseTxt(readed_file)
        questions_dict = data_for_building_questions.build_questions()
        return questions_dict


class ParserXls(Parser):
    parser_file_type = "xls"

    def parse_file(self, file) -> Dict:
        return {}


class ParserPy(Parser):
    parser_file_type = "py"

    def parse_file(self, file) -> Dict:
        return {}
