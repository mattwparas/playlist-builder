import spotipy
import spotipy.util as util
import json
import pprint
import math
import time
import os

def get_playlist_id(token, username, playlist_id):
    '''
    inputs: 
        token: authentication token
        username: string, spotify username
        playlist_id: string, playlist name
    
    returns:
        pid: playlist id
        sp: spotipy instance

    '''
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_playlists()
        for item in results['items']:
            track = item['name']
            if(track == playlist_id):
                pid = item['uri']
                print(pid)
    else:
        print("Can't get token for", username)
    
    return pid, sp



def get_playlist_tracks(username, playlist_id, sp):
    '''
    input: username <string>, playlist_id <string>, sp <spotipy token>
    output: the tracks for a playlist as a list
    '''
    results = sp.user_playlist_tracks(username, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


def get_features(playlist, sp):
    '''
    takes the playlist tracks and a spotipy token and returns the features for each song
    '''
    playlist_uris = [item['track']['uri'] for item in playlist]
    number_of_songs = len(playlist_uris)
    num_divisions = math.ceil(number_of_songs / 50)
    feature_list = []
    for i in range(1 + num_divisions):
        offset = i*50
        if (offset + 50) > number_of_songs:
            selected_tracks = playlist_uris[offset:]
        else:
            selected_tracks = playlist_uris[offset:offset + 50]
        feature_list = feature_list + sp.audio_features(tracks = selected_tracks)
    return feature_list


def get_audio_analysis(uri, sp):
    '''
    returns the audio analysis for the given song URI
    '''
    start = time.time()
    analysis = sp.audio_analysis(uri)
    delta = time.time() - start
    print("analysis retrieved in %.2f seconds" % (delta,))
    analysis['track'].pop('codestring', None)
    analysis['track'].pop('echoprintstring', None)
    analysis['track'].pop('synchstring', None)
    analysis['track'].pop('rhythmstring', None)
    return analysis


def make_new_playlist(playlist_name, is_public=True, tracks = None):
    if(is_public):
        modify_scope = "playlist-modify-public"
    else:
        modify_scope = "playlist-modify-private"
    auth_token = util.prompt_for_user_token(username, modify_scope, client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)
    spot = spotipy.Spotify(auth=auth_token)
    spot.user_playlist_create(username, playlist_name, public=is_public)
    return

# make_new_playlist("My Test Playlist")

# def add_tracks_to_playlist(playlist_name):
#     return


def get_playlist_audio_analysis(list_of_uris, sp):
    audio_analysis_output = []
    for uri in list_of_uris:
        time.sleep(1)
        print(uri)
        audio_analysis_output.append(get_audio_analysis(uri, sp))
    return audio_analysis_output
