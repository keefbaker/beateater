from midiutil import MIDIFile
import random

mf = MIDIFile(1)
track = 0
channel = 9  
tempo = 120
mf.addTempo(track, 0, tempo)
c_minor_scale = [36, 39, 41, 43, 46]


drum_notes = {
    "kick": 36,
    "snare": 38,
    "hihat": 42
}

def hatter(mf, beat):
    for _ in range(5):
        beatdivider = [beat, beat + 0.25, beat + 0.5, beat + 0.75]
        if random.randrange(0,120) > 80:
            beat_sub = random.choice(beatdivider)
            beatdivider.remove(beat_sub)
            mf.addNote(track, channel, drum_notes["hihat"], beat_sub, 0.05, random.randrange(70,120))
            if random.randrange(0,120) > 110: # triplet time
                mf.addNote(track, channel, drum_notes["hihat"], beat_sub + 0.083, 0.05, random.randrange(40,90))
                mf.addNote(track, channel, drum_notes["hihat"], beat_sub + 0.166, 0.05, random.randrange(40,90))
            elif random.randrange(0,120) > 110:
                mf.addNote(track, channel, drum_notes["hihat"], beat_sub + 0.125, 0.05, random.randrange(40,90))
    return mf

def kicker(mf, beat):
    beatdivider = [beat, beat + 0.25, beat + 0.5, beat + 0.75]
    if beat % 2 == 1:
        beatdivider.remove(beat)
    if beat == 0:
        mf.addNote(track, channel, drum_notes["kick"], beat, 0.1, 100)
        mf.addNote(track, 0, 36, beat, 0.1, 100)
    if random.randrange(0,120) > 30:
        for _ in range(2):
            if random.randrange(0,120) > 100:
                bang = random.choice(beatdivider)
                beatdivider.remove(bang)
                mf.addNote(track, channel, drum_notes["kick"], bang, 0.1, 100)
                mf.addNote(track, 0, random.choice(c_minor_scale), bang, 0.1, 100)
    else:
        if beat % 2 != 1:
            mf.addNote(track, channel, drum_notes["kick"], beat, 0.1, 100)
            mf.addNote(track, 0, random.choice(c_minor_scale), beat, 0.1, 100)
    return mf

# Add notes: (track, channel, pitch, time, duration, velocity)
for beat in range(256):
    # mf = kicker(mf, beat)

    mf = hatter(mf, beat)               
    # if beat % 2 == 1:
    #     if random.randrange(0,10) >  1:
    #         mf.addNote(track, channel, drum_notes["snare"], beat, 0.1, 100)
    #         mf.addNote(track, 0, random.choice(c_minor_scale), beat, 0.1, 100)
    #     else:
    #         mf.addNote(track, channel, drum_notes["snare"], beat + 0.5, 0.1, 100)
    #         mf.addNote(track, 0, random.choice(c_minor_scale), beat + 0.5, 0.1, 100)

with open("drumbeat.mid", "wb") as output_file:
    mf.writeFile(output_file)