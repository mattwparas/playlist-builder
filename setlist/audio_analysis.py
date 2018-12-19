def find_ending_segment(audio_analysis):
    '''
    step backwards in the segments until there is segment with a signficant loudness_start or loudness_max
    Find the significant values
    input: audio analysis for a specific song
    output: segment at which the audio is ending (fades out at)
    '''

    threshold = -40
    i = -1
    current_segment = audio_analysis['segments'][i]
    while(current_segment['loudness_max'] < threshold and abs(i < len(audio_analysis['segments']))):
        i -= 1
        current_segment = audio_analysis['segments'][i]
    ending_segment = current_segment
    return ending_segment


def find_starting_segment(audio_analysis):
    '''
    step forwards in the segments until there is a segment with a significant loudness
    input: audio analysis for a specific song
    output: segment at which the audio is starting (first significant sound)
    '''

    fade_in_time = audio_analysis['track']['end_of_fade_in']
    i = 0
    current_segment = audio_analysis[0]['segments'][i]
    while(current_segment['start'] < fade_in_time and i < len(audio_analysis['segments'])):
        i += 1
        current_segment = audio_analysis[0]['segments'][i]
    beginning_segment = current_segment
    return beginning_segment