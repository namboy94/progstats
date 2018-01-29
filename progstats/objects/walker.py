import os


def list_content(identifier: str, content_path: str) -> str:

    html = ""

    parent_path = os.path.join(content_path, identifier)

    for project in os.listdir(parent_path):
        index_file = os.path.join(parent_path, project, "index.html")
        relative = os.path.join("content", identifier, project, "index.html")

        if os.path.isfile(index_file):
            html += "<a href=\"" + relative + "\">" + project + "</a>"

    return html