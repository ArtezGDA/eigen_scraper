#pseudocode

capturing = False
allReferences = []

for elem in child_elements_of_div[class="list"]:

	if elem == h1:
		if elem.class == "li_group":
			if elem.text == "References":
				capturing = True

	if elem == h1:
		if elem.class == "li_group":
			if elem.text == "Referenced by":
				capturing = False

	if capturing:
		if elem == div:
			if elem.class == "soda even" or elem.class == "soda odd":

				get child a
				title = a.text
				link = a.href

				aReference = {'title': title, 'link': link}
				allReferences.append(aReference)

for ref in allReferences:

	open site with url = ref['link']

	get div[class="infobar"]

	# genre
	hasGenre = False
	for elem in div_get_child_elements_a:
		if elem.href.startswith("/genre/"):
			genre = elem.text

			if not hasGenre:
				ref['genre'] = genre
				hasGenre = True

				




