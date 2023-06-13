import rumps
import gpt4all
import sys

class App(rumps.App):
    def __init__(self):
        super(App, self).__init__("Search App", menu=None, icon="icon.png")

        # Create the menu items
        self.search_item = rumps.MenuItem("Ask GPT")
        self.gptj = gpt4all.GPT4All("ggml-gpt4all-j-v1.3-groovy", "models/")

        # Set the callback functions for menu item actions
        self.search_item.set_callback(self.on_search)

        # Create the menu
        self.menu = [self.search_item]

    def on_search(self, sender):
        # Handle the action for the search menu item
        gpt_response = "Enter your search query:"
        while(True):

            response = rumps.Window(
                title="Search",
                message= gpt_response,
                default_text="",
                cancel=True,
                ok="Search"
            ).run()

            if response.clicked:
                search_query = response.text
                if search_query:
                    gpt_response = self.gptj.generate(search_query, streaming = False)
                    # print(f"Searching for: {response}")
                    response.message = gpt_response
            else:
                quit()
    
    def on_quit(self):
        sys.exit("Closing Down")

if __name__ == '__main__':
    app = App()
    app.run()
