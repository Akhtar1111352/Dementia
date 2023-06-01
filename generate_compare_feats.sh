#!/bin/bash

opensmile_dir="C:\Users\HP\Downloads\SOFTWARES\opensmile-3.0-win-x64\opensmile-3.0-win-x64"
audio_dir="C:\Users\HP\Downloads\datset_dir\train\Full_wave_enhanced_audio\cc"

for entry in "$audio_dir"/*; do
  fn="${entry%.*}"

  SMILExtract -C "$opensmile_dir/config/is09-13/IS13_ComParE.conf" -I "$entry" -O "compare_${fn##*/}.csv"
done
