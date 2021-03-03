import gspread
import re

REGEX_BRACES_PATTERN = r'/[^{\}]+(?=})/g'

class MarkdownTemplate:
	def __init__(self, path_to_md):
		self.path_to_md = path_to_md
		self.markdown_as_text = self.read_md()
	
	def read_md(self):
		output = []
		with open(self.path_to_md, 'r') as f:
			for line in f:
				output.append(f)
		return output

	def unique_tags(self):
		all_tags = []
		for line in markdown_as_text:
			try:
				for match in re.findall(REGEX_BRACES_PATTERN, line):
					all_tags.append(match)
			except:
				pass

		return set(all_tags)
			
			

			
		

if __name__ == "__main__":
	print("hello!")
