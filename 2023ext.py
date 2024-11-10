import csv
with open("./popularity/live_popularity_process.csv","w+",encoding="utf-8",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(["city_id","year","pred"])
    for key in cities:
        pred = cities[key]['live_popularity'].loc['2023']
        csv_writer.writerow([key,2023,pred])
        
with open("./popularity/live_popularity_2023.csv","w+",encoding="utf-8",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(["city_id","year","pred"])
    for key in cities:
        pred = cities[key]['live_popularity'].loc['2023']
        csv_writer.writerow([key,2023,pred])