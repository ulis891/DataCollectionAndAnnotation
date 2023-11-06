from lxml import etree

tree = etree.parse("src/web_page.html")


def print_tree(element, depth=0):
    print("-" * depth + element.tag)

    for child in element.iterchildren():
        print_tree(child, depth + 1)


root = tree.getroot()

print_tree(root)


