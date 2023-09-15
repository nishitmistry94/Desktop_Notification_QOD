
# Imports
import requests
from plyer import notification
class quotesApiApp():
    def __init__(self):
        pass
    
    
    # Sub-Routines
    def fetch(self): 
        print("Request sent...") # This gets the quote from the API and turns it into the quote to be displayed
        quoteSite = requests.get("http://api.quotable.io/random")
        quoteJson = quoteSite.json()
        quote = quoteJson["content"] + "\n- " + quoteJson["author"]
        if len(quote) > 256:
            self.fetch()
        else:
            return quote


    def display(self,quote):  # Uses the plyer module to display the quote
        notification.notify(
            title="Quote of day",
            message=quote,
            app_name="QOD Notify",
            timeout=10,
            toast=False,
        )

    # Main Program
    def task(self):  # This puts it all together
        quote = self.fetch()
        self.display(quote)

    