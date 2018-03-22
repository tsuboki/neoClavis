class Asin_data_array_by_category:
    category = ""
    asin_data_array = []

    def __init__(self, category, asin_data):
        self.category = category
        self.asin_data_array = [asin_data]

    #append 1 row into asin data to_array
    def appned_one_row_to_asin_data_array(self, asin_data):
        self.asin_data_array.append(asin_data)
