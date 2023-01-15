class Language():
    def __init__(self,Language_List):
        self.Language_data = Language_List
        self.language_code = ""

    def choose_language(self,language):
        if language == "German":
            self.language_code = "de-De"
        if language == "English":
            self.language_code = "de-De"
