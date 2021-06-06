# Usage: bash -i mappings/map_hackmd_notes.sh
set -e

conda activate ml_course_project

rm -rf notes
mkdir notes
python mappings/map_hackmd_notes.py --raw_note_dir tmp/HackMD_User_1622948336029 \
                                    --dest_note_dir notes \
                                    --dest_image_dir media
