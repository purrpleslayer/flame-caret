import gi # GObject Introspection

gi.require_version("Atspi", "2.0")
from gi.repository import Atspi

def main():
    desktop = Atspi.get_desktop(0)
    
    for index in range(desktop.get_child_count()):
        child = desktop.get_child_at_index(index)
        print(child.get_name())

        if child.get_name() == "code":
            print("Found VS Code")

            count = child.get_child_count()
            print("Number of children:", count)

            if count > 0:
                window = child.get_child_at_index(0)

                print("Window name:", window.get_name())
                print("Window role:", window.get_role_name())
                print("Window children:", window.get_child_count())

if __name__ == "__main__":
    main()

