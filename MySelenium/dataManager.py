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
            