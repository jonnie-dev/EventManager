class Event:
    """
    Represents a single event with the following attributes:
      - name    : str  — the event name
      - date    : str  — the event date in yyyy-mm-dd format
      - location: str  — where the event will be held
      - guests  : int  — expected number of guests (5–500)
    """
    # ------------------------------------------------------------------
    # TODO 9 — Write the __init__ method.
    #           It should accept name, date, location, and guests as
    #           parameters and store them as instance attributes.
    # ------------------------------------------------------------------

    def __init__(self, name, date, location, guests):
        self.name = name
        self.date = date
        self.location = location
        self.guests = guests

    # ------------------------------------------------------------------
    # TODO 10 — Write the __str__ method.
    #           Return a formatted string so that print(event) displays
    #           something readable, e.g.:
    #           "Event: Tech Summit | Date: 2025-06-15 | Location: Brisbane | Guests: 120"
    # ------------------------------------------------------------------
    def __str__(self):
        return (
            f"Event: {self.name:<25} | "
            f"Date: {self.date:<10} | "
            f"Location: {self.location:<15} | "
            f"Guests: {self.guests:>5}"
        )
