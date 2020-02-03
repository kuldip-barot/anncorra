# Tags of AnnCorra 

Indian Language Machine Translation (ILMT) project has taken the task of annotating corpora **(AnnCorra)** of several Indian languages and came up with tags which have been defined for the tagging schemes POS (part of speech) tagging.

The project here is about to create a small library file named `anncorra.py`, using language python,to give the meaning of the POS ( Part Of Speech ) tags just using the tag name.


## Requirements

Module requires the following to run:

  * [python][https://www.python.org/downloads/] (preferable version 3+)


## Installation
```python
pip install anncorra
```
or
```python
pip install s
```
 
 
## Usage

Firstly make sure that file `pos_tags_data.json` and `anncorra.py` in same folder.

* `pos_tags_data.json` file contains the POS data in records of `{POS Tags :, Full form: , Examples: , Definition:}`.

You need to import `anncorra.py` file 

```python
import anncorra                # module file to import
```

You can now get the information of any `tag` stored in `POS_TAGS.json` using below code.

```python
anncorra.explain('NN')  # NN is a tag stored in json file. input : tag_name
```


## Reference Links

   *[POS tagger][http://ltrc.iiit.ac.in/winterschool08/content/data/revised-chunk-pos-ann-guidelines-15-Dec-06.doc]

