from Event import Event


class EventManager:
    """
    Manages a collection of Event objects.
    Responsibilities:
      - Maintain a list of Event objects (self.events)
      - Provide methods to add, display, save, search and load events      
    """

    FILE_NAME = "events.txt"   # The file used to persist events

    # ------------------------------------------------------------------
    # TODO 11 — Write the __init__ method.
    #           Initialise the internal event list self.events
    #           Automatically load any events saved from a previous session
    #           by calling a load_events method
    # ------------------------------------------------------------------
    def __init__(self):
        self.events = []
        self.load_events()

    # ------------------------------------------------------------------
    # TODO 12 — add_event(self, name, date, location, guests)
    #
    #     create an Event object, append it to
    #     self.events, and print a success message.
    # ------------------------------------------------------------------
    def add_event(self, name, date, location, guests):
        event = Event(name, date, location, guests)
        self.events.append(event)
        print(f"Event successfully added in the directory:\n{event}")

    # ------------------------------------------------------------------
    # TODO 13 — display_events(self)
    #
    #   Print all events stored in self.events.
    #   If the list is empty, print a suitable message instead.
    #   Number each event (1, 2, 3 …) for readability.
    # ------------------------------------------------------------------
    def display_events(self):
        if not self.events:
            print("No events to display.")
            return

        print("\nCURRENT EVENTS")
        print("-" * 100)

        for index, event in enumerate(self.events, start=1):
            print(f"{index:<2}. {event}")

        print("-" * 100)

    # ------------------------------------------------------------------
    # TODO 14 — save_events(self)
    #
    #   Save every event in self.events to FILE_NAME (events.txt).
    #   Each event should be written as one line using the comma character
    #   "," as a separator, e.g.:
    #       Tech Summit,2025-06-15,Brisbane,120
    #
    #   Print a confirmation message once the file is written.
    # ------------------------------------------------------------------
    def save_events(self):
        with open(self.FILE_NAME, "w") as f:
            for event in self.events:
                f.write(
                    f"{event.name},{event.date},{event.location},{event.guests}\n")

        print(f"Events saved to '{self.FILE_NAME}'.")

    # ------------------------------------------------------------------
    # load_events(self)  - provided
    #
    #   Read events from FILE_NAME (events.txt) and populate self.events.
    #   Each line has the format: name,date,location,guests
    #   Skip any line that does not have exactly 4 fields.
    #   If the file does not exist, do nothing (start with an empty list).
    #   Print a message showing how many events were loaded.
    # ------------------------------------------------------------------
    def load_events(self):
        try:
            with open(self.FILE_NAME, "r") as f:
                lines = f.readlines()

            loaded = 0
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) != 4:
                    continue  # skip malformed lines
                name, date, location, guests_str = parts
                try:
                    guests = int(guests_str)
                except ValueError:
                    continue
                self.events.append(Event(name, date, location, guests))
                loaded += 1

            if loaded > 0:
                print(f"   {loaded} event(s) loaded from '{self.FILE_NAME}'.")

        except FileNotFoundError:
            pass  # No file yet — that is fine
    # ------------------------------------------------------------------
    # TODO 15 - search_events(self, keyword)
    #
    #   Search for events whose name contains the keyword (case-insensitive,
    #   partial match). Print the event found.
    #   If no matches are found, print a suitable message.
    # ------------------------------------------------------------------

    def search_events(self, keyword):
        keyword_lower = keyword.lower()
        matches = [
            event for event in self.events if keyword_lower in event.name.lower()]

        if not matches:
            print(f"No events found matching '{keyword}'.")
            return

        for event in matches:
            print(event)
