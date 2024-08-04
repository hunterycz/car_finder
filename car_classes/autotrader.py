class AutoTrader:
    """
    AutoTrader class is used to generate URLs for car listings based on specific criteria.

    This class takes in a zip code, maximum and minimum price, and a distance in miles from your current location,
    and then creates URLs for all the cars listed/saved inside of the class.

    Attributes:
        zip_code (int): The zip code to search for cars.
        max_price (int): The maximum price for the car search.
        min_price (int): The minimum price for the car search.
        distance (int): The distance in miles from the given zip code.
        autotrader_car_ids (list): A list containing car names as strings.

    Methods:
        autotrader_url_maker(car_id):
            Generates an AutoTrader URL for a specific car ID based on the provided search criteria.

        generate_urls():
            Iterates over the saved car IDs and generates a list of URLs.
    """

    def __init__(self, zip_code: int = 85296, max_price: int = 10000, min_price: int = 0, distance: int = 50):
        self.zip_code = zip_code
        self.max_price = max_price
        self.min_price = min_price
        self.distance = distance
        self.autotrader_car_ids = [
            "toyota/highlander",
            "toyota/rav4",
            "honda/cr-v",
            "subaru/impreza",
            "subaru/forester",
            "subaru/outback"
        ]

    def url_maker(self, car_id: str) -> str:
        """
        Generates an AutoTrader URL for a specific car ID based on the provided search criteria.

        Parameters:
            car_id (str): The ID of the car (formatted as a string).

        Returns:
            str: The generated URL for the car listing.
        """
        return f"https://www.autotrader.com/cars-for-sale/cars-between-{self.min_price}-and-{self.max_price}/{car_id}/gilbert-az?newSearch=true&searchRadius={self.distance}&vehicleHistoryType=NO_ACCIDENTS&vehicleHistoryType=CLEAN_TITLE&zip={self.zip_code}"

    def generate_urls(self) -> list[str]:
        """
        Iterates over the saved car IDs and generates a list of URLs.

        Returns:
            list: A list where each element is a URL string for a car listing.
        """
        urls = []
        for car in self.autotrader_car_ids:
            url = self.url_maker(car_id=car)
            urls.append(url)
        return urls

    def generate_urls_webpage(self) -> dict[str]:
        """
        Iterates over the saved car IDs and creates a dictionary format for 
        the frontend to interpret and portray on the webpage.

        Returns:
            List: A list of dictionaries with the "title" and "Url" are saved.
        """
        urls = []
        for car in self.autotrader_car_ids:
            format_dict = {}
            url = self.url_maker(car_id=car)
            format_dict = {
                "title": car.upper(),
                "url": url
            }

            urls.append(format_dict)

        return urls
