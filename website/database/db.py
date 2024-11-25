import requests
from . import encrypt
from . import __trash

# CON_KEY = "david.nzube.official22@gmail.com/david.nzube.official22@gmail.com/8x7bty112(8jIj8*22@P21=+~-+1.m"
CON_KEY = encrypt.decrypter(encrypt.decrypter(encrypt.decrypter(encrypt.decrypter((__trash.retTr())))))

print(CON_KEY)

# from_ = "http://127.0.0.1:781"
from_ = "https://sarahdb.pythonanywhere.com"

link_prefix = f"{from_}/{CON_KEY}/handler"
DB_URL = f"{from_}/login/{CON_KEY}"

try:
    response = requests.get(DB_URL)

    def connect():
        """
        Establishes a connection to the database server using a GET request.
        """
        requests.get(DB_URL)

    def request_then_text(url):
        """
        Sends a GET request to the provided URL and returns the response text.
        
        Args:
            url (str): The URL to send the GET request to.
        
        Returns:
            str: The response text from the server.
        """
        req = requests.get(url)
        return req.text

    def request_then_text_post(url, data):
        """
        Sends a POST request to the provided URL with the given data and returns the response text.
        
        Args:
            url (str): The URL to send the POST request to.
            data (dict): The data to include in the POST request.
        
        Returns:
            str: The response text from the server.
        """
        req = requests.post(url, data)
        return req.text

    if response.status_code:
        print("Connected to db server successfully")
        print(f"\n\n>>>>>>>>>>>>>>>>>>>>>{response.text}\n\n\n")

        db = {}

        class dbORM:
            """
            ORM class for interacting with the database. Provides various methods for 
            querying, updating, adding, and deleting entries in the database.
            """
            def __init__(self):
                self.database = db

            def all():
                """
                Retrieves all data from the database.

                Returns:
                    eval: Evaluates the response from the database handler.
                """
                return eval(request_then_text(url=f'{link_prefix}/handler'))

            def get_all(model):
                """
                Retrieves all entries of a specific model from the database.
                
                Args:
                    model (str): The name of the model/table to retrieve.
                
                Returns:
                    eval: Evaluates the response containing all entries of the model.
                """
                return eval(request_then_text(url=f'{link_prefix}/get_all/{model}'))

            def find_all(model, column, value):
                """
                Finds all entries in a model where the specified column matches the given value.
                
                Args:
                    model (str): The name of the model/table.
                    column (str): The column to search in.
                    value (str): The value to search for.
                
                Returns:
                    eval: Evaluates the response containing matching entries.
                """
                return eval(request_then_text(url=f'{link_prefix}/find_all/{model}/{column}/{value}'))

            def add_one(model, column, value):
                """
                Adds a new entry to a model with a single column-value pair.
                
                Args:
                    model (str): The name of the model/table.
                    column (str): The column to add the value to.
                    value (str): The value to add.
                
                Returns:
                    eval: Evaluates the response after adding the entry.
                """
                return eval(request_then_text(url=f'{link_prefix}/add_one/{model}/{column}/{value}'))

            def add_entry(model, column_value_pairs):
                """
                Adds a new entry with multiple column-value pairs to the model.
                
                Args:
                    model (str): The name of the model/table.
                    column_value_pairs (dict): A dictionary of column-value pairs.
                
                Returns:
                    eval: Evaluates the response after adding the entry.
                """
                try:
                    _ = {
                        "model": f"{model}", 
                        "column_value_pairs": f"{column_value_pairs}"
                    }
                    return eval(request_then_text_post(url=f'{link_prefix}/add_entry', data=_))
                except Exception as e:
                    print(f">>>>>>>>>>>>>>>>>>>>>>>>>>\ne: {e}\nmodel: {model}\ncvp: {column_value_pairs}")

            def find_one(model, column, value):
                """
                Finds a single entry in a model where the specified column matches the given value.
                
                Args:
                    model (str): The name of the model/table.
                    column (str): The column to search in.
                    value (str): The value to search for.
                
                Returns:
                    eval: Evaluates the response containing the matching entry.
                """
                return eval(request_then_text(url=f'{link_prefix}/find_one/{model}/{column}/{value}'))

            def update_one(model, column, value_search, value_update):
                """
                Updates a single entry in a model where the column matches the search value.
                
                Args:
                    model (str): The name of the model/table.
                    column (str): The column to search in.
                    value_search (str): The value to search for in the column.
                    value_update (str): The value to update the column with.
                
                Returns:
                    eval: Evaluates the response after updating the entry.
                """
                return eval(request_then_text(url=f'{link_prefix}/update_one/{model}/{column}/{value_search}/{value_update}'))

            def update_entry(model, column, column_value_pairs, dnd):
                """
                Updates an entry with column-value pairs. If dnd is True, updates without connecting.
                
                Args:
                    model (str): The name of the model/table.
                    column (str): The column to update.
                    column_value_pairs (dict): A dictionary of column-value pairs.
                    dnd (bool): Whether to skip connection and update directly.
                
                Returns:
                    eval: Evaluates the response after updating the entry.
                """
                if dnd:
                    _ = {
                        "model": f"{model}", 
                        "column": f"{column}", 
                        "cvp": f"{column_value_pairs}"
                    }
                    return eval(request_then_text_post(url=f'{link_prefix}/update_entry_dnd', data=_))
                else:
                    return eval(request_then_text(url=f'{link_prefix}/update_entry/{model}/{column}/{column_value_pairs}'))

            def delete_entry(model, column):
                """
                Deletes an entry in the specified model where the column matches the given value.
                
                Args:
                    model (str): The name of the model/table.
                    column (str): The column to delete the entry from.
                
                Returns:
                    eval: Evaluates the response after deleting the entry.
                """
                return eval(request_then_text(url=f'{link_prefix}/delete_entry/{model}/{column}'))

            def sanitize_string(string):
                """
                Sanitizes a string by removing unwanted characters such as quotes and slashes.
                
                Args:
                    string (str): The string to sanitize.
                
                Returns:
                    str: The sanitized string.
                """
                try:
                    return str(string.replace("'", "").replace('"', '').replace("/", "").replace("\\", ""))
                except:
                    return string

            def GetBase64Media(mediaID):
                """
                Retrieves a Base64-encoded media file (image, video, or document) from the database.
                
                Args:
                    mediaID (str): The ID of the media file to retrieve.
                
                Returns:
                    str: The Base64-encoded media file if found, otherwise None.
                """
                if dbORM.find_one('base64_images', 'id', mediaID)['status'][0] == "not found":
                    res = None
                    return res
                else:
                    res = dbORM.find_one('base64_images', 'id', mediaID)['status'][1]
                    return dbORM.get_all('base64_images')[res]['base64']

    else:
        print("Error connecting to db server")
        dbORM = None

except Exception as e:
    print(f"\n\n\n\nerror>>>>>>>>>> {e}\n\n\n\n")
    db = None
    dbORM = None
