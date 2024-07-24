import os
import logging
from config import (
    LOG_FILE_NAME,
    QUERY_FILE_NAME,
    CSV_FILE_PATH,
    NEXTDAY_CSV_FILE_PATH,
    YESTERDAY_CSV_FILE_PATH,
    CREATE_TEMP_CSV_FILE_NAME,
    CREATE_TEMP_JSON_FILE_NAME,
    DELETE_TEMP_CSV_FILE_NAME,
    DELETE_TEMP_JSON_FILE_NAME,
    OUT_FOLDER,
    INPUT_FOLDER,
    EXCEPT_FILES,
    OLD_LOG_FILE,
)
from core.api.cip_request_get_ip import process_ioc
from core.api.managefiles import (
    QueryData,
    find_unique_ip_addresses,
    create_csv_file,
    convert_csv_to_json,
    filter_old_data_and_get_ip_addresses,
    extract_and_save_to_json,
    merge_files_and_create_nextday_file,
    delete_files_in_folder,
    remove_file_with_log,
)


logging.basicConfig(
    filename=LOG_FILE_NAME,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s",
)


def load_queries(query_file_name):
    return QueryData.from_file(query_file_name)


def chunk_list(lst, chunk_size):
     """Function to split a list into specified chunk sizes"""
    for i in range(0, len(lst), chunk_size):
        yield lst[i : i + chunk_size]


def check_new_ip_address(CSV_FILE_PATH, YESTERDAY_CSV_FILE_PATH):
    """Function to check for new IP address data"""
    logging.info("CSV file is ready.")
    new_ip_list = find_unique_ip_addresses(CSV_FILE_PATH, YESTERDAY_CSV_FILE_PATH)
    logging.info(f"Unique IP addresses: {new_ip_list}")
    if new_ip_list:
        create_csv_file(new_ip_list, CREATE_TEMP_CSV_FILE_NAME)
        convert_csv_to_json(CREATE_TEMP_CSV_FILE_NAME, CREATE_TEMP_JSON_FILE_NAME)
    return new_ip_list


def check_delete_ip_address(YESTERDAY_CSV_FILE_PATH):
    """Function to check for IP address data that needs to be deleted"""
    delete_ip_list = filter_old_data_and_get_ip_addresses(YESTERDAY_CSV_FILE_PATH)
    logging.info(f"IP addresses to delete: {delete_ip_list}")

    if delete_ip_list:
        create_csv_file(delete_ip_list, DELETE_TEMP_CSV_FILE_NAME)
        extract_and_save_to_json(DELETE_TEMP_CSV_FILE_NAME, DELETE_TEMP_JSON_FILE_NAME)
    return delete_ip_list


def main():
    queries = load_queries(QUERY_FILE_NAME)
    for c2_name, query_list in queries.data.items():
        process_ioc(c2_name, query_list)

    if os.path.exists(CSV_FILE_PATH):
        new_ip_list = check_new_ip_address(CSV_FILE_PATH, YESTERDAY_CSV_FILE_PATH)
        delete_ip_list = check_delete_ip_address(YESTERDAY_CSV_FILE_PATH)

    merge_files_and_create_nextday_file(
        CREATE_TEMP_CSV_FILE_NAME, YESTERDAY_CSV_FILE_PATH, NEXTDAY_CSV_FILE_PATH
    )
    logging.info("Files merged and next day file created.")

    # delete files
    delete_files_in_folder(OUT_FOLDER)
    delete_files_in_folder(INPUT_FOLDER, EXCEPT_FILES)
    remove_file_with_log(OLD_LOG_FILE)


if __name__ == "__main__":
    main()
