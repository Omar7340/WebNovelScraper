def htmlSearchToNovels(html):
  novels = []
  i = 0
  for n in html:
    n = n.find("a")
    novels.append({
      "id": i,
      "name": n.getText(),
      "url": n['href']
    })
    i += 1
  
  return novels