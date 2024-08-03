class CarsCom:
    """
    CarsCom class is used to generate URLs for car listings based on specific criteria.

    This class takes in a zip code, maximum and minimum price, and a distance in miles from your current location,
    and then creates URLs for all the cars listed/saved inside of the class.

    Attributes:
        zip_code (int): The zip code to search for cars.
        max_price (int): The maximum price for the car search.
        min_price (int): The minimum price for the car search.
        distance (int): The distance in miles from the given zip code.
        carcom_car_ids (dict): A dictionary containing car models as keys and their corresponding makes as values.

    Methods:
        carscom_url_maker(make, model):
            Generates a Cars.com URL for a specific car make and model based on the provided search criteria.

        generate_urls():
            Iterates over the saved car makes and models and generates a list of URLs.
    """

    def __init__(self, zip_code: int = 85296, max_price: int = 10000, min_price: int = 0, distance: int = 50):
        self.zip_code = zip_code
        self.max_price = max_price
        self.min_price = min_price
        self.distance = distance
        self.carcom_car_ids = {
            "toyota-highlander": "toyota",
            "toyota-rav4": "toyota",
            "honda-cr-v": "honda",
            "subaru-impreza": "subaru",
            "subaru_forester": "subaru",
            "subaru_outback": "subaru"
        }

    def url_maker(self, make: str, model: str) -> str:
        """
        Generates a Cars.com URL for a specific car make and model based on the provided search criteria.

        Parameters:
            make (str): The make of the car.
            model (str): The model of the car.

        Returns:
            str: The generated URL for the car listing.
        """
        return f"https://www.cars.com/shopping/results/?clean_title=true&dealer_id=&keyword=&list_price_max={self.max_price}&list_price_min={self.min_price}&makes[]={make}&maximum_distance={self.distance}&mileage_max=&models[]={model}&no_accidents=true&sort=best_match_desc&stock_type=all&year_max=&year_min=&zip={self.zip_code}"

    def generate_urls(self) -> list[str]:
        """
        Iterates over the saved car makes and models and generates a list of URLs.

        Returns:
            list: A list where each element is a URL string for a car listing.
        """
        urls = []
        for model, make in self.carcom_car_ids.items():
            url = self.url_maker(make=make, model=model)
            urls.append(url)
        return urls
