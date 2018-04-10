# dsml - Dataset Sort for Machine Learning
by Javier O. Cordero Pérez, licensed under the MIT License 

Usage
-------------
usage: dsml [-h] [-R] [-m] [-e [EXTENSIONS [EXTENSIONS ...]]]
            [--source SOURCE] [--destination DESTINATION]
            [N [N ...]]

Randomly selected files and split them into training, testing and validation
subfolders, according to user specified percentages.

positional arguments:
  N                     specify percentage groups in which to split the files:
                        [train] [test] [validate] (default: 60 20 20)

optional arguments:
  -h, --help            show this help message and exit
  -R                    search files from subdirectories, recursively
                        (default: False)
  -m                    move files, default="copy files" (default: False)
  -e [EXTENSIONS [EXTENSIONS ...]]
                        specify file extensions to filter with (default: .png
                        .PNG .jpg .JPG .jpeg .JPEG)
  --source SOURCE       path to source folder (default: ./)
  --destination DESTINATION
                        path to destination folder (default: ./)
