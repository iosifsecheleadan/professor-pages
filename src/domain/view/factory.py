from src.domain.view.color import black, transparent


def text(content,
         color: str = black,
         size: int = 12,
         bold: bool = False,
         italics: bool = False,
         underline: bool = False,
         strikethrough: bool = False,
         ) -> str:
    if bold: content = __bold(content)
    if italics: content = __italics(content)
    if underline: content = __underline(content)
    if strikethrough: content = __strikethrough(content)

    style = __style_size(size) + __style_color(color)
    content = __style(content, style)

    return content


def title(content,
          color: str = black,
          italics: bool = False,
          strikethrough: bool = False,
          ) -> str:
    return text(content=content,
                color=color,
                size=40,
                bold=True,
                italics=italics,
                underline=True,
                strikethrough=strikethrough
                )


def sub_title(content,
              color: str = black,
              italics: bool = False,
              underline: bool = False,
              strikethrough: bool = False,
              ) -> str:
    return text(content=content,
                color=color,
                size=24,
                bold=True,
                italics=italics,
                underline=underline,
                strikethrough=strikethrough
                )


def description(content,
                color: str = black,
                underline: bool = False,
                strikethrough: bool = False,
                ) -> str:
    return text(content=content,
                color=color,
                size=12,
                bold=False,
                italics=True,
                underline=underline,
                strikethrough=strikethrough
                )


def link_text(content,
              link: str,
              size: int = 12,
              bold: bool = False,
              italics: bool = False,
              underline: bool = False,
              strikethrough: bool = False,
              ) -> str:
    return text(content=__link(content, link),
                size=size,
                bold=bold,
                italics=italics,
                underline=underline,
                strikethrough=strikethrough
                )


def email(content,
          address: str,
          size: int = 12,
          bold: bool = False,
          italics: bool = False,
          underline: bool = False,
          strikethrough: bool = False,
          ) -> str:
    return text(content=__mailto(content, address),
                size=size,
                bold=bold,
                italics=italics,
                underline=underline,
                strikethrough=strikethrough
                )


def material_card(content,
                  rounded: int = 8,
                  color: str = transparent,
                  ) -> str:
    return f"<div style=\"background-color:{color}; border-radius: {rounded}pt;\" " \
           f"class=\"card\" >\n {content} </div>\n"


def image(link: str,
          ) -> str:
    return f"<img src=\"{link}\">\n"


break_line = "<br>"


def __bold(content) -> str:
    return f"<b> {content} </b>"


def __italics(content) -> str:
    return f"<i> {content} </i>"


def __strikethrough(content) -> str:
    return f"<del> {content} </del>"


def __underline(content) -> str:
    return f"<u> {content} </u>"


def __link(content,
           link: str,
           ):
    return f"<a href=\"{link}\"> {content} </a>\n"


def __mailto(content,
             address: str,
             ):
    return __link(content, f"mailto:{address}")


def __style(content,
            style: str,
            ) -> str:
    return f"<div style=\"{style}\">\n {content} </div>\n"


def __style_color(color: str = black) -> str:
    return f"color:{color}; "


def __style_size(size: int = 14) -> str:
    return f"font-size:{size}pt; "
