# Australian Component of the International Corpus of English (ICE-AUS)

## Overview

The [Australian component of the International Corpus of English (ICE-AUS)](https://figshare.mq.edu.au/articles/dataset/International_Corpus_of_English_ICE_/24769173?file=43778337) is an approximately **one million word corpus** of **transcribed spoken and written Australian English** from 1992-1995. It consists of **500 samples of Australian English** (60% speech, 40% writing) that match the structure of other ICE corpora (associated with the International corpus of English). 

The **spoken data** includes transcriptions of face-to-face spoken conversations, telephone conversations, monologues, broadcast dialogues, and scripted speech. The **written texts** include samples of unpublished letters (personal and professional), student essays, newspaper writing, popular nonfiction, academic writing, and fiction.

This collection was previously accessible online via the Australian National Corpus (AusNC), an initiative managed by Griffith University between 2012 and 2023.

**Keywords**: Australian English, Corpus linguistics

## Data Source

The original dataset is from [Macquarie University Research Data - Australian component of the International Corpus of English (ICE-AUS)](https://figshare.mq.edu.au/articles/dataset/International_Corpus_of_English_ICE_/24769173?file=43778337) and licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Dataset Structure

After unzipping `ICE Corpus.zip`, there are 500 corpus in `.txt` format and 5 metadata in spreadsheets:

- `ICE Spoken`: 301 `.txt` files that include the transcriptions from spoken data.
- `ICE Written`: 199 `.txt` files that include the samples of written texts.
- `metadata` 5 `.xls` files that include the metadata of all the `.txt` files.

A detailed tree structure can be found below:

```bash
ICE Corpus
├── ICE Spoken
│   ├── S1A
│   │   ├── S1A-001.TXT
│   │   ├── ...
│   │   └── S1A-100.TXT
│   ├── S1B
│   │   ├── S1B-001.TXT
│   │   ├── ...
│   │   └── S1B-080.TXT
│   ├── S2A
│   │   ├── S2A-001.TXT
│   │   ├── ...
│   │   └── S2A-070.TXT
│   └── S2B
│       ├── S2B-001.TXT
│   │   ├── ...
│       └── S2B-050.TXT
├── ICE Written
│   ├── W1A
│   │   ├── W1A-001.TXT
│   │   ├── ...
│   │   └── W1A-020.TXT
│   ├── W1B
│   │   ├── W1B-001.TXT
│   │   ├── ...
│   │   └── W2A-040.TXT
│   ├── W2B
│   │   ├── W2B-001.TXT
│   │   ├── ...
│   │   └── W2B-040.TXT
│   ├── W2C
│   │   ├── W2C-001.TXT
│   │   ├── ...
│   │   └── W2C-020.TXT
│   ├── W2D
│   │   ├── W2D-001.TXT
│   │   ├── ...
│   │   └── W2D-020.TXT
│   ├── W2E
│   │   ├── W2E-001.TXT
│   │   ├── ...
│   │   └── W2E-010.TXT
│   └── W2F
│       ├── W2F-001.TXT
│   │   ├── ...
│       └── W2F-020.TXT
└── metadata
    ├── ICE-catalogue.xls
    ├── demographic_info_ice-aus_s1a.xls
    ├── demographic_info_ice-aus_s1b.xls
    ├── demographic_info_ice-aus_s2a.xls
    └── demographic_info_ice-aus_s2b.xls

16 directories, 505 files

```

## Download

You can download it directly from [Macquarie University Research Data - Australian component of the International Corpus of English (ICE-AUS)](https://figshare.mq.edu.au/articles/dataset/International_Corpus_of_English_ICE_/24769173?file=43778337).

You can also download it by running `download.py` in your terminal:

```bash
$ python3 download.py --help                       
usage: download.py [-h] [--save_path SAVE_PATH] [--unzip]

Download a file and optionally unzip it.

options:
  -h, --help            show this help message and exit
  --save_path SAVE_PATH
                        Path to save the downloaded file.
  --unzip               Unzip the file if it's a zip archive.
```

For example:

- `python3 download.py --save_path my_data --unzip` will download and unzip the dataset `ACE.zip` under the directory `my_data`.
- `python3 download.py` will only download under the current directory.

## License

This repository is licensed under [MIT](https://opensource.org/license/mit).
