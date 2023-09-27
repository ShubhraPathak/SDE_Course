# Currently pywinauto does not support macOS, I'll upload the auto cursor code for macOS very soon.
# stay tuned.

# The auto clicker project utilises pywinauto library to automate mouse and keyboard.
# under this project we will slowly automate our day-to-day task starting with very basic,
# running a cursor on its own and click at some co-ordinates.

# In this particular section we will be learning the very basic, in next section we will implement the same
# automation with threading, so keep in touch.

# pre-requisites
# 1. make sure pywinauto is installed in your virtual environment


from pywinauto import mouse
from time import sleep

class AutoCursor:

    def __init__(self):
        self.mouse = mouse

    def run(self):

        try:
            self.mouse_move_event(co_ordinates=(500,500)) # move to center position
            self.wait_time(wait_till=2)
            self.mouse_move_event(co_ordinates=(110, 120)) # move the cursor to top left corner
            self.wait_time(wait_till=1)
            self.mouse_move_event(co_ordinates=(230, 300))
            self.wait_time(wait_till=10)
            self.mouse_click_event(button='right', co_ordinates=(500, 500))
        except:
            print("some exception occurred!!!\n bugs bugs bugs ... \n Happy hunting...")

    def wait_time(self, wait_till=0.5):
        return sleep(wait_till)

    def mouse_move_event(self, co_ordinates: tuple[int, int]):
        return mouse.move(coords=co_ordinates)

    def mouse_click_event(self, co_ordinates: tuple[int, int], button='left'):
        return mouse.click(button=button, coords=co_ordinates)


if __name__ == "__main__":
    auto = AutoCursor()
    auto.run()
