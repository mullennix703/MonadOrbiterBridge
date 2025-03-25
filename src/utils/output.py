import os
from rich.console import Console
from rich.text import Text
from tabulate import tabulate
from rich.table import Table
from rich import box
from typing import List
from prompt_toolkit import Application
from prompt_toolkit.layout import Layout, Window, HSplit
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style
import questionary
from questionary import Style as QuestionaryStyle
import asyncio
import sys


def show_logo():
    """Отображает стильный логотип STARLABS"""
    # Очищаем экран
    os.system("cls" if os.name == "nt" else "clear")

    console = Console()

    # Создаем звездное небо со стилизованным логотипом
    logo_text = """
✦ ˚ . ⋆   ˚ ✦  ˚  ✦  . ⋆ ˚   ✦  . ⋆ ˚   ✦ ˚ . ⋆   ˚ ✦  ˚  ✦  . ⋆   ˚ ✦  ˚  ✦  . ⋆ ✦ ˚ 
. ⋆ ˚ ✧  . ⋆ ˚  ✦ ˚ . ⋆  ˚ ✦ . ⋆ ˚  ✦ ˚ . ⋆  ˚ ✦ . ⋆ ˚  ✦ ˚ . ⋆  ˚ ✦ . ⋆  ˚ ✦ .✦ ˚ . 
·˚ ⋆｡⋆｡. ★ ·˚ ★ ·˚ ⋆｡⋆｡. ★ ·˚ ★ ·˚ ⋆｡⋆｡. ★ ·˚ ★ ·˚ ⋆｡⋆｡. ★ ·˚ ⋆｡⋆｡. ★ ·˚ ★ ·˚ ·˚ ★ ·˚
✧ ⋆｡˚✦ ⋆｡  ███████╗████████╗ █████╗ ██████╗ ██╗      █████╗ ██████╗ ███████╗  ⋆｡ ✦˚⋆｡ 
★ ·˚ ⋆｡˚   ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔══██╗██╔══██╗██╔════╝  ✦˚⋆｡ ˚· 
⋆｡✧ ⋆ ★    ███████╗   ██║   ███████║██████╔╝██║     ███████║██████╔╝███████╗   ˚· ★ ⋆
˚· ★ ⋆｡    ╚════██║   ██║   ██╔══██║██╔══██╗██║     ██╔══██║██╔══██╗╚════██║   ⋆ ✧｡⋆ 
✧ ⋆｡ ˚·    ███████║   ██║   ██║  ██║██║  ██║███████╗██║  ██║██████╔╝███████║   ★ ·˚ ｡
★ ·˚ ✧     ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝   ｡⋆ ✧ 
·˚ ⋆｡⋆｡. ★ ·˚ ★ ·˚ ⋆｡⋆｡. ★ ·˚ ★ ·˚ ⋆｡⋆｡. ★ ·˚ ★ ·˚ ⋆｡⋆｡. ★ ·˚ ⋆｡⋆｡. ★ ·˚ ★ ·˚·˚ ⋆｡⋆｡.
. ⋆ ˚ ✧  . ⋆ ˚  ✦ ˚ . ⋆  ˚ ✦ . ⋆ ˚  ✦ ˚ . ⋆  ˚ ✦ . ⋆ ˚  ✦ ˚ . ⋆  ˚ ✦ . ⋆  ˚ ✦ .. ⋆  ˚ 
✦ ˚ . ⋆   ˚ ✦  ˚  ✦  . ⋆ ˚   ✦  . ⋆ ˚   ✦ ˚ . ⋆   ˚ ✦  ˚  ✦  . ⋆   ˚ ✦  ˚  ✦  . ⋆  ✦"""

    # Создаем градиентный текст
    gradient_logo = Text(logo_text)
    gradient_logo.stylize("bold bright_cyan")

    # Выводим с отступами
    console.print(gradient_logo)
    print()


def show_dev_info():
    """Displays development and version information"""
    console = Console()

    # Создаем красивую таблицу
    table = Table(
        show_header=False,
        box=box.DOUBLE,
        border_style="bright_cyan",
        pad_edge=False,
        width=85,
        highlight=True,
    )

    # Добавляем колонки
    table.add_column("Content", style="bright_cyan", justify="center")

    # Добавляем строки с контактами
    table.add_row("✨ StarLabs Monad Bot 1.8 ✨")
    table.add_row("─" * 43)
    table.add_row("")
    table.add_row("⚡ GitHub: [link]https://github.com/0xStarLabs[/link]")
    table.add_row("👤 Dev: [link]https://t.me/StarLabsTech[/link]")
    table.add_row("💬 Chat: [link]https://t.me/StarLabsChat[/link]")
    table.add_row(
        "📚 Tutorial: [link]https://star-labs.gitbook.io/star-labs/monad-eng[/link]"
    )
    table.add_row(
        "🎥 Video Guide: [link]https://www.youtube.com/watch?v=48kfCJhjsaI[/link]"
    )
    table.add_row("")

    # Выводим таблицу с отступом
    print("   ", end="")
    print()
    console.print(table)
    print()


async def show_menu(title: str, options: List[str]) -> str:
    """
    Displays an interactive menu with the given options and returns the selected option.
    """
    try:
        # Add empty lines for spacing
        print("\n")

        # Create custom style with larger text
        custom_style = QuestionaryStyle(
            [
                ("question", "fg:#B8860B bold"),  # Title color - muted gold
                ("answer", "fg:#ffffff bold"),  # Selected option color - white
                ("pointer", "fg:#B8860B bold"),  # Pointer color - muted gold
                (
                    "highlighted",
                    "fg:#B8860B bold",
                ),  # Highlighted option color - muted gold
                ("instruction", "fg:#666666"),  # Instruction text color - gray
            ]
        )

        print()

        # Show the menu with custom style
        result = await questionary.select(
            title,
            choices=options,  # Используем options напрямую, так как эмодзи уже есть
            style=custom_style,
            qmark="🎯",  # Custom pointer
            instruction="(Use arrow keys and Enter to select)",
        ).ask_async()

        return result

    except KeyboardInterrupt:
        print("\n\nExiting program... Goodbye! 👋")
        sys.exit(0)
