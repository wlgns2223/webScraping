import csv
class catDataManager():
    
    def __init__(self, file_name):
    
        self.file_name = file_name
        self.file_path = './' + self.file_name
        
    def save_cat_data(self,name, img_location):
        with open(self.file_path,'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([name.strip('/') , img_location])
        
    def get_saved_cat_data(self):
        with open(self.file_path, 'r') as csvFile:
            data = csv.reader(csvFile)
            return list(data)

    def delete_duplicated_data(self):
        old_data = self.get_saved_cat_data()
        new_list = []
        for data in old_data:
            if data not in new_list:
                new_list.append(data)

        with open(self.file_path,'w') as csv_file:
            writer = csv.writer(csv_file)
            for data in new_list:
                writer.writerow(data)