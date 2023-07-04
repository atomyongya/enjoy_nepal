from app.models.hotel.component.hotel_detail_model import HotelDetailModel
from app.models.hotel.hotel_model import HotelModel


class HotelService:
    def getData(self, hotel_object: HotelModel):
        hotel_details = hotel_object.hotel_detail.all()

        data = {
            'hotel_details': hotel_details,
        }

        return data