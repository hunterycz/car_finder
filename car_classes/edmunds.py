class Edmunds:
    """
    A class used to generate URLs for car listings on Edmunds based on specific criteria

    Attributes
    ----------
    zip_code : int
        The ZIP code for the search area.
    max_price : int
        The maximum price of the car.
    min_price : int
        The minimum price of the car.
    distance : int
        The search radius distance.
    edmunds_car_ids : dict
        A dictionary mapping car models to their respective makes.
    """

    def __init__(self, zip_code: int = 85296, max_price: int = 50000, min_price: int = 1, distance: int = 50):
        """
        Initializes the Edmunds class with the specified ZIP code, price range, and search distance.

        Parameters
        ----------
        zip_code : int
            The ZIP code for the search area.
        max_price : int
            The maximum price of the car.
        min_price : int
            The minimum price of the car.
        distance : int
            The search radius distance.
        """
        self.zip_code = zip_code
        self.max_price = max_price
        self.min_price = min_price
        self.distance = distance
        self.edmunds_car_ids = {
            "highlander": "toyota",
            "rav4": "toyota",
            "cr-v": "honda",
            "impreza": "subaru",
            "forester": "subaru",
            "outback": "subaru"
        }

    def url_maker(self, make: str, model: str) -> str:
        """
        Creates a URL for the car listings on Edmunds based on the specified make and model.

        Parameters
        ----------
        make : str
            The make of the car.
        model : str
            The model of the car.

        Returns
        -------
        str
            The URL for the car listings on Edmunds.
        """
        return f"https://www.edmunds.com/inventory/srp.html?price={self.min_price}-{self.max_price}&inventorytype=used%2Ccpo&make={make}&model={make}%7C{model}&radius={self.distance}&historyinfo=noAccidents"

    def generate_urls(self) -> list[str]:
        """
        Generates a list of URLs for car listings on Edmunds for all car models in the edmunds_car_ids dictionary.

        Returns
        -------
        list[str]
            A list of URLs for the car listings on Edmunds.
        """
        urls = []

        for model, make in self.edmunds_car_ids.items():
            url = self.url_maker(make, model)
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
        for model, make in self.edmunds_car_ids.items():
            url = self.url_maker(make, model)
            format_dict = {
                "title": make.upper() + " " + model.upper(),
                "url": url
            }

            urls.append(format_dict)

        return urls
 