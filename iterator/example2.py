class APIPageIterator:
    def __init__(self, fetch_page):
        """ This one is used to intialize the  Iteraor of page"""
        
        #  this help us to call bthe function which help us to get the page
        self.fetch_page = fetch_page 
        #  curr Page
        self.page = 1
        #  used to store data of somecurr page
        self.buffer = []
    def __iter__(self):
        return self
    def __next__(self):
        #  check weather buffer is empty o not 
        #  if the buffer some data we only return the first element stored as element
        if not self.buffer:
            data = self.fetch_page(self.page)
            if not data:
                raise StopIteration
            self.buffer.extend(data)
            self.page += 1
        return self.buffer.pop(0)
    
    
def mock_api(page):
    pages = {
        1: ["User 1", "User 2", "User 3"], 
        2: ["User 5"], 
        3: []
        
    }
    
    return pages.get(page, [])


for page in APIPageIterator(mock_api):
    print(page)