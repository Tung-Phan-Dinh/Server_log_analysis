import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Visualize:
    '''

    The main task is to visualize the data that has been processed and transformed from
    the original data, specifically a server log file from 30/11 to 1/12.
    Through the processing steps, the data is considered to have several fields such as:
    IP, Time, Request, Status, Size, Referrer, User-Agent.
    - The main task is to select 2-3 data fields to visualize.
    - Depending on the variables given, choose the appropriate type of visualization.
    - Then select the time frame to present the data in column format (it can be by hour or even by minute).
    * Note: Visualize keeps the data for embedding purposes, etc.

    Input: file data about server log that has already been converted to csv format.

    Output: The data is visualized in forms of graphs, charts, etc.

    '''


    def __init__(self, file_path):
        self.file_path = file_path
        self.hourly_bytes_sent = self.read_data(file_path)
        self.log_df = pd.read_csv(file_path)
        

    def read_data(self, file_path):
        # Read the data into DataFrame
        log_df = pd.read_csv(file_path)

        # Check if the necessary columns exist in the DataFrame
        if 'datetime' not in log_df.columns or 'bytes_sent' not in log_df.columns:
            raise ValueError("The CSV file must contain 'datetime' and 'bytes' columns.")

        # Convert the date column to datetime format
        log_df['datetime'] = pd.to_datetime(log_df['datetime'], errors='coerce', format='%d/%b/%Y:%H:%M:%S +0000')

        # Add a new column for "hour" to group data by hours
        log_df['hour'] = log_df['datetime'].dt.hour

        # Compute the total bytes sent per hour
        hourly_bytes_sent = log_df.groupby('hour')['bytes_sent'].sum()

        return hourly_bytes_sent

    
    
    def visualize_data(self):
        # Plot the data
        plt.figure(figsize=(10, 6))
        sns.barplot(x=self.hourly_bytes_sent.index, y=self.hourly_bytes_sent.values, palette="viridis")
        plt.title('Bytes gửi mỗi giờ')
        plt.xlabel('Giờ')
        plt.ylabel('Tổng số bytes gửi')
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()

# Example usage
file_path = '/Users/phamthiphuongthuy/Desktop/Intern/server_log/D:\CODING\Project\Server Log Analysis\data\interim\parsed_logs.csv'
visualizer = Visualize(file_path)
hourly_bytes_sent = visualizer.read_data(file_path)
visualizer.visualize_data()
