# https://github.com/dracula/dracula-theme#color-palette
# https://www.tints.dev/?red=282A36&brand=BD93F9&BLACK=50FA7B&black=282A36&neutral=282A36&primary=BD93F9&secondary=50FA7B


def hex_to_rgb(hex_value: str) -> str:
    stripped_hex = hex_value.strip("#").strip(";")
    red = int(stripped_hex[0:2], base=16)
    green = int(stripped_hex[2:4], base=16)
    blue = int(stripped_hex[4:6], base=16)
    return f"{red},{green},{blue};"


def main() -> None:
    final_css: list[str] = []
    with open("./dracula_hex.css", "r") as f:
        for line in f:
            parts = line.split(": ")
            if len(parts) < 2:
                final_css.append(line.strip() + "\n")
            else:
                new_color = hex_to_rgb(parts[1].strip())
                final_css.append(f"{parts[0].strip()}: {new_color}\n")

    with open("./assets/css/schemes/dracula.css", "w") as f:
        f.writelines(final_css)


if __name__ == "__main__":
    main()
