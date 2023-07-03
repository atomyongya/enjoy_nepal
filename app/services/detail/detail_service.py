class DetailService:
    def get_data(
        self,
        popular_destination_object,
        kathmandu_tour_object,
    ):
        if popular_destination_object != None:
            return {
                'id': popular_destination_object.id,
            }

        else:
            return {
                'id': kathmandu_tour_object.id,
            }

        return data