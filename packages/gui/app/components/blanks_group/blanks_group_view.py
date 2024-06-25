from flet import (
    Row,
    Column,
    Text,
    MainAxisAlignment,
    TextAlign,
    CrossAxisAlignment,
    colors,
)


def blanks_group_view(category, blanks: list[str]):
    blanks_group_texts = Row(
        [Text(blank.upper(), color=colors.WHITE, size=48) for blank in blanks],
        alignment=MainAxisAlignment.CENTER,
        spacing=12,
    )

    category_text = Row(
        [
            Text(
                "Category: ", color=colors.WHITE, size=24, text_align=TextAlign.CENTER
            ),
            Text(
                category.upper(),
                color=colors.BLUE_400,
                size=24,
                text_align=TextAlign.CENTER,
            ),
        ],
        alignment=MainAxisAlignment.CENTER,
    )

    return Row(
        [
            Column(
                [
                    blanks_group_texts,
                    category_text,
                ],
                alignment=CrossAxisAlignment.CENTER,
                width=500,
            )
        ],
        alignment=MainAxisAlignment.CENTER,
    )
