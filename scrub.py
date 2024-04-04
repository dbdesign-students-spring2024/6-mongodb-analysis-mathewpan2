import csv
import os



keep = ["host_id", "host_is_superhost", "name", "price", "neighbourhood", "host_name", "beds", "neighbourhood_group_cleansed", "review_scores_rating"]
col_to_delete = []
first_row = True
with open(os.path.join('data', 'listings.csv'), 'r', encoding='utf-8') as read:
    with open(os.path.join('data', 'listings_clean.csv'), 'w',  newline='', encoding='utf-8') as write:
        writer = csv.writer(write)
        reader = csv.reader(read)
        for row in reader:
            if first_row:
                for index, category in enumerate(row):
                    if category not in keep:
                        col_to_delete.append(index)
                first_row = False
            row = [row[i] for i in range(len(row)) if i not in col_to_delete]
            writer.writerow(row)
            

