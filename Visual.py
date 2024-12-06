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

    def __init__(self, data):
        self.data = data
