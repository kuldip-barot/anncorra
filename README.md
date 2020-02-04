# Tags of AnnCorra 

[![GitHub issues](https://img.shields.io/github/issues/kuldip-barot/anncorra)](https://github.com/kuldip-barot/anncorra/issues) [![GitHub forks](https://img.shields.io/github/forks/kuldip-barot/anncorra)](https://github.com/kuldip-barot/anncorra/network) [![GitHub stars](https://img.shields.io/github/stars/kuldip-barot/anncorra)](https://github.com/kuldip-barot/anncorra/stargazers) ![GitHub](https://img.shields.io/github/license/kuldip-barot/anncorra)  
Indian Language Machine Translation (ILMT) project has taken the task of annotating corpora **(AnnCorra)** of several Indian languages and came up with tags which have been defined for the tagging schemes for POS (part of speech) tagging.

This repository would explain the [POS](https://en.wikipedia.org/wiki/Part-of-speech_tagging) (Part Of Speech) Tags along with examples.

## Requirements

Package requires the following to run:

  * [python](https://www.python.org/downloads/) (preferable version 3+)


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install anncorra
``` 

## Usage

Import the package after installation.

```python
import anncorra
```

Use the *explain* function and pass the name of the POS Tag as the argument.

```python
anncorra.explain('NN')  # Prints the tag, full form, description and example associated with the input tag.
```
Output of the above function call.

```bash
> POS Tags :  NN
> Full form :  Noun
> Desription :  The tag NN tag set makes a distinction between noun singular (NN) and noun plural (NNS).
> Example :
> yaha bAta  galI_NN galI_RDP meM  phEla gayI
>  'this' 'talk'  'lane'      'lane'         'in'    'spread' 'went'
>  “The word was spread in every lane”.
``` 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## References

[AnnCorra : Annotating Corpora; Guidelines For POS And Chunk Annotation For Indian Languages](http://ltrc.iiit.ac.in/winterschool08/content/data/revised-chunk-pos-ann-guidelines-15-Dec-06.doc)
