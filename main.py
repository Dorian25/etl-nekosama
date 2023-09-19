import pandas
import os





if __name__ ==  "__main__":
    files_pages_xlsx = os.listdir("./data")

    for file_page_xlsx in files_pages_xlsx:
        raw_data = read_xlsx_file(file_page_xlsx)
        transform_data = transform(raw_data)
        load_sql_db()
        load_mongo_db()


