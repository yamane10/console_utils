# console_utils
A simple collection of utility functions for building CLI scripts.

## query_select
A function for creating prompts asking the user to select a choice from a list 
given list. Based on the provided max_columns, the function will determine the 
best column arrangement and create columns of numbered choices, prompting the
user to enter a choice (by number).

The function will return the value of the selected choice.

Usage:

```python
favorite_color = query_select(
	"What's your favorite color?",
	["Red", "Orange", "Yellow",
		"Green", "Blue", "Indigo",
		"Violet", "Brown", "Black",
		"White"],
	max_columns=2,
	multi=False
	)
```

Prints the following to the console:

```text
What's your favorite color?
 1) Red      6) Indigo
 2) Orange   7) Violet
 3) Yellow   8) Brown
 4) Green    9) Black
 5) Blue    10) White
Enter selection (by number):
```

If the user enters "10", the function will return "White".

## query_yes_no
A function for prompting user to answer yes or no to a given prompt.
Usage:

```python
response = query_yes_no("Accept match?")
```

Prints the following to the console:

```text	
Accept match? (yes or no):
```

- If user enters "y", "ye", or "yes", the function will return "yes".
- If user enters "n" or "no", the function will return "no".
- If user enters nothing, the default value is returned.

## determine_plural
A function that takes an `item_to_check`, as either an `int` or a `list`, and
determines if a plural suffix should be used. If `item_to_check` is either a 
list of more than one item or an `int` greater than `1`, it will return 's', 
otherwise it will return ''.

Usage:

```python
number_of_pies = 1
types_of_apples = ["granny smith", "red delicious", "honeycrisp"]

print("We have {} pie{}, and used {} type{} of apple when baking:".format(
	number_of_pies,
	determine_plural(number_of_pies),
	len(types_of_apples),
	determine_plural(types_of_apples)
	))

for type_of_apple in types_of_apples:
	print("  -" + type_of_apple)
```

Prints the following to the console:

```text
We have 1 pie, and used 3 types of apple when baking:
  -granny smith
  -red delicious
  -honeycrisp
```

## print_verbose
A wrapper function for the built-in `print` method that only prints if `verbose` 
is `True`.

This function can be used to build console output that will be printed if
the cli command was run with a `verbal` setting of `True`. This allows for the
writing of cli commands that have a `--silent` flag, or commands that only 
print the status of the operation to the console if a `--verbal` flag is passed.

Usage:

```python
print_verbose(console_text, is_verbose)
```

The above `console_text` will only be printed to the console if `is_verbose` is
`True`.
