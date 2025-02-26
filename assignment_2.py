# -*- coding: utf-8 -*-
"""Assignment 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XrE5Wbtk7Sg5xB8PwUpgawnrRcOzsv3W
"""

class Artwork:
    def __init__(self, id, title, artist, date_of_creation, historical_significance, exhibition_location):
        self.__id = id
        self.__title = title
        self.__artist = artist
        self.__date_of_creation = date_of_creation
        self.__historical_significance = historical_significance
        self.__exhibition_location = exhibition_location

    # Getter methods
    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_artist(self):
        return self.__artist

    def get_date_of_creation(self):
        return self.__date_of_creation

    def get_historical_significance(self):
        return self.__historical_significance

    def get_exhibition_location(self):
        return self.__exhibition_location

    # Setter methods
    def set_id(self, id):
        self.__id = id

    def set_title(self, title):
        self.__title = title

    def set_artist(self, artist):
        self.__artist = artist

    def set_date_of_creation(self, date_of_creation):
        self.__date_of_creation = date_of_creation

    def set_historical_significance(self, historical_significance):
        self.__historical_significance = historical_significance

    def set_exhibition_location(self, exhibition_location):
        self.__exhibition_location = exhibition_location

# Example of creating an Artwork object and accessing its properties
artwork = Artwork("001", "Starry Night", "Vincent van Gogh", "1889", "Represents van Gogh's turbulent psyche", "MoMA, New York")

# Accessing properties
print(artwork.get_title())
print(artwork.get_artist())

# Updating the exhibition location
artwork.set_exhibition_location("Van Gogh Museum, Amsterdam")
print(artwork.get_exhibition_location())

class MuseumCollection:
    def __init__(self):
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def display_collection(self):
        for artwork in self.artworks:
            print(f"ID: {artwork.get_id()}, Title: {artwork.get_title()}, Artist: {artwork.get_artist()}, Date: {artwork.get_date_of_creation()}, Significance: {artwork.get_historical_significance()}, Location: {artwork.get_exhibition_location()}")

# Reusing the Artwork class from the previous example

# Initialize the museum collection
museum_collection = MuseumCollection()

# Existing artwork
artwork1 = Artwork("001", "Starry Night", "Vincent van Gogh", "1889", "Represents van Gogh's turbulent psyche", "MoMA, New York")
museum_collection.add_artwork(artwork1)

# New artwork addition
artwork2 = Artwork("002", "The Persistence of Memory", "Salvador Dali", "1931", "Symbolizes the relativity of space and time", "MoMA, New York")
museum_collection.add_artwork(artwork2)

# Display the collection
museum_collection.display_collection()

class Exhibition:
    def __init__(self, id, name, start_date, end_date, location):
        self.__id = id
        self.__name = name
        self.__start_date = start_date
        self.__end_date = end_date
        self.__location = location
        self.__artworks = []  # Initialize an empty list to hold Artwork instances

    # Getter methods
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_location(self):
        return self.__location

    def get_artworks(self):
        return self.__artworks

    # Setter methods
    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def set_location(self, location):
        self.__location = location

    def add_artwork(self, artwork):
        if artwork not in self.__artworks:
            self.__artworks.append(artwork)

# Example of using the Exhibition class along with the Artwork class
# Assume Artwork class is defined as in the previous examples

# Create some Artwork instances
artwork1 = Artwork("001", "Starry Night", "Vincent van Gogh", "1889", "Represents van Gogh's turbulent psyche", "MoMA, New York")
artwork2 = Artwork("002", "The Persistence of Memory", "Salvador Dali", "1931", "Symbolizes the relativity of space and time", "MoMA, New York")

# Create an Exhibition instance
exhibition = Exhibition("E001", "Masterpieces of the 20th Century", "2024-01-01", "2024-12-31", "Main Hall")

# Add artworks to the exhibition
exhibition.add_artwork(artwork1)
exhibition.add_artwork(artwork2)

# Example of accessing exhibition details
print(f"Exhibition: {exhibition.get_name()}")
print("Artworks in the exhibition:")
for artwork in exhibition.get_artworks():
    print(f" - {artwork.get_title()} by {artwork.get_artist()}")

class MuseumCollection:
    def __init__(self):
        self.artworks = []
        self.exhibitions = []  # Added to manage exhibitions

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def add_exhibition(self, exhibition):
        self.exhibitions.append(exhibition)

    def cancel_exhibition(self, exhibition_id):
        self.exhibitions = [exhibition for exhibition in self.exhibitions if exhibition.get_id() != exhibition_id]

    def display_exhibitions(self):
        for exhibition in self.exhibitions:
            print(f"ID: {exhibition.get_id()}, Name: {exhibition.get_name()}, Location: {exhibition.get_location()}, Dates: {exhibition.get_start_date()} to {exhibition.get_end_date()}")

# Example of adding and cancelling exhibitions

# Initialize the museum collection
museum = MuseumCollection()

# Creating two exhibitions
exhibition1 = Exhibition("E001", "Masterpieces of the 20th Century", "2024-01-01", "2024-12-31", "Main Hall")
exhibition2 = Exhibition("E002", "Impressionism and Beyond", "2024-06-01", "2024-12-31", "Gallery 2")

# Adding exhibitions to the museum collection
museum.add_exhibition(exhibition1)
museum.add_exhibition(exhibition2)

# Display current exhibitions
print("Current Exhibitions:")
museum.display_exhibitions()

# Cancel an exhibition
museum.cancel_exhibition("E001")
print("\nAfter Cancelling an Exhibition:")
museum.display_exhibitions()

# Adding a new exhibition
new_exhibition = Exhibition("E003", "Modern Art Selections", "2025-01-01", "2025-12-31", "New Wing")
museum.add_exhibition(new_exhibition)
print("\nAfter Adding a New Exhibition:")
museum.display_exhibitions()

class Visitor:
    def __init__(self, id, name, age, visitor_type, national_id,):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__visitor_type = visitor_type
        self.__national_id = national_id

    # Getter methods
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_visitor_type(self):
        return self.__visitor_type

    def get_national_id(self):
        return self.__national_id

    # Setter methods
    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_visitor_type(self, visitor_type):
        self.__visitor_type = visitor_type

    def set_national_id(self, national_id):
        self.__national_id = national_id

# Example usage
visitor1 = Visitor("001", "Essa", 30, "adult", "AB1234567")
print(f"Visitor Name: {visitor1.get_name()}, Age: {visitor1.get_age()}")

# Updating visitor information
visitor1.set_name("Hessa")
visitor1.set_age(20)
print(f"Updated Visitor Name: {visitor1.get_name()}, Age: {visitor1.get_age()}")

class Ticket:
    def __init__(self, ticket_id, visitor_id, event_id, purchase_date, event_date, price):
        self.__ticket_id = ticket_id
        self.__visitor_id = visitor_id
        self.__event_id = event_id
        self.__purchase_date = purchase_date
        self.__event_date = event_date
        self.__price = price

    # Getter methods
    def get_ticket_id(self):
        return self.__ticket_id

    def get_visitor_id(self):
        return self.__visitor_id

    def get_event_id(self):
        return self.__event_id

    def get_purchase_date(self):
        return self.__purchase_date

    def get_event_date(self):
        return self.__event_date

    def get_price(self):
        return self.__price

    # Setter methods
    def set_ticket_id(self, ticket_id):
        self.__ticket_id = ticket_id

    def set_visitor_id(self, visitor_id):
        self.__visitor_id = visitor_id

    def set_event_id(self, event_id):
        self.__event_id = event_id

    def set_purchase_date(self, purchase_date):
        self.__purchase_date = purchase_date

    def set_event_date(self, event_date):
        self.__event_date = event_date

    def set_price(self, price):
        self.__price = price

# Example usage
ticket = Ticket("T001", "V001", "E001", "2024-01-01", "2024-06-01", 50.0)
print(f"Ticket ID: {ticket.get_ticket_id()}, Event ID: {ticket.get_event_id()}, Purchase Date: {ticket.get_purchase_date()}, Price: ${ticket.get_price()}")

# Updating ticket information
ticket.set_price(55.0)
print(f"Updated Ticket Price: ${ticket.get_price()}")

class Event:
    def __init__(self, event_id, name, start_date, end_date, location, base_price, event_type):
        self.__event_id = event_id
        self.__name = name
        self.__start_date = start_date
        self.__end_date = end_date
        self.__location = location
        self.__base_price = base_price
        self.__event_type = event_type

    # Getter methods
    def get_event_id(self):
        return self.__event_id

    def get_name(self):
        return self.__name

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_location(self):
        return self.__location

    def get_base_price(self):
        return self.__base_price

    def get_event_type(self):
        return self.__event_type

    # Setter methods
    def set_event_id(self, event_id):
        self.__event_id = event_id

    def set_name(self, name):
        self.__name = name

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def set_location(self, location):
        self.__location = location

    def set_base_price(self, base_price):
        self.__base_price = base_price

    def set_event_type(self, event_type):
        self.__event_type = event_type

# Example usage
event = Event("E001", "Night at the Museum", "2024-05-01", "2024-05-31", "Main Hall", 20.0, "Exhibition")
print(f"Event: {event.get_name()}, Type: {event.get_event_type()}, Location: {event.get_location()}, Start Date: {event.get_start_date()}")

# Updating event information
event.set_base_price(25.0)
print(f"Updated Event Base Price: ${event.get_base_price()}")

class Tour(Event):
    def __init__(self, event_id, name, start_date, end_date, location, base_price, event_type, guide_name, max_visitors, min_visitors):
        super().__init__(event_id, name, start_date, end_date, location, base_price, event_type)
        self.__guide_name = guide_name
        self.__max_visitors = max_visitors
        self.__min_visitors = min_visitors
        self.__tour_visitors = []

    # Getter methods for Tour specific attributes
    def get_guide_name(self):
        return self.__guide_name

    def get_max_visitors(self):
        return self.__max_visitors

    def get_min_visitors(self):
        return self.__min_visitors

    def get_tour_visitors(self):
        return self.__tour_visitors

    # Setter methods for Tour specific attributes
    def set_guide_name(self, guide_name):
        self.__guide_name = guide_name

    def set_max_visitors(self, max_visitors):
        self.__max_visitors = max_visitors

    def set_min_visitors(self, min_visitors):
        self.__min_visitors = min_visitors

    def add_tour_visitor(self, visitor):
        if len(self.__tour_visitors) < self.__max_visitors:
            self.__tour_visitors.append(visitor)

# Example usage
# Assume the Visitor class is defined as previously shown
visitor1 = Visitor("001", "essa", 30, "adult", "AB1234567")
tour = Tour("T001", "Historical Tour", "2024-05-01", "2024-05-31", "Historical Wing", 20.0, "Tour", "Jane Smith", 30, 5)
tour.add_tour_visitor(visitor1)

print(f"Tour Name: {tour.get_name()}, Guide: {tour.get_guide_name()}")
print("Tour Visitors:")
for visitor in tour.get_tour_visitors():
    print(f"- {visitor.get_name()}, ID: {visitor.get_id()}")

class SpecialEvent(Event):
    def __init__(self, event_id, name, start_date, end_date, location, base_price, event_type, special_features, sponsor):
        super().__init__(event_id, name, start_date, end_date, location, base_price, event_type)
        self.__special_features = special_features  # Assuming this is a list of features
        self.__sponsor = sponsor

    # Getter methods for SpecialEvent specific attributes
    def get_special_features(self):
        return self.__special_features

    def get_sponsor(self):
        return self.__sponsor

    # Setter methods for SpecialEvent specific attributes
    def set_special_features(self, special_features):
        self.__special_features = special_features

    def set_sponsor(self, sponsor):
        self.__sponsor = sponsor

    # Additional methods for managing special features
    def add_special_feature(self, feature):
        if feature not in self.__special_features:
            self.__special_features.append(feature)

    def remove_special_feature(self, feature):
        if feature in self.__special_features:
            self.__special_features.remove(feature)

# Example usage
special_event = SpecialEvent("SE001", "New Year's Gala", "2024-12-31", "2025-01-01", "Grand Ballroom", 100.0, "Gala", ["Live Music", "Fireworks"], "Acme Corp.")

# Accessing and modifying SpecialEvent properties
print(f"Event Name: {special_event.get_name()}, Sponsored by: {special_event.get_sponsor()}")
print("Special Features:")
for feature in special_event.get_special_features():
    print(f"- {feature}")

# Adding a new special feature and updating the sponsor
special_event.add_special_feature("Catered Dinner")
special_event.set_sponsor("Globex Corporation")
print("\nUpdated Special Features and Sponsor:")
print(f"Sponsored by: {special_event.get_sponsor()}")
for feature in special_event.get_special_features():
    print(f"- {feature}")

class TicketPricing:
    def __init__(self):
        # Define a dictionary to hold discount rates for different visitor types
        self.discount_rates = {
            "child": 0.5,  # 50% discount
            "senior": 0.25,  # 25% discount
            "adult": 0.0,  # no discount
        }
        # Assuming a standard base price for simplicity
        self.base_price = 100  # base price for ticket

    def calculate_price(self, visitor):
        # Retrieve the visitor type
        visitor_type = visitor.get_visitor_type()
        # Get the discount rate for the visitor type
        discount_rate = self.discount_rates.get(visitor_type, 0)  # Default discount is 0 if visitor type is not found
        # Calculate the final price
        final_price = self.base_price * (1 - discount_rate)
        return final_price

# Example usage
visitor_child = Visitor("002", "Alice Doe", 12, "child", "BC1234568")
visitor_senior = Visitor("003", "Bob Smith", 65, "senior", "CD1234569")
visitor_adult = Visitor("001", "Charlie Brown", 30, "adult", "AB1234567")

ticket_pricing = TicketPricing()

# Calculate and print ticket prices for each visitor type
print(f"Final Ticket Price for {visitor_child.get_name()}: ${ticket_pricing.calculate_price(visitor_child)}")
print(f"Final Ticket Price for {visitor_senior.get_name()}: ${ticket_pricing.calculate_price(visitor_senior)}")
print(f"Final Ticket Price for {visitor_adult.get_name()}: ${ticket_pricing.calculate_price(visitor_adult)}")

class VisitorManagement:
    def __init__(self):
        self.visitors = []  # Stores instances of Visitor
        self.ticket_pricing = TicketPricing()  # Assumes TicketPricing class is defined
        self.tours = {}  # Dictionary to manage tours by tour ID

    def add_visitor(self, visitor):
        """Add a new visitor to the system."""
        self.visitors.append(visitor)

    def purchase_ticket(self, visitor):
        """Calculates and returns the price of a ticket for a visitor."""
        price = self.ticket_pricing.calculate_price(visitor)
        # Assuming ticket purchase process here; could involve storing transaction details
        return price

    def register_for_tour(self, visitor, tour_id):
        """Registers a visitor for a tour given by the tour ID."""
        if tour_id in self.tours:
            tour = self.tours[tour_id]
            tour.add_tour_visitor(visitor)
            return True
        return False

    def add_tour(self, tour):
        """Adds a tour to the system."""
        self.tours[tour.get_event_id()] = tour

# Example usage assuming required classes (Visitor, TicketPricing, Tour) are defined
visitor1 = Visitor("001", "Abdulla", 30, "adult", "AB1234567")
tour1 = Tour("T001", "Historical Tour", "2024-05-01", "2024-05-31", "Historical Wing", 20.0, "Tour", "Jane Smith", 30, 5)

vm = VisitorManagement()
vm.add_visitor(visitor1)
vm.add_tour(tour1)

ticket_price = vm.purchase_ticket(visitor1)
print(f"Ticket Price for {visitor1.get_name()}: ${ticket_price}")

registration_success = vm.register_for_tour(visitor1, "T001")
if registration_success:
    print(f"{visitor1.get_name()} successfully registered for the tour.")
else:
    print("Tour registration failed.")