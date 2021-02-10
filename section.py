"""
TODO: Write documentation
"""


class Section:
    """Text section retrieved from the PDF text.
    """

    def __init__(self,
                 text: str,
                 lower_limit: any = None,
                 upper_limit: any = None):
        self.text = text
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.lines = self.set_lines()
        self.lower_limit_line = self.set_lower_limit_line()
        self.upper_limit_line = self.set_upper_limit_line()
        self.reduced_text = self.set_reduced_text()

    def set_lines(self):
        return self.text.split('\n')

    def set_lower_limit_line(self):
        if self.lower_limit is None:
            return None

        if type(self.lower_limit) == int:
            return self.lower_limit

        for num, line in enumerate(self.lines):
            if self.lower_limit[0] in line:
                lower_limit_line = num
                lower_limit_line += self.lower_limit[1]
                return lower_limit_line

    def set_upper_limit_line(self):
        if self.upper_limit is None:
            return None

        if type(self.upper_limit) == int:
            if self.upper_limit < len(self.lines):
                return self.upper_limit + 1
            else:
                return None

        for num, line in enumerate(self.lines):
            if self.upper_limit[0] in line:
                upper_limit_line = num
                upper_limit_line += self.upper_limit[1]
                return upper_limit_line

    def set_reduced_text(self):
        lim_1 = self.lower_limit_line
        lim_2 = self.upper_limit_line
        return '\n'.join(self.lines[lim_1:lim_2])
