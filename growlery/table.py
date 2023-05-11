"""Contains code for creating tables out of arbitrary data"""

from __future__ import annotations

from growlery.config import BOSS_NAMES, MINIGAME_NAMES, SKILL_NAMES, AccountType, AccountTypeName


class Table:
    """Used to generate ASCII tables"""

    def __init__(self: Table,  # pylint: disable=R0913
                 header_text: str,
                 table_data: list[list[str]],
                 row_names: tuple[str, ...],
                 col_names: tuple[str, ...],
                 cols_with_commas: tuple[str, ...] = ()) -> None:
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

    def preprocess_data(self: Table) -> None:
        """The data needs to be formatted to better suit our purposes"""

        for row_name, row_data in zip(self.row_names, self.table_data, strict=False):

            if len(row_name) > self.longest_cells_per_col[self.col_names[0]]:
                self.longest_cells_per_col[self.col_names[0]] = len(row_name)
            for col_name, col_value in zip(self.col_names[1:], row_data, strict=False):
                if len(col_value) > self.longest_cells_per_col[col_name]:
                    self.longest_cells_per_col[col_name] = len(col_value)

            if int(row_data[0]) >= 0:
                self.data_rows.append([row_name, *row_data])

        for col in self.cols_with_commas:
            comma_count = max((self.longest_cells_per_col[col] - 1) // 3, 0)
            self.longest_cells_per_col[col] += comma_count

    def columns_row_content(self: Table) -> str:
        """Formats the column header row"""

        return ' | '.join(
            f'{col:^{length}}'
            for col, length in self.longest_cells_per_col.items()
        )

    @property
    def column_lengths(self: Table) -> list[int]:
        """Returns the lengths of the longest cells in each column"""

        return list(self.longest_cells_per_col.values())

    def generate_header(self: Table) -> list[str]:
        """Generates the table header rows"""

        table_width = len(self.columns_row_content()) + 4
        column_row_content = '─┬─'.join(
            '─' * column_length
            for column_length in self.column_lengths
        )
        column_row = f'╟─{column_row_content}─╢'

        return [
            f"╔{'═' * (table_width - 2)}╗",
            f"║{self.header_text:^{table_width - 2}}║",
            f"╠{'═' * (table_width - 2)}╣",
            f"║ {self.columns_row_content()} ║",
            column_row,
        ]

    def generate_body(self: Table) -> tuple[list[str], list[str], list[str]]:
        """Generates the table body"""
        # There is a current max boss limit of 51, so rows per page can be set to 17.
        max_row_per_page = 17
        body = []
        second_row = []
        third_row = []
        for row_name, *data in self.data_rows:
            contents = ' │ '.join(
                f'{int(data_point):>{self.longest_cells_per_col[col_name]}{colon}}'
                for col_name, data_point in zip(self.col_names[1:], data, strict=False)
                if (colon := "," if col_name in self.cols_with_commas else "") is not None
            )
            body.append(
                f'║ {row_name:<{self.longest_cells_per_col[self.col_names[0]]}} │ {contents} ║',
            )
            if len(body) > max_row_per_page:
                second_row.append(
                    f'║ {row_name:<{self.longest_cells_per_col[self.col_names[0]]}} │ {contents} ║',
                )
                body.pop()
                if len(second_row) > max_row_per_page:
                    third_row.append(
                        f'║ {row_name:<{self.longest_cells_per_col[self.col_names[0]]}} │ {contents} ║',
                    )
                    second_row.pop()
        return body, second_row, third_row

    def generate_footer(self: Table) -> str:
        """Generates the footer of the table"""

        content = '═╧═'.join(
            '═' * column_length
            for column_length in self.column_lengths
        )
        return f'╚═{content}═╝'

    def render_table(self: Table) -> str | tuple[str, ...]:
        """Returns the full table with formatting"""
        # Checks if there is another page of data
        # In this case the second element in the tuple, which would be the second list of rows or page.
        # If there is another page present, this code creates a table_rows with the first page.
        if self.generate_body()[2]:
            table_rows = (
                *self.generate_header(),
                *self.generate_body()[0],
                self.generate_footer(),
            )
            second_row = (
                *self.generate_header(),
                *self.generate_body()[1],
                self.generate_footer(),
            )
            third_row = (
                *self.generate_header(),
                *self.generate_body()[2],
                self.generate_footer(),
            )
            return (
                f"```\n{chr(10).join(table_rows)}\n```",
                f"```\n{chr(10).join(second_row)}\n```",
                f"```\n{chr(10).join(third_row)}\n```",
            )

        if self.generate_body()[1]:
            table_rows = (
                *self.generate_header(),
                *self.generate_body()[0],
                self.generate_footer(),
            )
            second_row = (
                *self.generate_header(),
                *self.generate_body()[1],
                self.generate_footer(),
            )
            return (
                f"```\n{chr(10).join(table_rows)}\n```",
                f"```\n{chr(10).join(second_row)}\n```",
            )
        table_rows = (
            *self.generate_header(),
            *self.generate_body()[0],
            self.generate_footer(),
        )
        return f"```\n{chr(10).join(table_rows)}\n```"


class SkillsTable(Table):
    """Used to create ASCII tables for skill hiscores"""

    def __init__(self: SkillsTable,
                 username: str,
                 account_type: AccountType,
                 account_type_name: AccountTypeName,
                 table_data: list[list[str]]) -> None:
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
            cols_with_commas=columns_with_commas,
        )


class MinigamesTable(Table):
    """Used to create ASCII tables for minigame hiscores"""

    def __init__(self: MinigamesTable,
                 username: str,
                 account_type: AccountType,
                 account_type_name: AccountTypeName,
                 table_data: list[list[str]]) -> None:
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
            cols_with_commas=columns_with_commas,
        )


class BossesTable(Table):
    """Used to create ASCII tables for boss hiscores"""

    def __init__(self: BossesTable,
                 username: str,
                 account_type: AccountType,
                 account_type_name: AccountTypeName,
                 table_data: list[list[str]]) -> None:
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
            cols_with_commas=columns_with_commas,
        )
