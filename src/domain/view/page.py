from src.domain.data.base import DataEntity

__head = """
<!DOCTYPE html> <html lang="en">
<head>
    <title>Home - Professor Name</title>
    <style>
        html { font-family: Helvetica, sans-serif; }

        .body {
            position: fixed; overflow: auto;
            right: 0; left: 0; top: 0; bottom: 0;
        }

        .card {
            padding: 14pt;
            margin: 3pt;
            transition-duration: 0.3s;
            display: inline-block;
            box-shadow: 0 0 3pt black;
        }
        .card:hover { box-shadow: 1pt 1pt 3pt black; }

        .center { margin: auto; width: 50%; }

        .navigation-background {
            padding: 0 25%;
            display: flex;
            background-color: blue;
        }
        .navigation-item {
            width: 100%;
            padding: 14pt;
            text-align: center;
            cursor: pointer;
            transition-duration: 0.3s;
            text-decoration: none;
            background-color: blue;
            color: white;
        }
        .navigation-item:hover { background-color: darkblue; }

        @media screen and (max-aspect-ratio: 1/1){
            .center { width: 90%; }
            .navigation-item { width: 95%; }
            .navigation-background { flex-direction: column; padding: 0 5%; }
        }
    </style>
</head>
"""

__body_isback = """
<div class="body">

<div class="navigation-background">
    <a class="navigation-item" href="../home.html"> HOME </a>
    <a class="navigation-item" href="../all_courses.html"> COURSES </a>
    <a class="navigation-item" href="../announcements.html"> NEWS </a>
    <a class="navigation-item" href="../about.html"> ABOUT </a>
</div>

<div class="center">


"""

__body_notback = """
<div class="body">

<div class="navigation-background">
    <a class="navigation-item" href="home.html"> HOME </a>
    <a class="navigation-item" href="all_courses.html"> COURSES </a>
    <a class="navigation-item" href="announcements.html"> NEWS </a>
    <a class="navigation-item" href="about.html"> ABOUT </a>
</div>

<div class="center">


"""

__page_end = """

</div>

</div>
</html>
"""


def page(items: list, isback: bool = False):
    content = ""
    for item in items:
        if isinstance(item, DataEntity): content += item.to_html()
        else: content += str(item)
    result = __head
    if isback: result += __body_isback
    else: result += __body_notback
    result += content + __page_end
    return result
