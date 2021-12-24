#!/bin/bash

abcfile=$1
suffix=${abcfile%.abc}
abc2midi $abcfile -o "$suffix.mid"
timidity "$suffix.mid" -Ow "$suffix.wav"
cp "$suffix.wav" /app/audiogeneration/static/audio
rm "$suffix.abc" "$suffix.mid"