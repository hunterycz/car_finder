class CarGurus:
    """
    CarGurus class is used to generate URLs for car listings based on specific criteria.

    This class takes in a zip code, maximum and minimum price, and a distance in miles from your current location,
    and then creates URLs for all the cars listed/saved inside of the class.

    Attributes:
        zip_code (int): The zip code to search for cars.
        max_price (int): The maximum price for the car search.
        min_price (int): The minimum price for the car search.
        distance (int): The distance in miles from the given zip code.
        cargurus_car_ids (dict): A dictionary containing car names as keys and their corresponding CarGurus IDs as values.

    Methods:
        cargurus_url_maker(car_id):
            Generates a CarGurus URL for a specific car ID based on the provided search criteria.

        generate_urls():
            Iterates over the saved car IDs and generates a dictionary of car names and their corresponding URLs.
    """

    def __init__(self, zip_code, max_price, min_price, distance):
        self.zip_code = zip_code
        self.max_price = max_price
        self.min_price = min_price
        self.distance = distance
        self.cargurus_car_ids = {
            "toyota_highlander": 'd298',
            "toyota_rav4": 'd306',
            "honda_crv": 'd589',
            "subaru_impreza": 'd375',
            "subaru_forester": 'd374',
            "subaru_outback": 'd380'
        }

    def cargurus_url_maker(self, car_id):
        """
        Generates a CarGurus URL for a specific car ID based on the provided search criteria.

        Parameters:
            car_id (str): The CarGurus ID of the car.

        Returns:
            str: The generated URL for the car listing.
        """
        return f"https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?maxAccidents=0&zip={
            self.zip_code}&maxPrice={
            self.max_price}&shopByTypes=NEAR_BY&distance={
            self.distance}&minPrice={
                self.min_price}&entitySelectingHelper.selectedEntity={car_id}"

    def generate_urls(self):
        """
        Iterates over the saved car IDs and generates a dictionary of car names and their corresponding URLs.

        Returns:
            dict: A dictionary where the keys are car names and the values are their corresponding URLs.
        """
        urls = {}
        for key, value in self.cargurus_car_ids.items():
            url = self.cargurus_url_maker(car_id=value)
            urls[key] = url
        return urls