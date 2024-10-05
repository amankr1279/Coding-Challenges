# Coding Challenges Fyi- Build Your Own wc Tool


This is an implementation of the Coding Challenges FYI's [Build Your Own wc Tool](https://codingchallenges.fyi/challenges/challenge-wc). 


## Working

Given a text as an input either as file or buffered, this program generates statistics that the ```wc``` tool in linux and unix distros generate.

## Usage

```bash
python3 ccwc.py text.txt
python3 ccwc.py text.txt -l/m/c/w
cat test.txt | python3 ccwc.py
cat test.txt | python3 ccwc.py -l/m/c/w
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
