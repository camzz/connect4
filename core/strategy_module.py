class Strategy:
    def __init__(self, token, author="anonymous"):
        assert token in ("X", "O")
        self.author = author
        self.token = token
        
    
