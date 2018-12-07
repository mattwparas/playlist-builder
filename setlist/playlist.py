class Playlist(object):
    def __init__(self, *args, **kwargs):

        self.name = None
        self.username = None

        self.token = None
        self.pid = None
        self.sp = None

        self.tracks = None 
        self.playlist_uris = [item['track']['uri'] for item in self.tracks]
        self.feature_list = None
        self.audio_analysis = None


        return super().__init__(*args, **kwargs)
    
    def __str__(self):
        return super().__str__()

    def __eq__(self, value):
        return super().__eq__(value)

    def __hash__(self):
        return super().__hash__()