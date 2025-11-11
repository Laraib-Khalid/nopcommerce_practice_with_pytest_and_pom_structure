import logging
import os

class Log_maker:
    @staticmethod
    def log_gen():
        folder_path = "logs"
        file_name = "nopcommerce.log"

        # Create the folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        # Full path of the file
        file_path = os.path.join(folder_path, file_name)

        # Check karen agar file already exist na karti ho
        if not os.path.exists(file_path):
            open(file_path, "w").close()  # Empty file create
            print(f"{file_name} created successfully!")
        else:
            print(f"{file_name} already exists.")

        logging.basicConfig(filename=file_path, format='%(asctime)s : %(levelname)s : %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger