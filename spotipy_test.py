import spotipy
import spotipy.util as util
import json
import pprint
import math
import time
import matplotlib.pyplot as plt
import os

def get_playlist_id(token, username, playlist_id):
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
    output: the tracks for a playlist
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

def loudness_plot(audio_analysis):
    '''
    given an audio analysis, returns a plot of the loudness, with sections marked and the fade out marked
    '''
    # ignore beginning and end
    time_list = []
    value_list = []

    mean_times = []
    mean_values = []
    for item in audio_analysis['segments']:
        # starting time loudness
        # max time loudness
        starting_time = item['start']
        loudness_start = item['loudness_start']
        loudness_max_time = starting_time + item['loudness_max_time']
        loudness_max = item['loudness_max']

        time_list = time_list + [starting_time, loudness_max_time]
        value_list = value_list + [loudness_start, loudness_max]

        mean_loudness = (loudness_start + loudness_max) / 2
        mean_loudness_time = (starting_time + loudness_max_time) / 2

        mean_values.append(mean_loudness)
        mean_times.append(mean_loudness_time)
    
    plt.figure(figsize=(20, 5))
    fade_out_time = audio_analysis['track']['start_of_fade_out']
    fade_in_time = audio_analysis['track']['end_of_fade_in']
    plt.axvline(x=fade_out_time, color='b')
    plt.axvline(x=fade_in_time, color='b')

    # plot section markers
    for section in audio_analysis['sections']:
        plt.axvline(x=section['start'], color='y')
    
    # plt.plot(mean_times, mean_values, 'b.')
    plt.plot(time_list, value_list, 'r.')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Loudness (Db)")
    plt.show()
    return 0

def tatum_plot(audio_analysis):
    '''
    plots the tatum of a song over time given audio analysis
    '''
    tatums = audio_analysis['tatums']
    start_times = [x['start'] for x in tatums]
    duration = [60 / x['duration'] for x in tatums]
    # confidence = [x['confidence'] for x in tatums]

    plt.figure(figsize=(20, 5))
    plt.plot(start_times, duration, 'r.')
    # plt.plot(start_times, confidence, 'b.')
    plt.show()
    return


def feature_diagnostic_plot(feature_list, selected_feature):
    '''
    given a feature list (from a playlist), plots that feature vs track # in playlist
    '''
    feature_values = [track[selected_feature] for track in feature_list if track is not None]
    plt.plot(list(range(len(feature_values))), feature_values, '-o')
    # plt.ylim(0, 1)
    plt.show()
    return

def tempo_plot(audio_analysis):
    '''
    plots the tempo vs time
    '''
    sections = audio_analysis['sections']
    start_times = [x['start'] for x in sections]
    tempos = [x['tempo'] for x in sections]
    plt.plot(start_times, tempos, 'r.')
    plt.ylim(0, 250)
    plt.show()
    return


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



def save_to_json(path, data):
    js = json.dumps(data)
    fp = open(path, 'a')
    fp.write(js)
    fp.close()

def open_file(path):
    json1_file = open(path)
    json1_str = json1_file.read()
    json1_data = json.loads(json1_str)
    return json1_data


def get_playlist_audio_analysis(list_of_uris, sp):
    audio_analysis_output = []
    for uri in list_of_uris:
        time.sleep(1)
        print(uri)
        audio_analysis_output.append(get_audio_analysis(uri, sp))
    return audio_analysis_output









