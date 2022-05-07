from datetime import datetime

class App_Logger:
    """
    This class is used for log messages of files and return timestamp 
    of the file

    written By : Omkaram Rangasesha
    
    """
    def __init__(self):
        pass

    def logging_msg(self,object_files,log_messages):

        """
        This intialization constructor used to create the instance of the objects and class members 
        """
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        object_files.write(str(self.data) + "/" + str(self.current_time) + "\t\t"+log_messages + "\n")

