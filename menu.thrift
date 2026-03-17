namespace py menu

struct MenuItem {
    1: string id,
    2: optional string label
}

struct Menu {
    1: string header,
    2: list<MenuItem> items
}

struct RootData {
    1: Menu menu
}