import webbrowser

# Define the car sites and car IDs
car_sites = [
    "cargurus", "edmunds",
    "cars.com", "autotrader"
]

cargurus_car_ids = {
    "toyota_highlander": 'd298',
    "toyota_rav4": 'd306',
    "honda_crv": 'd589',
    "subaru_impreza": 'd375',
    "subaru_forester": 'd374',
    "subaru_outback": "d380"
}


# Function to create URLs for CarGurus
def cargurus_url_maker(zip_code, max_price, min_price, distance, car_id):
    return f"https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?maxAccidents=0&zip={zip_code}&maxPrice={max_price}&shopByTypes=NEAR_BY&distance={distance}&minPrice={min_price}&entitySelectingHelper.selectedEntity={car_id}"


if __name__ == "__main__":
    zip_code = 85296
    max_price = 8000
    min_price = 0
    distance = 50

    for key, value in cargurus_car_ids.items():
        url = cargurus_url_maker(
            zip_code=zip_code,
            max_price=max_price,
            min_price=min_price,
            distance=distance,
            car_id=value
        )
        print(f"{key.upper()}: {url}")

        # Open the URL in Google Chrome
        webbrowser.get('chrome').open_new_tab(url)
