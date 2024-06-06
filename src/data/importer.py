import os
import re
import random
import pandas as pd
import xml.etree.ElementTree as ET

class Importer:
    """Class for importing and processing data files."""
    
    def __init__(self) -> None:
        pass

    def abstract_names_function(self, path):
        """
        Lists all file names in the specified directory.

        Args:
        path (str): The path to the directory from which to list the files.

        Returns:
        list: A list with the names of all the files in the directory.
        """
        # Check if the directory exists
        if not os.path.exists(path):
            return "The directory does not exist."
        
        # Get all files and subdirectories in the specified directory
        file_names = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

        return file_names
    
    def abstract_sampler(self, full_list, prop=0.8):
        """
        Selects a random sample of elements from a list of strings.

        Args:
        full_list (list): The original list of strings from which to select the sample.
        prop (float): The proportion of elements to select from the list (default is 0.8).

        Returns:
        list: A list with randomly selected elements from the original list.
        """
        # Define the number of elements to sample based on the proportion
        self.n = int(len(full_list) * prop)

        # Check if the number of elements to sample is greater than the length of the list
        if self.n > len(full_list):
            return "Error: The number of elements to sample is greater than the number of elements in the list."
        
        # Select random elements from the list
        selected_sample = random.sample(full_list, self.n)
        
        return selected_sample
    
    def extract_data(self, file_path):
        """
        Extracts relevant data from an XML file.

        Args:
        file_path (str): Path to the XML file.

        Returns:
        dict: A dictionary with the title and abstract of the file.
        """
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Extract basic information
        title = root.find('.//AwardTitle').text if root.find('.//AwardTitle') is not None else "No Title"
        abstract = root.find('.//AbstractNarration').text if root.find('.//AbstractNarration') is not None else "No Abstract"
        
        return {
            "title": title,
            "abstract": abstract
        }
    
    def clean_text(self, text): 
        """
        Cleans the text of abstracts.

        Args:
        text (str): String with the text to transform.

        Returns:
        str: Transformed text.
        """
        if pd.isna(text):
            return ""  # Return an empty string if the text is NaN

        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Convert to lowercase
        text = text.lower()
        # Remove additional spaces
        text = re.sub(r'\s+', ' ', text).strip()

        return text
