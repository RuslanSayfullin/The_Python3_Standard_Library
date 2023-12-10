import textwrap
import textwrap_example

dedented_text = textwrap.dedent(textwrap_example.sample_text).strip()
for width in [45, 60]:
	print('{} Columns:\n'.format(width))
	print(textwrap.fill(dedented_text, width=width))
	print()
