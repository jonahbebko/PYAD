def cleanse(title):
    return (
        title
        .replace("/", "-").replace("\\", "-").replace(":", "-")
        .replace("*", "-").replace("?", "-").replace("\"", "-")
        .replace("<", "-").replace(">", "-").replace("|", "-")
        .replace(" ", "_")
    )