from core.base_api import BaseAPI
from utils.config import BASE_URL

class WishlistAPI:

    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    # fetch Wishlist using GET mtd
    def get_wishlist(self, shopper_id, headers):
        return self.api.get(
            f"/shoppers/{shopper_id}/wishlist",
            headers=headers
        )

    # Add product to wishlist using POST mtd
    def add_to_wishlist(self, shopper_id, headers, product_id, quantity):
        payload = {
            "productId": product_id,
            "quantity": quantity
        }

        return self.api.post(
            f"/shoppers/{shopper_id}/wishlist",
            headers=headers,
            json=payload
        )

    # remove from wishlist using DELETE mtd
    def del_from_wishlist(self, shopper_id, headers, product_id):
        return self.api.delete(
            f"/shoppers/{shopper_id}/wishlist/{product_id}",
            headers=headers
        )