# Karlchen

'''Karlchen''' is a simple python package to generate `.svg` files for playing-card backs, with a few variants/options.

## Version

* 0.1 (26/1/21 - basic functionality)

## Features

All cards use customisable dimensions for overall shape, margin, outline and actual design area.

Currently implemented designs:

* Plain colour
* SW-NE diagonal stripes in top-left half
* SW-NE diagonal stripes across entire design

## Usage


## Examples

Example files were generated via

```bash
python generate_examples.py
```

That [script](./generate_examples.py) should give a reasonable idea of how to use until more detailed instructions are available.

![Plain purple back](./examples/plain_cards/plain_card_alt_dims.svg)
![Italian flavoured design](./examples/diagonals/italian_flavoured.svg)
![Semi-striped design](./examples/diagonals/semi_barbershop.svg)

## Playing card dimensions

Some reference sizes for realistic examples, taken from [wikipedia](https://en.wikipedia.org/w/index.php?title=Standard_52-card_deck&oldid=1002254049#Size_of_the_cards)


|  | Height | Width |
| :------------- | :----------: | -----------: |
| Ravensburger | 92 | 59 |
| Handa (wide) | 91 | 62 |
| ASS Altenburger | 91 | 59 |
| Kem (wide) | 89 | 64 |
| Piatnik (narrow) | 89 | 58 |
| Kem (narrow) | 89 | 57 |
| Piatnik (wide) | 88 | 63 |
| Waddingtons | 88 | 58 |
| Handa (narrow) | 87 | 56 |
| Oberg | 87 | 56 |
| Bicycle |	88 | 63 |
| BGA Calypso (digital) | 92 | 76 |
