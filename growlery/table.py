"""Contains code for creating tables out of arbitrary data"""

from growlery.config import (
    AccountType,
    AccountTypeName,
    SKILL_NAMES,
    MINIGAME_NAMES,
    BOSS_NAMES,
)


class Table:
    """Used to generate ASCII tables"""

    def __init__(self,  # pylint: disable=R0913
                 header_text: str,
                 table_data: list[list[str]],
                 row_names: tuple[str, ...],
                 col_names: tuple[str, ...],
                 cols_with_commas: tuple[str, ...] = ()):
        """Initialises a table"""

        self.header_text = header_text
        self.table_data = table_data
        self.row_names = row_names
        self.col_names = col_names
        self.longest_cells_per_col = {
            column_name: len(column_name)
            for column_name in self.col_names
        }
        self.cols_with_commas = cols_with_commas
        self.data_rows: list[list[str]] = []
        self.preprocess_data()

    def preprocess_data(self):
        """The data needs to be formatted to better suit our purposes"""

        for row_name, row_data in zip(self.row_names, self.table_data):

            if len(row_name) > self.longest_cells_per_col[self.col_names[0]]:
                self.longest_cells_per_col[self.col_names[0]] = len(row_name)
            for col_name, col_value in zip(self.col_names[1:], row_data):
                if len(col_value) > self.longest_cells_per_col[col_name]:
                    self.longest_cells_per_col[col_name] = len(col_value)

            if int(row_data[0]) >= 0:
                self.data_rows.append([row_name, *row_data])

        for col in self.cols_with_commas:
            comma_count = max((self.longest_cells_per_col[col] - 1) // 3, 0)
            self.longest_cells_per_col[col] += comma_count

    def columns_row_content(self) -> str:
        """Formats the column header row"""

        return ' | '.join(
            f'{col:^{length}}'
            for col, length in self.longest_cells_per_col.items()
        )

    @property
    def column_lengths(self) -> list[int]:
        """Returns the lengths of the longest cells in each column"""

        return list(self.longest_cells_per_col.values())

    def generate_header(self) -> list[str]:
        """Generates the table header rows"""

        table_width = len(self.columns_row_content()) + 4
        column_row_content = '─┬─'.join(
            '─' * column_length
            for column_length in self.column_lengths
        )
        column_row = f'╟─{column_row_content}─╢'
        header_rows = [
            f"╔{'═' * (table_width-2)}╗",
            f"║{self.header_text:^{table_width-2}}║",
            f"╠{'═' * (table_width-2)}╣",
            f"║ {self.columns_row_content()} ║",
            column_row,
        ]
        return header_rows

    def generate_body(self) -> list[str]:
        """Generates the table body"""

        body = []
        for row_name, *data in self.data_rows:
            contents = ' │ '.join(
                f'{int(data_point):>{self.longest_cells_per_col[col_name]}{colon}}'
                for col_name, data_point in zip(self.col_names[1:], data)
                if (colon := "," if col_name in self.cols_with_commas else "") is not None
            )
            body.append(
                f'║ {row_name:<{self.longest_cells_per_col[self.col_names[0]]}} │ {contents} ║'
            )
        return body

    def generate_footer(self) -> str:
        """Generates the footer of the table"""

        content = '═╧═'.join(
            '═' * column_length
            for column_length in self.column_lengths
        )
        return f'╚═{content}═╝'

    def render_table(self):
        """Returns the full table with formatting"""

        table_rows = [
            *self.generate_header(),
            *self.generate_body(),
            self.generate_footer()
        ]
        return '```text\n'+'\n'.join(table_rows)+'\n```'


class SkillsTable(Table):
    """Used to create ASCII tables for skill hiscores"""

    def __init__(self,
                 username: str,
                 account_type: AccountType,
                 account_type_name: AccountTypeName,
                 table_data: list[list[str]]):
        """Handles converting the data for the parent class"""

        header_text = f"STATS FOR {username.replace('_', ' ').upper()}"
        if account_type != AccountType.NORMAL:
            header_text += f" [{account_type_name.upper()}]"
        column_names = ('Skill', 'Rank', 'Level', 'Experience')
        columns_with_commas = ('Rank', 'Experience')

        super().__init__(
            header_text=header_text,
            table_data=table_data,
            row_names=SKILL_NAMES,
            col_names=column_names,
            cols_with_commas=columns_with_commas
        )


class MinigamesTable(Table):
    """Used to create ASCII tables for minigame hiscores"""

    def __init__(self,
                 username: str,
                 account_type: AccountType,
                 account_type_name: AccountTypeName,
                 table_data: list[list[str]]):
        """Handles converting the data for the parent class"""

        sliced_data = table_data[len(SKILL_NAMES):]
        header_text = f"MINIGAMES FOR {username.replace('_', ' ').upper()}"
        if account_type != AccountType.NORMAL:
            header_text += f" [{account_type_name.upper()}]"
        column_names = ('Minigame', 'Rank', 'Score')
        columns_with_commas = ('Rank', 'Score')

        super().__init__(
            header_text=header_text,
            table_data=sliced_data,
            row_names=MINIGAME_NAMES,
            col_names=column_names,
            cols_with_commas=columns_with_commas
        )


class BossesTable(Table):
    """Used to create ASCII tables for boss hiscores"""

    def __init__(self,
                 username: str,
                 account_type: AccountType,
                 account_type_name: AccountTypeName,
                 table_data: list[list[str]]):
        """Handles converting the data for the parent class"""

        sliced_data = table_data[len(SKILL_NAMES)+len(MINIGAME_NAMES):]
        header_text = f"BOSS KILLS FOR {username.replace('_', ' ').upper()}"
        if account_type != AccountType.NORMAL:
            header_text += f" [{account_type_name.upper()}]"
        column_names = ('Boss', 'Rank', 'Killcount')
        columns_with_commas = ('Rank', 'Killcount')

        super().__init__(
            header_text=header_text,
            table_data=sliced_data,
            row_names=BOSS_NAMES,
            col_names=column_names,
            cols_with_commas=columns_with_commas
        )
