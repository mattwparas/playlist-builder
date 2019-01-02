import numpy as np
import matplotlib.pyplot as plt
from audio_analysis import *

'''
Generate playlist demographics...
features include:
    danceability, energy, key, loudness, mode, speechiness, 
    acousticness, instrumentalness, liveness, valence, tempo
'''
def feature_hist(feature_name, feature_list):
    '''
    Generates a histogram of the given feature for a playlist

    Args:
        feature_name (string): a feature that corresponds to one of the possible features from Spotify's API
        feature_list (list): a json response from Spotify - a list of feature responses from Spotify
    Returns:
        None
    '''

    feature_values = [track[feature_name] for track in feature_list if track is not None]
    mean_value = np.mean(np.array(feature_values))
    sd_value = np.std(np.array(feature_values))
    if feature_name == "tempo":
        range_values = None
    else:
        range_values = (0,1)
    plt.hist(feature_values, align = 'mid', alpha = 0.9, range = range_values,
             weights=np.ones_like(feature_values)/len(feature_values))
    plt.xlabel(feature_name)
    plt.ylabel('Frequency')
    plt.title("Histogram of " + feature_name + ": Mean = " + 
              str(round(mean_value, 2)) + ", SD = " + str(round(sd_value, 2)))
    plt.axvline(x = mean_value, color = "r")
    plt.show()
    return


def popularity_hist(track_list):
    '''
    Generates a histogram of the popularity for a playlist

    Args:
        track_list (list): the JSON response from Spotify, consisting of a track list
    Returns:
        None
    '''
    # popularity metrics
    popularity_values = [track['track']['popularity'] for track in track_list if track is not None]
    mean_value = np.mean(np.array(popularity_values))
    plt.hist(popularity_values, range = [0, 100], align = 'mid', alpha = 0.9)
    plt.axvline(x = mean_value, color = "r")
    print(mean_value)


def loudness_plot(audio_analysis):
    '''
    Returns a plot of the loudness, with sections marked and the fade out marked

    Args:
        audio_analysis (dict): the JSON response from Spotify, consisting of the audio analysis 
        for a single song
    Returns:
        None
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
    Plots the tatum of a song over time given audio analysis

    Args:
        audio_analysis (dict): The JSON response from Spotify, consisting of the audio analysis 
        for single song
    Returns:
        None
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
    Plots that feature vs track # in playlist

    Args:
        selected_feature (string): a feature that corresponds to one of the possible features from Spotify's API
        feature_list (list): a json response from Spotify - a list of feature responses from Spotify
    Returns:
        None
    '''
    feature_values = [track[selected_feature] for track in feature_list if track is not None]
    plt.plot(list(range(len(feature_values))), feature_values, '-o')
    # plt.ylim(0, 1)
    plt.show()
    return

def tempo_plot(audio_analysis):
    '''
    Plots the tempo vs time for a single song
    Args:
        audio_analysis (dict): The JSON response from Spotify, consisting of the audio analysis 
        for single song
    Returns:
        None
    '''
    sections = audio_analysis['sections']
    start_times = [x['start'] for x in sections]
    tempos = [x['tempo'] for x in sections]
    plt.plot(start_times, tempos, 'r.')
    plt.ylim(0, 250)
    plt.show()
    return




def sound_differences(audio_analysis_list):
    '''
    find difference vector for pitches at the end of the song and the beginning of the next
    also match timbre at the beginning and end of songs
    '''
    timbre_differences = []
    pitch_differences = []
    for i in range(len(audio_analysis_list) - 1):
        current_song = audio_analysis_list[i]
        next_song = audio_analysis_list[i + 1]
        
        ending_segment = find_ending_segment(current_song)
        starting_segment = find_starting_segment(next_song)
        
        timbre_df = np.linalg.norm(np.array(ending_segment['timbre'] - np.array(starting_segment['timbre'])))
        pitch_df = np.linalg.norm(np.array(ending_segment['pitches'] - np.array(starting_segment['pitches'])))
        
        timbre_differences.append(timbre_df)
        pitch_differences.append(pitch_df)
        
    # print(timbre_differences)
    print(np.mean(np.array(timbre_differences)))
    print(np.mean(np.array(pitch_differences)))
    # print(pitch_differences)

    # plt.style.use('dark_background')
    plt.plot(list(range(len(audio_analysis_list) - 1)), pitch_differences, '-r')
    plt.show



def transition_differences(audio_analysis_list):
    transitions = []
    list_of_fade_out = []
    list_of_fade_in = []
    list_of_combined_fades = []
    for i in range(len(audio_analysis_list) - 1):
        current_song = audio_analysis_list[i]
        next_song = audio_analysis_list[i + 1]
        fade_out = current_song['track']['duration'] - current_song['track']['start_of_fade_out']
        fade_in = next_song['track']['end_of_fade_in']
        # print(fade_out, fade_in)
        # print(math.log(fade_out + 1) - fade_in)
        # transitions.append(fade_out + fade_out*fade_in)
        transitions.append(fade_out*fade_in)
        list_of_fade_out.append(fade_out)
        list_of_fade_in.append(fade_in)
        list_of_combined_fades.append(fade_out+fade_in)
        

    # plt.plot(list(range(len(audio_analysis_list) - 1)), list_of_fade_in, 'ro')
    # plt.plot(list(range(len(audio_analysis_list) - 1)), list_of_fade_out, 'o')
    plt.plot(list(range(len(audio_analysis_list) - 1)), list_of_combined_fades, '-o')
    plt.show

    print(np.std(np.array(transitions)))
    print(np.mean(np.array(transitions)))


#################### gotta snag the find_starting_segment in the other pacakge
def analyze_pitch_distribution(audio_analysis_list, index):
    '''
    attempt to analyze pitch distribution at a given segment
    '''
    test_segment = find_starting_segment(audio_analysis_list[index])
    print(audio_analysis_list[index]['track'])
    # print(test_segment)
    pitch_vector = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

    plt.style.use('default')
    plt.xticks(list(range(len(test_segment['pitches']))), pitch_vector)
    plt.plot(list(range(len(test_segment['pitches']))), test_segment['pitches'], 'o')
    mean_pitch = np.mean(np.array(test_segment['pitches']))
    pitch_sd = np.std(np.array(test_segment['pitches']))
    plt.axvline(x=audio_analysis_list[index]['track']['key'], color = 'g')
    plt.axhline(y=audio_analysis_list[index]['track']['key_confidence'])
    # plt.axhline(y=mean_pitch, color='r')
    # plt.axhline(y=mean_pitch + pitch_sd / 2, color = 'y')

    pitches = []
    for i in range(len(test_segment['pitches'])):
        if test_segment['pitches'][i] >= mean_pitch + pitch_sd / 2:
            pitches.append(i)

    pitch_names = [pitch_vector[i] for i in pitches]
    print(pitch_names)


def plot_max_pitch_over_time(audio_ananlysis_list, index):
    '''
    plot max pitch over time
    '''
    current_song = audio_analysis_list[index]
    # for segment in current_song['segments']:
    print(current_song['segments'][index])
    segment_times = [x['start'] for x in current_song['segments']]
    pitch_values = [x['pitches'].index(max(x['pitches'])) for x in current_song['segments']]
    plt.plot(segment_times, pitch_values, 'o')

